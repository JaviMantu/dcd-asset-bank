"""Scene library of dynamic-commercial-decks: the shared helpers and base scenes, harvested from the Amaris decks of 2026-09
(the class «Presentar a Amaris con IA», the energía deck v4 and the pagos deck v2). Each scene lands once, within 2 s of the slide
becoming active, then breathes with an ambient loop while the presenter talks.

Engine contract (aula@0.1.0): fn(sl, ctx) -> (svg, D, freeze). The engine restarts the scene clock at 0 on entry
(setCurrentTime(0)), so a one-shot animation (fill="freeze") replays on every visit. Under reduced motion it seeks
to D * freeze (10.8 s here), when every entrance has finished. Markup holds the final pose; figures never animate.
Colors only from the pack (var(--...)); labels go through T/TC/TCW so they translate.
"""
from __future__ import annotations

import math
import os

from aula.core import register
from aula.i18n import _
from aula.svg import E, TC, TCW, T, bold_width, check, current_factor, fit, glow, move, person, pulse_r, spark, spin, token

D = 12          # loop period of every scene, seconds
FREEZE = .9     # reduced-motion frame: D * FREEZE = 10.8 s, after every entrance
LAND_MAX = 2.0  # no entrance may end later than this after the slide becomes active
W6 = 'font-weight="600"'
EASE = "0 0 1 1;.2 .8 .2 1"

# ---------------------------------------------------------------- orientation (0.5.0: every deck ships desktop + mobile)
# scripts/build.py renders the deck twice: desktop (DCD_ORIENT unset, the 1600x900 stage) and mobile
# (DCD_ORIENT=portrait, a 900x1600 stage; scripts/mobile.py rewrites the page). A portrait-aware scene draws on
# CANVAS() inside ART_ZONE(layout) and wraps its svg with portrait_mark(); any other scene is nested full-width
# under the text by mobile.py (the legacy fallback).
def ORIENT():
    """«portrait» while the mobile version is being built, else «landscape»."""
    return "portrait" if os.environ.get("DCD_ORIENT") == "portrait" else "landscape"


def CANVAS():
    """The stage of the version being built: (1600, 900) desktop, (900, 1600) mobile."""
    return (900, 1600) if ORIENT() == "portrait" else (1600, 900)


# the art zone per layout, where the text column is not: desktop «left» keeps the text at x 96-776, «top» above y 380;
# mobile puts every text block on top (y 0-600) and the art below
_ART = {"landscape": {"left": (820, 60, 740, 780), "top": (80, 390, 1440, 440), "full": (0, 0, 1600, 900)},
        "portrait": {"left": (40, 640, 820, 900), "top": (40, 640, 820, 900), "full": (0, 0, 900, 1600)}}


def ART_ZONE(layout="left"):
    """(x, y, w, h) of the art zone for a layout in the version being built."""
    z = _ART[ORIENT()]
    return z.get(layout, z["left"])


def portrait_mark(svg):
    """Tag a portrait-aware scene's output so mobile.py gives it the 900x1600 viewBox (no-op on desktop)."""
    return f'<g data-orient="portrait">{svg}</g>' if ORIENT() == "portrait" else svg



# ---------------------------------------------------------------- one-shot entrance (lands once)
def _once(attr, frm, to, begin, dur, typ=""):
    end = begin + dur
    if end > LAND_MAX + 1e-9:
        raise ValueError(f"entrance ends at {end:.2f} s, after {LAND_MAX} s")
    if begin <= 0:
        kt, vals, spl = "0;1", f"{frm};{to}", EASE.split(";")[1]
    else:
        kt, vals, spl = f"0;{begin / end:.4f};1", f"{frm};{frm};{to}", EASE
    tail = f'dur="{end:.3f}s" fill="freeze" keyTimes="{kt}" values="{vals}" calcMode="spline" keySplines="{spl}"'
    if typ:
        return f'<animateTransform attributeName="transform" type="{typ}" additive="sum" {tail}/>'
    return f'<animate attributeName="{attr}" {tail}/>'


def land(inner, begin=.1, dur=.55, dy=18, dx=0):
    """inner fades in and settles from (dx, dy): its markup is already the final pose."""
    return f'<g>{_once("opacity", 0, 1, begin, dur)}{_once("", f"{dx} {dy}", "0 0", begin, dur, "translate")}{inner}</g>'


def pop(inner, x, y, begin=.3, dur=.45):
    """inner (drawn around 0,0) scales up at (x, y)."""
    return (f'<g transform="translate({x:.1f} {y:.1f})"><g>{_once("opacity", 0, 1, begin, dur)}'
            f'{_once("", ".6 .6", "1 1", begin, dur, "scale")}{inner}</g></g>')


def trace(d, stroke="var(--c2)", width=4, begin=.05, dur=.9, extra=""):
    """A stroke that draws itself once."""
    return (f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{stroke}" stroke-width="{width}" '
            f'stroke-linecap="round" {extra}>{_once("stroke-dashoffset", 1, 0, begin, dur)}</path>')


def seq(parts, start=.1, dur=.5, dy=18, window=1.85):
    """Stagger parts so the last one still lands inside the window (the v3 keynote's spread cap)."""
    n = len(parts)
    step = 0 if n < 2 else min(.12, (window - start - dur) / (n - 1))
    return "".join(land(p, start + k * step, dur, dy) for k, p in enumerate(parts))


# ---------------------------------------------------------------- ambient loops (breathe while you talk)
def loop(attr, values, period, phase=0.0):
    n = len(values.split(";"))
    kt = ";".join(f"{k / (n - 1):.3f}" for k in range(n))
    spl = ";".join(["0.45 0 0.55 1"] * (n - 1))
    return (f'<animate attributeName="{attr}" values="{values}" keyTimes="{kt}" dur="{period}s" begin="-{phase:.2f}s" '
            f'repeatCount="indefinite" calcMode="spline" keySplines="{spl}"/>')


def sway(cx, cy, deg, period, phase=0.0):
    return (f'<animateTransform attributeName="transform" type="rotate" values="{-deg} {cx} {cy};{deg} {cx} {cy};{-deg} {cx} {cy}" '
            f'keyTimes="0;.5;1" dur="{period}s" begin="-{phase:.2f}s" repeatCount="indefinite" calcMode="spline" '
            f'keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>')


def bob(dx, dy, period, phase=0.0):
    return (f'<animateTransform attributeName="transform" type="translate" values="0 0;{dx} {dy};0 0" keyTimes="0;.5;1" '
            f'dur="{period}s" begin="-{phase:.2f}s" repeatCount="indefinite" calcMode="spline" '
            f'keySplines="0.45 0 0.55 1;0.45 0 0.55 1"/>')


def blink(period=1.1):
    return f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="{period}s" repeatCount="indefinite" calcMode="discrete"/>'


# ---------------------------------------------------------------- pieces
def card(x, y, w, h, fill="var(--card)", stroke="var(--line)", r=16, sw=1.5, extra=""):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def pill(cx, cy, text, fill, ctx, size=18, room=260, where="pill", pad=18):
    """A rounded label centered at (cx, cy), as wide as its text in this language."""
    s = fit(text, size, room - 2 * pad, where)
    w = min(room, bold_width(_(str(text)), s, current_factor()) + 2 * pad)
    h = s + 20
    fg = "var(--white)" if fill in ("var(--dim)", "var(--card)") else ctx.brand.on(fill)
    return card(cx - w / 2, cy - h / 2, w, h, fill, fill, h / 2, 0) + TC(f"{cx:.1f}", f"{cy + s * .36:.1f}", text, s, fg, W6)


def bubble(x, y, w, text, ctx, fill="var(--c1)", size=19, where="chat bubble", ai=False):
    s = fit(text, size, w - 60, where)
    fg = "var(--white)" if fill in ("var(--card)", "var(--dim)") else ctx.brand.on(fill)
    mark = spark(x + 24, y + 28, .7) if ai else f'<circle cx="{x + 24}" cy="{y + 28}" r="7" fill="{fg}"/>'
    return card(x, y, w, 56, fill, "var(--line)", 18) + mark + T(x + 44, y + 28 + s * .36, text, s, fg)


def thumb(x, y, w, h, title=None, hole=True, dim=True, size=16):
    g = [card(x, y, w, h, "var(--dim)" if dim else "var(--card)", "var(--line)", 10)]
    if title is not None:
        s = fit(title, size, w - 24, "thumbnail title")
        g.append(T(x + 12, y + 12 + s, title, s, "var(--muted)" if dim else "var(--white)", W6))
    if hole:
        g.append(f'<rect x="{x + 12}" y="{y + h * .5:.1f}" width="{w - 24}" height="{h * .3:.1f}" rx="6" fill="none" '
                 f'stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="5 5"/>')
    return "".join(g)


def bars(x, y, w, n=3, gap=16, color="var(--c2)", op=".55"):
    return "".join(f'<rect x="{x}" y="{y + k * gap}" width="{w * (.9 if k % 2 == 0 else .62):.0f}" height="7" rx="3.5" fill="{color}" opacity="{op}"/>'
                   for k in range(n))


def notebook(x, y, w, h, label):
    rings = "".join(f'<circle cx="{x + 16}" cy="{y + 30 + k * 34}" r="6" fill="none" stroke="var(--c2)" stroke-width="2.5"/>'
                    for k in range(int((h - 40) // 34)))
    s = fit(label, 18, w - 60, "notebook label")
    return card(x, y, w, h, "var(--card)", "var(--c2)", 14, 2) + rings + T(x + 40, y + 40, label, s, "var(--white)", W6) + bars(x + 40, y + 64, w - 70, 5, 22)


def lens(x, y, r=34):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="var(--c4)" stroke-width="5"/>'
            f'<path d="M{x + r * .72:.1f} {y + r * .72:.1f} L{x + r * 1.5:.1f} {y + r * 1.5:.1f}" stroke="var(--c4)" stroke-width="8" stroke-linecap="round"/>')


def ask(sl, ctx, x=860, y=120, w=660):
    return bubble(x, y, w, sl["prompt"], ctx) if sl.get("prompt") else ""


def ellipse_path(cx, cy, rx, ry):
    return f"M{cx} {cy - ry} A{rx} {ry} 0 1 1 {cx - .01} {cy - ry} Z"


# ---------------------------------------------------------------- scenes
@register("scene", "ring")
def sc_ring(sl, ctx):
    """The seven steps around one slide: blank on the cover, filled at the close."""
    names, cols = ctx.vocab["stages"], ctx.vocab["stage_colors"]
    close = sl.get("mode") == "close"
    cx, cy, rx, ry = (800, 690, 560, 122) if close else (1170, 455, 330, 300)
    fw, fh = (300, 124) if close else (300, 180)
    g = [glow(cx, cy, 380 if close else 420, "var(--brand)", .6),
         trace(ellipse_path(cx, cy, rx, ry), "var(--line)", 3, .05, .9)]
    frame = [card(cx - fw / 2, cy - fh / 2, fw, fh, "var(--card)", "var(--c2)", 14, 2)]
    if close:
        for k in range(3):
            frame.append(f'<rect x="{cx - fw / 2 + 24}" y="{cy - fh / 2 + 20 + k * 24}" width="{fw - 90 - k * 30}" height="9" rx="4.5" fill="var(--c2)"/>')
            frame.append(check(cx + fw / 2 - 36, cy - fh / 2 + 25 + k * 24, .7, ctx.brand.c("dark.ok")))
    else:
        frame.append(f'<rect x="{cx - fw / 2 + 24}" y="{cy - fh / 2 + 28}" width="{fw - 48}" height="30" rx="6" fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="6 6"/>')
    # the official lockup signs the bookend slide (same symbol as the cover and the footer, painted in currentColor)
    frame.append(f'<use href="#lockup" x="{cx + fw / 2 - 150:.0f}" y="{cy + fh / 2 - 42:.0f}" width="130" height="28" style="color:var(--white)"/>')
    g.append(land("".join(frame), .15, .6, 14))
    n = len(names)
    for k, (name, col) in enumerate(zip(names, cols)):
        a = math.radians(-90 + 360 / n * k)
        x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
        halo = f'<circle cx="0" cy="0" r="30" fill="{col}" opacity=".25">{pulse_r(30, 46, k / n if k else .001, D)}</circle>'
        g.append(pop(halo + pill(0, 0, name, col, ctx, 18, 190, "ring step"), x, y, .35 + k * .12, .45))
    orbit = ellipse_path(cx, cy, rx + 60, ry + 48)
    g.append(f'<g>{card(-17, -12, 34, 24, "var(--c4)", "var(--c4)", 8, 0)}{move(orbit, [(0, 0), (1, 1)], D)}</g>')
    return "".join(g), D, FREEZE


@register("scene", "meeting")
def sc_meeting(sl, ctx):
    cal = (card(860, 170, 200, 220, "var(--card)", "var(--line)", 16) + f'<rect x="860" y="170" width="200" height="56" rx="16" fill="var(--accent)"/>'
           + TC(960, 208, sl["day"], 24, ctx.brand.on("var(--accent)"), W6) + TC(960, 318, sl["time"], 52, "var(--white)", W6))
    screen = (card(1110, 150, 400, 230, "var(--dim)", "var(--c2)", 12, 2)
              + f'<rect x="1150" y="200" width="4" height="36" fill="var(--c4)">{blink()}</rect>'
              + f'<rect x="1110" y="150" width="400" height="230" rx="12" fill="var(--c2)" opacity=".05">{loop("opacity", ".03;.14;.03", 5)}</rect>')
    table = f'<ellipse cx="1240" cy="640" rx="250" ry="70" fill="var(--card)" stroke="var(--line)" stroke-width="2"/>'
    people = "".join(person(x, 600, 1.5, c) for x, c in ((1110, "var(--c2)"), (1370, "var(--c3)")))
    labels = "".join(pill(x, 730, t, "var(--brand)", ctx, 17, 240, "meeting seat") for x, t in zip((1110, 1370), sl["people"]))
    parts = [cal, screen, table, people, labels]
    if sl.get("outcome"):  # the case closes by its result: the decision the meeting produced
        ok = ctx.brand.c("dark.ok")
        parts.append(f'<g>{loop("opacity", ".7;1;.7", 3)}{pill(1240, 800, sl["outcome"], ok, ctx, 18, 420, "meeting outcome")}</g>')
    return glow(1180, 470, 420, "var(--brand)", .5) + seq(parts, .1, .55), D, FREEZE


@register("scene", "generic")
def sc_generic(sl, ctx):
    g = [land(bubble(96, 450, 760, sl["prompt"], ctx), .1, .5)]
    thumbs = []
    for k, title in enumerate(sl["thumbs"][:10]):
        x, y = 96 + (k % 5) * 286, 530 + (k // 5) * 150
        t = thumb(x, y, 262, 130, title)
        if k == 0:
            t += card(x + 196, y + 84, 54, 34, "var(--ink)", "var(--c2)", 6, 1) + TC(x + 223, y + 106, sl["cover"], 12, "var(--muted)")
        thumbs.append(t)
    g.append(seq(thumbs, .35, .45, 14))
    holes = "".join(f'<rect x="{96 + (k % 5) * 286 + 12}" y="{530 + (k // 5) * 150 + 65}" width="238" height="39" rx="6" fill="var(--c2)" opacity="0">'
                    f'{loop("opacity", "0;.22;0", 4, k * .4)}</rect>' for k in range(10))
    tag = f'<g>{sway(1082, 512, 4, 5)}{pill(1082, 512, sl["tag"], "var(--c5)", ctx, 15, 220, "unsourced tag")}</g>'
    g.append(holes + land(tag, 1.35, .45, -12))
    return "".join(g), D, FREEZE


@register("scene", "chatContext")
def sc_chat_context(sl, ctx):
    g = [glow(1180, 470, 420, "var(--brand)", .5), land(ask(sl, ctx), .1, .45)]
    cards = []
    for k, (label, value) in enumerate(sl["cards"]):
        x, y = 860 + (k % 2) * 340, 220 + (k // 2) * 160
        hot = k == 2
        c = card(x, y, 320, 140, "var(--card)", "var(--accent)" if hot else "var(--line)", 16, 2.5 if hot else 1.5)
        if hot:
            c = f'<g>{c}<rect x="{x}" y="{y}" width="320" height="140" rx="16" fill="none" stroke="var(--accent)" stroke-width="3">{loop("stroke-opacity", ".2;1;.2", 3)}</rect></g>'
        c += pill(x + 70, y + 32, label, "var(--c1)", ctx, 15, 130, "context card label")
        c += TCW(x + 20, y + 82, value, 26, 20, "var(--white)", W6, anchor="start")
        cards.append(c)
    g.append(seq(cards, .3, .45, 14))
    reply = bubble(860, 560, 540, sl["reply"], ctx, "var(--card)", 19, "ai reply", True) + f'<rect x="1412" y="574" width="4" height="28" fill="var(--c4)">{blink()}</rect>'
    g.append(land(reply, 1.3, .5, 12))
    return "".join(g), D, FREEZE


@register("scene", "research")
def sc_research(sl, ctx):
    g = [glow(1180, 470, 420, "var(--brand)", .5), land(ask(sl, ctx), .1, .45)]
    layers = [card(860, 220 + k * 92, 360, 70, "var(--card)", "var(--c2)", 12) + T(884, 263 + k * 92, lab, fit(lab, 19, 320, "research layer"), "var(--white)", W6)
              for k, lab in enumerate(sl["layers"])]
    g.append(seq(layers, .25, .45, -20))
    g.append("".join(trace(f"M1224 {255 + k * 92} C1250 {255 + k * 92} 1250 {330} 1270 {330}", "var(--c2)", 2.5, .6 + k * .1, .5) for k in range(3)))
    g.append(land(notebook(1270, 210, 250, 250, sl["book"]), .45, .5))
    lens_g = f'<g>{bob(0, 184, 6)}{lens(1180, 250)}</g>'
    case = (card(860, 520, 660, 150, "var(--card)", "var(--c4)", 16, 2) + T(884, 556, sl.get("case_label", "Caso de uso"), 15, "var(--c4)", W6)
            + TCW(884, 596, sl["case"], 44, 22, "var(--white)", W6, anchor="start"))
    tag = f'<g>{loop("opacity", ".75;1;.75", 3)}{pill(1330, 520, sl["tag"], "var(--c4)", ctx, 15, 300, "use case tag")}</g>'
    g.append(land(case, 1.1, .5) + land(tag, 1.35, .45, -10) + lens_g)
    return "".join(g), D, FREEZE


@register("scene", "funnel")
def sc_funnel(sl, ctx):
    g = [glow(1180, 470, 420, "var(--brand)", .5), land(ask(sl, ctx), .1, .45)]
    chips = [card(900 + k * 110, 210, 90, 30, "var(--c1)" if k < 3 else "var(--c2)", "none", 15, 0) for k in range(5)]
    g.append(seq(chips, .25, .4, -30))
    g.append(land('<path d="M1000 260 L1360 260 L1210 400 L1150 400 Z" fill="var(--card)" stroke="var(--c2)" stroke-width="2"/>', .45, .45, 0))
    drop = f'<circle cx="1180" cy="410" r="7" fill="var(--c4)">{loop("cy", "405;455;405", 2.4)}{loop("opacity", "1;0;1", 2.4)}</circle>'
    rows = [card(900, 430, 580, 380, "var(--card)", "var(--line)", 18) + T(924, 466, "brief.md", 18, "var(--c2)", W6)]
    for k, f in enumerate(sl["fields"]):
        y = 490 + k * 62
        hot = k == sl["hot"]
        row = T(924, y + 26, f, fit(f, 18, 120, "brief field"), "var(--c4)" if hot else "var(--muted)", W6)
        if hot:
            row += card(1060, y, 400, 52, "var(--dim)", "var(--accent)", 10, 2)
            row += f'<rect x="1060" y="{y}" width="400" height="52" rx="10" fill="none" stroke="var(--accent)" stroke-width="3">{loop("stroke-opacity", ".2;1;.2", 3)}</rect>'
            row += TCW(1074, y + 20, sl["phrase"], 44, 14, "var(--white)", W6, 1.25, "start")
        else:
            row += f'<rect x="1060" y="{y + 20}" width="{[330, 260, 300, 0, 280][k]}" height="9" rx="4.5" fill="var(--c2)" opacity=".5"/>'
        rows.append(row)
    g.append(seq(rows, .6, .45, 14) + drop)
    return "".join(g), D, FREEZE


@register("scene", "options3")
def sc_options3(sl, ctx):
    g = [land(ask(sl, ctx), .1, .45)]
    pick, cards = sl.get("pick", 0), []
    for k, text in enumerate(sl["options"]):
        key, body = text.split(" · ", 1)
        hot = k == pick
        x, y = 860 + k * 225, 230 if hot else 270
        c = ""
        if hot:
            c += f'<g>{loop("opacity", ".45;1;.45", 4)}{glow(x + 100, y + 150, 190, "var(--accent)", .35)}</g>'
        c += card(x, y, 200, 300, "var(--card)" if hot else "var(--dim)", "var(--accent)" if hot else "var(--line)", 18, 2.5 if hot else 1.5)
        c += f'<circle cx="{x + 40}" cy="{y + 42}" r="22" fill="{"var(--accent)" if hot else "var(--card)"}"/>'
        c += TC(x + 40, y + 50, key, 22, ctx.brand.on("var(--accent)") if hot else "var(--muted)", W6)
        c += TCW(x + 20, y + 110, body, 17, 19, "var(--white)" if hot else "var(--muted)", W6, 1.3, "start")
        cards.append(c)
    g.append(seq(cards, .3, .5, 30))
    return "".join(g), D, FREEZE


@register("scene", "structures")
def sc_structures(sl, ctx):
    g = [land(ask(sl, ctx), .1, .45)]
    pick, cols = sl.get("pick", 1), []
    for k, form in enumerate(sl["forms"]):
        x, hot = 860 + k * 225, k == pick
        c = card(x, 230, 200, 380, "var(--card)" if hot else "var(--dim)", "var(--accent)" if hot else "var(--line)", 16, 2.5 if hot else 1.5)
        if k == 0:
            c += "".join(card(x + 24, 262 + j * 104, 152, 84, "var(--c1)", "none", 10, 0) for j in range(3))
        elif k == 2:
            c += card(x + 24, 262, 152, 120, "var(--c1)", "none", 10, 0) + "".join(card(x + 24 + j * 52, 400, 44, 60, "var(--c2)", "none", 8, 0) for j in range(3))
        else:
            top, bot = sl["bands"][1], sl["bands"][0]
            c += T(x + 16, 258, top, fit(top, 14, 170, "structure band"), "var(--c2)")
            c += T(x + 16, 592, bot, fit(bot, 14, 170, "structure band"), "var(--c2)")
            pts = [(x + 30 + j * 28, 520 if j % 2 == 0 else 330) for j in range(6)]
            wave = "M" + " L".join(f"{px} {py}" for px, py in pts)
            c += f'<path d="{wave}" fill="none" stroke="var(--c2)" stroke-width="2.5" stroke-dasharray="4 6"/>'
            c += "".join(f'<rect x="{px - 11}" y="{py - 16}" width="22" height="32" rx="6" fill="var(--accent)"/>' for px, py in pts)
            c += pill(pts[0][0] + 14, 560, sl["marks"][0], "var(--c5)", ctx, 13, 90, "structure mark")
            c += pill(pts[-1][0] - 10, 290, sl["marks"][1], "var(--c4)", ctx, 13, 90, "structure mark")
            c += f'<g>{token("var(--c4)", 8)}{move(wave, [(0, 0), (1, 1)], D / 2)}</g>'
        c += TCW(x + 100, 650, form, 20, 17, "var(--white)" if hot else "var(--muted)", W6, 1.25)
        cols.append(c)
    g.append(seq(cols, .3, .5, 24))
    return "".join(g), D, FREEZE


@register("scene", "unsourced")
def sc_unsourced(sl, ctx):
    ok = ctx.brand.c("dark.ok")
    page = card(870, 150, 360, 520, "var(--card)", "var(--line)", 16) + T(898, 196, sl["doc"], 22, "var(--white)", W6) + bars(898, 230, 300, 10, 34)
    fake = (f'<g transform="rotate(7 1330 300)">{card(1150, 250, 360, 110, "var(--dim)", "var(--c5)", 14, 2)}'
            + TCW(1172, 300, sl["case"], 30, 19, "var(--muted)", W6, anchor="start")
            + f'<g>{sway(1440, 232, 3, 4)}{pill(1440, 232, sl["stamp"], "var(--c5)", ctx, 15, 150, "stamp")}</g></g>')
    fix = (card(990, 470, 400, 100, "var(--card)", ok, 14, 2) + T(1016, 528, sl["fix"], fit(sl["fix"], 20, 300, "source card"), "var(--white)", W6)
           + check(1356, 520, 1, ok)
           + f'<rect x="1004" y="462" width="30" height="8" rx="2" fill="var(--c2)">{loop("opacity", ".5;1;.5", 2.5)}</rect>')
    hole = f'<rect x="990" y="470" width="400" height="100" rx="14" fill="none" stroke="var(--c5)" stroke-width="2" stroke-dasharray="6 6"/>'
    g = [glow(1180, 470, 420, "var(--brand)", .5), land(page, .1, .5), land(hole, .35, .4, 0),
         land(fake, .45, .6, 60, -80), land(f'<g>{bob(40, 0, 5)}{lens(1060, 640)}</g>', .8, .45), land(fix, 1.2, .55, -30)]
    return "".join(g), D, FREEZE


@register("scene", "thread")
def sc_thread(sl, ctx):
    ok = ctx.brand.c("dark.ok")
    xs = [96 + k * 238 for k in range(6)]
    path = "M" + " L".join(f"{x + 108} {498 if k % 2 == 0 else 512}" for k, x in enumerate(xs))
    cards = []
    for k, (x, title) in enumerate(zip(xs, sl["titles"])):
        c = card(x, 520, 216, 210, "var(--card)", "var(--line)", 16)
        c += T(x + 18, 552, f"0{k + 1}", 16, "var(--c2)", W6)
        c += TCW(x + 18, 586, title, 17, 18, "var(--white)", W6, 1.3, "start")
        cards.append(c)
    checks = "".join(pop(f'<circle r="18" fill="{ok}"/>' + check(0, 1, .8, "var(--ink)"), x + 184, 698, .9 + k * .12, .35) for k, x in enumerate(xs))
    bead = f'<g>{token("var(--accent)", 9)}{move(path, [(0, 0), (1, 1)], D)}</g>'
    g = [seq(cards, .1, .45, 20), trace(path, "var(--accent)", 4, .6, .8), checks]
    g += [f'<circle cx="{x + 108}" cy="{498 if k % 2 == 0 else 512}" r="7" fill="var(--accent)"/>' for k, x in enumerate(xs)]
    g.append(bead)
    return "".join(g), D, FREEZE


@register("scene", "layers")
def sc_layers(sl, ctx):
    g = [glow(1180, 470, 420, "var(--brand)", .5)]
    cols = ("var(--c1)", "var(--c2)", "var(--accent)")
    parts = []
    for k, (label, col) in enumerate(zip(sl["layers"], cols)):
        y = 600 - k * 170
        frame = (f'<path d="M920 {y} L1380 {y} L1500 {y - 80} L1040 {y - 80} Z" fill="var(--card)" stroke="{col}" stroke-width="2.5"/>')
        if k == 0:
            frame += f'<circle cx="1200" cy="{y - 40}" r="26" fill="var(--c1)" opacity=".6"/><rect x="1260" y="{y - 58}" width="90" height="36" rx="8" fill="var(--c1)" opacity=".6"/>'
        elif k == 1:
            frame += bars(1100, y - 60, 240, 3, 14, "var(--c2)", ".7")
        else:
            frame += f'<g>{spark(1210, y - 40, 1.1, "var(--accent)")}{loop("opacity", ".35;1;.35", 2.6)}</g>'
            frame += f'<g>{token("var(--c4)", 7)}{move(f"M1080 {y - 40} L1340 {y - 40}", [(0, 0), (.5, 1), (1, 0)], 6)}</g>'
        frame += pill(930, y - 104, label, col, ctx, 16, 220, "layer label")
        parts.append(land(frame, .15 + k * .25, .6, (k - 1) * 150))
    g.append("".join(parts))
    return "".join(g), D, FREEZE


@register("scene", "calm")
def sc_calm(sl, ctx):
    halo = f'<circle cx="1180" cy="430" r="244" fill="var(--brand)" opacity=".35">{loop("r", "238;254;238", 5)}</circle>'
    orbit = (f'<g>{spin(1180, 430, 40)}<ellipse cx="1180" cy="430" rx="300" ry="300" fill="none" stroke="var(--c2)" '
             f'stroke-width="1.5" stroke-dasharray="3 14" opacity=".6"/></g>'
             f'<g>{token("var(--c4)", 9)}{move("M1180 130 A300 300 0 1 1 1179.99 130 Z", [(0, 0), (1, 1)], D * 1.5)}</g>')
    fig = TC(1180, 470, sl["figure"], fit(sl["figure"], 130, 440, "calm figure"), "var(--c4)", W6)
    label = TCW(1180, 540, sl["label"], 30, 24, "var(--white)", W6, 1.3)
    src = TC(1180, 616, sl["source"], 16, "var(--muted)") if sl.get("source") else ""
    return glow(1180, 430, 420, "var(--brand)", .5) + land(halo, .1, .6, 0) + orbit + land(fig + label + src, .3, .6, 14), D, FREEZE


@register("scene", "compare")
def sc_compare(sl, ctx):
    ok = ctx.brand.c("dark.ok")
    left = [pill(200, 462, sl["left"], "var(--dim)", ctx, 16, 200, "compare side")]
    for k in range(10):
        x, y = 96 + (k % 5) * 124, 500 + (k // 5) * 90
        left.append(thumb(x, y, 112, 76, None))
    left.append(f'<text x="96" y="710" font-size="16" fill="var(--muted)">{E(" · ".join(_(t) for t in sl["thumbs"][:3]))}</text>')
    right = [pill(870, 462, sl["right"], "var(--accent)", ctx, 16, 220, "compare side")]
    for k, title in enumerate(sl["titles"][:6]):
        x, y = 780 + (k % 3) * 244, 500 + (k // 3) * 132
        right.append(card(x, y, 232, 120, "var(--card)", "var(--accent)" if k == 0 else "var(--line)", 14, 2 if k == 0 else 1.5)
                     + TCW(x + 16, y + 30, title, 25, 15, "var(--white)", W6, 1.3, "start") + check(x + 212, y + 20, .6, ok))
    proof = T(780, 800, sl["proof"], fit(sl["proof"], 17, 720, "compare proof"), "var(--c4)", W6)
    pulse = f'<rect x="772" y="492" width="740" height="272" rx="18" fill="none" stroke="var(--accent)" stroke-width="2">{loop("stroke-opacity", ".15;.8;.15", 3.5)}</rect>'
    arrow = trace("M700 640 L760 640", "var(--c2)", 4, .7, .4, 'marker-end="url(#arrow)"')
    return land("".join(left), .1, .5) + arrow + land("".join(right), .5, .55) + land(proof, 1.1, .45, 10) + pulse, D, FREEZE


@register("scene", "tailored")
def sc_tailored(sl, ctx):
    cols = ctx.vocab["stage_colors"]
    covers = []
    for k, sector in enumerate(sl["sectors"][:6]):
        cx = 800 + (k - 2.5) * 232
        y = 520 + abs(k - 2.5) * 14
        rot = (k - 2.5) * 4
        body = (card(cx - 95, y, 190, 250, "var(--card)", "var(--line)", 14) + f'<rect x="{cx - 95}" y="{y}" width="190" height="54" rx="14" fill="{cols[k]}"/>'
                + T(cx - 78, y + 96, sector, fit(sector, 20, 156, "tailored cover"), "var(--white)", W6) + bars(cx - 78, y + 126, 150, 4, 22))
        covers.append(f'<g transform="rotate({rot:.1f} {cx:.0f} {y + 250})"><g>{sway(cx, y + 250, 1.5, 5 + k * .7, k * .9)}{body}</g></g>')
    center = pill(800, 456, sl["center"], "var(--c1)", ctx, 18, 320, "tailored center")
    return glow(800, 640, 520, "var(--brand)", .45) + seq(covers, .1, .5, 30) + land(center, 1.1, .45, -10), D, FREEZE


@register("scene", "agenda4")
def sc_agenda4(sl, ctx):
    ok = ctx.brand.c("dark.ok")
    cols = ctx.vocab["stage_colors"]
    xs, y = [260, 620, 980, 1340], 640
    g = [glow(800, 640, 560, "var(--brand)", .45), trace(f"M{xs[0]} {y} L{xs[-1]} {y}", "var(--line)", 6, .05, .9)]
    flow = f'<path d="M{xs[1]} {y} L{xs[-1]} {y}" fill="none" stroke="var(--c2)" stroke-width="3" stroke-dasharray="6 14">{loop("stroke-dashoffset", "0;-40", 2)}</path>'
    stops = []
    for k, (x, name) in enumerate(zip(xs, sl["stops"])):
        done = k < sl.get("done", 0)
        dot = f'<circle r="36" fill="{ok if done else "var(--card)"}" stroke="{cols[k]}" stroke-width="4"/>'
        dot += check(0, 2, 1.1, "var(--ink)") if done else TC(0, 8, f"0{k + 1}", 22, "var(--white)", W6)
        stops.append(pop(dot, x, y, .3 + k * .15, .45))
        stops.append(land(TC(x, y + 82, name, fit(name, 24, 300, "agenda stop"), "var(--white)", W6), .45 + k * .15, .45, 10))
    wait = f'<circle cx="{xs[1]}" cy="{y}" r="44" fill="none" stroke="var(--c4)" stroke-width="3" opacity=".7">{loop("r", "42;62;42", 2.4)}{loop("opacity", ".8;0;.8", 2.4)}</circle>'
    return "".join(g) + flow + "".join(stops) + wait, D, FREEZE


@register("scene", "placeholder")
def sc_placeholder(sl, ctx):
    g = [glow(1180, 470, 420, "var(--brand)", .45)]
    if sl.get("mode") == "after":
        cols = []
        for k, (head, cell) in enumerate(zip(sl["heads"], sl["cells"])):
            x = 860 + k * 225
            c = card(x, 190, 205, 460, "var(--card)", "var(--c2)", 16, 1.5, 'stroke-dasharray="6 6"')
            c += pill(x + 102, 226, head, "var(--c1)" if k != 1 else "var(--accent)", ctx, 15, 180, "column head")
            c += TCW(x + 102, 300, cell, 16, 18, "var(--muted)", W6, 1.3)
            if k == 1:
                c += "".join(f'<rect x="{x + 22}" y="{400 + j * 44}" width="130" height="10" rx="5" fill="var(--c2)"/>' + check(x + 176, 405 + j * 44, .6, ctx.brand.c("dark.ok")) for j in range(4))
                c += f'<g>{token("var(--accent)", 7)}{move(f"M{x + 14} 405 L{x + 14} 537", [(0, 0), (1, 1)], 5)}</g>'
            cols.append(c)
        g.append(seq(cols, .1, .5, 20))
    else:
        frame = (card(860, 160, 640, 360, "var(--card)", "var(--c2)", 18, 2, 'stroke-dasharray="8 8"')
                 + TC(1180, 350, sl["frame"], fit(sl["frame"], 22, 580, "placeholder frame"), "var(--muted)", W6))
        chips = []
        for k, chip in enumerate(sl["chips"]):
            x = 860 + k * 164
            c = card(x, 570, 148, 60, "var(--dim)", "var(--line)", 30, 1.5)
            c += f'<rect x="{x}" y="570" width="148" height="60" rx="30" fill="none" stroke="var(--c5)" stroke-width="2.5">{loop("stroke-opacity", "0;1;0", 4, k)}</rect>'
            c += TC(x + 74, 607, chip, fit(chip, 18, 120, "missing chip"), "var(--muted)", W6)
            chips.append(c)
        g.append(land(frame, .1, .5) + seq(chips, .5, .45, 14))
    return "".join(g), D, FREEZE


@register("scene", "workshop")
def sc_workshop(sl, ctx):
    chat = card(860, 170, 300, 250, "var(--card)", "var(--line)", 16) + "".join(
        card(880 + (60 if k % 2 else 0), 196 + k * 54, 200, 38, "var(--c1)" if k % 2 == 0 else "var(--dim)", "none", 14, 0) for k in range(4))
    book = notebook(1190, 170, 310, 250, sl["book"])
    brief = [card(860, 450, 640, 360, "var(--card)", "var(--line)", 18), T(884, 488, "brief.md", 18, "var(--c2)", W6)]
    for k, f in enumerate(sl["fields"]):
        y = 520 + k * 56
        brief.append(T(884, y + 22, f, fit(f, 17, 120, "brief field"), "var(--muted)", W6))
        brief.append(f'<path d="M1020 {y + 24} H1470" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="5 6"/>')
    pencil = (f'<g>{bob(260, 0, 6)}<g transform="translate(1030 {520 + 3 * 56 + 4}) rotate(-35)">'
              f'<rect x="-6" y="-44" width="12" height="40" rx="3" fill="var(--c4)"/><path d="M-6 -4 L6 -4 L0 8 Z" fill="var(--c2)"/></g></g>')
    clock = f'<g>{pill(1420, 128, sl["clock"], "var(--accent)", ctx, 17, 150, "clock")}</g>'
    return glow(1180, 470, 420, "var(--brand)", .45) + seq([chat, book, "".join(brief), clock], .1, .5) + pencil, D, FREEZE


@register("scene", "pair")
def sc_pair(sl, ctx):
    people = person(980, 560, 1.9, "var(--c2)") + person(1400, 560, 1.9, "var(--c3)")
    lst = card(1030, 470, 130, 170, "var(--card)", "var(--c2)", 12, 2) + T(1046, 500, sl["list"], fit(sl["list"], 14, 100, "title list"), "var(--c2)", W6) + bars(1046, 520, 100, 5, 22)
    bubbles = (f'<g opacity="0">{loop("opacity", "1;1;0;0;1", 6)}{card(900, 300, 190, 70, "var(--c1)", "none", 22, 0)}{bars(924, 322, 140, 2, 18, "var(--white)", ".8")}</g>'
               f'<g opacity="0">{loop("opacity", "0;0;1;1;0", 6)}{card(1310, 300, 190, 70, "var(--card)", "var(--c3)", 22, 2)}{bars(1334, 322, 140, 2, 18, "var(--c3)", ".8")}</g>')
    times = "".join(pill(990 + k * 200, 740, t, "var(--brand)", ctx, 17, 170, "pair timer") for k, t in enumerate(sl["times"]))
    return glow(1180, 480, 420, "var(--brand)", .45) + seq([people, lst, times], .1, .55) + bubbles, D, FREEZE


@register("scene", "dossier")
def sc_dossier(sl, ctx):
    """The dossier feeds three scripts: create, polish, challenge."""
    doc_ = [card(860, 150, 320, 500, "var(--card)", "var(--c2)", 16, 2), T(884, 192, sl["doc"], fit(sl["doc"], 20, 280, "dossier title"), "var(--white)", W6)]
    for k, sec in enumerate(sl["sections"]):
        y = 226 + k * 104
        hot = k == 0
        row = T(884, y + 24, sec, fit(sec, 17, 272, "dossier section"), "var(--c4)" if hot else "var(--c2)", W6) + bars(884, y + 40, 260, 3, 16)
        if hot:
            row = f'<g>{row}<rect x="872" y="{y}" width="296" height="92" rx="10" fill="none" stroke="var(--c4)" stroke-width="2">{loop("stroke-opacity", ".15;.9;.15", 3)}</rect></g>'
        doc_.append(row)
    g = [glow(1180, 450, 420, "var(--brand)", .5), land("".join(doc_), .1, .55)]
    cols = ("var(--c1)", "var(--accent)", "var(--c3)")
    cards = []
    for k, (label, col) in enumerate(zip(sl["scripts"], cols)):
        y = 170 + k * 170
        cards.append(card(1240, y, 280, 130, "var(--card)", col, 16, 2) + pill(1310, y + 32, label, col, ctx, 16, 130, "script label") + bars(1262, y + 66, 230, 3, 16))
    g.append("".join(trace(f"M1180 {320 + k * 60} C1210 {320 + k * 60} 1210 {235 + k * 170} 1240 {235 + k * 170}", "var(--c2)", 2.5, .5 + k * .12, .5) for k in range(3)))
    g.append(seq(cards, .6, .45, 0))
    sheet = f'<g>{card(-14, -18, 28, 36, "var(--white)", "none", 4, 0)}{move("M1180 330 C1210 330 1210 405 1240 405", [(0, 0), (1, 1)], 3.2)}</g>'
    g.append(sheet)
    return "".join(g), D, FREEZE


@register("scene", "versus")
def sc_versus(sl, ctx):
    """Vague request versus dossier + context: the same ask, two outputs."""
    ok = ctx.brand.c("dark.ok")
    vague = sl.get("mode") == "vague"
    g = [glow(1180, 450, 420, "var(--brand)", .45), land(bubble(860, 110, 660, sl["ask"], ctx), .1, .45)]
    if not vague:
        g.append(land(card(1330, 60, 190, 40, "var(--c4)", "none", 12, 0) + TC(1425, 86, sl["doc"], fit(sl["doc"], 15, 170, "dossier chip"), ctx.brand.on("var(--c4)"), W6), .3, .45, 0, 60))
    rows = []
    titles = sl["titles"][:8] if vague else sl["titles"][:6]
    h, gap = (48, 8) if vague else (60, 10)
    for k, title in enumerate(titles):
        y = 190 + k * (h + gap)
        if vague:
            s = fit(title, 16, 630, "vague title")
            r = card(860, y, 660, h, "var(--dim)", "var(--line)", 10) + T(878, y + h / 2 + s * .36, title, s, "var(--muted)", W6)
            if k in sl.get("generic_idx", []):  # by position, not by text: every language keeps the same structure
                r += (f'<rect x="878" y="{y + h - 12}" width="{min(620, bold_width(_(str(title)), s, current_factor())):.0f}" height="3" rx="1.5" fill="var(--c5)">'
                      f'{loop("opacity", ".25;1;.25", 3, k * .5)}</rect>')
        else:
            s = fit(title, 18, 600, "tailored title")
            r = (card(860, y, 660, h, "var(--card)", "var(--accent)" if k == 0 else "var(--line)", 12, 2 if k == 0 else 1.5)
                 + T(880, y + h / 2 + s * .36, title, s, "var(--white)", W6) + check(1494, y + h / 2, .7, ok))
        rows.append(r)
    g.append(seq(rows, .35, .4, 12))
    if vague:
        g.append(land(pill(1040, 660, sl["flag"], "var(--c5)", ctx, 16, 360, "wrong entity"), 1.4, .4, -10))
    else:
        for k, (label, before, after) in enumerate(sl["metrics"]):
            x = 860 + k * 224
            m = (card(x, 640, 212, 96, "var(--card)", "var(--c2)", 14, 1.5) + T(x + 16, 668, label, fit(label, 14, 180, "metric label"), "var(--muted)", W6)
                 + T(x + 16, 714, f"{before}  →  {after}", 30, "var(--c4)", W6))
            g.append(land(m, 1.25 + k * .12, .4, 10))
        g.append(f'<g>{token("var(--accent)", 7)}{move("M846 220 L846 520", [(0, 0), (1, 1)], 6)}</g>')
    return "".join(g), D, FREEZE


@register("scene", "gasnet")
def sc_gasnet(sl, ctx):
    """Four business lines around one operation, joined by pipes where gas flows."""
    cx, cy = 1180, 460
    pos = [(1180, 190), (1410, 460), (1180, 730), (950, 460)]
    cols = ("var(--c1)", "var(--accent)", "var(--c3)", "var(--c2)")
    g = [glow(cx, cy, 440, "var(--brand)", .5)]
    pipes = []
    for (x, y) in pos:
        d = f"M{cx} {cy} L{x} {y}"
        pipes.append(f'<path d="{d}" stroke="var(--line)" stroke-width="10" stroke-linecap="round"/>')
        pipes.append(f'<path d="{d}" fill="none" stroke="var(--c4)" stroke-width="3" stroke-dasharray="6 16">{loop("stroke-dashoffset", "0;-44", 1.8)}</path>')
    g.append(land("".join(pipes), .1, .5, 0))
    hub = f'<circle r="86" fill="var(--card)" stroke="var(--c4)" stroke-width="3"/>' + TCW(0, -6, sl["center"], 14, 18, "var(--white)", W6, 1.2)
    g.append(pop(hub, cx, cy, .3, .5))
    for k, ((x, y), col, (name, sub)) in enumerate(zip(pos, cols, sl["lines"])):
        node = (card(-120, -46, 240, 92, "var(--card)", col, 16, 2.5) + TC(0, -6, name, fit(name, 19, 220, "business line"), "var(--white)", W6)
                + TC(0, 24, sub, fit(sub, 14, 220, "business line detail"), "var(--muted)"))
        g.append(pop(node, x, y, .55 + k * .15, .45))
    g.append(f'<circle cx="{cx}" cy="{cy}" r="96" fill="none" stroke="var(--c4)" stroke-width="2" opacity=".6">{loop("r", "92;112;92", 3.2)}{loop("opacity", ".6;0;.6", 3.2)}</circle>')
    return "".join(g), D, FREEZE


@register("scene", "gates")
def sc_gates(sl, ctx):
    """The four gates, each with the test that would measure it; the pain decides which one opens."""
    ok = ctx.brand.c("dark.ok")
    g = [glow(1180, 460, 420, "var(--brand)", .45)]
    cards = []
    for k, (name, test) in enumerate(sl["gates"]):
        x, y = 860 + (k % 2) * 340, 190 + (k // 2) * 230
        hot = k == sl.get("open", 0)
        c = card(x, y, 320, 200, "var(--card)", ok if hot else "var(--line)", 18, 3 if hot else 1.5)
        c += T(x + 24, y + 48, f"0{k + 1}", 16, "var(--c2)", W6) + T(x + 24, y + 88, name, fit(name, 26, 272, "gate name"), "var(--white)", W6)
        c += TCW(x + 24, y + 126, test, 26, 17, "var(--muted)", W6, 1.3, "start")
        if hot:
            c += f'<g>{loop("opacity", ".4;1;.4", 2.6)}<circle cx="{x + 284}" cy="{y + 40}" r="18" fill="{ok}"/></g>' + check(x + 284, y + 41, .75, "var(--ink)")
        cards.append(c)
    g.append(seq(cards, .1, .5, 16))
    case = pill(1180, 690, sl["case"], "var(--accent)", ctx, 17, 560, "gate case")
    g.append(land(case, 1.1, .45, 16))
    return "".join(g), D, FREEZE


@register("scene", "flow")
def sc_flow(sl, ctx):
    """A gas line through four stations. mode steady | early (the deviation is seen in time) | late (it goes unnoticed) |
    future (the close: every station confirms in time under a rising horizon, signed with the Mantu tagline)."""
    ok = ctx.brand.c("dark.ok")
    mode = sl.get("mode", "steady")
    y, xs = 470, [900, 1100, 1300, 1480]
    g = [glow(1180, 470, 430, "var(--brand)", .5)]
    pipe = (f'<path d="M850 {y} H1530" stroke="var(--line)" stroke-width="16" stroke-linecap="round"/>'
            f'<path d="M850 {y} H1530" fill="none" stroke="var(--c4)" stroke-width="4" stroke-dasharray="8 18">{loop("stroke-dashoffset", "0;-52", 1.6)}</path>')
    g.append(land(pipe, .1, .5, 0))
    for k, (x, name) in enumerate(zip(xs, sl["stations"])):
        st = card(-44, -44, 88, 88, "var(--card)", "var(--c2)", 18, 2) + f'<circle r="16" fill="var(--c1)"/>'
        st += TC(0, 78, name, fit(name, 16, 150, "station"), "var(--muted)", W6)
        g.append(pop(st, x, y, .3 + k * .12, .45))
    if mode in ("early", "late"):
        hot = f'<g>{loop("opacity", ".35;1;.35", 2.2)}{spark(xs[1], y - 72, .9, "var(--c5)")}</g>'
        g.append(land(hot, .9, .4, 0))
    if mode == "early":
        g.append(land(f'<g>{bob(0, -6, 3)}{lens(xs[1] - 20, y - 150, 38)}</g>', 1.05, .45, -20))
        g.append(land(pill(xs[1] + 60, y - 230, sl["chip"], ok, ctx, 16, 320, "flow chip"), 1.3, .45, -10))
    elif mode == "future":
        g.insert(0, land(glow(1190, y + 300, 460, "var(--c4)", .3) + f'<circle cx="1190" cy="{y + 300}" r="300" fill="none" stroke="var(--c4)" stroke-width="2" opacity=".22">{loop("r", "296;316;296", 6)}</circle>', .05, .7, 80))
        g.append(land(f'<path d="M1542 {y - 14} L1566 {y} L1542 {y + 14}" fill="none" stroke="var(--c4)" stroke-width="4" stroke-linecap="round"/>', .8, .4, 0))
        for k, x in enumerate(xs):
            mark = (f'<circle cx="{x}" cy="{y - 76}" r="20" fill="{ok}"/>' + check(x, y - 75, .8, "var(--ink)")
                    + f'<circle cx="{x}" cy="{y - 76}" r="20" fill="none" stroke="{ok}" stroke-width="3">{loop("r", "20;20;36;20", 8, k * 2)}{loop("opacity", "0;0;.9;0", 8, k * 2)}</circle>')
            g.append(land(mark, .9 + k * .15, .4, 10))
        g.append(land(TC(1190, y + 180, sl["sign"], fit(sl["sign"], 24, 640, "flow sign"), "var(--c4)", W6), 1.5, .45, 10))
    elif mode == "late":
        g.append(land(pill(xs[3] - 20, y - 150, sl["chip"], "var(--c5)", ctx, 16, 260, "flow chip"), 1.3, .45, -10))
        g.append(land(trace(f"M{xs[1]} {y + 130} H{xs[3]}", "var(--c2)", 2.5, 1.1, .5, 'marker-end="url(#arrow)" stroke-dasharray="6 8"')
                      + T(xs[1], y + 162, sl.get("gap", ""), 15, "var(--muted)"), 1.1, .45, 0))
    return "".join(g), D, FREEZE


@register("scene", "usecase")
def sc_usecase(sl, ctx):
    """One use case as a chain: pain, data, the gate with its test, then layer and delivery model."""
    ok = ctx.brand.c("dark.ok")
    g = [glow(1180, 460, 420, "var(--brand)", .45)]
    rows = [("Dolor", sl["pain"], "var(--c5)"), ("Dato", sl["data"], "var(--c2)")]
    parts = []
    for k, (label, text, col) in enumerate(rows):
        y = 150 + k * 150
        parts.append(card(860, y, 660, 124, "var(--card)", col, 16, 2) + T(884, y + 34, label, 15, col, W6)
                     + TCW(884, y + 68, text, 56, 19, "var(--white)", W6, 1.3, "start"))
    gate = (card(860, 450, 660, 150, "var(--card)", ok, 18, 3) + pill(960, 482, sl["gate"], ok, ctx, 17, 200, "use case gate")
            + TCW(884, 536, sl["test"], 56, 18, "var(--white)", W6, 1.3, "start")
            + f'<rect x="860" y="450" width="660" height="150" rx="18" fill="none" stroke="{ok}" stroke-width="3">{loop("stroke-opacity", ".2;1;.2", 3)}</rect>')
    parts.append(gate)
    chips = pill(1010, 650, sl["layer"], "var(--c1)", ctx, 16, 300, "use case layer") + pill(1360, 650, sl["model"], "var(--accent)", ctx, 16, 300, "use case model")
    parts.append(chips)
    g.append(seq(parts, .1, .45, 16))
    g.append(f'<g>{token("var(--c4)", 7)}{move("M846 200 L846 560", [(0, 0), (1, 1)], 5)}</g>')
    return "".join(g), D, FREEZE


@register("scene", "hypotheses")
def sc_hypotheses(sl, ctx):
    """Four hypotheses from the outside, each with the gate that would test it and a question mark: to validate together."""
    cols = ("var(--c1)", "var(--c3)", "var(--c2)", "var(--accent)")
    cards = []
    for k, ((area, text, gate), col) in enumerate(zip(sl["cards"], cols)):
        x, y = 860 + (k % 2) * 340, 150 + (k // 2) * 300
        c = card(x, y, 320, 270, "var(--card)", col, 18, 2)
        c += pill(x + 20 + min(140, bold_width(_(str(area)), 15, current_factor()) / 2 + 18), y + 34, area, col, ctx, 15, 280, "hypothesis area")
        c += TCW(x + 22, y + 90, text, 26, 19, "var(--white)", W6, 1.3, "start")
        c += T(x + 22, y + 244, gate, fit(gate, 15, 240, "hypothesis gate"), "var(--c4)", W6)
        c += f'<g>{loop("opacity", ".35;1;.35", 2.6, k * .6)}<circle cx="{x + 290}" cy="{y + 34}" r="16" fill="none" stroke="var(--c4)" stroke-width="2.5"/></g>'
        c += TC(x + 290, y + 41, "?", 20, "var(--c4)", W6)
        cards.append(c)
    return glow(1180, 450, 430, "var(--brand)", .45) + seq(cards, .1, .5, 16), D, FREEZE


@register("scene", "models")
def sc_models(sl, ctx):
    """Ways to start working together, side by side. A frame visits each one in turn: the proposal picks with them."""
    cols = ("var(--c1)", "var(--accent)", "var(--c3)", "var(--c2)")
    n, gap, y0, h = len(sl["models"]), 24, 430, 290
    w = (1408 - gap * (n - 1)) / n
    xs = [96 + k * (w + gap) for k in range(n)]
    parts = []
    for x, (name, promise, items), col in zip(xs, sl["models"], cols):
        c = card(x, y0, w, h, "var(--card)", col, 18, 2)
        c += pill(x + 24 + min(w / 2 - 24, bold_width(_(str(name)), 17, current_factor()) / 2 + 18), y0 + 36, name, col, ctx, 17, w - 48, "model name")
        c += T(x + 24, y0 + 88, promise, fit(promise, 20, w - 48, "model promise"), "var(--c4)", W6)
        for j, it in enumerate(items[:4]):
            c += f'<circle cx="{x + 30:.1f}" cy="{y0 + 126 + j * 42}" r="5" fill="{col}"/>' + T(x + 46, y0 + 132 + j * 42, it, fit(it, 17, w - 70, "model item"), "var(--white)")
        parts.append(c)
    hop = (f'<rect x="{xs[0] - 6:.1f}" y="{y0 - 6}" width="{w + 12:.1f}" height="{h + 12}" rx="22" fill="none" stroke="var(--c4)" stroke-width="3">'
           f'<animateTransform attributeName="transform" type="translate" values="{";".join(f"{x - xs[0]:.1f} 0" for x in xs)}" '
           f'keyTimes="{";".join(f"{k / n:.3f}" for k in range(n))}" dur="{2.5 * n}s" repeatCount="indefinite" calcMode="discrete"/>'
           f'{loop("stroke-opacity", ".3;1;.3", 2.5)}</rect>')
    return glow(800, 600, 560, "var(--brand)", .4) + seq(parts, .1, .5, 20) + land(hop, 1.2, .4, 0), D, FREEZE


@register("scene", "challenge")
def sc_challenge(sl, ctx):
    """The AI plays the client and objects to the script before the meeting does."""
    ok = ctx.brand.c("dark.ok")
    doc_ = (card(860, 170, 290, 440, "var(--card)", "var(--c2)", 16, 2) + T(884, 212, sl["doc"], fit(sl["doc"], 20, 250, "script title"), "var(--white)", W6)
            + bars(884, 244, 240, 10, 32))
    g = [glow(1180, 450, 430, "var(--brand)", .45), land(doc_, .1, .5)]
    bubbles = []
    for k, obj in enumerate(sl["objections"][:3]):
        y = 190 + k * 130
        b = card(1180, y, 340, 104, "var(--dim)", "var(--c5)", 16, 2) + spark(1206, y + 30, .6, "var(--c5)")
        b += TCW(1226, y + 38, obj, 26, 17, "var(--white)", W6, 1.3, "start")
        bubbles.append(b)
    g.append(seq(bubbles, .4, .45, 0))
    g.append(f'<rect x="1180" y="190" width="340" height="104" rx="16" fill="none" stroke="var(--c5)" stroke-width="3">{loop("stroke-opacity", ".15;1;.15", 2.8)}</rect>')
    g.append(land(pill(1005, 660, sl["fixed"], ok, ctx, 17, 300, "script fixed"), 1.4, .4, 10))
    return "".join(g), D, FREEZE


@register("scene", "pilot")
def sc_pilot(sl, ctx):
    """The next step as a path: today's options (our hypotheses or their own priority), a discovery workshop, a prototype a
    week later, then their call and a proposal fitted to them. A frame keeps visiting the options: the choice is theirs."""
    ok = ctx.brand.c("dark.ok")
    cols = ("var(--c1)", "var(--c3)", "var(--c2)", "var(--accent)", "var(--c4)")
    y0, h = 430, 300
    xs = [(96, 280), (446, 360), (876, 300), (1246, 258)]
    (ax, aw), (bx, bw), (cx, cw), (dx, dw) = xs
    opts = sl["cards"][:5]
    a = "".join(card(ax, y0 + k * 60, aw, 50, "var(--card)", col, 14, 2) + f'<circle cx="{ax + 26}" cy="{y0 + 25 + k * 60}" r="7" fill="{col}"/>'
                + T(ax + 44, y0 + 31 + k * 60, name, fit(name, 17, aw - 60, "pilot option"), "var(--white)", W6)
                for k, (name, col) in enumerate(zip(opts, cols)))
    title, rows = sl["workshop"]
    b = card(bx, y0, bw, h, "var(--card)", "var(--c2)", 18, 2) + pill(bx + bw / 2, y0 + 38, title, "var(--c2)", ctx, 17, bw - 40, "pilot workshop")
    for j, (verb, text) in enumerate(rows[:3]):
        y = y0 + 96 + j * 70
        b += T(bx + 24, y, verb, 15, "var(--c4)", W6) + T(bx + 24, y + 28, text, fit(text, 18, bw - 48, "pilot workshop row"), "var(--white)", W6)
    chart = f"M{cx + 30} {y0 + 250} C{cx + 90} {y0 + 240} {cx + 120} {y0 + 180} {cx + 170} {y0 + 190} S{cx + 240} {y0 + 120} {cx + cw - 30} {y0 + 110}"
    c = (card(cx, y0, cw, h, "var(--card)", "var(--c3)", 18, 2) + f'<path d="M{cx} {y0 + 44} H{cx + cw}" stroke="var(--line)" stroke-width="1.5"/>'
         + "".join(f'<circle cx="{cx + 24 + k * 20}" cy="{y0 + 22}" r="5" fill="var(--line)"/>' for k in range(3))
         + T(cx + 24, y0 + 80, sl["proto"], fit(sl["proto"], 18, cw - 48, "pilot prototype"), "var(--white)", W6))
    c_line = trace(chart, "var(--c3)", 4, 1.0, .8) + f'<g>{token("var(--c4)", 7)}{move(chart, [(0, 0), (.8, 1), (1, 1)], 6)}</g>'
    ask_, ways = sl["offer"]
    d = card(dx, y0, dw, h, "var(--card)", ok, 18, 2) + T(dx + 24, y0 + 48, ask_, fit(ask_, 20, dw - 48, "pilot offer"), "var(--white)", W6)
    for j, way in enumerate(ways[:4]):
        y = y0 + 92 + j * 36
        d += (f'<circle cx="{dx + 32}" cy="{y}" r="6" fill="{ok}">{loop("opacity", ".25;1;.25;.25", 8, j * 2)}</circle>'
              + T(dx + 48, y + 6, way, fit(way, 17, dw - 72, "pilot way"), "var(--white)", W6))
    d += pill(dx + dw / 2, y0 + 264, sl["decide"], ok, ctx, 16, dw - 24, "pilot decision")
    arrows = "".join(f'<path d="M{x0 + 10} {y0 + 150} H{x1 - 16}" stroke="var(--c2)" stroke-width="3" stroke-dasharray="6 10">{loop("stroke-dashoffset", "0;-32", 1.6)}</path>'
                     f'<path d="M{x1 - 18} {y0 + 141} L{x1 - 6} {y0 + 150} L{x1 - 18} {y0 + 159}" fill="none" stroke="var(--c2)" stroke-width="3" stroke-linecap="round"/>'
                     for x0, x1 in ((ax + aw, bx), (bx + bw, cx), (cx + cw, dx)))
    when = "".join(TC(x + w / 2, y0 + h + 52, t, fit(t, 17, w, "pilot when"), "var(--c4)", W6) for (x, w), t in zip(xs, sl["when"]))
    n = len(opts)
    hop = (f'<rect x="{ax - 6}" y="{y0 - 5}" width="{aw + 12}" height="60" rx="16" fill="none" stroke="var(--c4)" stroke-width="3">'
           f'<animateTransform attributeName="transform" type="translate" values="{";".join(f"0 {k * 60}" for k in range(n))}" '
           f'keyTimes="{";".join(f"{k / n:.3f}" for k in range(n))}" dur="{2 * n}s" repeatCount="indefinite" calcMode="discrete"/>'
           f'{loop("stroke-opacity", ".3;1;.3", 2)}</rect>')
    return (glow(800, 580, 560, "var(--brand)", .4) + seq([a, b, c, d], .1, .5, 18) + c_line
            + land(arrows + when, .9, .45, 0) + land(hop, 1.3, .4, 0)), D, FREEZE


@register("scene", "criteria")
def sc_criteria(sl, ctx):
    """Why we build: a clear return or a key enabler, joined by an «o». The two cards light up in turns."""
    ok = ctx.brand.c("dark.ok")
    cols = (ok, "var(--c2)")
    cards, glows = [], []
    for k, ((name, text, example), col) in enumerate(zip(sl["criteria"], cols)):
        x, y = 860 + k * 340, 170
        c = card(x, y, 320, 420, "var(--card)", col, 18, 2)
        if k == 0:
            c += "".join(f'<rect x="{x + 28 + j * 30}" y="{y + 110 - hh}" width="20" height="{hh}" rx="4" fill="{col}"/>' for j, hh in enumerate((28, 48, 72)))
        else:
            c += (f'<rect x="{x + 28}" y="{y + 94}" width="100" height="16" rx="4" fill="{col}"/>'
                  + "".join(f'<rect x="{x + 34 + j * 52}" y="{y + 46}" width="36" height="42" rx="4" fill="none" stroke="{col}" stroke-width="3"/>' for j in range(2)))
        c += T(x + 28, y + 172, name, fit(name, 26, 272, "criterion name"), "var(--white)", W6)
        c += TCW(x + 28, y + 216, text, 26, 18, "var(--muted)", W6, 1.35, "start")
        c += T(x + 28, y + 384, example, fit(example, 16, 272, "criterion example"), "var(--c4)", W6)
        cards.append(c)
        glows.append(f'<rect x="{x}" y="{y}" width="320" height="420" rx="18" fill="none" stroke="{col}" stroke-width="4">'
                     f'{loop("stroke-opacity", "0;1;0;0", 6, k * 3)}</rect>')
    orb = (f'<circle cx="1190" cy="380" r="30" fill="var(--dim)" stroke="var(--c4)" stroke-width="3">{loop("stroke-opacity", ".3;1;.3", 3)}</circle>'
           + TC(1190, 389, sl["or"], 24, "var(--white)", W6))
    return (glow(1190, 400, 420, "var(--brand)", .45) + seq(cards, .1, .5, 16) + land("".join(glows) + orb, .9, .4, 0)), D, FREEZE



# ---------------------------------------------------------------- people and a timed loop (the control room close)
# skin and hair are mixed from pack tokens only: no literal colors, and they follow the theme
SKIN_BROWN = "color-mix(in srgb, color-mix(in srgb, var(--c3) 70%, var(--c5)) 58%, var(--ink))"
SKIN_LIGHT = "color-mix(in srgb, color-mix(in srgb, var(--c3) 55%, var(--c5)) 32%, var(--white))"
HAIR = "color-mix(in srgb, var(--ink) 82%, var(--c1))"


def shade(c, k=22):
    return f"color-mix(in srgb, {c} {100 - k}%, var(--ink))"


def beat(attr, pairs, period=D, mode="linear"):
    """A loop with explicit times: pairs = [(fraction of the period, value)], from 0 to 1."""
    kt = ";".join(f"{t:.3f}" for t, _ in pairs)
    vals = ";".join(str(v) for _, v in pairs)
    return f'<animate attributeName="{attr}" values="{vals}" keyTimes="{kt}" dur="{period}s" repeatCount="indefinite" calcMode="{mode}"/>'


def _eye(x, y, period, phase=0.0):
    return (f'<ellipse cx="{x}" cy="{y}" rx="3.2" ry="4.2" fill="var(--ink)">'
            f'<animate attributeName="ry" values="4.2;4.2;.4;4.2" keyTimes="0;.92;.96;1" dur="{period}s" begin="-{phase}s" repeatCount="indefinite"/></ellipse>')


def _woman(x, y, s, skin, jacket):
    """Faceless, three-quarter view, facing right and up at the wall screen, pointing at it: long hair, earring."""
    rim = 'fill="none" stroke="var(--c2)" stroke-width="1.2" opacity=".55"'
    arm = (f'<path d="M56 50 L96 8 L112 -46" fill="none" stroke="{jacket}" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/>'
           f'<path d="M56 50 L96 8 L112 -46" {rim}/>'
           f'<circle cx="113" cy="-54" r="8" fill="{skin}"/><path d="M115 -60 L121 -76" stroke="{skin}" stroke-width="4" stroke-linecap="round"/>')
    body = (f'<path d="M-36 -58 C-46 -106 6 -128 34 -102 C46 -90 44 -70 40 -58 L28 -68 C10 -82 -10 -80 -18 -62 C-22 -40 -20 -12 -26 12 '
            f'C-30 32 -50 46 -58 30 C-64 12 -46 -14 -42 -32 C-40 -42 -38 -50 -36 -58 Z" fill="{HAIR}"/>'
            f'<path d="M-66 176 C-68 100 -52 50 -20 36 C-8 32 12 32 26 36 C56 48 72 100 74 176 Z" fill="{jacket}"/>'
            f'<path d="M-66 176 C-68 100 -52 50 -20 36 C-8 32 12 32 26 36 C56 48 72 100 74 176" {rim}/>'
            f'<path d="M-8 36 C-3 48 7 48 14 36 L20 78 L3 100 L-14 78 Z" fill="var(--white)" opacity=".92"/>'
            f'<path d="M-11 -6 C-10 12 -10 24 -12 38 C-2 44 10 44 16 38 C12 24 12 10 12 -6 Z" fill="{shade(skin, 14)}"/>'
            f'<path d="M-20 -60 C-22 -94 4 -106 26 -97 C42 -90 46 -72 42 -56 C40 -43 34 -31 24 -24 C13 -17 -3 -19 -13 -30 C-20 -39 -20 -49 -20 -60 Z" fill="{skin}"/>'
            f'<ellipse cx="-11" cy="-54" rx="5" ry="8" fill="{shade(skin, 14)}"/><circle cx="-11" cy="-43" r="2.8" fill="var(--c4)"/>'
            f'<path d="M-22 -66 C-20 -100 14 -112 36 -94 C43 -87 43 -80 41 -74 C30 -87 12 -90 -2 -83 C-11 -78 -16 -70 -19 -59 Z" fill="{HAIR}"/>'
            f'<path d="M-12 -94 C4 -105 24 -101 33 -90" {rim}/>')
    return f'<g transform="translate({x} {y}) scale({s})">{body}<g>{sway(56, 50, 3, 5)}{arm}</g></g>'


def _man(x, y, s, skin, shirt, tap):
    """Faceless, three-quarter view, facing right, head down at the tablet where he approves the move; thin headset."""
    rim = 'fill="none" stroke="var(--c2)" stroke-width="1.2" opacity=".55"'
    head = (f'<path d="M-22 -58 C-24 -94 2 -108 26 -99 C44 -92 48 -74 44 -55 C42 -40 36 -28 26 -21 C13 -13 -5 -15 -15 -26 C-22 -35 -22 -46 -22 -58 Z" fill="{skin}"/>'
            f'<ellipse cx="-13" cy="-52" rx="5" ry="8" fill="{shade(skin, 14)}"/>'
            f'<path d="M-26 -56 C-30 -98 6 -116 32 -101 C43 -94 46 -84 44 -77 C35 -86 20 -89 8 -87 C-2 -85 -9 -79 -12 -68 C-14 -62 -17 -57 -21 -51 Z" fill="{HAIR}"/>'
            f'<path d="M-30 -60 C-26 -106 28 -114 41 -80" fill="none" stroke="var(--c4)" stroke-width="3" stroke-linecap="round"/>'
            f'<rect x="-21" y="-64" width="12" height="22" rx="5" fill="var(--c4)"/>'
            f'<path d="M-12 -44 C0 -30 14 -28 27 -30" fill="none" stroke="var(--c4)" stroke-width="2" stroke-linecap="round"/><circle cx="29" cy="-30" r="3" fill="var(--c4)"/>')
    tablet = (f'<g transform="translate(44 102) rotate(-10)">'
              f'<rect x="-62" y="-42" width="124" height="86" rx="10" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.5"/>'
              f'<rect x="-55" y="-35" width="110" height="72" rx="6" fill="var(--card)"/>'
              + bars(-46, -26, 88, 2, 12, "var(--c2)", ".5") + tap + '</g>')
    body = (f'<path d="M-70 178 C-72 102 -54 52 -20 38 C-8 34 12 34 26 38 C58 52 74 104 76 178 Z" fill="{shirt}"/>'
            f'<path d="M-70 178 C-72 102 -54 52 -20 38 C-8 34 12 34 26 38 C58 52 74 104 76 178" {rim}/>'
            f'<path d="M-16 38 L2 56 L20 38 L11 31 L2 44 L-7 31 Z" fill="var(--white)" opacity=".92"/>'
            f'<path d="M-11 -6 C-10 12 -10 24 -12 40 C-2 46 10 46 16 40 C12 24 12 10 12 -6 Z" fill="{shade(skin, 14)}"/>'
            f'<g transform="rotate(9 0 -20)"><g>{bob(0, 2.5, 4)}{head}</g></g>'
            f'<path d="M-54 80 Q-62 128 -22 116" fill="none" stroke="{shade(shirt, 12)}" stroke-width="15" stroke-linecap="round"/>'
            f'<path d="M58 80 Q76 118 98 98" fill="none" stroke="{shade(shirt, 12)}" stroke-width="15" stroke-linecap="round"/>'
            + tablet
            + f'<circle cx="-18" cy="114" r="8" fill="{skin}"/><circle cx="102" cy="95" r="8" fill="{skin}"/>')
    return f'<g transform="translate({x} {y}) scale({s})">{body}</g>'


@register("scene", "controlroom")
def sc_controlroom(sl, ctx):
    """The close, tomorrow's control room, told as one 12-second loop. The forecast crosses its limit (alert,
    anticipated), the AI suggests moving the spare part, the operator approves it on his tablet, the part travels from
    the warehouse to the station, and the station turns green: proactive maintenance declared. The frozen frame
    (reduced motion, 0.9 of the loop) is the resolved one."""
    ok = ctx.brand.c("dark.ok")
    sx, sy, sw, sh = 1000, 80, 550, 460
    alert_on = [(0, 1), (.56, 1), (.6, 0), (.97, 0), (1, 1)]
    done_on = [(0, 0), (.56, 0), (.6, 1), (.96, 1), (1, 0)]
    g = [glow(1275, 300, 470, "var(--brand)", .55)]
    cone = (f'<path d="M{sx + 30} {sy + sh} L{sx + sw - 30} {sy + sh} L1560 900 L800 900 Z" fill="var(--c2)" opacity=".07">'
            f'{loop("opacity", ".04;.12;.04", 5)}</path>')
    hud = "".join(f'<path d="M{x0} {y0 + dy * 22} V{y0} H{x0 + dx * 22}" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity=".8" transform="translate({dx * -8} {dy * -8})"/>'
                  for x0, y0, dx, dy in ((sx, sy, 1, 1), (sx + sw, sy, -1, 1), (sx, sy + sh, 1, -1), (sx + sw, sy + sh, -1, -1)))
    hud += (f'<rect x="{sx + 2}" y="{sy + 46}" width="{sw - 4}" height="2" fill="var(--c2)" opacity=".18">'
            f'<animateTransform attributeName="transform" type="translate" values="0 0;0 {sh - 52}" dur="5s" repeatCount="indefinite"/></rect>')
    screen = (card(sx, sy, sw, sh, "var(--card)", "var(--c2)", 22, 1.2) + hud
              + f'<path d="M{sx} {sy + 44} H{sx + sw}" stroke="var(--line)" stroke-width="1.5"/>'
              + f'<circle cx="{sx + 24}" cy="{sy + 22}" r="7" fill="var(--c5)">{blink(1.4)}</circle>'
              + T(sx + 42, sy + 28, sl["screen"], fit(sl["screen"], 16, 360, "control room screen"), "var(--white)", W6)
              + f'<g>{loop("opacity", ".4;1;.4", 3)}{spark(sx + sw - 26, sy + 22, .6, "var(--c4)")}</g>')
    # chart: the real trace stays under the limit; the forecast (dashed) crosses it
    ax, ay, aw = sx + 16, sy + 56, sw - 32
    real = [(0, 110), (34, 104), (68, 112), (102, 100), (136, 108), (170, 96), (204, 102), (238, 90), (272, 84), (306, 78), (340, 72), (364, 70)]
    d = "M" + " L".join(f"{ax + 16 + x} {ay + y}" for x, y in real)
    area = d + f" L{ax + 380} {ay + 140} L{ax + 16} {ay + 140} Z"
    fc = f"M{ax + 380} {ay + 70} L{ax + 440} {ay + 52} L{ax + aw - 16} {ay + 36}"
    chart = (card(ax, ay, aw, 150, "var(--dim)", "var(--line)", 14, 1.5)
             + T(ax + 16, ay + 26, sl["chart"], fit(sl["chart"], 15, 260, "control room chart"), "var(--muted)", W6)
             + T(ax + aw - 16, ay + 26, sl["forecast"], fit(sl["forecast"], 15, 150, "control room forecast"), "var(--c4)", 'text-anchor="end" font-weight="600"')
             + f'<path d="M{ax + 16} {ay + 60} H{ax + aw - 16}" stroke="var(--c5)" stroke-width="1.2" stroke-dasharray="4 5" opacity=".85"/>')
    lines = (land(f'<path d="{area}" fill="var(--c3)" opacity=".14"/>', .5, .6, 0) + trace(d, "var(--c3)", 2, .45, .8)
             + f'<g>{beat("opacity", [(0, 1), (.56, 1), (.62, .25), (.96, .25), (1, 1)])}{trace(fc, "var(--c4)", 1.8, 1.2, .5, chr(32) + "stroke-dasharray=" + chr(34) + "7 7" + chr(34))}</g>'
             + f'<g>{token("var(--c4)", 6)}{move(d, [(0, 0), (.85, 1), (1, 1)], 6)}</g>')
    hx = ax + 440 - 30
    alert = (f'<g>{beat("opacity", alert_on)}'
             f'<circle cx="{hx}" cy="{ay + 60}" r="12" fill="none" stroke="var(--c5)" stroke-width="1.5">{loop("r", "10;24;10", 2.4)}</circle>'
             + pill(ax + aw - 110, ay + 122, sl["alert"], "var(--c5)", ctx, 15, 200, "control room alert", 14) + '</g>')
    # map: warehouse, route, station; the suggestion toast, the part in transit, proactive maintenance on arrival
    mx, my, mw, mh = sx + 16, sy + 218, sw - 32, 226
    grid = "".join(f'<path d="M{mx + k * 40} {my} V{my + mh}" stroke="var(--c2)" stroke-width="1" opacity=".07"/>' for k in range(1, mw // 40 + 1))
    grid += "".join(f'<path d="M{mx} {my + k * 40} H{mx + mw}" stroke="var(--c2)" stroke-width="1" opacity=".07"/>' for k in range(1, mh // 40 + 1))
    wx, wy = mx + 84, my + 160
    tx, ty = mx + mw - 64, my + 148
    route = f"M{wx + 36} {wy + 4} C{wx + 130} {wy + 40} {wx + 210} {wy - 90} {tx - 30} {ty}"
    mp = (card(mx, my, mw, mh, "var(--dim)", "var(--line)", 14, 1.5) + grid
          + f'<path d="M{wx - 36} {wy - 12} L{wx} {wy - 38} L{wx + 36} {wy - 12} Z" fill="none" stroke="var(--c2)" stroke-width="1.5"/>'
          + card(wx - 32, wy - 12, 64, 42, "var(--card)", "var(--c2)", 4, 1.2) + f'<rect x="{wx - 11}" y="{wy + 4}" width="22" height="26" rx="3" fill="none" stroke="var(--c2)" stroke-width="1.2"/>'
          + TC(wx, wy + 56, sl["warehouse"], fit(sl["warehouse"], 15, 150, "control room warehouse"), "var(--muted)", W6)
          + f'<path d="{route}" fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="3 7" opacity=".8">{loop("stroke-dashoffset", "0;-28", 1.4)}</path>'
          + f'<circle cx="{tx}" cy="{ty}" r="26" fill="var(--card)" stroke="var(--c2)" stroke-width="1.2"/><circle cx="{tx}" cy="{ty}" r="9" fill="none" stroke="var(--c2)" stroke-width="1.5"/><circle cx="{tx}" cy="{ty}" r="44" fill="none" stroke="var(--c2)" stroke-width="1" stroke-dasharray="2 6" opacity=".6">{loop("stroke-dashoffset", "0;-32", 3)}</circle>'
          + TC(tx, ty + 56, sl["station"], fit(sl["station"], 15, 150, "control room station"), "var(--muted)", W6))
    st_alert = f'<g>{beat("opacity", alert_on)}<circle cx="{tx}" cy="{ty}" r="26" fill="none" stroke="var(--c3)" stroke-width="1.5">{loop("r", "26;38;26", 2)}</circle></g>'
    st_ok = (f'<g>{beat("opacity", done_on)}<circle cx="{tx}" cy="{ty}" r="26" fill="{ok}"/>' + check(tx, ty + 1, .9, "var(--ink)")
             + pill(tx - 90, ty - 58, sl["done"], ok, ctx, 15, 250, "control room done", 14) + '</g>')
    wh_ping = f'<circle cx="{wx}" cy="{wy}" r="30" fill="none" stroke="var(--c4)" stroke-width="1.5">{beat("r", [(0, 30), (.22, 30), (.34, 56), (1, 56)])}{beat("opacity", [(0, 0), (.22, 0), (.23, 1), (.34, 0), (1, 0)])}</circle>'
    van = (f'<g>{beat("opacity", [(0, 0), (.25, 0), (.28, 1), (.57, 1), (.62, 0), (1, 0)])}{move(route, [(0, 0), (.28, 0), (.58, 1), (1, 1)], D)}'
           + token("var(--c4)", 6)
           + f'<rect x="-20" y="-11" width="26" height="18" rx="3" fill="var(--c4)" fill-opacity=".25" stroke="var(--c4)" stroke-width="1.5"/><rect x="6" y="-7" width="13" height="14" rx="3" fill="var(--c4)" fill-opacity=".25" stroke="var(--c4)" stroke-width="1.5"/>'
           f'<circle cx="-11" cy="9" r="3.5" fill="none" stroke="var(--c4)" stroke-width="1.5"/><circle cx="12" cy="9" r="3.5" fill="none" stroke="var(--c4)" stroke-width="1.5"/></g>')
    toast = (f'<g>{beat("opacity", [(0, 0), (.08, 0), (.11, 1), (.46, 1), (.5, 0), (1, 0)])}'
             + card(mx + 14, my + 12, 420, 44, "var(--card)", "var(--c2)", 12, 1.2) + spark(mx + 36, my + 34, .55, "var(--c4)")
             + T(mx + 56, my + 40, sl["suggest"], fit(sl["suggest"], 15, 360, "control room suggestion"), "var(--white)", W6) + '</g>')
    # the tablet: «Aprobar» until he taps it, then approved
    tap = (f'<g>{beat("opacity", [(0, 1), (.22, 1), (.25, 0), (.97, 0), (1, 1)])}' + pill(0, 16, sl["approve"], "var(--c4)", ctx, 14, 110, "control room approve", 12) + '</g>'
           f'<g>{beat("opacity", [(0, 0), (.23, 0), (.26, 1), (.96, 1), (1, 0)])}<rect x="-34" y="4" width="68" height="24" rx="12" fill="{ok}"/>' + check(0, 17, .6, "var(--ink)") + '</g>'
           f'<circle cx="0" cy="16" r="6" fill="none" stroke="var(--white)" stroke-width="1.5">{beat("r", [(0, 6), (.21, 6), (.3, 34), (1, 34)])}'
           f'{beat("opacity", [(0, 0), (.21, 0), (.22, 1), (.3, 0), (1, 0)])}</circle>')
    people = _woman(905, 690, 1.1, SKIN_BROWN, "var(--accent)") + _man(1250, 716, 1.0, SKIN_LIGHT, "var(--c1)", tap)
    sign = T(sx + sw, sy + sh + 34, sl["sign"], fit(sl["sign"], 20, 330, "control room sign"), "var(--c4)", 'text-anchor="end" font-weight="600"')
    return (g[0] + land(cone, .2, .6, 0) + land(screen, .1, .5, 16) + land(chart + mp, .3, .45, 10) + lines
            + alert + st_alert + st_ok + wh_ping + van + toast + land(sign, 1.4, .45, 10)
            + land(_woman(905, 690, 1.1, SKIN_BROWN, "var(--accent)"), .25, .6, 40) + land(_man(1250, 716, 1.0, SKIN_LIGHT, "var(--c1)", tap), .4, .6, 40)), D, FREEZE



@register("scene", "chain")
def sc_chain(sl, ctx):
    """«¿Dónde están hoy?»: the four layers as one chain (governance, data, insights, agents), each with the question
    that places the client in it. The presenter taps the layer they name (deck.js marks it and stops the slide from
    advancing); the glowing field fills with their answer. Until then a «?» visits the layers and the field waits."""
    cols = ("var(--c4)", "var(--c2)", "var(--c3)", "var(--accent)")
    n, gap, y0, h = len(sl["layers"]), 20, 444, 290
    w = (1408 - gap * (n - 1)) / n
    xs = [96 + k * (w + gap) for k in range(n)]
    g = [glow(800, 600, 600, "var(--brand)", .45),
         land(card(96, 388, 1408, 40, "var(--dim)", "var(--line)", 20, 1.2)
              + TC(800, 414, sl["base"], fit(sl["base"], 15, 1320, "chain base"), "var(--muted)", W6), .1, .45, 0)]
    for k, (x, (name, question, items), col) in enumerate(zip(xs, sl["layers"], cols)):
        c = (card(x, y0, w, h, "var(--card)", "var(--line)", 16, 1.2) + f'<rect x="{x:.1f}" y="{y0}" width="{w:.1f}" height="4" rx="2" fill="{col}"/>'
             + T(x + 18, y0 + 40, f"0{k + 1}", 18, "var(--c4)", W6) + T(x + 56, y0 + 40, name, fit(name, 18, w - 76, "chain layer"), "var(--white)", W6)
             + TCW(x + 18, y0 + 78, question, 34, 16, "var(--muted)", 'font-weight="600" font-style="italic"', 1.3, "start"))
        for j, it in enumerate(items[:3]):
            yy = y0 + 150 + j * 44
            c += f'<path d="M{x + 18:.1f} {yy} H{x + w - 18:.1f}" stroke="var(--line)" stroke-width="1"/>' + T(x + 18, yy + 30, it, fit(it, 16, w - 36, "chain item"), "var(--white)", W6)
        c += (f'<g class="pick-ring"><rect x="{x - 4:.1f}" y="{y0 - 4}" width="{w + 8:.1f}" height="{h + 8}" rx="20" fill="none" stroke="var(--c4)" stroke-width="3"/>'
              + pill(x + w - 50, y0 + 34, sl["today"], "var(--c4)", ctx, 15, 90, "chain today", 14) + '</g>')
        c += f'<rect x="{x:.1f}" y="{y0}" width="{w:.1f}" height="{h}" rx="16" fill="var(--ink)" opacity="0"/>'
        g.append(land(f'<g data-pick="{k}">{c}</g>', .2 + k * .12, .5, 18))
        if k:
            g.append(land(f'<path d="M{x - 14:.1f} {y0 + 30} L{x - 6:.1f} {y0 + 36} L{x - 14:.1f} {y0 + 42}" fill="none" stroke="var(--c4)" stroke-width="1.8" stroke-linecap="round"/>', .8, .4, 0))
    g.append(f'<g>{token("var(--c4)", 5)}{move(f"M96 {y0 + 2} H1504", [(0, 0), (1, 1)], 8)}</g>')
    ys = [(x + w - 34, y0 + 34) for x in xs]
    g.append(land(f'<g data-hop=""><animateTransform attributeName="transform" type="translate" values="{";".join(f"{x - ys[0][0]:.1f} 0" for x, _ in ys)}" '
                  f'keyTimes="{";".join(f"{k / n:.3f}" for k in range(n))}" dur="{3 * n}s" repeatCount="indefinite" calcMode="discrete"/>'
                  f'<circle cx="{ys[0][0]:.1f}" cy="{ys[0][1]}" r="16" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5">{loop("r", "16;20;16", 3)}</circle>'
                  + TC(f"{ys[0][0]:.1f}", ys[0][1] + 6, "?", 18, "var(--c4)", W6) + '</g>', 1.2, .4, 0))
    # the placeholder: a glowing field that waits for their answer
    fx, fy, fw_ = 360, 752, 880
    ph = sl["placeholder"]
    cur_x = fx + 64 + bold_width(_(str(ph)), 22, current_factor()) + 8
    field = (card(fx, fy, fw_, 60, "var(--card)", "var(--c4)", 30, 1.5)
             + f'<rect x="{fx}" y="{fy}" width="{fw_}" height="60" rx="30" fill="none" stroke="var(--c4)" stroke-width="4" opacity=".5">{loop("stroke-opacity", ".1;.8;.1", 3)}</rect>'
             + spark(fx + 36, fy + 30, .6, "var(--c4)")
             + f'<g data-placeholder="">' + T(fx + 64, fy + 38, ph, 22, "var(--muted)", W6)
             + f'<rect x="{cur_x:.1f}" y="{fy + 16}" width="3" height="28" fill="var(--c4)">{blink(1.1)}</rect></g>'
             + "".join(f'<g data-answer="{k}" opacity="0">' + T(fx + 64, fy + 38, ans, fit(ans, 22, fw_ - 260, "chain answer"), "var(--white)", W6) + '</g>'
                       for k, ans in enumerate(sl["answers"]))
             + T(fx + fw_ - 28, fy + 37, sl["hint"], fit(sl["hint"], 15, 200, "chain hint"), "var(--c4)", 'text-anchor="end" font-weight="600"'))
    g.append(land(field, 1.0, .5, 14))
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- T-002 · pagos: the Dust delta (our case, federated autonomy)
def _user(x, y, s=1.0, color="var(--c2)"):
    """A faceless person in thin strokes: the technological look of the Dust slides."""
    return (f'<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round">'
            f'<circle cx="0" cy="-22" r="12"/><path d="M-22 16 C-22 -2 -12 -8 0 -8 C12 -8 22 -2 22 16"/></g>')


def _lock(x, y, color="var(--accent)"):
    return (f'<g fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round"><path d="M{x - 6} {y - 2} V{y - 7} A6 6 0 0 1 {x + 6} {y - 7} V{y - 2}"/>'
            f'<rect x="{x - 9}" y="{y - 2}" width="18" height="14" rx="3" fill="{color}" fill-opacity=".2"/></g>')


def _hop(path, ph, frac, r):
    """A token that travels path during the first frac of the loop, starting ph seconds in, then hides until the next lap."""
    shown = beat("opacity", [(0, 1), (frac, 1), (frac + .02, 0), (1, 0)]).replace("<animate ", f'<animate begin="-{ph}s" ')
    return f'<g>{token("var(--c4)", r)}{move(path, [(0, 0), (frac, 1), (1, 1)], D, -ph)}{shown}</g>'


@register("scene", "dustcase")
def sc_dustcase(sl, ctx):
    """Our own case, as three tiers: the company's connected knowledge, the agents each team builds on it, and the people
    who use them. Each tier names itself on the left; on the right, knowledge rises column by column and an agent lights
    up when it answers."""
    xs = (1140, 1250, 1360, 1470)
    tiers = ((150, sl["people"], "var(--c2)"), (345, sl["agents"], "var(--accent)"), (540, sl["knowledge"], "var(--c1)"))
    g = [glow(1195, 450, 440, "var(--brand)", .5)]
    bands = [card(860, y, 670, 150, "var(--card)", col, 16, 1.4) + TCW(884, y + 56, label, 18, 17, "var(--white)", W6, 1.25, "start")
             for y, label, col in tiers]
    g.append(seq(bands, .1, .5, 16))
    people = "".join(_user(x, 262, 1.1, "var(--c2)") for x in xs)
    agents = "".join(card(x - 40, 392, 80, 60, "var(--dim)", "var(--accent)", 14, 1.4) + spark(x, 422, .8, "var(--accent)") for x in xs)
    docs = "".join(card(x - 34 + k * 10, 578 + k * 8, 50, 62, "var(--dim)", "var(--c1)", 6, 1.2) for x in xs for k in range(2))
    docs += "".join(bars(x - 18, 606, 30, 3, 10, "var(--c2)", ".6") for x in xs)
    g.append(land(people, .5, .5, 12) + land(agents, .65, .5, 12) + land(docs, .8, .5, 12))
    wires = "".join(f'<path d="M{x} 574 V456 M{x} 388 V284" fill="none" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 6"/>' for x in xs)
    g.append(land(wires, 1.0, .4, 0))
    for k, x in enumerate(xs):  # knowledge climbs to the agent, the agent answers the person: one column after another
        ph = (D - k * 3) % D  # column k starts 3k s in: left to right
        g.append(_hop(f"M{x} 600 L{x} 280", ph, .25, 5))
        g.append(f'<rect x="{x - 40}" y="392" width="80" height="60" rx="14" fill="none" stroke="var(--c4)" stroke-width="3">'
                 f'{loop("stroke-opacity", "0;1;0;0;0;0;0;0", D, ph)}</rect>')
    g.append(land(pill(1195, 752, sl["badge"], "var(--c4)", ctx, 17, 560, "dust case badge"), 1.3, .45, 12))
    return "".join(g), D, FREEZE


@register("scene", "federated")
def sc_federated(sl, ctx):
    """Federated autonomy under central governance: four team spaces (one restricted) each run their own agents, while
    governance at the center sets who sees what, watches usage and keeps the record. Signals travel from every space to
    the center, which answers with a pulse; usage bars and log rows breathe on the side panels."""
    ok = ctx.brand.c("dark.ok")
    cx, cy = 1195, 455
    boxes = ((860, 120), (1290, 120), (860, 640), (1290, 640))
    bw, bh = 240, 150
    corners = ((1100, 270), (1290, 270), (1100, 640), (1290, 640))
    g = [glow(cx, cy, 440, "var(--brand)", .5)]
    links = "".join(f'<path d="M{x} {y} L{cx} {cy}" stroke="var(--line)" stroke-width="6" stroke-linecap="round"/>'
                    f'<path d="M{cx} {cy} L{x} {y}" fill="none" stroke="var(--c4)" stroke-width="2" stroke-dasharray="5 12">{loop("stroke-dashoffset", "0;-34", 1.8)}</path>'
                    for x, y in corners)
    g.append(land(links, .1, .5, 0))
    hub = (f'<circle r="96" fill="var(--card)" stroke="var(--c4)" stroke-width="3"/>'
           + TC(0, 6, sl["center"], fit(sl["center"], 22, 168, "federated hub"), "var(--white)", W6)
           + TC(0, 38, sl["center_sub"], fit(sl["center_sub"], 14, 150, "federated hub sub"), "var(--c4)", W6))
    g.append(pop(hub, cx, cy, .3, .5))
    spaces = []
    for k, ((x, y), (name, kind, closed)) in enumerate(zip(boxes, sl["spaces"])):
        col = "var(--accent)" if closed else "var(--c2)"
        c = card(x, y, bw, bh, "var(--card)", col, 16, 2)
        c += T(x + 20, y + 36, name, fit(name, 19, 170, "federated space"), "var(--white)", W6)
        c += T(x + 20, y + 60, kind, fit(kind, 14, 190, "federated space kind"), "var(--muted)", W6)
        c += _lock(x + bw - 26, y + 30) if closed else ""
        c += _user(x + 48, y + 120, .95, "var(--c2)")
        c += "".join(f'<path d="M{x + 72} {y + 108} L{x + 112 + j * 48} {y + 110}" stroke="var(--line)" stroke-width="1.5"/>' for j in range(3))
        c += "".join(card(x + 94 + j * 48, y + 92, 36, 36, "var(--dim)", col, 10, 1.2) for j in range(3))
        c += "".join(f'<g>{loop("opacity", ".3;1;.3", 3, k * .7 + j * 1)}{spark(x + 112 + j * 48, y + 110, .6, col)}</g>' for j in range(3))
        spaces.append(c)
    g.append(seq(spaces, .45, .5, 14))
    for k, (x, y) in enumerate(corners):  # each space reports to the center; the center answers with a pulse
        ph = (D - k * 3) % D
        g.append(_hop(f"M{x} {y} L{cx} {cy - 0.01}", ph, .27, 6) + f'<circle cx="{cx}" cy="{cy}" r="96" fill="none" stroke="var(--c4)" stroke-width="2">'
                 f'{loop("r", "96;96;120;96;96;96;96;96", D, ph)}{loop("opacity", "0;0;.8;0;0;0;0;0", D, ph)}</circle>')
    # side panels: usage per team (monitoring) and the record (control)
    px, py, pw, ph_ = 860, 385, 205, 140
    use = card(px, py, pw, ph_, "var(--dim)", "var(--line)", 14, 1.2) + T(px + 16, py + 30, sl["monitor"], fit(sl["monitor"], 15, pw - 32, "federated monitor"), "var(--c4)", W6)
    for j, (w0, w1) in enumerate(((.8, .55), (.5, .8), (.65, .4), (.35, .6))):
        yy, full = py + 50 + j * 21, pw - 32
        use += (f'<rect x="{px + 16}" y="{yy}" width="{full}" height="9" rx="4.5" fill="var(--line)" opacity=".5"/>'
                f'<rect x="{px + 16}" y="{yy}" width="{full * w0:.0f}" height="9" rx="4.5" fill="{"var(--accent)" if j == 3 else "var(--c2)"}">'
                f'{loop("width", f"{full * w0:.0f};{full * w1:.0f};{full * w0:.0f}", 6 + j, j)}</rect>')
    qx = 1325
    rec = card(qx, py, pw, ph_, "var(--dim)", "var(--line)", 14, 1.2) + T(qx + 16, py + 30, sl["audit"], fit(sl["audit"], 15, pw - 32, "federated audit"), "var(--c4)", W6)
    for j, row in enumerate(sl["rows"][:3]):
        yy = py + 60 + j * 28
        rec += (f'<g>{loop("opacity", ".45;1;.45", 4, j * 1.3)}<circle cx="{qx + 26}" cy="{yy - 5}" r="8" fill="{ok}"/>{check(qx + 26, yy - 4, .45, "var(--ink)")}</g>'
                + T(qx + 42, yy, row, fit(row, 14, pw - 56, "federated audit row"), "var(--white)", W6))
    g.append(land(use, 1.1, .45, 10) + land(rec, 1.25, .45, 10))
    return "".join(g), D, FREEZE


def _leg(path, a, b, r=6):
    """A token that travels path between fractions a and b of the loop and is hidden the rest of the time."""
    shown = beat("opacity", [(0, 0), (a, 0), (a + .005, 1), (b, 1), (b + .005, 0), (1, 0)])
    return f'<g>{token("var(--c4)", r)}{move(path, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{shown}</g>'


def _swap(pairs_on, inner):
    return f'<g>{beat("opacity", pairs_on)}{inner}</g>'


@register("scene", "tickets")
def sc_tickets(sl, ctx):
    """The close of the pagos deck, merchant tickets that answer themselves, told as one 12-second loop. Four tickets arrive; a
    governed knowledge agent answers the three simple ones from its space (restricted, with its lock) and they close as
    self-served; the sensitive one goes to a person with the full context, who resolves it on his tablet: people decide.
    IT watches the self-served share (a bar, never a number), usage per space and the record. The frozen frame (0.9 of the
    loop) is the resolved one: a calm queue."""
    ok = ctx.brand.c("dark.ok")
    sx, sy, sw, sh = 860, 80, 690, 460
    g = [glow(1205, 300, 480, "var(--brand)", .55)]
    cone = (f'<path d="M{sx + 40} {sy + sh} L{sx + sw - 30} {sy + sh} L1560 900 L800 900 Z" fill="var(--c2)" opacity=".07">'
            f'{loop("opacity", ".04;.12;.04", 5)}</path>')
    hud = "".join(f'<path d="M{x0} {y0 + dy * 22} V{y0} H{x0 + dx * 22}" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity=".8" transform="translate({dx * -8} {dy * -8})"/>'
                  for x0, y0, dx, dy in ((sx, sy, 1, 1), (sx + sw, sy, -1, 1), (sx, sy + sh, 1, -1), (sx + sw, sy + sh, -1, -1)))
    hud += (f'<rect x="{sx + 2}" y="{sy + 46}" width="{sw - 4}" height="2" fill="var(--c2)" opacity=".18">'
            f'<animateTransform attributeName="transform" type="translate" values="0 0;0 {sh - 52}" dur="5s" repeatCount="indefinite"/></rect>')
    screen = (card(sx, sy, sw, sh, "var(--card)", "var(--c2)", 22, 1.2) + hud
              + f'<path d="M{sx} {sy + 44} H{sx + sw}" stroke="var(--line)" stroke-width="1.5"/>'
              + f'<circle cx="{sx + 24}" cy="{sy + 22}" r="7" fill="var(--c5)">{blink(1.4)}</circle>'
              + T(sx + 42, sy + 28, sl["screen"], fit(sl["screen"], 16, 420, "tickets screen"), "var(--white)", W6)
              + f'<g>{loop("opacity", ".4;1;.4", 3)}{spark(sx + sw - 26, sy + 22, .6, "var(--c4)")}</g>')
    # the queue: four tickets; each status swaps on its beat (new, then self-served; the sensitive one: routed, then closed)
    qx, qw, qh = 876, 330, 56
    ys = [166 + k * 64 for k in range(4)]
    done = [.23, .39, .55]          # the three simple tickets close here
    head = T(qx, 150, sl["queue"], 14, "var(--muted)", W6)
    tickets = []
    for k, (q, y) in enumerate(zip(sl["tickets"][:4], ys)):
        c = card(qx, y, qw, qh, "var(--dim)", "var(--line)", 12, 1.2) + T(qx + 16, y + 23, q, fit(q, 15, qw - 40, "ticket question"), "var(--white)", W6)
        new = f'<circle cx="{qx + qw - 18}" cy="{y + 18}" r="5" fill="var(--c2)"/>' + T(qx + 16, y + 45, sl["new"], 13, "var(--muted)", W6)
        if k < 3:
            r = done[k]
            c += _swap([(0, 1), (r, 1), (r + .01, 0), (.97, 0), (1, 1)], new)
            c += _swap([(0, 0), (r, 0), (r + .01, 1), (.97, 1), (1, 0)],
                       f'<circle cx="{qx + qw - 18}" cy="{y + 18}" r="5" fill="{ok}"/>' + T(qx + 16, y + 45, sl["solved"], fit(sl["solved"], 13, qw - 40, "ticket status"), ok, W6))
        else:
            c += _swap([(0, 1), (.64, 1), (.65, 0), (.97, 0), (1, 1)], new)
            c += _swap([(0, 0), (.64, 0), (.65, 1), (.80, 1), (.81, 0), (1, 0)],
                       f'<circle cx="{qx + qw - 18}" cy="{y + 18}" r="5" fill="var(--accent)"/>' + T(qx + 16, y + 45, sl["routed"], fit(sl["routed"], 13, qw - 40, "ticket status"), "var(--c2)", W6)
                       + f'<rect x="{qx}" y="{y}" width="{qw}" height="{qh}" rx="12" fill="none" stroke="var(--accent)" stroke-width="2.5">{loop("stroke-opacity", ".3;1;.3", 1.2)}</rect>')
            c += _swap([(0, 0), (.80, 0), (.81, 1), (.97, 1), (1, 0)],
                       f'<circle cx="{qx + qw - 18}" cy="{y + 18}" r="5" fill="{ok}"/>' + T(qx + 16, y + 45, sl["closed"], fit(sl["closed"], 13, qw - 40, "ticket status"), ok, W6))
        tickets.append(c)
    calm = _swap([(0, 0), (.84, 0), (.86, 1), (.97, 1), (1, 0)], pill(qx + qw - 70, 145, sl["calm"], ok, ctx, 13, 140, "tickets calm", 12))
    # the space the agent answers from: restricted, with its lock and its sources
    bx, by, bw, bh = 1222, 138, 312, 272
    ax, ay = bx + bw / 2, 244
    space = (card(bx, by, bw, bh, "var(--card)", "var(--accent)", 16, 1.6) + _lock(bx + bw - 24, by + 22)
             + T(bx + 18, by + 28, sl["space"], fit(sl["space"], 15, bw - 70, "tickets space"), "var(--white)", W6)
             + T(bx + 18, by + 50, sl["space_sub"], fit(sl["space_sub"], 13, bw - 40, "tickets space sub"), "var(--muted)", W6)
             + card(ax - 50, ay - 32, 100, 64, "var(--dim)", "var(--accent)", 14, 1.4) + spark(ax, ay, .9, "var(--accent)")
             + TC(ax, ay + 54, sl["agent"], fit(sl["agent"], 14, bw - 40, "tickets agent"), "var(--c4)", W6))
    for j, lab in enumerate(sl["docs"][:3]):
        yy = 336 + j * 24
        space += (f'<path d="M{bx + 18} {yy - 13} h8 l5 5 v12 h-13 Z M{bx + 21} {yy - 3} h7 M{bx + 21} {yy + 1} h7" fill="none" stroke="var(--c2)" stroke-width="1.3" stroke-linejoin="round"/>'
                  + T(bx + 40, yy, lab, fit(lab, 13, bw - 60, "tickets doc"), "var(--muted)", W6))
    answering = [(0, 0)]
    for a, b in ((.16, .22), (.32, .38), (.48, .54), (.63, .66)):
        answering += [(a, 0), (a + .02, 1), (b, 1), (b + .02, 0)]
    answering.append((1, 0))
    ring = f'<rect x="{ax - 56}" y="{ay - 38}" width="112" height="76" rx="18" fill="none" stroke="var(--c4)" stroke-width="3">{beat("stroke-opacity", answering)}</rect>'
    # the legs: question to the agent, answer back; the sensitive one leaves the screen by its right edge to the tablet
    legs = ""
    for k, a in enumerate((.10, .26, .42)):
        y = ys[k] + qh / 2
        to = f"M{qx + qw} {y} C{qx + qw + 60} {y} {ax - 110} {ay} {ax - 50} {ay}"
        back = f"M{ax - 50} {ay} C{ax - 110} {ay} {qx + qw + 60} {y} {qx + qw} {y}"
        legs += _leg(to, a, a + .06) + _leg(back, a + .06, a + .12)
    y4 = ys[3] + qh / 2
    legs += _leg(f"M{qx + qw} {y4} C{qx + qw + 60} {y4} {ax - 110} {ay} {ax - 50} {ay}", .58, .63)
    legs += _leg(f"M{ax + 50} {ay} C{sx + sw - 10} {ay} {sx + sw - 8} {sy + sh - 60} {sx + sw - 8} {sy + sh} C{sx + sw - 20} 700 1330 720 1296 800", .64, .72)
    # IT monitoring and control: the self-served share as a bar (no number), usage per space, the record
    mx, my, mw, mh = 876, 424, 658, 104
    tw, fw = 300, [90, 135, 180, 225]
    share = beat("width", [(0, fw[0]), (.23, fw[0]), (.24, fw[1]), (.39, fw[1]), (.40, fw[2]), (.55, fw[2]), (.56, fw[3]), (.97, fw[3]), (1, fw[0])])
    band = (card(mx, my, mw, mh, "var(--dim)", "var(--line)", 14, 1.2) + T(mx + 16, my + 24, sl["monitor"], fit(sl["monitor"], 14, 440, "tickets monitor"), "var(--c4)", W6)
            + T(mx + 16, my + 52, sl["share"], fit(sl["share"], 13, 130, "tickets share"), "var(--white)", W6)
            + f'<rect x="1030" y="{my + 43}" width="{tw}" height="10" rx="5" fill="var(--line)"/>'
            + f'<rect x="1030" y="{my + 43}" width="{fw[3]}" height="10" rx="5" fill="{ok}">{share}</rect>'
            + T(mx + 16, my + 82, sl["usage"], fit(sl["usage"], 13, 130, "tickets usage"), "var(--white)", W6))
    for j, (w0, w1) in enumerate(((.7, .45), (.4, .75), (.55, .3))):
        x0 = 1030 + j * 104
        band += (f'<rect x="{x0}" y="{my + 73}" width="90" height="8" rx="4" fill="var(--line)"/>'
                 f'<rect x="{x0}" y="{my + 73}" width="{90 * w0:.0f}" height="8" rx="4" fill="var(--c2)">{loop("width", f"{90 * w0:.0f};{90 * w1:.0f};{90 * w0:.0f}", 5 + j, j)}</rect>')
    for j, row in enumerate(sl["rows"][:2]):
        yy = my + 52 + j * 30
        band += (f'<g>{loop("opacity", ".5;1;.5", 4, j * 1.5)}<circle cx="1364" cy="{yy - 5}" r="8" fill="{ok}"/>{check(1364, yy - 4, .45, "var(--ink)")}</g>'
                 + T(1380, yy, row, fit(row, 13, 150, "tickets record"), "var(--white)", W6))
    # the operator's tablet: the routed case with its context, «Resolver», his tap, then resolved
    tap = (_swap([(0, 0), (.70, 0), (.71, 1), (.78, 1), (.79, 0), (1, 0)], pill(0, 16, sl["review"], "var(--c4)", ctx, 14, 110, "tickets review", 12))
           + _swap([(0, 0), (.79, 0), (.80, 1), (.97, 1), (1, 0)], f'<rect x="-34" y="4" width="68" height="24" rx="12" fill="{ok}"/>' + check(0, 17, .6, "var(--ink)"))
           + f'<circle cx="0" cy="16" r="6" fill="none" stroke="var(--white)" stroke-width="1.5">{beat("r", [(0, 6), (.77, 6), (.85, 34), (1, 34)])}'
           f'{beat("opacity", [(0, 0), (.77, 0), (.78, 1), (.85, 0), (1, 0)])}</circle>')
    sign = T(sx + sw, sy + sh + 34, sl["sign"], fit(sl["sign"], 20, 330, "tickets sign"), "var(--c4)", 'text-anchor="end" font-weight="600"')
    return (g[0] + land(cone, .2, .6, 0) + land(screen, .1, .5, 16) + land(head, .3, .4, 8) + seq(tickets, .35, .45, 12, 1.4)
            + land(space, .5, .5, 12) + land(band, .7, .5, 10) + calm + ring + legs + land(sign, 1.4, .45, 10)
            + land(_woman(905, 690, 1.1, SKIN_BROWN, "var(--accent)"), .25, .6, 40)
            + land(_man(1250, 716, 1.0, SKIN_LIGHT, "var(--c1)", tap), .4, .6, 40)), D, FREEZE
