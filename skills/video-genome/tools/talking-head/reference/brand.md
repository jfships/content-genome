# Brand

Everything visual reads from `motion/brand/brand.json`: clips (CSS variables and `window.BRAND`), captions (UI font and accent) and thumbnails.

```json
{
 "name": "Acme",
 "colors": {
   "canvas": "#0F1117",     "surface": "#141824",   "inset": "#1E2433",   "line": "#2A3346",
   "ink": "#F8FAFC",        "muted": "#94A3B8",     "faint": "#64748B",
   "accent": "#6366F1",     "accentSoft": "rgba(99,102,241,.18)",
   "ok": "#22C55E",         "warn": "#FBBF24",      "warnInk": "#1A1205", "bad": "#EF4444"
 },
 "fonts": { "ui": "fonts/Geist-400.woff2", "display": "fonts/SpaceGrotesk-400.woff2", "mono": "fonts/JetBrainsMono-400.woff2" },
 "shape_shadow": "0 0 0 1.5px #1E2433,0 30px 80px -24px rgba(0,0,0,.7)"
}
```

- **Roles, not names.** canvas = clip background. surface = the shape. inset/line = rows, dividers, tracks. ink/muted/faint = text levels. accent = the one brand colour. ok/warn/bad = status only.
- In clip CSS use `var(--accent)` etc. In JS use `BRAND.accent` with a fallback: `const C=Object.assign({accent:'#FF5A1F',…},window.BRAND)`. The shape's `bg` needs a hex, not a CSS variable.
- Fonts: `.disp` = display font (headings, word pops), default text = ui font, `.num`/`.mono` = mono font (numbers, times, IDs). Missing roles fall back to Geist / Geist Mono.
- Variable fonts: one file covers every weight. The file name's weight doesn't matter.

## Getting a brand in

- **HTML brand kit or design-system page** (including bundled pages that unpack with JS):
  `NODE_PATH=motion/node_modules node $SKILL/scripts/brand_from_html.js kit.html motion/brand`
  It saves the Latin font files, `kit.png` (look at it) and `found.json` (fonts, most-used colours, page text with named tokens). Then write brand.json yourself: map the kit's own token names to the roles above.
- **Image or PDF kit, or colours in a message:** read it, write brand.json, and ask for the font files (woff2/ttf/otf). Google Fonts families can be downloaded as files.
- **No brand:** use the skill default (warm gray canvas, white shapes, black ink, one orange accent), or ask for one colour and build roles from it.

## Choosing light or dark
Match the footage. Dim, warm or night footage wants a **dark canvas** (a white cutaway flashes). Bright, daylight or studio footage wants a **light canvas**. If the brand only defines one, derive the other from its greys and say so.

## Check before building
- Accent on surface and ink on surface both readable (contrast ≥ 4.5:1 for text).
- Generic tells: stock Tailwind indigo `#6366F1`, purple gradients, Inter everywhere. If the brand is new or "may change", say so once. Don't rewrite someone's brand.
