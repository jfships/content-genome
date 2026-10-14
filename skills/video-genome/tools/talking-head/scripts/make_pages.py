"""Write viewer.html (step through clips) and compare.html (original vs preview, synced) next to the renders.
usage: python3 make_pages.py motion/plan.json motion/out/preview.mp4"""
import json, sys, pathlib, os
S = pathlib.Path(__file__).resolve().parent.parent / 'templates'
plan_p = pathlib.Path(sys.argv[1]); P = json.load(open(plan_p)); base = plan_p.parent
preview = pathlib.Path(sys.argv[2]).resolve(); out = preview.parent
rel = lambda f: os.path.relpath((base / f).resolve(), out)
fmt = lambda t: f"{int(t//60)}:{t%60:05.2f}"
title = P.get('title', 'Video')
def web_src(c):
    f = (base / c['file']).resolve()
    if f.suffix.lower() == '.mov':  # browsers can't play ProRes: make an on-black preview for the page
        pv = out / (f.stem + '_preview.mp4')
        os.system(f'ffmpeg -loglevel error -y -f lavfi -i color=black:s=1920x1080 -i "{f}" -filter_complex "[0][1]overlay=shortest=1" -c:v libx264 -crf 20 -pix_fmt yuv420p "{pv}"')
        return pv.name
    return os.path.relpath(f, out)
clips = [{'n': c['id'], 't': c['title'], 'tc': f"{fmt(c['in'])} – {fmt(c['out'])}", 'q': c.get('line', ''), 'f': pathlib.Path(c['file']).name,
          'src': web_src(c), **({'alpha': True} if c.get('kind') in ('panel', 'pop') else {})} for c in P['clips']]
clips.insert(0, {'n': '▶', 'full': True, 't': 'Full preview · your video with every clip', 'tc': 'whole video', 'q': 'Composite for review. For the final cut, place the clips in your editor.', 'f': preview.name, 'src': preview.name})
v = open(S / 'viewer.html').read().replace('/*CLIPS*/[]', json.dumps(clips, ensure_ascii=False)).replace('/*TITLE*/', title).replace('/*SUB*/', f"{len(P['clips'])} clips + full preview")
open(out / 'viewer.html', 'w').write(v)
dur = float(os.popen(f'ffprobe -v error -show_entries format=duration -of csv=p=0 "{preview}"').read().strip() or 0)
marks = [[c['in'], c['out'], c['id'], c['title']] for c in P['clips']]
c = (open(S / 'compare.html').read().replace('/*DUR*/0', f'{dur:.2f}').replace('/*MARKS*/[]', json.dumps(marks, ensure_ascii=False))
     .replace('/*ORIG*/', rel(P['video'])).replace('/*BROLL*/', preview.name).replace('/*TITLE*/', title)
     .replace('/*SUB*/', 'Left or top is the original. Right or bottom has the motion graphics cut in.'))
open(out / 'compare.html', 'w').write(c); print('wrote', out / 'viewer.html', 'and', out / 'compare.html')
# TIMING.md for the editor
rows = ['| File | In | Out | Treatment | Covers the line |', '|---|---|---|---|---|']
for c in P['clips']:
    rows.append(f"| {pathlib.Path(c['file']).name} | {fmt(c['in'])} | {fmt(c['out'])} | { {'panel':'transparent panel','pop':'transparent word pop','pip':'speaker shrinks to corner','full':'full-frame cutaway'}.get(c.get('kind'),'full-frame cutaway') }{' (behind speaker)' if c.get('behind') else ''} | {c.get('line', '')} |")
notes = P.get('notes', [])
open(out / 'TIMING.md', 'w').write(f"# Motion graphics for {title}\n\n**The finished video is the composite (preview/final mp4): upload that.** The clips below are only for re-editing in your own editor. Each file name ends with its timeline in-point (`0m32s40` = 0:32.40). Transparent clips are ProRes 4444 .mov (a small .webm copy with transparency opens in CapCut and DaVinci Resolve): put them on a track above the video. Background treatment, zoom-ins, things placed behind the speaker and captions are baked into the composite only.\n\n" + '\n'.join(rows) + ('\n\nNotes\n' + '\n'.join('- ' + n for n in notes) if notes else '') + '\n')
print('wrote', out / 'TIMING.md')
