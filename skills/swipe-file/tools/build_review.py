"""Build the review page for every save in batch.json that has a cards.json.
usage: python build_review.py <work folder>   ->  <work>/review.html (publish it as the artifact)
cards.json (written by Claude per save, see SKILL.md "Cards"):
  {"title", "gist", "content": [{"id","tag","title","line","gist"}], "visual": [{"id","tag","title","line","vis","t":[seconds]}]}
Stills come from <id>/stills (one every prep step, default 2 s); a visual card's "t" picks the nearest ones."""
import sys, json, base64, pathlib, datetime

STEP = 2
TPL = pathlib.Path(__file__).resolve().parent.parent / 'templates' / 'review.html'

def uri(p): return 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()

def main():
    work = pathlib.Path(sys.argv[1])
    batch = json.loads((work / 'batch.json').read_text(encoding='utf-8-sig'))
    saves = []
    for it in batch:
        d = work / it['id']; cf = d / 'cards.json'
        if not cf.exists(): continue
        cards = json.loads(cf.read_text(encoding='utf-8'))
        prep = json.loads((d / 'prep.json').read_text(encoding='utf-8')) if (d / 'prep.json').exists() else {}
        stills = sorted((d / 'stills').glob('s*.jpg'))
        step = prep.get('step', STEP)
        pick = lambda t: stills[min(len(stills) - 1, round(t / step))] if stills else None
        for c in cards.get('visual', []):
            c['imgs'] = [uri(p) for p in map(pick, c.get('t', [])) if p]
        n = len(stills)
        thumbs = [uri(stills[i]) for i in sorted({0, n // 3, 2 * n // 3, n - 1}) if n]
        secs = prep.get('duration', 0)
        saves.append({'id': it['id'], 'url': it['url'], 'title': cards['title'], 'gist': cards.get('gist', ''),
                      'creator': cards.get('creator') or prep.get('creator', ''),
                      'length': f'{int(secs // 60)} min {round(secs % 60)} s' if secs >= 60 else f'{round(secs)} s',
                      'thumbs': thumbs, 'content': cards.get('content', []), 'visual': cards.get('visual', [])})
    if not saves: raise SystemExit('no cards.json found; write the cards first')
    html = TPL.read_text(encoding='utf-8')
    html = html.replace('/*SAVES*/[]', json.dumps(saves, ensure_ascii=False).replace('</', '<\\/'))
    html = html.replace('/*BATCH*/""', json.dumps(datetime.date.today().isoformat()))
    out = work / 'review.html'; out.write_text(html, encoding='utf-8')
    print(out, f'{len(saves)} saves, {out.stat().st_size // 1024} KB')

if __name__ == '__main__': main()
