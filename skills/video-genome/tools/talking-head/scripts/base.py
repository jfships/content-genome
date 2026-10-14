"""Treat the speaker footage itself: background blur/dim/colour/image and zoom-ins on key words. One pass.
usage: python3 base.py motion/plan.json            (reads plan["base"], writes work/base.mp4 and, if asked, work/matte.mp4)

plan["base"] = {
  "background": {"mode": "blur" | "dim" | "color" | "image" | "none",
                 "amount": 0.6,          # blur strength (blur) or how dark (dim), 0..1
                 "blur": true,           # dim only: also blur
                 "desaturate": 0.3,      # optional, 0..1
                 "color": "#0F1117",     # color mode
                 "image": "inputs/bg.jpg"},  # image mode (path relative to plan.json)
  "zooms": [ {"t": 12.30, "hold": 1.2, "scale": 1.12, "focus": "auto", "style": "ease" | "punch"} ],
  "matte": true      # also write work/matte.mp4 (white = speaker). Needed for anything placed BEHIND the speaker.
}
Zoom: t = word time, eases in over 0.35s (punch = instant), holds `hold` s, eases out over 0.5s. Keep scale 1.06-1.2.
focus "auto" (default) = the zoom re-centres on the speaker's head as detected at that moment, so an off-centre speaker is pulled
toward the middle of the frame as it zooms (as far as the zoom allows without showing edges). [fx, fy] fixes a point instead.
Also writes work/subject.json: per frame [head_x, head_y, left, top, right, bottom] as fractions of the frame (smoothed),
used by speaker_frames.py and subject.py.
Person detection: MediaPipe selfie segmentation (pip install mediapipe==0.10.14 opencv-python-headless), fallback rembg.
After running, set plan["base_video"]="work/base.mp4" (and "matte":"work/matte.mp4"); composite.py and speaker_frames.py use it."""
import sys, json, subprocess, pathlib
import numpy as np, cv2

def probe(src):
    o = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height,r_frame_rate,nb_frames', '-show_entries', 'format=duration', '-of', 'json', src]))
    s = o['streams'][0]; n, d = s['r_frame_rate'].split('/')
    return int(s['width']), int(s['height']), n + '/' + d, float(n)/float(d), float(o['format']['duration'])

class Seg:
    def __init__(self):
        try:
            import mediapipe as mp
            self.m = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection=1); self.kind = 'mediapipe'
        except Exception as e:
            print('mediapipe unavailable (%s), using rembg' % str(e)[:80])
            from rembg import new_session, remove
            self.sess = new_session('u2net_human_seg'); self.remove = remove; self.kind = 'rembg'
        self.prev = None
    def __call__(self, small_rgb):
        if self.kind == 'mediapipe': m = self.m.process(small_rgb).segmentation_mask
        else: m = self.remove(small_rgb, session=self.sess, only_mask=True).astype(np.float32)/255
        m = m.astype(np.float32)
        self.prev = m if self.prev is None else 0.55*m + 0.45*self.prev      # temporal smoothing, less flicker
        m = np.clip((self.prev-0.3)/0.4, 0, 1)
        return cv2.GaussianBlur(m, (7, 7), 0)

def measure(m):
    # m: low-res mask 0..1 -> [head_x, head_y, left, top, right, bottom] as fractions, or None
    h, w = m.shape; b = m > 0.5; rows = np.where(b.sum(1) > 0.03*w)[0]
    if len(rows) == 0: return None
    top = rows[0]; bottom = rows[-1]; cols = np.where(b.any(0))[0]
    band = b[top:top+max(2, int(0.2*h))]; xs = np.where(band)[1]
    hx = xs.mean()/w if len(xs) else (cols[0]+cols[-1])/2/w
    return [round(hx, 4), round((top+0.1*h)/h, 4), round(cols[0]/w, 4), round(top/h, 4), round(cols[-1]/w, 4), round(bottom/h, 4)]

def zoom_at(t, zooms):
    z, fx, fy = 1.0, 0.5, 0.4
    for Z in zooms:
        a, h, s = Z['t'], Z.get('hold', 1.0), Z.get('scale', 1.12); ei, eo = (0.001, 0.001) if Z.get('style') == 'punch' else (0.35, 0.5)
        if t < a or t > a+ei+h+eo: continue
        u = min(1, (t-a)/ei) if t < a+ei+h else max(0, 1-(t-a-ei-h)/eo)
        u = u*u*(3-2*u)
        if 1+(s-1)*u > z: z, (fx, fy) = 1+(s-1)*u, Z['_f']
    return z, fx, fy

def main(plan_p):
    plan_p = pathlib.Path(plan_p); root = plan_p.parent; P = json.load(open(plan_p)); cfg = P.get('base', {})
    src = str(root/P['video']); W, H, fr, fps, dur = probe(src)
    bgc = cfg.get('background', {'mode': 'none'}); mode = bgc.get('mode', 'none'); zooms = cfg.get('zooms', []); want_matte = cfg.get('matte', False)
    need_seg = mode != 'none' or want_matte or any(Z.get('focus', 'auto') == 'auto' for Z in zooms)
    seg = Seg() if need_seg else None
    bgimg = None
    if mode == 'color':
        h = bgc.get('color', '#0F1117').lstrip('#'); bgimg = np.full((H, W, 3), [int(h[4:6], 16), int(h[2:4], 16), int(h[0:2], 16)], np.uint8)
    if mode == 'image': bgimg = cv2.resize(cv2.imread(str(root/bgc['image'])), (W, H), interpolation=cv2.INTER_AREA)
    rd = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', src, '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
    enc = lambda out, pf: subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', pf, '-s', f'{W}x{H}', '-r', fr, '-i', '-',
        *(['-i', src, '-map', '0:v', '-map', '1:a?', '-c:a', 'copy'] if pf == 'bgr24' else []),
        '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(out)], stdin=subprocess.PIPE)
    wb = enc(root/'work'/'base.mp4', 'bgr24'); wm = enc(root/'work'/'matte.mp4', 'gray') if want_matte else None
    n = 0; fs = W*H*3; sw, sh = 640, int(640*H/W); track = []; ema = None
    for Z in zooms: Z['_f'] = Z['focus'] if isinstance(Z.get('focus'), list) else None
    amt = float(bgc.get('amount', 0.6)); ds = float(bgc.get('desaturate', 0))
    while True:
        buf = rd.stdout.read(fs)
        if len(buf) < fs: break
        f = np.frombuffer(buf, np.uint8).reshape(H, W, 3); t = n/fps; n += 1
        m = None
        if seg is not None:
            ms = seg(cv2.cvtColor(cv2.resize(f, (sw, sh), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2RGB))
            me = measure(ms)
            if me: ema = me if ema is None else [0.85*a+0.15*b for a, b in zip(ema, me)]
            track.append([round(v, 4) for v in ema] if ema else None)
            m = cv2.resize(ms, (W, H), interpolation=cv2.INTER_LINEAR)
        for Z in zooms:
            if Z['_f'] is None and t >= Z['t']-0.05: Z['_f'] = [ema[0], ema[1]] if ema else [0.5, 0.4]
        if mode != 'none':
            if mode in ('blur', 'dim'):
                k = 8 if mode == 'blur' else 12; small = cv2.resize(f, (W//k, H//k), interpolation=cv2.INTER_AREA)
                if mode == 'blur' or bgc.get('blur', True):
                    r = max(1, int(1+amt*10))*2+1; small = cv2.GaussianBlur(small, (r, r), 0)
                bg = cv2.resize(small, (W, H), interpolation=cv2.INTER_LINEAR)
                if mode == 'dim': bg = cv2.convertScaleAbs(bg, alpha=max(0.05, 1-amt))
            else: bg = bgimg
            if ds > 0: g = cv2.cvtColor(cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR); bg = cv2.addWeighted(bg, 1-ds, g, ds, 0)
            f = cv2.blendLinear(f, bg, m, 1-m)
        z, fx, fy = zoom_at(t, [Z for Z in zooms if Z['_f'] is not None])
        if z > 1.0005:
            # zoom around the subject AND slide it toward the frame centre (head at 40% height), as far as the zoom
            # allows without exposing an edge: shift must stay within [(z-1)(c-W), (z-1)c]
            cx, cy = fx*W, fy*H
            sx = min(max(W/2-cx, (z-1)*(cx-W)), (z-1)*cx); sy = min(max(0.4*H-cy, (z-1)*(cy-H)), (z-1)*cy)
            A = np.float32([[z, 0, (1-z)*cx+sx], [0, z, (1-z)*cy+sy]])
            f = cv2.warpAffine(f, A, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
            if m is not None: m = cv2.warpAffine(m, A, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        wb.stdin.write(np.ascontiguousarray(f).tobytes())
        if wm: wm.stdin.write((m*255).astype(np.uint8).tobytes())
        if n % 300 == 0: print(f'{t:6.1f}s / {dur:.1f}s', flush=True)
    wb.stdin.close(); wb.wait()
    if wm: wm.stdin.close(); wm.wait()
    if track:
        json.dump({'fps': fps, 'width': W, 'height': H, 'frames': track}, open(root/'work'/'subject.json', 'w'))
        print('wrote work/subject.json; zoom focus used:', [[Z['t'], [round(v, 3) for v in Z['_f']]] for Z in zooms])
    print('wrote work/base.mp4' + (' and work/matte.mp4' if wm else ''), n, 'frames')

if __name__ == '__main__': main(sys.argv[1])
