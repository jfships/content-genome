"""Captions in two steps, so you can fix the phrasing by hand in between.

1) phrases:  python3 captions.py phrases motion/work/words.json motion/plan.json motion/work/captions.json
   Splits words into short phrases (at punctuation and pauses, max ~5 words / 32 chars, no one-word orphans),
   drops fillers (um, uh), collapses stutters ("and and"), applies plan["caption_fixes"] ({"wrong":"right"}),
   and applies each clip's caption rule for its window: plan clip "captions": "hide" | "high" | "show"
   (defaults: full and pip -> hide, everything else -> show). READ captions.json and fix awkward splits before step 2.
   Each phrase: {"a":start,"b":end,"text":"...","pos":"low"|"high","words":[[t,"word"],...]}

2) ass:      python3 captions.py ass motion/work/captions.json motion/work/captions.ass [--style plain|highlight]
             [--brand motion/brand/brand.json] [--size 92] [--low 140] [--high 320] [--res 2560x1440]
   Writes an ASS subtitle file plus a static TTF of the brand UI font (weight 600) in motion/work/capfonts/
   (libass cannot read woff2). composite.py burns it in last, on top of everything.
   plain: white text, soft shadow, no box. highlight: the word being spoken turns the brand accent colour.
   Sizes are for the video's own resolution: scale --size/--low/--high with the height (92/140/320 at 1440p)."""
import sys, json, pathlib, re

FILL = {'um', 'uh', 'erm', 'uhm', 'hmm', 'ah'}
def norm(w): return re.sub(r'[^\w\']', '', w.lower())

def phrases(words_p, plan_p, out_p):
    W = json.load(open(words_p)); P = json.load(open(plan_p)) if plan_p and pathlib.Path(plan_p).exists() else {}
    if isinstance(W, dict): W = W.get('words', [])   # remap_words.py output: {"words": [...], "duration": s}
    fixes = P.get('caption_fixes', {})
    ws = []
    for w in W:
        if norm(w['w']) in FILL: continue
        t = w['w']
        for a, b in fixes.items(): t = re.sub(rf'\b{re.escape(a)}\b', b, t)
        if ws and norm(ws[-1]['w']) == norm(t): ws[-1] = {**w, 'w': t}; continue   # stutter: "and and"
        if ws and len(norm(ws[-1]['w'])) >= 1 and norm(t).startswith(norm(ws[-1]['w'])) and "'" in t: ws[-1] = {**w, 'w': t}; continue  # false start: "what what's", "I I'm"
        ws.append({**w, 'w': t})
    # ASR often capitalises the first word of its own segments: lower-case a word mid-sentence when the transcript
    # also uses it in lower case elsewhere (keeps names like "Sam" or "YouTube" intact)
    lower = {norm(w['w']) for w in ws if w['w'][:1].islower()} | set('a an and any are as at be but by can do for from have how if in is it its just my no not of on or our so that the their then there these this to up was we what when where which who why will with you your'.split())
    for i, w in enumerate(ws):
        if i and w['w'][:1].isupper() and ws[i-1]['w'][-1] not in '.?!' and norm(w['w']) in lower and norm(w['w']) != 'i':
            w['w'] = w['w'][:1].lower() + w['w'][1:]
    for i, w in enumerate(ws):
        nx = ws[i+1]['t0'] if i+1 < len(ws) else w['t0']+0.6
        w['t1'] = min(w.get('t1', nx) or nx, nx, w['t0']+0.8)
    chunks, cur = [], []
    for w in ws:
        if cur and (w['t0']-cur[-1]['t1'] > 0.45 or cur[-1]['w'][-1] in '.,?!'): chunks.append(cur); cur = []
        cur.append(w)
    if cur: chunks.append(cur)
    L = lambda p: len(' '.join(x['w'] for x in p))
    merged, carry = [], []
    for i, c in enumerate(chunks):
        c = carry + c; carry = []
        if len(c) == 1 and len(chunks) > 1:
            prev_ok = merged and merged[-1][-1]['w'][-1] not in '.?!' and c[0]['t0']-merged[-1][-1]['t1'] < 1.1 and L(merged[-1]+c) <= 32
            if prev_ok: merged[-1] += c; continue
            if i+1 < len(chunks) and chunks[i+1][0]['t0']-c[-1]['t1'] < 1.1: carry = c; continue
        merged.append(c)
    if carry: merged.append(carry)
    ph = []
    for c in merged:
        n = 1
        while True:
            k = len(c)/n; parts = [c[round(i*k):round((i+1)*k)] for i in range(n)]
            if all(len(p) <= 5 and L(p) <= 32 for p in parts) or n >= len(c): break
            n += 1
        ph += [p for p in parts if p]
    # windows from the plan
    rules = []
    for c in P.get('clips', []):
        r = c.get('captions') or ('hide' if c.get('kind') in ('full', 'pip') else 'show')
        rules.append((c['in'], c['out'], r))
    out, prev_end = [], '.'
    for p in ph:
        a, b = p[0]['t0']-0.05, p[-1]['t1']+0.15
        text = ' '.join(x['w'] for x in p).rstrip('.,')
        if prev_end[-1] in '.?!': text = text[:1].upper()+text[1:]
        prev_end = p[-1]['w']
        segs = [(a, b)]; pos = 'low'
        for c0, c1, r in rules:
            if r == 'hide':
                ns = []
                for s0, s1 in segs:
                    if s1 <= c0 or s0 >= c1: ns.append((s0, s1)); continue
                    if s0 < c0 and c0-s0 > 0.4: ns.append((s0, c0))
                    if s1 > c1 and s1-c1 > 0.4: ns.append((c1, s1))
                segs = ns
            elif r == 'high' and b > c0 + 0.3 and a < c1: pos = 'high'
        for s0, s1 in segs:
            out.append({'a': round(s0, 2), 'b': round(s1, 2), 'text': text, 'pos': pos, 'words': [[x['t0'], x['w']] for x in p]})
    out.sort(key=lambda e: e['a'])
    for i in range(len(out)-1):
        if out[i]['b'] > out[i+1]['a'] or out[i+1]['a']-out[i]['b'] < 0.25: out[i]['b'] = out[i+1]['a']
    json.dump(out, open(out_p, 'w'), indent=1, ensure_ascii=False)
    for e in out: print(f"{e['a']:7.2f}-{e['b']:7.2f} {e['pos']:4} {e['text']}")

def ttf_font(brand_p, work):
    from fontTools.ttLib import TTFont
    from fontTools.varLib import instancer
    src = pathlib.Path(__file__).resolve().parent.parent/'engine'/'fonts'/'Geist-Variable.woff2'
    if brand_p and pathlib.Path(brand_p).exists():
        B = json.load(open(brand_p)); f = B.get('fonts', {}).get('ui')
        if f and (pathlib.Path(brand_p).parent/f).exists(): src = pathlib.Path(brand_p).parent/f
    f = TTFont(str(src)); f.flavor = None
    if 'fvar' in f and any(a.axisTag == 'wght' for a in f['fvar'].axes): f = instancer.instantiateVariableFont(f, {'wght': 600})
    fam = f['name'].getDebugName(16) or f['name'].getDebugName(1)
    d = work/'capfonts'; d.mkdir(parents=True, exist_ok=True); f.save(str(d/'caption.ttf'))
    return fam

def ass_color(h, a='00'): h = h.lstrip('#'); return f'&H{a}{h[4:6]}{h[2:4]}{h[0:2]}'.upper()

def ass(caps_p, out_p, style='plain', brand_p=None, size=92, low=140, high=320, res='2560x1440'):
    E = json.load(open(caps_p)); out_p = pathlib.Path(out_p)
    fam = ttf_font(brand_p, out_p.parent)
    acc = '#FF5A1F'
    if brand_p and pathlib.Path(brand_p).exists(): acc = json.load(open(brand_p)).get('colors', {}).get('accent', acc)
    RX, RY = res.split('x'); white = ass_color('#F8FAFC')
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {RX}
PlayResY: {RY}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: low,{fam},{size},{white},{white},&H00000000,&H90000000,0,0,0,0,100,100,0,0,1,0,4,2,200,200,{low},1
Style: high,{fam},{size},{white},{white},&H00000000,&H90000000,0,0,0,0,100,100,0,0,1,0,4,2,200,200,{high},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ts = lambda x: f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"
    ev = []
    for e in E:
        if style == 'highlight' and e.get('words'):
            ws = e['words']; toks = e['text'].split(' ')
            if len(toks) != len(ws): toks = [w for _, w in ws]
            for i, (t, _) in enumerate(ws):
                a = max(e['a'], t if i else e['a']); b = ws[i+1][0] if i+1 < len(ws) else e['b']; b = min(b, e['b'])
                if b-a < 0.03: continue
                txt = ' '.join((f'{{\\c{ass_color(acc)}}}{w}{{\\c{white}}}' if j == i else w) for j, w in enumerate(toks))
                ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},{e['pos']},,0,0,0,,{{\\blur2}}{txt}")
        else:
            ev.append(f"Dialogue: 0,{ts(e['a'])},{ts(e['b'])},{e['pos']},,0,0,0,,{{\\fad(80,80)\\blur2}}{e['text']}")
    out_p.write_text(head + '\n'.join(ev) + '\n'); print('wrote', out_p, 'font:', fam, '| fontsdir:', out_p.parent/'capfonts')

if __name__ == '__main__':
    a = sys.argv[1:]
    opt = lambda k, d: a[a.index(k)+1] if k in a else d
    if a[0] == 'phrases': phrases(a[1], a[2], a[3])
    elif a[0] == 'ass': ass(a[1], a[2], opt('--style', 'plain'), opt('--brand', None), int(opt('--size', 92)), int(opt('--low', 140)), int(opt('--high', 320)), opt('--res', '2560x1440'))
    else: print(__doc__)
