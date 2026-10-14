"""Word-level transcript from the video's own audio.
usage: python3 transcribe.py motion/work/source.mp4 motion/work [--lang en] [--engine auto|whisper|parakeet]
writes: work/audio.wav, work/words.json [{t0,t1,w}], work/words.txt (t:word ...), work/transcript.srt

Engines, tried in order with --engine auto:
  whisper  : faster-whisper (pip install faster-whisper). Model download comes from Hugging Face.
  parakeet : sherpa-onnx + NVIDIA Parakeet TDT 0.6B v2 (English only), model downloaded from GitHub releases.
             Use it when Hugging Face is blocked. pip install sherpa-onnx
Models are cached in motion/models/."""
import sys, os, json, subprocess, pathlib, urllib.request, tarfile

def ts(x): return f"{int(x//3600):02d}:{int(x%3600//60):02d}:{x%60:06.3f}".replace('.', ',')

def whisper(wav, lang, models):
    from faster_whisper import WhisperModel
    name = 'medium.en' if lang == 'en' else 'medium'
    m = WhisperModel(name, device='cpu', compute_type='int8', download_root=str(models))
    segs, _ = m.transcribe(str(wav), word_timestamps=True, language=lang, vad_filter=True)
    words, cues = [], []
    for s in segs:
        cues.append((s.start, s.end, s.text.strip()))
        for w in s.words: words.append({'t0': round(w.start, 2), 't1': round(w.end, 2), 'w': w.word.strip()})
    return words, cues

GH = 'https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/'
def fetch(url, dst):
    if not dst.exists():
        print('downloading', url); urllib.request.urlretrieve(url, dst)

def parakeet(wav, lang, models):
    if lang != 'en': raise RuntimeError('parakeet is English only')
    import sherpa_onnx, wave, numpy as np
    D = models/'sherpa-onnx-nemo-parakeet-tdt-0.6b-v2-int8'
    if not D.exists():
        tb = models/'parakeet.tar.bz2'; fetch(GH + 'sherpa-onnx-nemo-parakeet-tdt-0.6b-v2-int8.tar.bz2', tb)
        tarfile.open(tb).extractall(models); tb.unlink()
    vadm = models/'silero_vad.onnx'; fetch(GH + 'silero_vad.onnx', vadm)
    rec = sherpa_onnx.OfflineRecognizer.from_transducer(encoder=str(D/'encoder.int8.onnx'), decoder=str(D/'decoder.int8.onnx'),
        joiner=str(D/'joiner.int8.onnx'), tokens=str(D/'tokens.txt'), model_type='nemo_transducer', num_threads=os.cpu_count() or 2)
    w = wave.open(str(wav)); sr = w.getframerate()
    a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32)/32768
    cfg = sherpa_onnx.VadModelConfig(); cfg.silero_vad.model = str(vadm); cfg.silero_vad.min_silence_duration = 0.35
    cfg.silero_vad.max_speech_duration = 12; cfg.sample_rate = sr
    vad = sherpa_onnx.VoiceActivityDetector(cfg, buffer_size_in_seconds=600); ws = cfg.silero_vad.window_size; segs = []
    def drain():
        while not vad.empty(): segs.append((vad.front.start, np.array(vad.front.samples))); vad.pop()
    for i in range(0, len(a), ws): vad.accept_waveform(a[i:i+ws]); drain()
    vad.flush(); drain()
    words, cues = [], []
    for st, s in segs:
        t0 = st/sr; stream = rec.create_stream(); stream.accept_waveform(sr, s); rec.decode_stream(stream); r = stream.result
        cur = None; seg_words = []
        for tok, tt in zip(r.tokens, r.timestamps):
            if tok.startswith(' ') or cur is None:
                if cur: seg_words.append(cur)
                cur = {'t0': round(t0+tt, 2), 'w': tok.strip()}
            else: cur['w'] += tok
        if cur: seg_words.append(cur)
        end = t0 + len(s)/sr
        for i, x in enumerate(seg_words): x['t1'] = round(min(seg_words[i+1]['t0'] if i+1 < len(seg_words) else end, x['t0']+0.8), 2)
        words += seg_words; cues.append((t0, end, r.text.strip()))
    return words, cues

if __name__ == '__main__':
    args = sys.argv[1:]
    opt = lambda k, d: args[args.index(k)+1] if k in args else d
    src, work = pathlib.Path(args[0]), pathlib.Path(args[1]); lang = opt('--lang', 'en'); eng = opt('--engine', 'auto')
    models = work.parent/'models'; models.mkdir(parents=True, exist_ok=True); work.mkdir(parents=True, exist_ok=True)
    wav = work/'audio.wav'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(src), '-ac', '1', '-ar', '16000', str(wav)], check=True)
    order = ['whisper', 'parakeet'] if eng == 'auto' else [eng]; last = None
    for e in order:
        try: words, cues = (whisper if e == 'whisper' else parakeet)(wav, lang, models); print('engine:', e); break
        except Exception as ex: last = ex; print(f'{e} failed: {str(ex)[:200]}')
    else: raise SystemExit(f'no transcription engine worked: {last}')
    json.dump(words, open(work/'words.json', 'w'), indent=0)
    open(work/'words.txt', 'w').write(' '.join(f"{x['t0']:.2f}:{x['w']}" for x in words))
    open(work/'transcript.srt', 'w').write('\n'.join(f"{i}\n{ts(a)} --> {ts(b)}\n{t}\n" for i, (a, b, t) in enumerate(cues, 1)))
    print(len(words), 'words ->', work/'words.json')
