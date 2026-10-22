"""Transcript, stills and a contact sheet for every downloaded save in batch.json.
usage: python swipe_prep.py <work folder> [--model small.en] [--step 2] [--redo <id>]
needs: ffmpeg + ffprobe on PATH, pip install faster-whisper pillow
writes per save (<work>/<id>/): transcript.json [{t0,t1,text}], transcript.txt, stills/s000.jpg (every 2 s, 216x384),
contact.jpg (10 columns, time under each), prep.json {duration, stills, speech, creator, caption}.
Skips a save whose prep.json already exists."""
import sys, json, subprocess, pathlib

STEP = 2  # seconds between stills; use 0.5 for fast montage videos

def run(*a): return subprocess.run(a, capture_output=True, text=True)

def duration(v):
    r = run('ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=nw=1:nk=1', str(v))
    return float(r.stdout.strip() or 0)

def stills(v, d, step):
    out = d / 'stills'; out.mkdir(exist_ok=True)
    run('ffmpeg', '-y', '-v', 'error', '-i', str(v), '-vf',
        f'fps=1/{step},scale=216:384:force_original_aspect_ratio=decrease,pad=216:384:(ow-iw)/2:(oh-ih)/2',
        '-q:v', '4', '-start_number', '0', str(out / 's%03d.jpg'))
    return sorted(out.glob('s*.jpg'))

def contact(files, dst, step):
    from PIL import Image, ImageDraw
    cols, w, h, cap = 10, 216, 384, 22
    rows = (len(files) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * w, rows * (h + cap)), 'white')
    dr = ImageDraw.Draw(sheet)
    for i, f in enumerate(files):
        x, y = i % cols * w, i // cols * (h + cap)
        sheet.paste(Image.open(f), (x, y))
        dr.text((x + 6, y + h + 4), f'{i * step:g}s', fill='black')
    sheet.save(dst, quality=80)

def transcribe(v, d, model):
    from faster_whisper import WhisperModel
    wav = d / 'audio.wav'
    run('ffmpeg', '-y', '-v', 'error', '-i', str(v), '-ac', '1', '-ar', '16000', str(wav))
    m = transcribe.m = getattr(transcribe, 'm', None) or WhisperModel(model, device='cpu', compute_type='int8')
    segs, _ = m.transcribe(str(wav), vad_filter=True)
    out = [{'t0': round(s.start, 1), 't1': round(s.end, 1), 'text': s.text.strip()} for s in segs]
    wav.unlink(missing_ok=True)
    return out

def main():
    args = sys.argv[1:]
    model = args[args.index('--model') + 1] if '--model' in args else 'small.en'
    step = float(args[args.index('--step') + 1]) if '--step' in args else STEP
    redo = args[args.index('--redo') + 1] if '--redo' in args else None
    work = pathlib.Path(args[0])
    batch = json.loads((work / 'batch.json').read_text(encoding='utf-8-sig'))
    for it in batch:
        d = work / it['id']; v = d / 'video.mp4'
        if it.get('status') != 'ok' or not v.exists() or ((d / 'prep.json').exists() and it['id'] != redo): continue
        print('prep', it['id'])
        segs = transcribe(v, d, model)
        (d / 'transcript.json').write_text(json.dumps(segs, indent=1), encoding='utf-8')
        (d / 'transcript.txt').write_text('\n'.join(f"[{s['t0']}-{s['t1']}] {s['text']}" for s in segs) or '(no speech)', encoding='utf-8')
        for old in (d / 'stills').glob('s*.jpg') if (d / 'stills').exists() else []: old.unlink()
        files = stills(v, d, step)
        if files: contact(files, d / 'contact.jpg', step)
        info = d / 'video.info.json'
        meta = json.loads(info.read_text(encoding='utf-8')) if info.exists() else {}
        (d / 'prep.json').write_text(json.dumps({
            'duration': round(duration(v), 1), 'stills': len(files), 'step': step, 'speech': bool(segs),
            'creator': meta.get('uploader') or meta.get('channel') or '', 'caption': (meta.get('description') or '')[:600],
        }, indent=1), encoding='utf-8')
    print('done')

if __name__ == '__main__': main()
