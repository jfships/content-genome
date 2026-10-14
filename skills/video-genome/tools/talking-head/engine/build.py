"""Assemble clip fragments + engine + fonts + brand into self-contained HTML files.
usage: python3 build.py <out_dir> clips/01-name.html [clips/02-name.html ...] [--brand motion/brand/brand.json]

Brand: if --brand is not given, <out_dir>/../brand/brand.json is used when it exists.
brand.json -> CSS variables (--canvas, --surface, --ink, --muted, --accent ...), window.BRAND (same keys, for JS),
and @font-face 'BrandUI' / 'BrandDisplay' / 'BrandMono' from font files next to brand.json."""
import base64, json, re, sys, pathlib
E = pathlib.Path(__file__).resolve().parent
b64 = lambda p: base64.b64encode(open(p, 'rb').read()).decode()
CURSOR = '<svg id="cursor" viewBox="0 0 40 56"><path d="M3 3 L3 41 L12.5 32 L19 47 L25.5 44.2 L19.2 29.8 L32 29.8 Z" fill="#0B0B0B" stroke="#fff" stroke-width="2.6" stroke-linejoin="round"/></svg>'
FMT = {'.woff2': 'woff2', '.woff': 'woff', '.ttf': 'truetype', '.otf': 'opentype'}

def brand_css(bp):
    if not bp or not pathlib.Path(bp).exists(): return '', '{}'
    B = json.load(open(bp)); d = pathlib.Path(bp).parent
    cols = B.get('colors', {})
    css = ':root{' + ''.join(f'--{k}:{v};' for k, v in cols.items())
    if B.get('shape_shadow'): css += f"--shape-shadow:{B['shape_shadow']};"
    css += '}'
    for role, fam in (('ui', 'BrandUI'), ('display', 'BrandDisplay'), ('mono', 'BrandMono')):
        f = B.get('fonts', {}).get(role)
        if f and (d / f).exists():
            p = d / f
            css += f"@font-face{{font-family:'{fam}';src:url(data:font/{FMT.get(p.suffix,'woff2')};base64,{b64(p)}) format('{FMT.get(p.suffix,'woff2')}');font-weight:100 900}}"
    return css, json.dumps(cols)

def build(src, dst, bp):
    frag = open(src, encoding='utf-8').read()
    m = re.search(r'<title>(.*?)</title>', frag); title = m.group(1) if m else pathlib.Path(src).stem
    css = ''.join(re.findall(r'<style>(.*?)</style>', frag, re.S))
    slot = lambda n: (re.search(rf'<div data-slot="{n}">(.*?)</div><!--/{n}-->', frag, re.S) or [None, ''])[1]
    js = ''.join(re.findall(r'<script>(.*?)</script>', frag, re.S))
    base = open(E/'base.css').read().replace('__GEIST__', b64(E/'fonts/Geist-Variable.woff2')).replace('__GEISTMONO__', b64(E/'fonts/GeistMono-Medium.woff2'))
    bcss, bjs = brand_css(bp)
    # speaker layer: load the per-frame head track written by speaker_frames.py (focus.js next to the frames)
    sm = re.search(r"speaker\s*:\s*\{[^}]*?src\s*:\s*'([^']+)'", js)
    foc = f'<script src="{sm.group(1)}focus.js"></script>' if sm else ''
    html = (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title><style>{base}{bcss}{css}</style></head><body>\n'
            f'<div id="wrap"><div id="stage"><div id="world">{slot("world")}<div id="shape">{slot("shape")}</div>{slot("over")}</div><div id="spk"><img alt=""></div>{slot("top")}{CURSOR}</div></div>\n'
            f'<script>window.BRAND={bjs};</script>{foc}<script>{open(E/"motion.js").read()}</script><script>{js}</script></body></html>')
    open(dst, 'w', encoding='utf-8').write(html)

if __name__ == '__main__':
    args = sys.argv[1:]; bp = None
    if '--brand' in args: i = args.index('--brand'); bp = args[i+1]; del args[i:i+2]
    out = pathlib.Path(args[0]); out.mkdir(parents=True, exist_ok=True)
    if bp is None:
        cand = out.parent/'brand'/'brand.json'
        bp = str(cand) if cand.exists() else None
    for s in args[1:]:
        d = out/(pathlib.Path(s).stem + '.html'); build(s, d, bp); print('built', d, '(brand: %s)' % (bp or 'default'))
