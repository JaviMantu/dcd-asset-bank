"""World «Luz de operación» (the lx_* kit, v2): harvested from the webinar «IA: ¿el fin del piloto eterno? Agentes que
escalan» (2026-10, examples/webinar-piloto-eterno/), the world of the webinar-panel scenes (story/webinar_s01_15.py), so
every slide of a deck reads as one world on the pack's dark purple stage. Any deck may draw with it.

Art direction
- thin luminous strokes (1.2-2 px): var(--c2) lilac for structure, var(--accent) magenta for THE thread (the pilot's
  path, lx_trail), var(--c4) yellow sparingly (the spark, a lit exit, the objective cell); soft light with the engine's
  glow(); nodes and orbits;
- dark-glass cards (lx_card): fill color-mix of var(--ink) and var(--brand), a thin lilac edge; text on dark is
  var(--white) or var(--muted), 17 px for a label that means something (LX_TEXT, lx_label's default), never under
  15 px (LX_MIN: lx_label, lx_lines); the letters of E-S-C-A-L-A are the one big type, never under 64 px (lx_letter);
- depth and camera (v2): a far layer of faint nodes and stars under everything (lx_depth) and a slow camera drift on
  the art (lx_drift), both inside the 12 s loop and frozen at 10.8 s under reduced motion;
- labels are painted last (lx_on_top): after every glow, spark, lit glass and lit copy, and never on a glow's centre;
- recurring objects, always drawn by these helpers so slide to slide they read as the same object: the loop Idea → POC
  → Demo with its exit «Operar» (lx_loop, lx_gate), the bridge of five pillars (lx_bridge), the ladder and its rails
  (lx_ladder, lx_rail, lx_rail_legend), the KPI gauge (lx_gauge), the console (lx_console), the panel table (lx_seat,
  lx_table), a static public figure (lx_figure) and the speaker (lx_signer);
- the Amaris mark is never drawn here: the engine's lockup (cover) or footer is the slide's one Amaris mark.

Contract (same as every scene of the deck): colors only var(--…) or color-mix() of them, no hex; figures never animate
(lx_figure is static: land it, never count it up); entrances end by 2.0 s (land/seq/pop/trace from lib.py, lx_trail);
the loop is 12 s (D) and the reduced-motion frame is 10.8 s (FREEZE .9): every lit state should hold at fraction .9.
Timing helpers take fractions of the 12 s loop (0 to 1). Loaded by ext.py after lib.py and before story/*.py and the
deck's own sNN_MM.py; the speaker's portrait is PX_PHOTO_SIGNER of <work>/scenes/s00_img.py (new.py --photo), read when
the scene is drawn (without it, a faceless figure). Helpers are lx_*, constants LX_*; never redefine them in a scene file.

The label rule (the check-ui sensor measures the 10.8 s frame, reduced motion): a label is painted after the glows,
sparks and lit glass around it (a shape painted later over its core fails «covered by»); no glow sits under a label's
centre (a glow is a radial gradient and every stop of it counts as the label's background: the contrast drops); no
filled dot or star sits under a label's anchor (it would become the label's «box»). lx_on_top keeps the order for you.

Helpers (signature → returns)
  lx_lit(a, b=.97, f=.02)                                       → <animate opacity>: dark until a, lit a..b, reset
  lx_label(x, y, s, size=17, room=320, where="luz label", fill="var(--white)", anchor="start", bold=True) → <text>
  lx_on_top(parts, wrap=None)                                   → svg: every art of parts, then every label
  lx_letter(x, y, ch, size=110, lit=None, color=LX_MAGENTA, room=None, where="luz letter") → (svg, z), z >= 64
  lx_depth(box=LX_ZONE["left"], n=28, seed="luz", avoid=(), labels="", drift=(14, -6))    → svg (paint it first)
  lx_drift(inner, cx=1190, cy=455, scale=1.02, dx=0, dy=-6)                                 → svg
  lx_lines(x, y, s, room, size=17, where="luz text", fill="var(--muted)", anchor="start", lh=1.3, bold=False) → (svg, h)
  lx_card(x, y, w, h, r=18, edge=LX_EDGE, sw=1.2, fill=LX_GLASS, extra="")                   → <rect>
  lx_node(x, y, r=7, color=LX_LILAC, halo=True)                                              → svg
  lx_spark(x, y, s=1.0, color=LX_GOLD)                                                       → svg
  lx_orbit(cx, cy, rx, ry=None, color=LX_LILAC, sw=1.2, dash="2 12", period=0, rev=False, op=.55) → svg
  lx_trail(d, color=LX_MAGENTA, width=2, begin=.1, dur=1.4, spark=True, stops=((0, 0), (1, 1)), period=D) → svg
  lx_gate(x, y, label, w=70, h=96, lit=None, color=LX_GOLD, size=18)                         → svg
  lx_loop(cx, cy, r=150, stops=("Idea", "POC", "Demo"), exit="Operar", exit_lit=None, lap=4, agents=0,
          size=18, gate=True)                                                                → svg
  lx_bridge(x0, x1, y, pillars=LX_PILLARS, left="Piloto", right="Operación", light_at=None, h=110, size=16,
            stagger=None)                                                                    → svg
  lx_ladder(x, y, w, h, n=6, light_at=None)                                                  → (svg, ys bottom→top)
  lx_rail(x, y, states, cw=34, ch=18, gap=6, fill_at=None)                                   → svg (width lx_rail_w())
  lx_rail_w(cw=34, gap=6)                                                                    → float
  lx_rail_legend(x, y, labels=("Usted", "Pactado", "La IA"), cw=34, ch=18, size=16)           → (svg, w)
  lx_gauge(cx, cy, r=80, label=None, pairs=((0, 0), (1, 0)), color=LX_GOLD, size=18)          → svg
  lx_console(x, y, w, h, panels, light_at=None, title_size=18, item_size=16)                 → svg
  lx_table(x0, x1, y, h=44)                                                                  → svg
  lx_seat(x, y, s=1.0, color=LX_LILAC, lit=None)                                             → svg
  lx_figure(x, y, value, label, src, w=400, pre=None, size=76, small=(18, 17, 16)) → (svg, h)
  lx_signer(x, y, d, name, role, sizes=(20, 17))                                             → svg
Placeholder scene: w00_luz (an orbit and the trail around a spark), for benches until a slide gets its own scene.
"""
import random
import re

from aula.i18n import every
from aula.svg import ring_path, wrap

LX_LILAC = "var(--c2)"
LX_MAGENTA = "var(--accent)"
LX_GOLD = "var(--c4)"
LX_GLASS = "color-mix(in srgb, var(--ink) 80%, var(--brand))"        # dark glass (opaque: contrast stays measurable)
LX_GLASS_LIT = "color-mix(in srgb, var(--ink) 64%, var(--brand))"    # the same glass, lit
LX_EDGE = "color-mix(in srgb, var(--c2) 55%, transparent)"           # thin lilac edge
LX_DIM = "color-mix(in srgb, var(--c2) 26%, transparent)"            # an unlit stroke
LX_SW = 1.6                                                           # the default luminous stroke, px
LX_MIN = 15                                                           # the smallest label, px (the floor)
LX_TEXT = 17                                                          # a label that means something, px
LX_LETTER_MIN = 64                                                    # the smallest big letter (lx_letter), px
LX_PILLARS = ("datos", "integración", "control", "adopción", "valor")
LX_ZONE = {"left": (820, 60, 740, 780), "top": (80, 390, 1440, 440)}  # each layout's art zone: (x, y, w, h)


def _lx_n(v):
    return f"{v:.1f}"


# ---------------------------------------------------------------- time and text
def lx_lit(a, b=.97, f=.02):
    """An opacity loop for a lit copy: 0 until fraction a, fades in by a + f, stays lit until b, fades out by b + f,
    0 to the end of the 12 s loop. a <= 0: lit from the start. Keep b >= .9 so the reduced-motion frame shows it lit."""
    if a <= 0:
        pts = [(0, 1), (b, 1), (min(b + f, 1), 0), (1, 0)]
    else:
        pts = [(0, 0), (a, 0), (min(a + f, b), 1), (b, 1), (min(b + f, 1), 0), (1, 0)]
    return beat("opacity", pts)


def lx_label(x, y, s, size=LX_TEXT, room=320, where="luz label", fill="var(--white)", anchor="start", bold=True):
    """One line of text at (x, y) (baseline), fitted to room px: 17 px by default (LX_TEXT, a label that means
    something), never under 15 px (LX_MIN): a label that does not fit at 15 is reported by the build (i18n gate) instead
    of shrinking. anchor: start | middle | end. Paint it after the glows around it (lx_on_top)."""
    z = fit(s, max(size, LX_MIN), room, where, floor=LX_MIN, bold=bold)
    ex = W6 if bold else ""
    if anchor == "middle":
        return TC(_lx_n(x), _lx_n(y), s, z, fill, ex)
    if anchor == "end":
        return T(_lx_n(x), _lx_n(y), s, z, fill, f'text-anchor="end" {ex}')
    return T(_lx_n(x), _lx_n(y), s, z, fill, ex)


def lx_lines(x, y, s, room, size=17, where="luz text", fill="var(--muted)", anchor="start", lh=1.3, bold=False):
    """A paragraph wrapped to room px, first baseline at y, never under 15 px (the longest word sets the size, the rest
    wraps). Returns (svg, h): h = lines x size x lh, the height to lay out what comes below."""
    txt = _(str(s))
    z = fit(max(txt.split(), key=len), max(size, LX_MIN), room, where + " word", floor=LX_MIN, bold=bold)
    fac = current_factor()
    chars = max(4, int(room / (bold_width(txt, z, fac, bold) / max(len(txt), 1))))
    while chars > 4 and any(bold_width(line, z, fac, bold) > room for line in wrap(txt, chars)):
        chars -= 1
    n = len(wrap(txt, chars))
    ex = W6 if bold else ""
    return TCW(_lx_n(x), _lx_n(y), s, chars, z, fill, ex, lh, anchor), n * z * lh


# ---------------------------------------------------------------- light
def lx_card(x, y, w, h, r=18, edge=LX_EDGE, sw=1.2, fill=LX_GLASS, extra=""):
    """A dark-glass card at (x, y), w x h: opaque glass fill, thin lilac edge. extra: more attributes for the <rect>."""
    return card(x, y, w, h, fill, edge, r, sw, extra)


def lx_node(x, y, r=7, color=LX_LILAC, halo=True):
    """A luminous node at (x, y): soft glow, a solid core and a thin ring around it."""
    g = glow(_lx_n(x), _lx_n(y), _lx_n(r * 4), color, .5) if halo else ""
    return (g + f'<circle cx="{_lx_n(x)}" cy="{_lx_n(y)}" r="{r}" fill="{color}"/>'
            f'<circle cx="{_lx_n(x)}" cy="{_lx_n(y)}" r="{r + 5}" fill="none" stroke="{color}" stroke-width="1.2" opacity=".6"/>')


def lx_spark(x, y, s=1.0, color=LX_GOLD):
    """The spark (the four-point star of the engine) with its glow, centered at (x, y); draw at (0, 0) to move it."""
    return glow(_lx_n(x), _lx_n(y), _lx_n(26 * s), color, .75) + spark(_lx_n(x), _lx_n(y), round(s * .8, 2), color)


def lx_orbit(cx, cy, rx, ry=None, color=LX_LILAC, sw=1.2, dash="2 12", period=0, rev=False, op=.55):
    """A dashed orbit (ellipse) around (cx, cy). period > 0 spins it around its center (use rx == ry to spin only the
    dashes; an ellipse would turn as a whole). dash "" draws it solid."""
    ry = ry or rx
    da = f' stroke-dasharray="{dash}"' if dash else ""
    inner = (f'<ellipse cx="{_lx_n(cx)}" cy="{_lx_n(cy)}" rx="{_lx_n(rx)}" ry="{_lx_n(ry)}" fill="none" stroke="{color}" '
             f'stroke-width="{sw}"{da} opacity="{op}"/>')
    return f'<g>{spin(cx, cy, period, rev)}{inner}</g>' if period else inner


def lx_trail(d, color=LX_MAGENTA, width=2, begin=.1, dur=1.4, spark=True, stops=((0, 0), (1, 1)), period=D):
    """THE light trail (the pilot's path): the path d draws itself once (begin..begin+dur, ending by 2.0 s) with a soft
    halo, then a spark travels along it for ever: stops = [(fraction of the period, fraction of the path)], period in
    seconds (12 by default; 4 or 6 also divide the loop). The spark appears when the stroke is drawn."""
    g = trace(d, color, width * 5, begin, dur, 'opacity=".13"') + trace(d, color, width, begin, dur)
    if spark:
        t0 = begin + dur
        g += (f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t0:.2f}s" fill="freeze"/>'
              f'{move(d, list(stops), period, begin=t0)}{lx_spark(0, 0, .7)}</g>')
    return g


# ---------------------------------------------------------------- the pilot's loop and its exit
def lx_gate(x, y, label, w=70, h=96, lit=None, color=LX_GOLD, size=18):
    """A doorway (arch) whose base center is (x, y): it rises h px, with its label centered 30 px under the base.
    lit None: unlit (lilac outline, muted label) · a fraction: it lights at that moment of the loop and stays lit
    (lx_lit) · True: always lit. The loop's exit «Operar» and any narrow door (luz-figures) use it."""
    a = w / 2
    d = f"M{_lx_n(x - a)} {_lx_n(y)} V{_lx_n(y - h + a)} A{_lx_n(a)} {_lx_n(a)} 0 0 1 {_lx_n(x + a)} {_lx_n(y - h + a)} V{_lx_n(y)}"
    base = (f'<path d="{d}" fill="{LX_GLASS}" stroke="{LX_EDGE}" stroke-width="{LX_SW}" stroke-linejoin="round"/>'
            f'<path d="M{_lx_n(x - a - 16)} {_lx_n(y)} H{_lx_n(x + a + 16)}" stroke="{LX_EDGE}" stroke-width="1.2"/>'
            + lx_label(x, y + 30, label, size, w + 120, "luz gate", "var(--muted)", "middle"))
    if lit is None:
        return base
    on = "" if lit is True else lx_lit(lit)
    return base + (f'<g>{on}{glow(_lx_n(x), _lx_n(y - h / 2), _lx_n(h * .9), color, .55)}'
                   f'<path d="{d}" fill="{LX_GLASS_LIT}" stroke="{color}" stroke-width="2" stroke-linejoin="round"/>'
                   + glow(_lx_n(x), _lx_n(y - h * .42), _lx_n(a * .9), color, .45)
                   + lx_label(x, y + 30, label, size, w + 120, "luz gate", color, "middle") + '</g>')


def _lx_flash(frac, period):
    """Opacity of a node's flash when the carrier passes it at frac of each lap."""
    if frac <= .001:
        return (f'<animate attributeName="opacity" values="1;0;0;1" keyTimes="0;.1;.94;1" dur="{period}s" '
                f'repeatCount="indefinite"/>')
    a, b = max(frac - .04, .001), min(frac + .1, .999)
    return (f'<animate attributeName="opacity" values="0;0;1;0;0" keyTimes="0;{a:.3f};{frac:.3f};{b:.3f};1" dur="{period}s" '
            f'repeatCount="indefinite"/>')


def _lx_agent(color=LX_MAGENTA):
    """An agent token around (0, 0): a small glass core with its own orbiting dot (it acts on its own)."""
    return (glow(0, 0, 26, color, .5) + f'<circle r="11" fill="{LX_GLASS}" stroke="{color}" stroke-width="1.6"/>'
            f'<circle r="3.5" fill="{color}"/><g>{spin(0, 0, 2)}<circle cx="0" cy="-17" r="2.6" fill="{LX_GOLD}"/></g>')


def lx_loop(cx, cy, r=150, stops=("Idea", "POC", "Demo"), exit="Operar", exit_lit=None, lap=4, agents=0, size=18, gate=True):
    """The pilot's loop centered at (cx, cy): a luminous ring with three stops (top, lower right, lower left: Idea →
    POC → Demo, clockwise), an outer dashed orbit that turns, and a carrier that laps it every `lap` seconds (4 or 6:
    it must divide 12) flashing each stop as it passes. agents = 0: the carrier is the spark; agents = n: n agent
    tokens lap it instead (luz-wave). gate: the exit lx_gate(exit) outside the ring, base at (cx + r + 120, cy + 10),
    with a dashed stub from the ring that never reaches it; exit_lit as lx_gate's lit (None, a fraction, True).
    Footprint: x cx - r - 60 … cx + r + 190, y cy - r - 50 … cy + r + 50."""
    ring = ring_path(cx, cy, r)
    g = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LX_LILAC}" stroke-width="10" opacity=".08"/>',
         f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{LX_LILAC}" stroke-width="1.8" opacity=".9"/>',
         lx_orbit(cx, cy, r + 28, color=LX_LILAC, dash="2 12", period=24, op=.45)]
    for ang in (-30, 90, 210):  # chevrons between the stops, pointing clockwise
        a = math.radians(ang)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        g.append(f'<path d="M-5 -6 L4 0 L-5 6" fill="none" stroke="{LX_LILAC}" stroke-width="1.6" stroke-linecap="round" '
                 f'stroke-linejoin="round" transform="translate({_lx_n(x)} {_lx_n(y)}) rotate({ang + 90})"/>')
    for k, (lab, ang) in enumerate(zip(stops, (-90, 30, 150))):
        a = math.radians(ang)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        g.append(lx_node(x, y, 8, LX_LILAC))
        g.append(f'<g opacity="0">{_lx_flash(k / 3, lap)}{glow(_lx_n(x), _lx_n(y), 40, LX_GOLD, .8)}'
                 f'<circle cx="{_lx_n(x)}" cy="{_lx_n(y)}" r="9" fill="{LX_GOLD}"/></g>')
        if k == 0:
            g.append(lx_label(x, y - 26, lab, size, 200, "luz loop stop", "var(--white)", "middle"))
        elif k == 1:
            g.append(lx_label(x + 18, y + 34, lab, size, 160, "luz loop stop", "var(--white)"))
        else:
            g.append(lx_label(x - 18, y + 34, lab, size, 160, "luz loop stop", "var(--white)", "end"))
    if agents:
        for k in range(agents):
            g.append(f'<g>{move(ring, [(0, 0), (1, 1)], lap, begin=-k * lap / agents)}{_lx_agent()}</g>')
    else:
        g.append(f'<g>{move(ring, [(0, 0), (1, 1)], lap)}{lx_spark(0, 0, .75)}</g>')
    if gate and exit:
        gx = cx + r + 120
        g.append(f'<path d="M{cx + r + 10} {cy} H{gx - 58}" stroke="{LX_EDGE}" stroke-width="1.4" stroke-dasharray="3 7"/>')
        g.append(lx_gate(gx, cy + 10, exit, lit=exit_lit, size=size))
    return "".join(g)


# ---------------------------------------------------------------- the bridge from pilot to operation
def _lx_wide(s, size, bold=True):
    """The widest rendering of label s at size, over every language of the module (the same measure as fit())."""
    fac = current_factor()
    return max(bold_width(v, size, fac, bold) for v in every(_(str(s)))) if s else 0


def lx_bridge(x0, x1, y, pillars=LX_PILLARS, left="Piloto", right="Operación", light_at=None, h=110, size=16,
              stagger=None):
    """The bridge between «Piloto» (x0) and «Operación» (x1) at deck height y: a luminous deck, two faint cables and the
    pillars (datos · integración · control · adopción · valor) hanging h px below it, each labeled under its foot.
    light_at: one fraction per pillar (it lights then and stays lit), or None (all unlit). End labels sit 26 px above
    the deck. stagger: None (auto) staggers the pillar labels when the room is narrow, i.e. when any of them does not
    fit one step (step - 8 px, step = (x1 - x0) / (n + 1)) at `size` in some language: the odd pillars' labels drop
    26 px on a dim leader from the foot, so each label gets two steps (2·step - 12 px) and none overflows or shrinks;
    True / False force it. Footprint: x x0 - 60 … x1 + 60, y y - 50 … y + h + 34 (+ 26 when staggered)."""
    n = len(pillars)
    step = (x1 - x0) / (n + 1)
    mid = (x0 + x1) / 2
    if stagger is None:
        stagger = any(_lx_wide(lab, size) > step - 8 for lab in pillars)
    room = 2 * step - 12 if stagger else step - 8
    g = [f'<path d="M{x0} {y} H{x1}" stroke="{LX_LILAC}" stroke-width="8" opacity=".1"/>',
         f'<path d="M{x0} {y} H{x1}" stroke="{LX_LILAC}" stroke-width="2"/>',
         f'<path d="M{x0} {y} Q{_lx_n(mid)} {y + h * .9:.1f} {x1} {y}" fill="none" stroke="{LX_DIM}" stroke-width="1.2"/>',
         f'<path d="M{x0} {y - 20} Q{_lx_n(mid)} {y + h * .5:.1f} {x1} {y - 20}" fill="none" stroke="{LX_DIM}" stroke-width="1.2"/>',
         lx_node(x0, y, 8), lx_node(x1, y, 8),
         lx_label(x0, y - 26, left, size + 2, 220, "luz bridge end", "var(--white)", "middle"),
         lx_label(x1, y - 26, right, size + 2, 220, "luz bridge end", "var(--white)", "middle")]
    for k, lab in enumerate(pillars):
        px = x0 + step * (k + 1)
        low = stagger and k % 2 == 1
        ly = y + h + 28 + (26 if low else 0)
        lead = (f'<path d="M{_lx_n(px)} {y + h + 8} V{ly - 18}" stroke="{LX_DIM}" stroke-width="1.2"/>'
                if low and lab else "")
        g.append(f'<path d="M{_lx_n(px)} {y} V{y + h}" stroke="{LX_EDGE}" stroke-width="{LX_SW}"/>'
                 f'<circle cx="{_lx_n(px)}" cy="{y + h}" r="4" fill="{LX_LILAC}"/>' + lead
                 + lx_label(px, ly, lab, size, room, "luz bridge pillar", "var(--muted)", "middle"))
        if light_at is not None:  # the foot's glow stays inside 16 px: the label's center sits 22 px below the foot
            g.append(f'<g>{lx_lit(light_at[k])}<path d="M{_lx_n(px)} {y} V{y + h}" stroke="{LX_GOLD}" stroke-width="2"/>'
                     f'{glow(_lx_n(px), y + h, 16, LX_GOLD, .7)}<circle cx="{_lx_n(px)}" cy="{y + h}" r="5" fill="{LX_GOLD}"/>'
                     + lx_label(px, ly, lab, size, room, "luz bridge pillar", "var(--white)", "middle") + '</g>')
    return "".join(g)


# ---------------------------------------------------------------- the ladder and its rails (luz-ladder)
def lx_ladder(x, y, w, h, n=6, light_at=None):
    """A luminous ladder in the box (x, y, w, h): two side rails and n rungs, evenly spaced. light_at: one fraction per
    rung, bottom to top (the rung lights then and stays lit), or None. Returns (svg, ys): the rungs' y, bottom → top."""
    ys = [y + h - (k + .5) * h / n for k in range(n)]
    g = [f'<path d="M{x} {y} V{y + h} M{x + w} {y} V{y + h}" stroke="{LX_LILAC}" stroke-width="8" opacity=".08"/>',
         f'<path d="M{x} {y} V{y + h} M{x + w} {y} V{y + h}" stroke="{LX_LILAC}" stroke-width="{LX_SW}"/>']
    for k, ry in enumerate(ys):
        g.append(f'<path d="M{x} {_lx_n(ry)} H{x + w}" stroke="{LX_EDGE}" stroke-width="{LX_SW}"/>')
        if light_at is not None:
            g.append(f'<g>{lx_lit(light_at[k])}<path d="M{x} {_lx_n(ry)} H{x + w}" stroke="{LX_MAGENTA}" stroke-width="2"/>'
                     f'{glow(x, _lx_n(ry), 16, LX_MAGENTA, .7)}{glow(x + w, _lx_n(ry), 16, LX_MAGENTA, .7)}</g>')
    return "".join(g), ys


def lx_rail_w(cw=34, gap=6):
    """The width of a four-cell rail."""
    return 4 * cw + 3 * gap


def lx_rail(x, y, states, cw=34, ch=18, gap=6, fill_at=None):
    """The four-cell rail objetivo · pasos · ejecución · revisión, top-left at (x, y). states: four values, 0 = empty
    (la persona), 1 = half (pactado: lilac, half width), 2 = full (la IA: magenta). The objective cell (the first) is
    always drawn empty with a thin yellow edge: it is always yours. fill_at: the fraction when the fills appear (they
    stay until the loop resets), or None (static)."""
    g, fills = [], []
    for k, st in enumerate(states[:4]):
        cx = x + k * (cw + gap)
        edge = "color-mix(in srgb, var(--c4) 70%, transparent)" if k == 0 else LX_EDGE
        g.append(f'<rect x="{_lx_n(cx)}" y="{_lx_n(y)}" width="{cw}" height="{ch}" rx="5" fill="{LX_GLASS}" stroke="{edge}" stroke-width="1.2"/>')
        if k and st == 1:
            fills.append(f'<rect x="{_lx_n(cx + 3)}" y="{_lx_n(y + 3)}" width="{(cw - 6) / 2:.1f}" height="{ch - 6}" rx="3" fill="{LX_LILAC}"/>')
        elif k and st == 2:
            fills.append(f'<rect x="{_lx_n(cx + 3)}" y="{_lx_n(y + 3)}" width="{cw - 6}" height="{ch - 6}" rx="3" fill="{LX_MAGENTA}"/>')
    if fills:
        g.append(f'<g>{lx_lit(fill_at) if fill_at is not None else ""}{"".join(fills)}</g>')
    return "".join(g)


def lx_rail_legend(x, y, labels=("Usted", "Pactado", "La IA"), cw=34, ch=18, size=16):
    """The legend of the rail at (x, y) (top-left of the first sample cell): an empty, a half and a full cell, each with
    its label to its right. Returns (svg, w): the width it takes."""
    g, cur = [], x
    for st, lab in zip((0, 1, 2), labels):
        g.append(f'<rect x="{_lx_n(cur)}" y="{y}" width="{cw}" height="{ch}" rx="5" fill="{LX_GLASS}" stroke="{LX_EDGE}" stroke-width="1.2"/>')
        if st == 1:
            g.append(f'<rect x="{_lx_n(cur + 3)}" y="{y + 3}" width="{(cw - 6) / 2:.1f}" height="{ch - 6}" rx="3" fill="{LX_LILAC}"/>')
        elif st == 2:
            g.append(f'<rect x="{_lx_n(cur + 3)}" y="{y + 3}" width="{cw - 6}" height="{ch - 6}" rx="3" fill="{LX_MAGENTA}"/>')
        z = fit(lab, max(size, LX_MIN), 160, "luz rail legend", floor=LX_MIN, bold=False)
        g.append(T(_lx_n(cur + cw + 10), _lx_n(y + ch / 2 + z * .36), lab, z, "var(--muted)"))
        cur += cw + 10 + bold_width(_(str(lab)), z, current_factor(), False) + 28
    return "".join(g), cur - 28 - x


# ---------------------------------------------------------------- the KPI gauge (luz-bridge)
def lx_gauge(cx, cy, r=80, label=None, pairs=((0, 0), (1, 0)), color=LX_GOLD, size=18):
    """A KPI gauge, a half dial centered at (cx, cy) opening upwards, with ticks and no numbers. The needle points left
    at 0 and right at 1; pairs = [(fraction of the loop, value 0..1)] moves it (the markup's pose is its value at the
    10.8 s frame). label: centered 36 px under the hub."""
    pts = sorted(pairs)
    at = next((v0 + (v1 - v0) * (.9 - t0) / (t1 - t0) for (t0, v0), (t1, v1) in zip(pts, pts[1:]) if t0 <= .9 <= t1 and t1 > t0),
              pts[-1][1])
    arc = f"M{cx - r} {cy} A{r} {r} 0 0 1 {cx + r} {cy}"
    g = [f'<path d="{arc}" fill="none" stroke="{LX_LILAC}" stroke-width="10" opacity=".1"/>',
         f'<path d="{arc}" fill="none" stroke="{LX_LILAC}" stroke-width="{LX_SW}"/>']
    for k in range(7):
        a = math.radians(180 + k * 30)
        x0, y0 = cx + (r - 12) * math.cos(a), cy + (r - 12) * math.sin(a)
        x1, y1 = cx + r * math.cos(a), cy + r * math.sin(a)
        g.append(f'<path d="M{_lx_n(x0)} {_lx_n(y0)} L{_lx_n(x1)} {_lx_n(y1)}" stroke="{LX_EDGE}" stroke-width="1.4"/>')
    kt = ";".join(f"{t:.3f}" for t, _v in pts)
    vals = ";".join(f"{v * 180:.1f} {cx} {cy}" for _t, v in pts)
    anim_ = (f'<animateTransform attributeName="transform" type="rotate" values="{vals}" keyTimes="{kt}" dur="{D}s" '
             f'repeatCount="indefinite" calcMode="linear"/>') if len(pts) > 1 else ""
    g.append(f'<g transform="rotate({at * 180:.1f} {cx} {cy})">{anim_}'
             f'<path d="M{cx} {cy} L{cx - r + 18} {cy}" stroke="{color}" stroke-width="2.4" stroke-linecap="round"/>'
             f'{glow(cx - r + 18, cy, 14, color, .8)}</g>')
    g.append(lx_node(cx, cy, 6, color))
    if label:
        g.append(lx_label(cx, cy + 36, label, size, 2 * r + 80, "luz gauge", "var(--white)", "middle"))
    return "".join(g)


# ---------------------------------------------------------------- the console (luz-console)
def lx_console(x, y, w, h, panels, light_at=None, title_size=18, item_size=16):
    """A console in the box (x, y, w, h): a dark-glass frame with a status strip and len(panels) panels side by side.
    panels = [(title, [item, …])]; each panel has a status light and its items, each with an indicator. light_at: one
    fraction per panel (its light, edge and indicators turn on then and stay on), or None (all off)."""
    n, pad, gap = len(panels), 18, 14
    pw = (w - 2 * pad - (n - 1) * gap) / n
    g = [lx_card(x, y, w, h, 22), f'<path d="M{x + 22} {y + 34} H{x + w - 22}" stroke="{LX_EDGE}" stroke-width="1"/>']
    g += [f'<circle cx="{x + 30 + k * 16}" cy="{y + 18}" r="3.5" fill="{LX_DIM}"/>' for k in range(3)]
    for k, (title, items) in enumerate(panels):
        px, py, ph = x + pad + k * (pw + gap), y + 50, h - 68
        g.append(lx_card(px, py, pw, ph, 14, LX_EDGE, 1, "color-mix(in srgb, var(--ink) 70%, var(--brand))"))
        g.append(lx_node(px + 20, py + 26, 4, LX_DIM, False))
        g.append(lx_label(px + 34, py + 32, title, title_size, pw - 46, "luz console title", "var(--white)"))
        lit = []
        yy = py + 72
        for it in items:
            ln, lh_ = lx_lines(px + 34, yy, it, pw - 50, item_size, "luz console item", "var(--muted)")
            g.append(f'<circle cx="{_lx_n(px + 20)}" cy="{_lx_n(yy - 5)}" r="4" fill="none" stroke="{LX_EDGE}" stroke-width="1.2"/>' + ln)
            lit.append(f'<circle cx="{_lx_n(px + 20)}" cy="{_lx_n(yy - 5)}" r="4" fill="{LX_GOLD}"/>')
            yy += lh_ + 14
        if light_at is not None:
            g.append(f'<g>{lx_lit(light_at[k])}'
                     f'<rect x="{_lx_n(px)}" y="{py}" width="{_lx_n(pw)}" height="{ph}" rx="14" fill="none" stroke="{LX_MAGENTA}" stroke-width="1.8"/>'
                     f'{glow(_lx_n(px + 20), py + 26, 22, LX_GOLD, .8)}<circle cx="{_lx_n(px + 20)}" cy="{py + 26}" r="5" fill="{LX_GOLD}"/>'
                     + "".join(lit) + '</g>')
    return "".join(g)


# ---------------------------------------------------------------- the panel table (luz-panel)
def lx_table(x0, x1, y, h=44):
    """The panel's table: a dark-glass slab from x0 to x1 whose top edge (a luminous line) is at y."""
    return (glow(_lx_n((x0 + x1) / 2), y, _lx_n((x1 - x0) * .45), "var(--brand)", .45)
            + lx_card(x0, y, x1 - x0, h, 10, LX_EDGE, 1.2)
            + f'<path d="M{x0 + 6} {y} H{x1 - 6}" stroke="{LX_LILAC}" stroke-width="2"/>')


def lx_seat(x, y, s=1.0, color=LX_LILAC, lit=None):
    """A faceless panelist seated behind the table: shoulders resting on the table line y, centered on x, scaled by s
    (about 80 x 108 px at s = 1). lit: None · a fraction (lights then and stays lit) · [(t, opacity)] pairs for a
    spotlight that comes and goes (beat)."""
    def body(stroke, fill, sw):
        return (f'<circle cx="{_lx_n(x)}" cy="{_lx_n(y - 88 * s)}" r="{_lx_n(18 * s)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
                f'<path d="M{_lx_n(x - 40 * s)} {y} Q{_lx_n(x - 40 * s)} {_lx_n(y - 58 * s)} {_lx_n(x)} {_lx_n(y - 60 * s)} '
                f'Q{_lx_n(x + 40 * s)} {_lx_n(y - 58 * s)} {_lx_n(x + 40 * s)} {y} Z" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    g = body(LX_EDGE, LX_GLASS, 1.4)
    if lit is None:
        return g
    on = beat("opacity", lit) if isinstance(lit, (list, tuple)) else lx_lit(lit)
    return g + (f'<g>{on}{glow(_lx_n(x), _lx_n(y - 70 * s), _lx_n(90 * s), color, .45)}'
                + body(color, LX_GLASS_LIT, 1.8) + '</g>')


# ---------------------------------------------------------------- a public figure, static (luz-figures, luz-wave)
def lx_figure(x, y, value, label, src, w=400, pre=None, size=76, small=(18, 17, 16)):
    """A public figure, static (figures never animate: land it), top-left at (x, y): an optional qualifier above
    («Al menos», «Más del»), the value large in white, its label wrapped in muted text, and its source line in lilac
    («Gartner · 2025»). small: the sizes of qualifier, label and source (the portrait twins pass larger ones).
    Returns (svg, h)."""
    g, yy = [], y
    zp, zl, zs = small
    if pre:
        g.append(lx_label(x, yy + zp, pre, zp, w, "luz figure pre", "var(--muted)"))
        yy += zp + 8
    z = fit(value, size, w, "luz figure value", floor=40)
    g.append(T(_lx_n(x), _lx_n(yy + z * .82), value, z, "var(--white)", W6))
    yy += z * .82 + 12
    g.append(f'<path d="M{_lx_n(x)} {_lx_n(yy)} h56" stroke="{LX_MAGENTA}" stroke-width="2" stroke-linecap="round"/>')
    ln, h_ = lx_lines(x, yy + zl + 13, label, w, zl, "luz figure label", "var(--muted)")
    g.append(ln)
    yy += zl + 13 + h_
    g.append(lx_label(x, yy + zs - 12, src, zs, w, "luz figure source", LX_LILAC))
    return "".join(g), yy + 10 - y


# ---------------------------------------------------------------- the speaker (luz-end)
def lx_signer(x, y, d, name, role, sizes=(20, 17)):
    """The speaker's portrait (PX_PHOTO_SIGNER, from s00_img.py) in a luminous ring, top-left of its square at (x, y),
    d px wide; a dashed orbit turns around it; name (white) and role (muted) centered under it, at sizes (name, role;
    the portrait twins pass larger ones). Without a photo, a faceless figure in the same ring."""
    zn, zr = sizes
    r = d / 2
    cx, cy = x + r, y + r
    cid = "lx-signer-clip"
    photo = globals().get("PX_PHOTO_SIGNER", "")   # <work>/scenes/s00_img.py, when new.py got --photo
    face = (f'<image href="{photo}" x="{x}" y="{y}" width="{d}" height="{d}" clip-path="url(#{cid})" '
            f'preserveAspectRatio="xMidYMid slice"/>' if photo else
            f'<g clip-path="url(#{cid})"><rect x="{x}" y="{y}" width="{d}" height="{d}" fill="{LX_GLASS}"/>'
            f'<circle cx="{_lx_n(cx)}" cy="{_lx_n(y + r * .78)}" r="{_lx_n(r * .34)}" fill="{LX_GLASS_LIT}" stroke="{LX_EDGE}"/>'
            f'<path d="M{_lx_n(x + r * .28)} {y + d} Q{_lx_n(x + r * .28)} {_lx_n(y + r * 1.22)} {_lx_n(cx)} {_lx_n(y + r * 1.22)} '
            f'Q{_lx_n(x + r * 1.72)} {_lx_n(y + r * 1.22)} {_lx_n(x + r * 1.72)} {y + d} Z" fill="{LX_GLASS_LIT}" stroke="{LX_EDGE}"/></g>')
    return (f'<defs><clipPath id="{cid}"><circle cx="{_lx_n(cx)}" cy="{_lx_n(cy)}" r="{_lx_n(r)}"/></clipPath></defs>'
            + glow(_lx_n(cx), _lx_n(cy), _lx_n(r * 1.7), "var(--brand)", .7) + face
            + f'<circle cx="{_lx_n(cx)}" cy="{_lx_n(cy)}" r="{_lx_n(r + 5)}" fill="none" stroke="{LX_LILAC}" stroke-width="1.8"/>'
            + lx_orbit(cx, cy, r + 20, color=LX_MAGENTA, dash="3 14", period=24, op=.8)
            + lx_label(cx, y + d + 26 + zn, name, zn, d + 240, "luz signer name", "var(--white)", "middle")
            + lx_label(cx, y + d + 37 + zn + zr, role, zr, d + 240, "luz signer role", "var(--muted)", "middle", bold=False))


# ---------------------------------------------------------------- v2: labels last, the big letter, depth, camera
def lx_on_top(parts, wrap=None):
    """Paint labels last. parts: [(art, label), …], or a plain string for art with no label. Returns every art in
    order, then every label in order, so no glass, glow, spark or lit copy of a later part lands over an earlier part's
    label. wrap: a function applied to each layer's list, e.g. lambda xs: seq(xs, .1, .5): both layers then land in
    step, part k's label with part k's art (default: "".join). The lit copy of a label (lx_lit) belongs in the label
    half. The rule it serves — labels after glows and sparks, no glow under a label's centre — is measured by check-ui on
    the 10.8 s frame: a moving spark may cross a label, but its pose at 10.8 s must not sit on one."""
    arts, labels = [], []
    for p in parts:
        a, b = (p, "") if isinstance(p, str) else p
        arts.append(a)
        labels.append(b)
    wrap = wrap or "".join
    return wrap(arts) + wrap(labels)


def lx_letter(x, y, ch, size=110, lit=None, color=LX_MAGENTA, room=None, where="luz letter"):
    """A big luminous letter (the E-S-C-A-L-A of luz-escala), centered on x, baseline y, never under 64 px (LX_LETTER_MIN):
    room (default size x 1.2) is the width it may take; one that does not fit at 64 is reported by the build, not
    shrunk further. Unlit: its outline only, a thin lilac stroke on no fill (a sensor reads no fill as decoration).
    lit: None (unlit) · a fraction (it lights then and stays lit, lx_lit) · True (always lit): a neon halo drawn with the
    letter's own strokes in color (wide and faint, then narrow) and the white letter on top. The halo is text, never a
    glow circle, so nothing is painted under the letter's centre and its contrast is read against the stage: do not add
    a glow() there. Returns (svg, z): z is the size used, to lay out its word under it."""
    z = fit(ch, max(size, LX_LETTER_MIN), room or size * 1.2, where, floor=LX_LETTER_MIN)
    X, Y = _lx_n(x), _lx_n(y)
    svg = TC(X, Y, ch, z, "none", f'{W6} stroke="{LX_EDGE}" stroke-width="1.4"')
    if lit is None:
        return svg, z
    on = "" if lit is True else lx_lit(lit)
    return svg + (f'<g>{on}'
                  + TC(X, Y, ch, z, "none", f'{W6} stroke="{color}" stroke-width="{z * .12:.1f}" stroke-linejoin="round" opacity=".16"')
                  + TC(X, Y, ch, z, "none", f'{W6} stroke="{color}" stroke-width="{z * .045:.1f}" stroke-linejoin="round" opacity=".55"')
                  + TC(X, Y, ch, z, "var(--white)", W6) + '</g>'), z


def _lx_text_boxes(markup):
    """Approximate stage boxes (x, y, w, h) of the <text> labels in markup (T, TC, TCW output), for lx_depth to avoid.
    Only texts positioned in stage coordinates are seen: one inside a translated group goes in lx_depth's avoid."""
    out = []
    for m in re.finditer(r'<text x="([-\d.]+)" y="([-\d.]+)" font-size="([\d.]+)"([^>]*)>(.*?)</text>', markup, re.S):
        x, y, z, attrs, body = float(m[1]), float(m[2]), float(m[3]), m[4], m[5]
        lines = re.findall(r"<tspan[^>]*>(.*?)</tspan>", body, re.S) or [body]
        w = max(len(re.sub(r"<[^>]+>|&\w+;", "_", ln)) for ln in lines) * .62 * z
        x0 = x - w / 2 if 'text-anchor="middle"' in attrs else x - w if 'text-anchor="end"' in attrs else x
        out.append((x0, y - z, w, z * (1.3 * len(lines)) + 4))
    return out


def lx_depth(box=LX_ZONE["left"], n=28, seed="luz", avoid=(), labels="", drift=(14, -6)):
    """A far layer of depth under the art: n faint stars and far nodes (pack colors: mostly lilac, some white, a little
    gold; opacity .12-.45) scattered in box (x, y, w, h; LX_ZONE["left"] or ["top"], the layouts' art zones), in two
    planes that drift slowly and seamlessly over the 12 s loop, the far one half as much (parallax); a few twinkle.
    Paint it FIRST, under every card, glow and label. It never lies under a label: no star is placed within reach of a
    rect in avoid [(x, y, w, h), …] or of a <text> found in labels (pass the scene's markup; see _lx_text_boxes), the
    drift and a margin included. Deterministic: the same seed draws the same sky on every build."""
    rnd = random.Random(seed)
    bx, by, bw, bh = box
    dx, dy = drift
    mx, my = abs(dx) + 10, abs(dy) + 10
    keep = [(x - mx, y - my, w + 2 * mx, h + 2 * my) for x, y, w, h in list(avoid) + _lx_text_boxes(labels)]
    near, far = [], []
    tries = 0
    while len(near) + len(far) < n and tries < n * 40:
        tries += 1
        x, y = bx + rnd.random() * bw, by + rnd.random() * bh
        if any(ax <= x <= ax + aw and ay <= y <= ay + ah for ax, ay, aw, ah in keep):
            continue
        k = len(near) + len(far)
        color = LX_GOLD if k % 13 == 5 else "var(--white)" if k % 4 == 1 else LX_LILAC
        is_far = rnd.random() < .6
        r = (.7 + rnd.random() * .6) if is_far else (1.1 + rnd.random() * .9)
        op = (.12 + rnd.random() * .16) if is_far else (.22 + rnd.random() * .23)
        tw = (loop("opacity", f"{op:.2f};{op * .3:.2f};{op:.2f}", (3, 4, 6)[k % 3], rnd.random() * 3)
              if k % 3 == 0 else "")
        dot = f'<circle cx="{_lx_n(x)}" cy="{_lx_n(y)}" r="{r:.1f}" fill="{color}" opacity="{op:.2f}">{tw}</circle>'
        if k % 7 == 3:  # a far node: the dot with its thin ring
            dot += (f'<circle cx="{_lx_n(x)}" cy="{_lx_n(y)}" r="{r + 4:.1f}" fill="none" stroke="{LX_LILAC}" '
                    f'stroke-width=".8" opacity="{op * .8:.2f}"/>')
        (far if is_far else near).append(dot)
    return (f'<g aria-hidden="true"><g>{bob(dx / 2, dy / 2, D)}{"".join(far)}</g>'
            f'<g>{bob(dx, dy, D)}{"".join(near)}</g></g>')


def lx_drift(inner, cx=1190, cy=455, scale=1.02, dx=0, dy=-6):
    """A gentle camera on inner: over the 12 s loop it eases 1 → scale → 1 around (cx, cy) (the left layout's art centre;
    the top band's is (800, 612)) and drifts (0, 0) → (dx, dy) → (0, 0), seamless at the reset. Under reduced motion
    the engine seeks every scene to 10.8 s and pauses it (setCurrentTime + pauseAnimations): the camera holds its pose
    there (scale ≈ 1.002), which is the frame check-ui and the contact sheet read. At the peak, 2 % of a 370 px
    half-zone is ~7 px: keep that margin at the stage's edges. Wrap the art with its labels (they move together); leave
    lx_depth outside (it drifts on its own)."""
    ks = "0.45 0 0.55 1;0.45 0 0.55 1"
    zoom = (f'<animateTransform attributeName="transform" type="scale" values="1;{scale};1" keyTimes="0;.5;1" dur="{D}s" '
            f'repeatCount="indefinite" calcMode="spline" keySplines="{ks}"/>')
    return (f'<g>{bob(dx, dy, D)}<g transform="translate({_lx_n(cx)} {_lx_n(cy)})"><g>{zoom}'
            f'<g transform="translate({_lx_n(-cx)} {_lx_n(-cy)})">{inner}</g></g></g></g>')


# ---------------------------------------------------------------- placeholder until a slide gets its own scene
@register("scene", "w00_luz")
def sc_w00_luz(sl, ctx):
    """An orbit and the magenta trail looping around a spark, in the art zone of the slide's layout (left: x 820-1560;
    top: the band y 390-830). A placeholder while the benches build the real scenes."""
    if sl.get("layout") == "top":
        cx, cy, rx, ry = 800, 612, 470, 150
    else:
        cx, cy, rx, ry = 1190, 455, 300, 250
    d = ellipse_path(cx, cy, rx, ry)
    g = [glow(cx, cy, int(max(rx, ry) * 1.1), "var(--brand)", .55),
         land(lx_orbit(cx, cy, rx + 40, ry + 40, dash="2 14", op=.4), .1, .5, 0),
         lx_trail(d, begin=.2, dur=1.4, stops=((0, 0), (1, 1)), period=6),
         pop(lx_spark(0, 0, 1.3), cx, cy, .3, .5)]
    return "".join(g), D, FREEZE
