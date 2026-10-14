"""Where the speaker is, and whether anything placed behind them stays readable.

box:        python3 subject.py box motion/plan.json <t0> <t1>
            From work/subject.json (written by base.py): the speaker's head and body box over that window, in video pixels,
            plus the free space left of, right of and above them. Use it to lay out word pops and to choose side-box positions.

occlusion:  python3 subject.py occlusion motion/plan.json <clip id> [--min 0.7]
            For a clip with "behind": true: compares the rendered clip's text (its alpha) with the speaker matte, frame by frame.
            Every word blob must stay at least --min (default 70%) visible whenever the text is fully in. FAIL = move or resize
            the words, re-render, and run it again. A word the speaker hides is pointless: never deliver a FAIL."""
import sys, json, subprocess, pathlib
import numpy as np, cv2

def frames(src, t0, dur, w, fps, alpha=False):
    vf = (f'alphaextract,' if alpha else '') + f'scale={w}:-2,fps={fps},format=gray'
    p = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t0:.3f}', '-i', str(src), '-t', f'{dur:.3f}', '-vf', vf, '-f', 'rawvideo', '-'], capture_output=True, check=True).stdout
    probe = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t0:.3f}', '-i', str(src), '-frames:v', '1', '-vf', vf, '-f', 'rawvideo', '-'], capture_output=True, check=True).stdout
    h = len(probe)//w
    return np.frombuffer(p, np.uint8).reshape(-1, h, w)

def box(plan_p, t0, t1):
    root = pathlib.Path(plan_p).parent; S = json.load(open(root/'work'/'subject.json'))
    W, H, fps = S['width'], S['height'], S['fps']
    fr = [f for f in S['frames'][int(t0*fps):int(t1*fps)+1] if f]
    if not fr: raise SystemExit('no subject detected in that window')
    a = np.array(fr); L, T, R, B = a[:, 2].min()*W, a[:, 3].min()*H, a[:, 4].max()*W, a[:, 5].max()*H
    hx, hy = np.median(a[:, 0])*W, np.median(a[:, 1])*H
    print(json.dumps({'video': [W, H], 'head_center': [round(hx), round(hy)], 'body_box': [round(L), round(T), round(R), round(B)],
        'free_left': [0, 0, round(L), H], 'free_right': [round(R), 0, W, H], 'free_above': [0, 0, W, round(T)]}, indent=1))

def occlusion(plan_p, cid, vmin=0.7):
    root = pathlib.Path(plan_p).parent; P = json.load(open(plan_p)); c = next(c for c in P['clips'] if c['id'] == cid)
    if not P.get('matte'): raise SystemExit('plan has no matte (run base.py with "matte": true)')
    dur = c['out'] - c['in']; w = 640; fps = 20
    VW = int(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width', '-of', 'csv=p=0', str(root/P['matte'])]).strip()); sc = VW/w
    A = frames(root/c['file'], 0, dur, w, fps, alpha=True); Mt = frames(root/P['matte'], c['in'], dur, w, fps)
    n = min(len(A), len(Mt)); tot = A[:n].astype(np.float32).sum((1, 2)); full = tot.max()
    worst = []; ok = True
    for i in range(n):
        if tot[i] < 0.8*full: continue                      # skip frames where text is still popping in/out
        txt = A[i] > 128; hid = txt & (Mt[i] > 128)
        k = max(3, w//80)
        num, lab, stats, _ = cv2.connectedComponentsWithStats(cv2.dilate(txt.astype(np.uint8), np.ones((3, k), np.uint8)))
        for j in range(1, num):
            x, y, bw, bh, area = stats[j]
            if area < 40: continue
            reg = lab == j; t_ = (txt & reg).sum(); v = 1 - (hid & reg).sum()/max(1, t_)
            if v < vmin: ok = False
            worst.append((round(float(v), 2), round(c['in'] + i/fps, 2), [int(x*sc), int(y*sc), int(bw*sc), int(bh*sc)]))
    worst.sort()
    print(('PASS' if ok else 'FAIL') + f': clip {cid}, least visible word blobs (visible share, time, [x,y,w,h] in video px):')
    for v in worst[:6]: print('  ', v)
    return ok

if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'box': box(a[1], float(a[2]), float(a[3]))
    elif a and a[0] == 'occlusion': sys.exit(0 if occlusion(a[1], a[2], float(a[a.index('--min')+1]) if '--min' in a else 0.7) else 1)
    else: print(__doc__)
