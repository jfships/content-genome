"""Final composite: speaker footage (treated base) + clips + things behind the speaker + captions. Hard cuts, original audio.
usage: python3 composite.py motion/plan.json motion/out/preview.mp4 [--deliver motion/out/final-1080p.mp4 --size 1920x1080 --fps 30 --crf 21]
(raise --crf to 23-25 to make the delivered file smaller, e.g. to fit an upload or transfer limit)

plan.json keys used:
  video       source footage (audio is always taken from here)
  base_video  optional, from base.py (background treatment + zooms). Used instead of video for the picture.
  matte       optional, from base.py. Needed for clips with "behind": true.
  clips[]     {id, in, out, kind: full|panel|pip|pop, file, behind?: bool}
              full/pip = opaque full-frame clips (.mp4). panel/pop = transparent (.mov ProRes 4444).
              behind: the clip is drawn, then the speaker (cut out with the matte) is drawn back on top of it.
  captions    optional ASS file from captions.py; burned last, fonts from work/capfonts.
Clips shorter than their slot hold their last frame."""
import json, sys, subprocess, pathlib
a = sys.argv[1:]; opt = lambda k, d: a[a.index(k)+1] if k in a else d
plan_p = pathlib.Path(a[0]); base = plan_p.parent; P = json.load(open(plan_p)); out = a[1]
rel = lambda f: str((base/f).resolve()) if not pathlib.Path(f).is_absolute() else f
pic = P.get('base_video') or P['video']
cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-i', rel(pic), '-i', rel(P['video'])]; n = 2; fc = []
behind = [c for c in P['clips'] if c.get('behind')]
if behind:
    if not P.get('matte'): raise SystemExit('clips with "behind": true need plan["matte"] (run base.py with "matte": true)')
    cmd += ['-i', rel(P['matte'])]; mi = n; n += 1
    fc.append(f'[0:v]split=2[b0][bp]'); fc.append(f'[{mi}:v]format=gray[mt]'); fc.append('[bp][mt]alphamerge[person]')
    fc.append(f'[person]split={len(behind)}' + ''.join(f'[pp{i}]' for i in range(len(behind))))
    last = 'b0'
else: last = '0:v'
bi = 0
for i, c in enumerate(P['clips'], 1):
    cmd += ['-i', rel(c['file'])]; k = n; n += 1
    fc.append(f"[{k}:v]format=yuva444p,tpad=stop_mode=clone:stop_duration=2,setpts=PTS-STARTPTS+{c['in']}/TB[c{i}]")
    fc.append(f"[{last}][c{i}]overlay=enable='between(t,{c['in']},{c['out']})':eof_action=pass[v{i}]"); last = f'v{i}'
    if c.get('behind'):
        fc.append(f"[{last}][pp{bi}]overlay=enable='between(t,{c['in']},{c['out']})'[vb{i}]"); last = f'vb{i}'; bi += 1
if P.get('captions'):
    fd = str((base/'work'/'capfonts').resolve())
    fc.append(f"[{last}]ass={rel(P['captions'])}:fontsdir={fd}[vc]"); last = 'vc'
fc.append(f'[{last}]format=yuv420p[v]')
enc = ['-map', '[v]', '-map', '1:a?', '-c:v', 'libx264', '-crf', '18', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', '-shortest']
subprocess.run(cmd + ['-filter_complex', ';'.join(fc)] + enc + [out], check=True); print('wrote', out)
d = opt('--deliver', None)
if d:
    w, h = opt('--size', '1920x1080').split('x')
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', out, '-vf', f'scale={w}:{h}:flags=lanczos,fps={opt("--fps", "30")}', '-c:v', 'libx264', '-crf', opt('--crf', '21'),
                    '-preset', 'medium', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', d], check=True); print('wrote', d)
