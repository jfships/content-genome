"""Extract the speaker's footage for one clip as a JPEG sequence, for the engine's speaker layer (shrink-to-side / corner),
and track the speaker's head in those exact frames so the box re-centres on the subject (not the frame) as it moves.
usage: python3 speaker_frames.py motion/plan.json <clip id> [--in 12.3 --out 22.8]
Uses plan["base_video"] if set (so background treatment and zooms carry through), else plan["video"].
Writes motion/work/frames/<id>/00001.jpg ... (frame 1 = clip in-point) and focus.js (window.SPK_FOCUS, per-frame head position,
smoothed both ways so it never lags). In the clip: speaker:{src:'../work/frames/<id>/', fps:<video fps>, focus:'auto', ...}."""
import sys, json, subprocess, pathlib
a = sys.argv[1:]; opt = lambda k, d: float(a[a.index(k)+1]) if k in a else d
plan_p = pathlib.Path(a[0]); root = plan_p.parent; P = json.load(open(plan_p)); cid = a[1]
c = next((c for c in P.get('clips', []) if c['id'] == cid), {})
t0, t1 = opt('--in', c.get('in')), opt('--out', c.get('out'))
if t0 is None or t1 is None: raise SystemExit('clip not in plan.json yet: pass --in and --out')
src = root/(P.get('base_video') or P['video']); out = root/'work'/'frames'/cid; out.mkdir(parents=True, exist_ok=True)
for f in out.glob('*.jpg'): f.unlink()
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t0:.3f}', '-i', str(src), '-t', f'{t1-t0+0.5:.3f}', '-q:v', '2', str(out/'%05d.jpg')], check=True)
files = sorted(out.glob('*.jpg')); print('wrote', len(files), 'frames to', out)
fps = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate', '-of', 'json', str(src)]))['streams'][0]['r_frame_rate']
fps = eval(fps)
try:
    import cv2, numpy as np
    sys.path.insert(0, str(pathlib.Path(__file__).parent)); from base import Seg, measure
    seg = Seg(); raw = []
    for f in files:
        im = cv2.imread(str(f)); h, w = im.shape[:2]
        me = measure(seg(cv2.cvtColor(cv2.resize(im, (640, int(640*h/w)), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2RGB)))
        raw.append(me[:2] if me else None)
    last = next((r for r in raw if r), [0.5, 0.4]); filled = []
    for r in raw: last = r or last; filled.append(last)
    arr = np.array(filled, float)
    def ema(x, k=0.12):
        y = x.copy()
        for i in range(1, len(y)): y[i] = y[i-1] + k*(x[i]-y[i-1])
        return y
    sm = (ema(arr) + ema(arr[::-1])[::-1]) / 2       # forward + backward: smooth, no lag
    track = [[round(float(x), 4), round(float(y), 4)] for x, y in sm]
    print('head track: x %.2f-%.2f, y %.2f-%.2f' % (sm[:, 0].min(), sm[:, 0].max(), sm[:, 1].min(), sm[:, 1].max()))
except Exception as e:
    print('head tracking unavailable (%s): the box will centre on focus [0.5,0.4]; pass focus:[fx,fy] in the clip instead' % str(e)[:100]); track = []
(out/'focus.js').write_text('window.SPK_FOCUS=' + json.dumps({'fps': fps, 'f': track}) + ';')
