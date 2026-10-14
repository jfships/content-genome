"""Code-drawn mocks for video-genome example pages (no photos needed).

Real runs replace these with real stills of the creator's footage or the built scene
(Playwright stills for HyperFrames scenes, beats.js for engine clips). Every mock is a
16:9 SVG at viewBox 320x180 unless noted; 9:16 mocks use 108x192.
"""
BG = "#1d2430"; BG2 = "#252e3c"; SP = "#8a94a6"; INK = "#EEF1F5"


def svg(inner, bg=BG, vb="0 0 320 180"):
    return (f'<svg viewBox="{vb}" style="position:absolute;inset:0;width:100%;height:100%;background:{bg}">'
            f'{inner}</svg>')


def speaker(x, s=1.0, fill=SP, face=None):
    hy = 70 * s
    out = (f'<ellipse cx="{x}" cy="{hy}" rx="{22*s}" ry="{27*s}" fill="{fill}"/>'
           f'<path d="M{x-62*s},180 C{x-60*s},{hy+48*s} {x-30*s},{hy+34*s} {x},{hy+34*s} '
           f'C{x+30*s},{hy+34*s} {x+60*s},{hy+48*s} {x+62*s},180 Z" fill="{fill}"/>')
    if face:
        d = 1 if face == "right" else -1
        out += f'<path d="M{x+30*d*s},{hy-8*s} l{12*d*s},{8*s} l{-12*d*s},{8*s} Z" fill="{fill}" opacity=".9"/>'
    return out


def text(x, y, size, t, fill=INK, weight=700, anchor="start", font="Inter,Arial,sans-serif"):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}">{t}</text>')


def panel(x, y, w, h, accent, lines=3, title=True, fill=BG2):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}" stroke="{accent}" stroke-width="1.2"/>'
    ly = y + 10
    if title:
        th = max(6, h * 0.14)
        out += f'<rect x="{x+8}" y="{ly}" width="{w*0.62}" height="{th}" rx="2" fill="{accent}"/>'
        ly += th + 7
    for i in range(lines):
        if ly + 4 > y + h - 4:
            break
        out += f'<rect x="{x+8}" y="{ly}" width="{(w-16)*(0.9 if i % 2 == 0 else 0.7)}" height="4" rx="2" fill="{INK}" opacity=".7"/>'
        ly += 9
    return out


def lower_third(name, role, accent, ink=INK, font="Inter,Arial,sans-serif"):
    return (f'<rect x="16" y="132" width="132" height="30" rx="2" fill="{BG2}"/>'
            f'<rect x="16" y="132" width="4" height="30" fill="{accent}"/>'
            + text(26, 146, 11, name, ink, 800, font=font) + text(26, 157, 7.5, role, ink, 500))


def curve(points, color, label=""):
    """An energy line across a 16:9 card: points are (x 0..1, y 0..1, 1 = top)."""
    pts = " ".join(f"{20+p[0]*280:.0f},{150-p[1]*110:.0f}" for p in points)
    return (f'<line x1="20" y1="150" x2="300" y2="150" stroke="{SP}" stroke-opacity=".5"/>'
            f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3" stroke-linejoin="round"/>'
            + (text(160, 24, 11, label, INK, 600, "middle") if label else ""))


def thumb(title, accent, face_x=230, bg=BG):
    return svg(speaker(face_x, 1.1) + text(16, 70, 26, title.split("|")[0], INK, 900)
               + (text(16, 100, 26, title.split("|")[1], accent, 900) if "|" in title else ""), bg)


def phone(inner):
    return svg(inner, BG, "0 0 108 192")
