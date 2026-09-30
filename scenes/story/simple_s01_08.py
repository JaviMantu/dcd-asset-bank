"""Simple-first deck (0.5.0, the default type «simple»): eight dense, illustrated scenes for a first conversation with a
prospect of any vertical, after the method of the class «prospecciones de alto impacto» (clase VR2).

Every scene is portrait-aware: it draws inside ART_ZONE(layout) on CANVAS() and returns portrait_mark(svg), so the
mobile build (DCD_ORIENT=portrait) stacks the same story vertically, icons in two columns and labels 1.3× larger. The
icons come from icons.py: the slide's `vertical` (story.py copies meta.vertical onto each slide; «generico» when
missing or unknown), in catalog order unless args.icons names them («vertical/key» or a key). Labels are painted after
every glow and sit on opaque cards; figures never move; the 10.8 s frame is the resolved story.

- sm01_hero · simple-hero: their three worries (budget, the quarter's goal, the KPI promised) above their operation;
  a shipment runs the stations to their promise and each worry resolves.
- sm02_outside · simple-outside: three public sources read into our dossier; below a dotted line, their areas in faint
  lines; one question drops to each area.
- sm03_gap · simple-gap: fact (with source), hypothesis (with «?») and what we do not assume (locked); only the fact
  and the hypothesis reach today's conversation, as a question.
- sm04_hypotheses · simple-hypotheses: three ideas with a possible return and one enabler under them, each with «?».
- sm05_criterion · simple-criterion: three ideas cross «Retorno claro» or «Habilitador clave», or go aside.
- sm06_proof · simple-proof: a nameable reference or a prototype in a week, into a success case with its KPI.
- sm07_path · simple-path: three short steps down a route, with both teams and the person who reviews.
- sm08_next · simple-next: the invitation with its date, their operation lit again, the worries resolved, the signer.
"""
from aula.svg import wrap as _sm_wrap

_SM_END = .97
_SM_WORRIES = ("Dentro de su presupuesto", "La meta del trimestre", "El KPI que prometió")


# ---------------------------------------------------------------- shared pieces
def _sm_zone(sl):
    """(x, y, w, h, portrait, k): the art box of the slide's layout on this canvas, k the label scale (1.3 portrait)."""
    x, y, w, h = ART_ZONE(sl.get("layout") or "left")
    P = ORIENT() == "portrait"
    if not P:
        h = min(h, 830 - y)           # nothing below y 830 on the desktop stage
    return x, y, w, h, P, (1.3 if P else 1.0)


def _sm_icons(sl, n):
    """n icon names: args.icons first, then the vertical's catalog order (cycled)."""
    v = sl.get("vertical", "")
    base = icons(v if v in ICONS else "generico")
    given = list(sl.get("icons") or [])
    return [given[i] if i < len(given) and given[i] else base[i % len(base)] for i in range(n)]


def _sm_on(a, b=_SM_END, f=.02):
    """Hidden until a, shown from a + f until b."""
    return beat("opacity", [(0, 0), (a, 0), (a + f, 1), (b, 1), (min(b + f, .999), 0), (1, 0)])


def _sm_off(a, b=_SM_END, f=.02):
    """Shown until a, hidden from a + f until b (the pending state the story resolves)."""
    return beat("opacity", [(0, 1), (a, 1), (a + f, 0), (b, 0), (min(b + f, .999), 1), (1, 1)])


def _sm_ping(x, y, r0, r1, at, col="var(--c4)", span=.06):
    """A ring that opens once at `at` and fades (invisible in the frozen frame)."""
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r0:.1f}" fill="none" stroke="{col}" stroke-width="1.6" opacity="0">'
            f'{beat("r", [(0, r0), (at, r0), (at + span, r1), (1, r1)])}'
            f'{beat("opacity", [(0, 0), (at, 0), (at + .004, .9), (at + span, 0), (1, 0)])}</circle>')


def _sm_ride(path, a, b, r=6, col="var(--c4)"):
    """A token that rides path between a and b, hidden otherwise."""
    return (f'<g opacity="0">{beat("opacity", [(0, 0), (a, 0), (a + .004, 1), (b, 1), (b + .004, 0), (1, 0)])}'
            f'{move(path, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{token(col, r)}</g>')


def _sm_fitwrap(s, size, room, lines_max):
    """(size, chars per line, lines): the largest size (never under 15) whose wrap fits room in ≤ lines_max lines."""
    t, f = _(str(s)), current_factor()
    z, chars, ls = 15, 8, [t]
    for z in range(int(round(size)), 14, -1):
        for chars in range(max(6, int(room / (z * .40))), 5, -1):
            ls = _sm_wrap(t, chars)
            if all(bold_width(ln, z, f) <= room for ln in ls):
                break
        if len(ls) <= lines_max:
            break
    fit(max(ls, key=lambda ln: bold_width(ln, z, f)), z, room, "simple label", floor=15)   # records an overflow
    return z, chars, len(ls)


def _sm_text(x, cy, s, size, room, fill="var(--white)", anchor="start", lines_max=3, extra=W6, lh=1.2, top=False):
    """s wrapped into room at the largest size that fits, centered vertically on cy (top: its first line hangs from cy)."""
    z, chars, n = _sm_fitwrap(s, size, room, lines_max)
    y0 = cy + z * .8 if top else cy - (n - 1) * z * lh / 2 + z * .36
    return TCW(f"{x:.1f}", f"{y0:.1f}", s, chars, z, fill, extra, lh, anchor)


def _sm_badge(name, cx, cy, r, col="var(--c2)", ring="var(--line)", fill="var(--card)", dash=""):
    """A library icon inside a circle."""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{ring}" stroke-width="1.6"{d}/>'
            + icon(name, cx, cy, r * 1.15, col))


def _sm_lit_badge(name, cx, cy, r, at, col="var(--c4)"):
    """The lit copy of a badge, from at to the reset, with its ping."""
    fill = f"color-mix(in srgb, {col} 16%, var(--card))"
    return (f'<g opacity="0">{_sm_on(at)}' + glow(cx, cy, r * 1.25, col, .35)
            + _sm_badge(name, cx, cy, r, col, col, fill) + '</g>' + _sm_ping(cx, cy, r, r * 1.8, at, col))


def _sm_ok(cx, cy, r, at, ok):
    """A check in a green dot, from at."""
    return (f'<g opacity="0">{_sm_on(at)}<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{ok}"/>'
            + check(f"{cx:.1f}", f"{cy + 1:.1f}", r / 15, "var(--ink)") + '</g>')


def _sm_q(cx, cy, r, at, k):
    """The «?» of a hypothesis: a gold ring that beats at `at` and stays."""
    return (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="var(--card)" stroke="var(--c4)" stroke-width="2"/>'
            + TC(f"{cx:.1f}", f"{cy + r * .38:.1f}", "?", max(int(round(r * 1.05)), int(round(15 * k))), "var(--c4)", W6)
            + _sm_ping(cx, cy, r, r * 2, at))


def _sm_grid(n, cols, x, y, w, h, snake=False):
    """Centers of n cells in `cols` columns filling the box, row by row (snake: odd rows right to left)."""
    rows = -(-n // cols)
    cw, ch = w / cols, h / rows
    out = []
    for i in range(n):
        r, c = divmod(i, cols)
        if snake and r % 2:
            c = cols - 1 - c
        out.append((x + cw * (c + .5), y + ch * (r + .5)))
    return out, cw, ch


def _sm_chain(names, labels, x, y, w, h, k, P, times, room=None, cols=None):
    """Their operation: stations with their icons on one line (two columns snaking in portrait), lit at `times`, a
    token riding from each station to the next. Returns (art, labels, points, radius)."""
    n = len(labels)
    cols = cols or (2 if P and n > 3 else n)
    pts, cw, ch = _sm_grid(n, cols, x, y, w, h, snake=True)
    rows = -(-n // cols)
    R = min(cw * .24, ch * .3, 44 * k)
    pts = [(px, py - (0 if rows > 1 else ch * .12)) for px, py in pts]
    art, text = [], []
    line = "M" + " L".join(f"{px:.1f} {py:.1f}" for px, py in pts)
    art.append(f'<path d="{line}" fill="none" stroke="var(--c2)" stroke-width="2" stroke-dasharray="3 7" opacity=".55"/>')
    for i in range(n - 1):
        (ax, ay), (bx, by) = pts[i], pts[i + 1]
        seg = f"M{ax:.1f} {ay:.1f} L{bx:.1f} {by:.1f}"
        art.append(f'<path d="{seg}" stroke="var(--c4)" stroke-width="3" stroke-linecap="round" opacity="0">{_sm_on(times[i + 1])}</path>')
        art.append(_sm_ride(seg, times[i] + .01, times[i + 1], 6 * k))
    for i, ((px, py), nm) in enumerate(zip(pts, names)):
        art.append(_sm_badge(nm, px, py, R) + _sm_lit_badge(nm, px, py, R, times[i]))
        above = rows > 1 and i < cols          # two rows: the first row's labels go above, off the connectors
        ly = py - R - 22 * k if above else py + R + 26 * k
        text.append(_sm_text(px, ly, labels[i], 19 * k, room or cw - 14, anchor="middle", lines_max=1 if above else 2))
    return "".join(art), "".join(text), pts, R


def _sm_rot(pairs, cx, cy):
    """A rotation keyed on fractions of the loop: pairs = [(fraction, degrees)]."""
    kt = ";".join(f"{t:.3f}" for t, _v in pairs)
    vals = ";".join(f"{a} {cx:.1f} {cy:.1f}" for _t, a in pairs)
    return f'<animateTransform attributeName="transform" type="rotate" values="{vals}" keyTimes="{kt}" dur="{D}s" repeatCount="indefinite"/>'


def _sm_bust(x, y, s, skin, shirt):
    """A faceless head and shoulders centered on the head."""
    rim = 'fill="none" stroke="var(--c2)" stroke-width="1.2" opacity=".55"'
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({s:.2f})">'
            f'<path d="M-21 31 C-21 19 -13 14 0 14 C13 14 21 19 21 31 Z" fill="{shirt}"/><path d="M-21 31 C-21 19 -13 14 0 14 C13 14 21 19 21 31" {rim}/>'
            f'<rect x="-3.5" y="8" width="7" height="7" fill="{shade(skin, 14)}"/><ellipse cx="0" cy="0" rx="9" ry="10.5" fill="{skin}"/>'
            f'<path d="M-9.6 -1 C-10.4 -12 -3 -15.5 2 -15 C8 -14.6 10.8 -8.5 9.8 -2 C6.5 -8.4 -2 -9.2 -9.6 -1 Z" fill="{HAIR}"/></g>')


# ---------------------------------------------------------------- worry gauges (portada and cierre)
def _sm_budget(x0, x1, cy, s, ok, k):
    """The budget is the dashed frame: the proposal bar grows and stops inside it; at s it turns ok."""
    w, hh = x1 - x0, 26 * k
    full = (w - 8) * .76
    return (f'<rect x="{x0:.1f}" y="{cy - hh / 2:.1f}" width="{w:.1f}" height="{hh:.1f}" rx="9" fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="6 5"/>'
            f'<rect x="{x0 + 4:.1f}" y="{cy - hh / 2 + 4:.1f}" width="0" height="{hh - 8:.1f}" rx="6" fill="var(--c2)">'
            f'{beat("width", [(0, 0), (s - .14, 0), (s - .01, round(full, 1)), (_SM_END, round(full, 1)), (1, 0)])}</rect>'
            f'<g opacity="0">{_sm_on(s)}<rect x="{x0:.1f}" y="{cy - hh / 2:.1f}" width="{w:.1f}" height="{hh:.1f}" rx="9" fill="none" stroke="{ok}" stroke-width="2"/>'
            f'<rect x="{x0 + 4:.1f}" y="{cy - hh / 2 + 4:.1f}" width="{full:.1f}" height="{hh - 8:.1f}" rx="6" fill="{ok}"/></g>')


def _sm_goal(x0, x1, cy, s, ok, k):
    """The quarter in three months: the bar fills to the target line, which turns ok at s."""
    w, hh = x1 - x0, 14 * k
    xt = x0 + w * .86
    ticks = "".join(f'<path d="M{x0 + w * j / 3:.1f} {cy - hh:.1f} V{cy + hh:.1f}" stroke="var(--c2)" stroke-width="1.2" opacity=".45"/>' for j in (1, 2))
    return (f'<rect x="{x0:.1f}" y="{cy - hh / 2:.1f}" width="{w:.1f}" height="{hh:.1f}" rx="{hh / 2:.1f}" fill="var(--line)"/>' + ticks
            + f'<rect x="{x0:.1f}" y="{cy - hh / 2:.1f}" width="0" height="{hh:.1f}" rx="{hh / 2:.1f}" fill="var(--c2)">'
            f'{beat("width", [(0, 0), (s - .14, 0), (s - .01, round(xt - x0, 1)), (_SM_END, round(xt - x0, 1)), (1, 0)])}</rect>'
            f'<path d="M{xt:.1f} {cy - hh * 1.4:.1f} V{cy + hh * 1.4:.1f}" stroke="var(--c4)" stroke-width="2.5" stroke-dasharray="4 3"/>'
            + icon("generico/meta", xt, cy - hh * 2.6, 22 * k, "var(--c4)")
            + f'<g opacity="0">{_sm_on(s)}<rect x="{x0:.1f}" y="{cy - hh / 2:.1f}" width="{xt - x0:.1f}" height="{hh:.1f}" rx="{hh / 2:.1f}" fill="{ok}"/>'
            f'<path d="M{xt:.1f} {cy - hh * 1.4:.1f} V{cy + hh * 1.4:.1f}" stroke="{ok}" stroke-width="3" stroke-linecap="round"/></g>')


def _sm_kpi(x0, x1, cy, s, ok, k):
    """The KPI gauge: the needle climbs into the green zone; beside it, the boss it was promised to, checked at s."""
    r = 30 * k
    gx, gy = x0 + r + 4, cy + r * .45
    zx, zy = gx + r * math.cos(math.radians(48)), gy - r * math.sin(math.radians(48))
    arc = (f'<path d="M{gx - r:.1f} {gy:.1f} A{r:.1f} {r:.1f} 0 0 1 {gx + r:.1f} {gy:.1f}" fill="none" stroke="var(--line)" stroke-width="{8 * k:.1f}" stroke-linecap="round"/>'
           f'<path d="M{zx:.1f} {zy:.1f} A{r:.1f} {r:.1f} 0 0 1 {gx + r:.1f} {gy:.1f}" fill="none" stroke="{ok}" stroke-width="{8 * k:.1f}" stroke-linecap="round" opacity=".85"/>')
    needle = (f'<g transform="rotate(-62 {gx:.1f} {gy:.1f})">{_sm_rot([(0, -62), (s - .14, -62), (s - .01, 60), (_SM_END, 60), (1, -62)], gx, gy)}'
              f'<path d="M{gx:.1f} {gy:.1f} V{gy - r + 7:.1f}" stroke="var(--white)" stroke-width="3" stroke-linecap="round"/></g>'
              f'<circle cx="{gx:.1f}" cy="{gy:.1f}" r="{4 * k:.1f}" fill="var(--white)"/>')
    bx = min(x1 - 22 * k, gx + r + 58 * k)
    boss = _sm_bust(bx, cy - 4 * k, 1.25 * k, SKIN_LIGHT, "var(--c1)") + _sm_ok(bx + 20 * k, cy - 22 * k, 10 * k, s, ok)
    return arc + needle + boss


# ---------------------------------------------------------------- 1 · portada: their worries, their operation
@register("scene", "sm01_hero")
@register("scene", "simple-hero")
def sc_sm01_hero(sl, ctx):
    """Their three worries above their operation. Loop: a shipment runs the stations to their promise, then the budget
    fits its frame, the quarter reaches its line and the KPI needle enters the green. Frozen: all lit and resolved."""
    x, y, w, h, P, k = _sm_zone(sl)
    ok = ctx.brand.c("dark.ok")
    worries = list(sl.get("worries") or _SM_WORRIES)[:3]
    stations = list(sl.get("stations") or [])[:4]
    names = _sm_icons(sl, len(stations))
    times = [.08 + i * .12 for i in range(len(stations))]
    goal_at = times[-1] + .1 if times else .1
    solves = [goal_at + .06 + i * .07 for i in range(3)]
    art, text = [glow(x + w * .5, y + h * .72, w * .55, "var(--brand)", .35)], []
    # who: a pill with the person it is for
    ph = 44 * k
    art.append(land(card(x, y, w, ph, "var(--card)", "var(--line)", ph / 2, 1.2)
                    + icon("generico/equipo", x + ph * .6, y + ph / 2, ph * .56, "var(--c4)"), .1, .45, 10))
    text.append(land(_sm_text(x + ph * 1.1, y + ph / 2, sl.get("who", ""), 19 * k, w - ph * 1.4, "var(--white)", lines_max=1), .1, .45, 10))
    # their operation at the bottom, sized to its stations; the worries share the rest
    rows_c = 2 if P and len(stations) > 3 else 1
    gh = 50 * k
    chain_h = rows_c * (2 * 44 * k + 70 * k) + 10 * k
    oh = chain_h + gh + 34 * k
    oy = y + h - oh
    gap = 12 * k
    top = y + ph + 16 * k
    rh = (oy - 16 * k - top - 2 * gap) / 3
    gauges = (_sm_budget, _sm_goal, _sm_kpi)
    marks = ("generico/documento", "generico/meta", "generico/dato")
    rows, labs = [], []
    for i, text_ in enumerate(worries):
        ry = top + i * (rh + gap)
        cy = ry + rh / 2
        r = min(26 * k, rh * .3)
        vx0, vx1 = x + w * .6, x + w - 24 * k
        row = (card(x, ry, w, rh, "var(--card)", "var(--c2)", 16, 1.2)
               + f'<rect x="{x:.1f}" y="{ry:.1f}" width="{w:.1f}" height="{rh:.1f}" rx="16" fill="none" stroke="{ok}" stroke-width="2" opacity="0">{_sm_on(solves[i])}</rect>'
               + _sm_badge(marks[i], x + 20 * k + r, cy, r, "var(--c2)")
               + f'<g opacity="0">{_sm_on(solves[i])}' + _sm_badge(marks[i], x + 20 * k + r, cy, r, ok, ok) + '</g>'
               + gauges[i](vx0, vx1, cy, solves[i], ok, k))
        rows.append(row)
        labs.append(_sm_text(x + 34 * k + 2 * r, cy, text_, 22 * k, w * .6 - 50 * k - 2 * r, lines_max=2))
    art.append(seq(rows, .15, .5, 14))
    text.append(seq(labs, .15, .5, 14))
    art.append(land(card(x, oy, w, oh, "color-mix(in srgb, var(--c1) 10%, var(--card))", "var(--line)", 18, 1.2), .2, .5, 14))
    chain, labels, pts, R = _sm_chain(names, stations, x + 12, oy + 12 * k, w - 24, chain_h, k, P, times)
    art.append(land(chain, .3, .55, 12))
    text.append(land(labels, .3, .55, 12))
    # the promise, where the line arrives
    goal = sl.get("goal", "")
    gw = min(w - 48, bold_width(_(str(goal)), 20 * k, current_factor()) + 90 * k)
    gx, gy = x + w / 2 - gw / 2, oy + oh - gh - 14 * k
    art.append(land(card(gx, gy, gw, gh, "var(--card)", "var(--c4)", gh / 2, 1.6)
                    + f'<g opacity="0">{_sm_on(goal_at)}' + card(gx, gy, gw, gh, "color-mix(in srgb, var(--c4) 18%, var(--card))", "var(--c4)", gh / 2, 2.4) + '</g>'
                    + icon("generico/check", gx + gh * .62, gy + gh / 2, gh * .5, "var(--c4)")
                    + _sm_ping(x + w / 2, gy + gh / 2, gh / 2, gh * 1.6, goal_at), .4, .5, 10))
    text.append(land(_sm_text(gx + gh * 1.1, gy + gh / 2, goal, 20 * k, gw - gh * 1.3, "var(--white)", lines_max=1), .4, .5, 10))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 2 · desde afuera: what they publish
@register("scene", "sm02_outside")
@register("scene", "simple-outside")
def sc_sm02_outside(sl, ctx):
    """Three public sources and our dossier; a dotted line; their areas in faint lines below. Loop: the lens reads each
    source and a note flies to the dossier; then one question drops to each area and the ask lights. Frozen: sources
    read, the dossier full, a «?» in each area."""
    x, y, w, h, P, k = _sm_zone(sl)
    sources = [list(s) + [""] for s in (sl.get("sources") or [])][:3]
    areas = list(sl.get("areas") or [])[:4]
    names = _sm_icons(sl, len(areas))
    reads = [.06 + i * .13 for i in range(len(sources))]
    drops = [.5 + i * .07 for i in range(len(areas))]
    art, text = [], []
    # afuera: the label, the sources and the dossier
    lh = 30 * k
    text.append(land(T(f"{x:.1f}", f"{y + lh * .7:.1f}", sl.get("outside", "Afuera: lo que publican").upper(), int(15 * k), "var(--c4)",
                       'font-weight="600" letter-spacing="2"'), .1, .4, 6))
    sw = w * .6
    sh = (h * .42 - lh) / max(1, len(sources)) - 10 * k
    marks = ("generico/documento", "generico/dato", "generico/alerta")
    rows, labs = [], []
    for i, (name, what, *_r) in enumerate(sources):
        sy = y + lh + 8 * k + i * (sh + 10 * k)
        r = min(22 * k, sh * .3)
        rows.append(card(x, sy, sw, sh, "var(--card)", "var(--line)", 14, 1.2)
                    + f'<rect x="{x:.1f}" y="{sy:.1f}" width="{sw:.1f}" height="{sh:.1f}" rx="14" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity="0">{_sm_on(reads[i], reads[i] + .1)}</rect>'
                    + _sm_badge(marks[i % 3], x + 16 * k + r, sy + sh / 2, r)
                    + _sm_ok(x + sw - 20 * k, sy + 20 * k, 10 * k, reads[i] + .08, ctx.brand.c("dark.ok")))
        tx, room = x + 30 * k + 2 * r, sw - 60 * k - 2 * r
        labs.append(_sm_text(tx, sy + sh * .3, name, 17 * k, room, "var(--c4)", lines_max=1)
                    + _sm_text(tx, sy + sh * .66, what, 18 * k, room, lines_max=2))
    art.append(seq(rows, .1, .45, 12))
    text.append(seq(labs, .1, .45, 12))
    # the dossier fills with one note per source
    bx, bw = x + sw + 22 * k, w - sw - 22 * k
    by, bh = y + lh + 8 * k, len(sources) * (sh + 10 * k) - 10 * k
    # our dossier: rings, its name and one slot per source, filled by the note the lens takes
    book = (card(bx, by, bw, bh, "var(--card)", "var(--c2)", 14, 2)
            + "".join(f'<circle cx="{bx + 16 * k:.1f}" cy="{by + 34 * k + j * 30 * k:.1f}" r="{5 * k:.1f}" fill="none" stroke="var(--c2)" stroke-width="2.2"/>'
                      for j in range(int((bh - 40 * k) // (30 * k)))))
    head_h = 58 * k
    slot_h = (bh - head_h - 14 * k - (len(sources) - 1) * 10 * k) / max(1, len(sources))
    for i in range(len(sources)):
        ny = by + head_h + i * (slot_h + 10 * k)
        nx, nw = bx + 32 * k, bw - 46 * k
        book += (f'<rect x="{nx:.1f}" y="{ny:.1f}" width="{nw:.1f}" height="{slot_h:.1f}" rx="8" fill="none" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="4 5" opacity=".6"/>'
                 f'<g opacity="0">{_sm_on(reads[i] + .1)}' + card(nx, ny, nw, slot_h, "color-mix(in srgb, var(--c2) 14%, var(--card))", "var(--c2)", 8, 1.4)
                 + bars(nx + 12 * k, ny + slot_h / 2 - 11 * k, nw - 24 * k, 2, 14 * k, "var(--c2)", ".75") + '</g>')
        path = f"M{x + sw - 30:.1f} {y + lh + 8 * k + i * (sh + 10 * k) + sh / 2:.1f} C{bx - 20:.1f} {ny - 30:.1f} {bx + 20:.1f} {ny:.1f} {nx + nw / 2:.1f} {ny + slot_h / 2:.1f}"
        art.append(_sm_ride(path, reads[i] + .06, reads[i] + .1, 5 * k))
    art.append(land(book, .25, .5, 12))
    text.append(land(_sm_text(bx + 32 * k, by + head_h * .55, sl.get("book", "Nuestro dossier"), 19 * k, bw - 44 * k, lines_max=1), .25, .5, 12))
    # the lens visits each source
    lens_pts = [(x + sw * .78, y + lh + 8 * k + i * (sh + 10 * k) + sh / 2) for i in range(len(sources))]
    if lens_pts:
        vals = ";".join(f"{lx:.1f} {ly:.1f}" for lx, ly in [lens_pts[0]] + [p for p in lens_pts for _ in (0, 1)] + [lens_pts[-1], lens_pts[0]])
        kts = [0] + [t for r in reads for t in (r, r + .09)] + [.97, 1]
        art.append(f'<g><animateTransform attributeName="transform" type="translate" values="{vals}" keyTimes="{";".join(f"{t:.3f}" for t in kts)}" dur="{D}s" repeatCount="indefinite"/>'
                   f'<g transform="scale({k:.2f})">{lens(0, 0, 22)}</g></g>')
    # the dotted line: adentro
    dy = y + lh + 8 * k + bh + 34 * k
    art.append(land(f'<path d="M{x:.1f} {dy:.1f} H{x + w:.1f}" stroke="var(--c2)" stroke-width="2" stroke-dasharray="4 8" opacity=".7"/>', .3, .4, 0))
    art.append(land(pill(x + w / 2, dy, sl.get("inside", ""), "var(--dim)", ctx, int(17 * k), w * .8, "outside inside"), .35, .4, 0))
    # their areas, in faint lines: one question drops to each
    ay, ah = dy + 30 * k, y + h - dy - 30 * k - 64 * k
    art.append(land(card(x, ay, w, ah, "color-mix(in srgb, var(--ink) 40%, transparent)", "var(--c2)", 18, 1.2, 'stroke-dasharray="3 7"'), .3, .4, 0))
    cols = 2 if P else len(areas)
    pts, cw, ch = _sm_grid(len(areas), cols, x, ay + 20 * k, w, ah - 20 * k)
    R = min(cw * .22, ch * .3, 50 * k)
    for i, ((px, py), nm) in enumerate(zip(pts, names)):
        py -= ch * .12
        a = drops[i]
        art.append(land(_sm_badge(nm, px, py, R, "var(--c2)", "var(--c2)", "var(--ink)", "4 5"), .35 + i * .06, .45, 10))
        art.append(_sm_ride(f"M{bx + bw / 2:.1f} {by + bh:.1f} C{bx + bw / 2:.1f} {dy + 40:.1f} {px:.1f} {py - R * 2:.1f} {px:.1f} {py - R - 12:.1f}", a - .06, a, 5 * k))
        art.append(f'<g opacity="0">{_sm_on(a)}' + _sm_q(px + R * .85, py - R * .85, 13 * k, a, k) + '</g>')
        text.append(land(_sm_text(px, py + R + 22 * k, areas[i], 18 * k, cw - 14, "var(--muted)", "middle", 2), .35 + i * .06, .45, 10))
    # the ask, once every area has its question
    ask_at = (drops[-1] if drops else .5) + .08
    ay2 = y + h - 26 * k
    text.append(land(f'<g>{_sm_off(ask_at)}' + pill(x + w / 2, ay2, sl.get("ask", ""), "var(--dim)", ctx, int(19 * k), w * .9, "outside ask") + '</g>'
                     + f'<g opacity="0">{_sm_on(ask_at)}' + pill(x + w / 2, ay2, sl.get("ask", ""), "var(--c4)", ctx, int(19 * k), w * .9, "outside ask") + '</g>', .5, .45, 8))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 3 · la brecha: fact, hypothesis, not assumed
@register("scene", "sm03_gap")
@register("scene", "simple-gap")
def sc_sm03_gap(sl, ctx):
    """Three bins: facts with their source, hypotheses with «?», what we do not assume, locked. Loop: facts get their
    check, hypotheses beat, the third locks; only the fact and the hypothesis drop into today's conversation, where the
    hypothesis becomes a question. Frozen: the conversation holds a fact, a hypothesis and a question."""
    x, y, w, h, P, k = _sm_zone(sl)
    ok = ctx.brand.c("dark.ok")
    bins = [list(b) + [""] for b in (sl.get("bins") or [["Hecho", "con fuente"], ["Hipótesis", "por validar"], ["No suponemos", "lo cuentan ustedes"]])][:3]
    known = [list(f) + [""] for f in (sl.get("known") or [])][:2]
    guess = list(sl.get("guess") or [])[:2]
    unsaid = list(sl.get("unsaid") or [])[:2]
    brings = list(sl.get("brings") or ["Un hecho", "Una hipótesis", "Una pregunta"])[:3]
    names = _sm_icons(sl, len(known) + len(guess) + len(unsaid))
    heads = ("generico/check", "generico/ia", "generico/documento")
    cols_col = (ok, "var(--c4)", "var(--c2)")
    groups = [[(t, s_) for t, s_, *_r in known], [(t, "") for t in guess], [(t, "") for t in unsaid]]
    T_ITEM = [[.08, .16], [.28, .36], [.48, .52]]
    art, text = [], []
    ni = 0
    if P:
        sh = h * .2
        gh = h - sh - 20 * k
        weights = [max(1, len(g_)) for g_ in groups]
        band = [(gh - 24 * k) * wt / sum(weights) for wt in weights]
    else:
        cwid = (w - 28) / 3
        hh, ih_max = 96, 190
        n_max = max(1, max(len(g_) for g_ in groups))
        sh = h - hh - 12 - n_max * ih_max - (n_max - 1) * 10 - 22
    for b, ((head, tag, *_r), items) in enumerate(zip(bins, groups)):
        if P:   # a band per bin: its header on the left, its cards on the right
            by = y + sum(band[:b]) + b * 12 * k
            hx, hy, hw, hh_ = x, by, w * .28, band[b]
            cx0, cw_, cy0, ch_ = x + w * .28 + 12 * k, w * .72 - 12 * k, by, band[b]
        else:   # a column per bin: its header on top
            hx, hy, hw, hh_ = x + b * (cwid + 14), y, cwid, hh
            cx0, cw_, cy0, ch_ = hx, cwid, y + hh + 12, n_max * ih_max + (n_max - 1) * 10
        dash = 'stroke-dasharray="6 6"' if b == 2 else ""
        hr = 20 * k
        hcx, hcy = (hx + 16 * k + hr, hy + hh_ / 2 - 30 * k) if P else (hx + 16 + hr, hy + 34)
        hdr = card(hx, hy, hw, hh_, "var(--card)", cols_col[b], 14, 1.8, dash) + _sm_badge(heads[b], hcx, hcy, hr, cols_col[b], cols_col[b])
        hb = .1 + b * .08
        art.append(land(hdr, hb, .45, 12))
        if P:
            text.append(land(_sm_text(hx + 16 * k, hy + hh_ / 2 + 12 * k, head, 20 * k, hw - 24 * k, lines_max=1)
                             + _sm_text(hx + 16 * k, hy + hh_ / 2 + 40 * k, tag, 16 * k, hw - 24 * k, "var(--muted)", lines_max=1), hb, .45, 12))
        else:
            text.append(land(_sm_text(hx + 74, hy + 34, head, 20, hw - 86, lines_max=1)
                             + _sm_text(hx + 16, hy + 74, tag, 16, hw - 28, "var(--muted)", lines_max=1), hb, .45, 12))
        n = max(1, len(items))
        ih = (ch_ - (n - 1) * 10 * k) / n if P else ih_max
        for j, (t, src) in enumerate(items):
            iy, at = cy0 + j * (ih + 10 * k), T_ITEM[b][j]
            r = 16 * k
            c = card(cx0, iy, cw_, ih, "var(--dim)" if b == 2 else "var(--card)", "var(--line)", 12, 1.2, dash)
            c += icon(names[ni], cx0 + 14 * k + r, iy + 14 * k + r, 2 * r, "var(--c2)")
            mx, my = cx0 + cw_ - 20 * k, iy + 20 * k
            if b == 0:
                c += (_sm_ok(mx, my, 11 * k, at, ok)
                      + f'<rect x="{cx0:.1f}" y="{iy:.1f}" width="{cw_:.1f}" height="{ih:.1f}" rx="12" fill="none" stroke="{ok}" stroke-width="1.8" opacity="0">{_sm_on(at)}</rect>')
            elif b == 1:
                c += _sm_q(mx, my, 12 * k, at, k)
            else:
                c += (f'<g opacity="0">{_sm_on(at)}<rect x="{mx - 8 * k:.1f}" y="{my - 2 * k:.1f}" width="{16 * k:.1f}" height="{12 * k:.1f}" rx="2" fill="var(--c2)"/>'
                      f'<path d="M{mx - 5 * k:.1f} {my - 2 * k:.1f} V{my - 7 * k:.1f} A{5 * k:.1f} {5 * k:.1f} 0 0 1 {mx + 5 * k:.1f} {my - 7 * k:.1f} V{my - 2 * k:.1f}" fill="none" stroke="var(--c2)" stroke-width="2"/></g>')
            ib = .3 + ni * .08
            art.append(land(c, ib, .45, 10))
            fill = "var(--muted)" if b == 2 else "var(--white)"
            if P:   # beside the icon, one or two lines, the source under it
                tx, ty, room, lm = cx0 + 24 * k + 2 * r, iy + 10 * k, cw_ - 64 * k - 2 * r, 2
            else:   # under the icon, up to three lines
                tx, ty, room, lm = cx0 + 14 * k, iy + 24 * k + 2 * r, cw_ - 28 * k, 3
            lab = _sm_text(tx, ty, t, 17 * k, room, fill, lines_max=lm, top=True)
            if src:
                lab += f'<g opacity="0">{_sm_on(at)}' + _sm_text(tx, iy + ih - 16 * k, src, 15 * k, room, "var(--muted)", lines_max=1) + '</g>'
            text.append(land(lab, ib, .45, 10))
            ni += 1
    # today's conversation: a fact, a hypothesis and the question it becomes
    cy = y + h - sh
    conv = card(x, cy, w, sh, "color-mix(in srgb, var(--c1) 14%, var(--card))", "var(--c2)", 18, 1.4)
    slot_col, slot_at = (ok, "var(--c4)", "var(--c4)"), (.62, .7, .78)
    head_h = 44 * k
    sx0, sw_ = x + 20 * k, (w - 40 * k - 2 * 14 * k) / 3
    sy, shh = cy + head_h + 8 * k, sh - head_h - 22 * k
    labs = []
    for i, (lbl, col, at) in enumerate(zip(brings, slot_col, slot_at)):
        sx = sx0 + i * (sw_ + 14 * k)
        ic_y = sy + shh * .38
        glyph = (icon(heads[i], sx + sw_ / 2, ic_y, min(shh * .36, 40 * k), col) if i < 2
                 else _sm_q(sx + sw_ / 2, ic_y, min(shh * .18, 20 * k), at, k))
        conv += (f'<rect x="{sx:.1f}" y="{sy:.1f}" width="{sw_:.1f}" height="{shh:.1f}" rx="12" fill="none" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="5 5" opacity=".7"/>'
                 f'<g opacity="0">{_sm_on(at)}' + card(sx, sy, sw_, shh, f"color-mix(in srgb, {col} 14%, var(--card))", col, 12, 1.8) + glyph + '</g>'
                 + _sm_ping(sx + sw_ / 2, ic_y, 20 * k, 50 * k, at, col))
        labs.append(_sm_text(sx + sw_ / 2, sy + shh * .78, lbl, 18 * k, sw_ - 20 * k, anchor="middle", lines_max=1))
    art.append(land(conv, .4, .5, 14))
    text.append(land(_sm_text(x + 20 * k, cy + head_h * .62, sl.get("slide", ""), 19 * k, w - 40 * k, lines_max=1) + "".join(labs), .4, .5, 14))
    # the drops: the first two bins into their slots; the third stays out
    if P:
        srcs = [(x + w * .14, y + band[0] * .9), (x + w * .14, y + band[0] + band[1])]
    else:
        srcs = [(x + cwid / 2, cy - 22), (x + cwid * 1.5 + 14, cy - 22)]
    for i, (px, py) in enumerate(srcs):
        sx = sx0 + i * (sw_ + 14 * k) + sw_ / 2
        art.append(_sm_ride(f"M{px:.1f} {py:.1f} C{px:.1f} {cy:.1f} {sx:.1f} {cy:.1f} {sx:.1f} {sy + shh * .38:.1f}", slot_at[i] - .07, slot_at[i], 6 * k))
    art.append(_sm_ride(f"M{sx0 + sw_ * 1.5 + 14 * k:.1f} {sy + shh * .38:.1f} H{sx0 + sw_ * 2.5 + 28 * k:.1f}", .72, .78, 5 * k))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 4 · cuatro hipótesis: three returns, one enabler
@register("scene", "sm04_hypotheses")
@register("scene", "simple-hypotheses")
def sc_sm04_hypotheses(sl, ctx):
    """Three cards with their idea and possible return, each with «?», standing on a fourth, the enabler. Loop: a spark
    rises from the enabler to each card, which lights and beats its «?»; the enabler lights last. Frozen: all four lit,
    every «?» still there: they are chosen together."""
    x, y, w, h, P, k = _sm_zone(sl)
    cards = [list(c) + ["", "", ""] for c in (sl.get("cards") or [])][:4]
    top3, en = cards[:3], (cards[3] if len(cards) > 3 else None)
    names = _sm_icons(sl, 4)
    lights = [.12 + i * .16 for i in range(len(top3))]
    en_at = (lights[-1] if lights else .1) + .16
    ret = sl.get("ret", "Retorno posible")
    art, text = [glow(x + w / 2, y + h * .45, w * .5, "var(--brand)", .3)], []
    eh = h * (.27 if not P else .22)
    ey = y + h - eh
    gap = 14 * k
    boxes = []
    if P:
        rh = (ey - y - 40 * k - 2 * gap) / 3
        boxes = [(x + 34 * k, y + i * (rh + gap), w - 34 * k, rh) for i in range(len(top3))]
    else:
        cw = (w - 2 * gap) / 3
        boxes = [(x + i * (cw + gap), y, cw, ey - y - 50) for i in range(len(top3))]
    for i, ((area, idea, rv, *_r), (bx, by, bw, bh)) in enumerate(zip(top3, boxes)):
        at = lights[i]
        c = (card(bx, by, bw, bh, "var(--card)", "var(--line)", 16, 1.4)
             + f'<g opacity="0">{_sm_on(at)}' + card(bx, by, bw, bh, "color-mix(in srgb, var(--c4) 8%, var(--card))", "var(--c4)", 16, 2) + '</g>'
             + f'<rect x="{bx + 16:.1f}" y="{by:.1f}" width="{bw * .5:.1f}" height="4" rx="2" fill="var(--c{(1, 3, 2)[i]})"/>'
             + _sm_q(bx + bw - 26 * k, by + 26 * k, 15 * k, at, k))
        if P:
            r = min(40 * k, bh * .3)
            c += _sm_badge(names[i], bx + 18 * k + r, by + bh / 2, r) + _sm_lit_badge(names[i], bx + 18 * k + r, by + bh / 2, r, at)
            tx, room = bx + 36 * k + 2 * r, bw - 76 * k - 2 * r
            text.append(land(_sm_text(tx, by + bh * .2, area, 20 * k, room, "var(--white)", lines_max=1)
                             + _sm_text(tx, by + bh * .47, idea, 17 * k, room, "var(--white)", lines_max=2)
                             + _sm_text(tx, by + bh * .8, f"{ret}: {rv}", 17 * k, room + 40 * k, "var(--c4)", lines_max=1), .1 + i * .1, .5, 16))
        else:
            r, icy = 40, by + bh * .56
            c += _sm_badge(names[i], bx + bw / 2, icy, r) + _sm_lit_badge(names[i], bx + bw / 2, icy, r, at)
            # the idea at work: three pending items go in, one comes out resolved
            for m in range(3):
                qy = icy - 30 + m * 30
                c += f'<rect x="{bx + 16:.1f}" y="{qy - 7:.1f}" width="30" height="14" rx="4" fill="var(--dim)" stroke="var(--line)"/>'
            c += _sm_ride(f"M{bx + 46:.1f} {icy:.1f} H{bx + bw / 2 - r + 4:.1f}", at - .06, at, 4)
            c += (f'<path d="M{bx + bw / 2 + r + 6:.1f} {icy:.1f} H{bx + bw - 34:.1f}" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="3 5" opacity=".6"/>'
                  + _sm_ride(f"M{bx + bw / 2 + r:.1f} {icy:.1f} H{bx + bw - 30:.1f}", at + .01, at + .06, 5)
                  + f'<circle cx="{bx + bw - 22:.1f}" cy="{icy:.1f}" r="11" fill="none" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="3 3"/>'
                  + _sm_ok(bx + bw - 22, icy, 11, at + .06, ctx.brand.c("dark.ok")))
            text.append(land(_sm_text(bx + 18, by + 42, area, 20, bw - 70, "var(--white)", lines_max=1)
                             + _sm_text(bx + 18, by + bh * .27, idea, 17, bw - 34, "var(--white)", lines_max=3)
                             + _sm_text(bx + 18, by + bh - 62, ret, 15, bw - 34, "var(--muted)", lines_max=1)
                             + _sm_text(bx + 18, by + bh - 30, rv, 19, bw - 34, "var(--c4)", lines_max=2), .1 + i * .1, .5, 16))
        art.append(land(c, .1 + i * .1, .5, 16))
    # the enabler under the three, with a connector to each
    if en:
        area, idea, rv, *_r = en
        c = (card(x, ey, w, eh, "var(--card)", "var(--c4)", 18, 1.6)
             + f'<g opacity="0">{_sm_on(en_at)}' + card(x, ey, w, eh, "color-mix(in srgb, var(--c4) 12%, var(--card))", "var(--c4)", 18, 2.4) + '</g>'
             + _sm_q(x + w - 26 * k, ey + 26 * k, 15 * k, en_at, k))
        r = min(38 * k, eh * .3)
        c += _sm_badge("generico/ia", x + 22 * k + r, ey + eh / 2, r) + _sm_lit_badge("generico/ia", x + 22 * k + r, ey + eh / 2, r, en_at)
        # the enabler joins the three: their icons on one line, a token running between them
        hub = [x + w - (52 + j * 62) * k for j in range(3)][::-1]
        hy_ = ey + eh - 34 * k
        c += f'<path d="M{hub[0]:.1f} {hy_:.1f} H{hub[-1]:.1f}" stroke="var(--c4)" stroke-width="1.6" opacity=".6"/>'
        c += _sm_ride(f"M{hub[0]:.1f} {hy_:.1f} H{hub[-1]:.1f}", en_at, en_at + .08, 5 * k)
        for j, (hx_, nm) in enumerate(zip(hub, names[:3])):
            c += _sm_badge(nm, hx_, hy_, 20 * k, "var(--c2)") + _sm_lit_badge(nm, hx_, hy_, 20 * k, en_at + .02 + j * .03)
        art.append(land(c, .4, .5, 16))
        tx = x + 44 * k + 2 * r
        text.append(land(_sm_text(tx, ey + eh * .24, area, 20 * k, w * .5, "var(--white)", lines_max=1)
                         + _sm_text(tx, ey + eh * .52, idea, 17 * k, w - (tx - x) - 60 * k, "var(--white)", lines_max=2)
                         + _sm_text(tx, ey + eh * .82, rv, 18 * k, w * .5, "var(--c4)", lines_max=1), .4, .5, 16))
        for i, (bx, by, bw, bh) in enumerate(boxes):
            if P:
                px, py = x + 14 * k, by + bh / 2
                d = f"M{x + 14 * k:.1f} {ey:.1f} V{py:.1f} H{bx:.1f}"
                art.append(f'<path d="M{x + 14 * k:.1f} {ey:.1f} V{py:.1f} H{bx:.1f}" fill="none" stroke="var(--c4)" stroke-width="1.6" opacity=".5"/>'
                           f'<circle cx="{bx:.1f}" cy="{py:.1f}" r="4" fill="var(--c4)"/>')
            else:
                px = bx + bw / 2
                d = f"M{px:.1f} {ey:.1f} V{by + bh:.1f}"
                art.append(f'<path d="{d}" stroke="var(--c4)" stroke-width="1.6" opacity=".5"/><circle cx="{px:.1f}" cy="{by + bh:.1f}" r="4" fill="var(--c4)"/>'
                           f'<circle cx="{px:.1f}" cy="{ey:.1f}" r="4" fill="var(--c4)"/>')
            art.append(_sm_ride(d, lights[i] - .08, lights[i], 6 * k))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 5 · criterio: return or enabler, or not yet
@register("scene", "sm05_criterion")
@register("scene", "simple-criterion")
def sc_sm05_criterion(sl, ctx):
    """Three ideas, two doors («Retorno claro» o «Habilitador clave»), two trays («Construimos», «Por ahora, no»).
    Loop: each idea in turn crosses its door into «Construimos», or goes aside. Frozen: two built, one aside."""
    x, y, w, h, P, k = _sm_zone(sl)
    ok = ctx.brand.c("dark.ok")
    ideas = [list(i) + ["no"] for i in (sl.get("ideas") or [])][:3]
    crit = [list(c) + [""] for c in (sl.get("criteria") or [])][:2]
    names = _sm_icons(sl, len(ideas))
    starts = [.06 + i * .24 for i in range(len(ideas))]
    art, text = [], []
    gap = 14 * k
    # the ideas, in a row
    iw = (w - (len(ideas) - 1) * gap) / max(1, len(ideas))
    ih = 132 * k
    ipos = []
    for i, ((label, verdict, *_r), nm) in enumerate(zip(ideas, names)):
        ix = x + i * (iw + gap)
        ipos.append((ix + iw / 2, y + ih))
        c = (card(ix, y, iw, ih, "var(--card)", "var(--line)", 14, 1.2)
             + f'<rect x="{ix:.1f}" y="{y:.1f}" width="{iw:.1f}" height="{ih:.1f}" rx="14" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_sm_on(starts[i], starts[i] + .2)}</rect>'
             + icon(nm, ix + 18 * k + 16 * k, y + 22 * k + 12 * k, 32 * k, "var(--c2)"))
        art.append(land(c, .1 + i * .08, .45, 12))
        text.append(land(_sm_text(ix + 16 * k, y + ih * .66, label, 18 * k, iw - 30 * k, lines_max=2), .1 + i * .08, .45, 12))
    # the ask and the two doors
    ay = y + ih + 40 * k
    art.append(land(pill(x + w / 2, ay, sl.get("ask", ""), "var(--dim)", ctx, int(18 * k), w * .8, "criterion ask"), .25, .45, 8))
    dy, dh = ay + 36 * k, 176 * k
    ow = 52 * k
    dw = (w - ow) / 2
    doors = []
    for j, (head, desc, *_r) in enumerate(crit):
        dx = x + j * (dw + ow)
        doors.append((dx + dw / 2, dy, dy + dh))
        nm = ("generico/meta", "generico/ia")[j]
        passes = [starts[i] + .07 for i, idea in enumerate(ideas) if idea[1] == ("retorno", "habilitador")[j]]
        lit = "".join(f'<g opacity="0">{beat("opacity", [(0, 0), (a, 0), (a + .01, 1), (a + .1, 1), (a + .12, 0), (1, 0)])}'
                      + card(dx, dy, dw, dh, "color-mix(in srgb, var(--c4) 14%, var(--card))", "var(--c4)", 16, 2.2) + '</g>' for a in passes)
        c = card(dx, dy, dw, dh, "var(--card)", "var(--c2)", 16, 1.6) + lit + _sm_badge(nm, dx + 18 * k + 22 * k, dy + 36 * k, 22 * k, "var(--c4)", "var(--c4)")
        art.append(land(c, .3 + j * .1, .45, 12))
        text.append(land(_sm_text(dx + 50 * k + 22 * k, dy + 36 * k, head, 20 * k, dw - 84 * k, lines_max=2)
                         + _sm_text(dx + 18 * k, dy + dh * .7, desc, 16 * k, dw - 34 * k, "var(--muted)", lines_max=2), .3 + j * .1, .45, 12))
    if len(crit) == 2:
        art.append(land(f'<circle cx="{x + w / 2:.1f}" cy="{dy + dh / 2:.1f}" r="{20 * k:.1f}" fill="var(--c4)"/>'
                        + TC(f"{x + w / 2:.1f}", f"{dy + dh / 2 + 7 * k:.1f}", sl.get("or", "o"), int(20 * k), ctx.brand.on("var(--c4)"), W6), .4, .4, 0))
    # the trays
    ty = dy + dh + 44 * k
    th = y + h - ty
    bw_ = w * .62
    aw = w - bw_ - gap
    trays = (card(x, ty, bw_, th, "color-mix(in srgb, var(--c1) 10%, var(--card))", ok, 16, 1.8)
             + card(x + bw_ + gap, ty, aw, th, "var(--dim)", "var(--line)", 16, 1.4, 'stroke-dasharray="6 6"')
             + _sm_badge("generico/check", x + 18 * k + 18 * k, ty + 30 * k, 18 * k, ok, ok))
    art.append(land(trays, .45, .5, 12))
    text.append(land(_sm_text(x + 64 * k, ty + 30 * k, sl.get("build", "Construimos"), 20 * k, bw_ - 80 * k, lines_max=1)
                     + _sm_text(x + bw_ + gap + 16 * k, ty + 30 * k, sl.get("aside", "Por ahora, no"), 18 * k, aw - 30 * k, "var(--muted)", lines_max=1), .45, .5, 12))
    # each idea lands in its tray and stays
    built = [i for i, idea in enumerate(ideas) if idea[1] in ("retorno", "habilitador")]
    for i, (label, verdict, *_r) in enumerate(ideas):
        a = starts[i]
        sx, sy = ipos[i]
        if verdict in ("retorno", "habilitador"):
            n, slot = len(built), built.index(i)
            cw2 = (bw_ - 32 * k - (n - 1) * 10 * k) / max(1, n)
            cx2, cy2 = x + 16 * k + slot * (cw2 + 10 * k), ty + 58 * k
            chh = th - 76 * k
            door = doors[("retorno", "habilitador").index(verdict)] if len(doors) == 2 else (x + w / 4, dy, dy + dh)
            path = f"M{sx:.1f} {sy:.1f} C{sx:.1f} {sy + 40:.1f} {door[0]:.1f} {door[1] - 40:.1f} {door[0]:.1f} {door[1] + 10:.1f} L{door[0]:.1f} {door[2]:.1f} C{door[0]:.1f} {door[2] + 30:.1f} {cx2 + cw2 / 2:.1f} {cy2 - 20:.1f} {cx2 + cw2 / 2:.1f} {cy2 + 10:.1f}"
            chip = (card(cx2, cy2, cw2, chh, "color-mix(in srgb, var(--c1) 8%, var(--card))", ok, 12, 1.6)
                    + _sm_badge(names[i], cx2 + cw2 / 2, cy2 + chh * .36, min(30 * k, chh * .22), ok, ok)
                    + _sm_ok(cx2 + cw2 - 18 * k, cy2 + 18 * k, 10 * k, a + .17, ok)
                    + _sm_text(cx2 + cw2 / 2, cy2 + chh * .76, label, 17 * k, cw2 - 24 * k, anchor="middle", lines_max=2))
        else:
            cx2, cy2 = x + bw_ + gap + 12 * k, ty + 58 * k
            cw2, chh = aw - 24 * k, th - 76 * k
            path = f"M{sx:.1f} {sy:.1f} C{sx + 40:.1f} {sy + 60:.1f} {x + w - 10:.1f} {dy:.1f} {cx2 + cw2 / 2:.1f} {cy2 + 10:.1f}"
            chip = (card(cx2, cy2, cw2, chh, "var(--card)", "var(--line)", 12, 1.2, 'stroke-dasharray="4 4"')
                    + _sm_badge(names[i], cx2 + cw2 / 2, cy2 + chh * .36, min(30 * k, chh * .22), "var(--muted)", "var(--line)", "var(--dim)", "4 4")
                    + _sm_text(cx2 + cw2 / 2, cy2 + chh * .76, label, 17 * k, cw2 - 22 * k, "var(--muted)", "middle", 2))
        art.insert(0, land(f'<path d="{path}" fill="none" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="2 6" opacity=".5"/>', .5, .4, 0))
        art.append(_sm_ride(path, a + .02, a + .17, 7 * k))
        text.append(f'<g opacity="0">{_sm_on(a + .17)}{chip}</g>' + _sm_ping(cx2 + cw2 / 2, cy2 + chh / 2, 16 * k, 44 * k, a + .17,
                                                                              ok if verdict != "no" else "var(--c2)"))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 6 · la prueba: a reference or a prototype, and the KPI
@register("scene", "sm06_proof")
@register("scene", "simple-proof")
def sc_sm06_proof(sl, ctx):
    """Their question on top; two paths, a nameable reference or a prototype in a week; both into the success case and
    its KPI (indicator, from → to, owner, date). Loop: the reference lights, the week runs to the prototype, each KPI
    field gets its check; the values never move. Frozen: the four fields checked."""
    x, y, w, h, P, k = _sm_zone(sl)
    ok = ctx.brand.c("dark.ok")
    paths = [list(p) + [""] for p in (sl.get("paths") or [])][:2]
    kpi = sl.get("kpi") or []
    kpi = [list(f) + [""] for f in kpi][:4] if isinstance(kpi, list) else [["KPI", str(kpi)]]
    names = _sm_icons(sl, 3)
    art, text = [], []
    # their question
    qh = 56 * k
    art.append(land(card(x, y, w, qh, "var(--card)", "var(--line)", qh / 2, 1.2)
                    + _sm_bust(x + qh * .55, y + qh * .42, .95 * k, SKIN_BROWN, "var(--accent)"), .1, .45, 10))
    text.append(land(_sm_text(x + qh * 1.15, y + qh / 2, sl.get("ask", ""), 20 * k, w - qh * 1.4, lines_max=1), .1, .45, 10))
    # the two paths
    py, ph = y + qh + 20 * k, h * .3
    ow = 48 * k
    pw = (w - ow) / 2
    marks = ("generico/check", "generico/reloj")
    lit_at = (.1, .36)
    for j, (head, desc, *_r) in enumerate(paths):
        px = x + j * (pw + ow)
        c = (card(px, py, pw, ph, "var(--card)", "var(--c2)", 16, 1.4)
             + f'<g opacity="0">{_sm_on(lit_at[j])}' + card(px, py, pw, ph, "color-mix(in srgb, var(--c4) 10%, var(--card))", "var(--c4)", 16, 2.2) + '</g>'
             + _sm_badge(marks[j], px + 16 * k + 22 * k, py + 34 * k, 22 * k, "var(--c4)", "var(--c4)"))
        if j == 0:   # the reference: their sector's icons, lit by the case
            for m, nm in enumerate(names):
                c += icon(nm, px + 30 * k + m * 44 * k, py + ph - 30 * k, 28 * k, "var(--c2)")
            c += _sm_ok(px + pw - 24 * k, py + ph - 30 * k, 12 * k, lit_at[0] + .04, ok)
        else:        # the week: five days, the fifth the prototype
            dw_ = (pw - 40 * k - 4 * 8 * k) / 5
            for d_ in range(5):
                dx = px + 20 * k + d_ * (dw_ + 8 * k)
                at = lit_at[1] + d_ * .035
                c += (f'<rect x="{dx:.1f}" y="{py + ph - 44 * k:.1f}" width="{dw_:.1f}" height="{26 * k:.1f}" rx="6" fill="var(--dim)" stroke="var(--line)"/>'
                      f'<rect x="{dx:.1f}" y="{py + ph - 44 * k:.1f}" width="{dw_:.1f}" height="{26 * k:.1f}" rx="6" fill="{"var(--c4)" if d_ == 4 else "var(--c2)"}" opacity="0">{_sm_on(at)}</rect>')
            c += f'<g opacity="0">{_sm_on(lit_at[1] + .16)}' + spark(px + 20 * k + 4.5 * (dw_ + 8 * k) - 4 * k, py + ph - 58 * k, .7 * k) + '</g>'
        art.append(land(c, .15 + j * .1, .5, 12))
        text.append(land(_sm_text(px + 70 * k, py + 34 * k, head, 20 * k, pw - 84 * k, lines_max=1)
                         + _sm_text(px + 18 * k, py + ph * .5, desc, 17 * k, pw - 34 * k, "var(--white)", lines_max=2), .15 + j * .1, .5, 12))
    if len(paths) == 2:
        art.append(land(f'<circle cx="{x + w / 2:.1f}" cy="{py + ph / 2:.1f}" r="{19 * k:.1f}" fill="var(--c4)"/>'
                        + TC(f"{x + w / 2:.1f}", f"{py + ph / 2 + 7 * k:.1f}", sl.get("or", "o"), int(19 * k), ctx.brand.on("var(--c4)"), W6), .3, .4, 0))
    # the success case and its KPI
    cy, chh = py + ph + 34 * k, y + h - (py + ph + 34 * k)
    for j in range(len(paths)):
        sx = x + j * (pw + ow) + pw / 2
        d = f"M{sx:.1f} {py + ph:.1f} C{sx:.1f} {cy - 10:.1f} {x + w / 2:.1f} {cy - 20:.1f} {x + w / 2:.1f} {cy + 4:.1f}"
        art.append(f'<path d="{d}" fill="none" stroke="var(--c2)" stroke-width="1.6" stroke-dasharray="3 6" opacity=".6"/>'
                   + _sm_ride(d, lit_at[j] + .14, lit_at[j] + .22, 6 * k))
    case = card(x, cy, w, chh, "color-mix(in srgb, var(--c1) 12%, var(--card))", "var(--c4)", 18, 1.8)
    head_h = 58 * k
    case += _sm_badge("generico/meta", x + 18 * k + 20 * k, cy + head_h / 2 + 4, 20 * k, "var(--c4)", "var(--c4)")
    tag = sl.get("tag", "")
    labs = [_sm_text(x + 70 * k, cy + head_h / 2 + 4, sl.get("case", ""), 21 * k, w - 120 * k - (190 * k if tag else 0), lines_max=1)]
    if tag:
        labs.append(pill(x + w - 20 * k - 85 * k, cy + head_h / 2 + 4, tag, "var(--dim)", ctx, int(15 * k), 170 * k, "proof tag"))
    fx0, fy0 = x + 16 * k, cy + head_h + 8 * k
    fw, fh = (w - 32 * k - 12 * k) / 2, (chh - head_h - 24 * k - 12 * k) / 2
    checks = [.62 + i * .06 for i in range(len(kpi))]
    for i, (label, val, *_r) in enumerate(kpi):
        fx, fy = fx0 + (i % 2) * (fw + 12 * k), fy0 + (i // 2) * (fh + 12 * k)
        case += (card(fx, fy, fw, fh, "var(--card)", "var(--line)", 12, 1.2)
                 + f'<rect x="{fx:.1f}" y="{fy:.1f}" width="{fw:.1f}" height="{fh:.1f}" rx="12" fill="none" stroke="{ok}" stroke-width="1.8" opacity="0">{_sm_on(checks[i])}</rect>'
                 + _sm_ok(fx + fw - 18 * k, fy + 18 * k, 10 * k, checks[i], ok))
        labs.append(_sm_text(fx + 16 * k, fy + fh * .28, label, 16 * k, fw - 54 * k, "var(--muted)", lines_max=1)
                    + _sm_text(fx + 16 * k, fy + fh * .64, val, 25 * k, fw - 30 * k, "var(--white)", lines_max=2))
    art.append(land(case, .35, .5, 14))
    text.append(land("".join(labs), .35, .5, 14))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 7 · cómo trabajamos: three short steps
@register("scene", "sm07_path")
@register("scene", "simple-path")
def sc_sm07_path(sl, ctx):
    """A route of three numbered steps, each with what happens and how long; below, both teams and the person who
    reviews. Loop: a spark runs down the route; each step lights, the prototype runs on their operation, the decision
    gets its check; the review lights last. Frozen: three steps lit and the human review."""
    x, y, w, h, P, k = _sm_zone(sl)
    ok = ctx.brand.c("dark.ok")
    phases = [list(p) + ["", "", ""] for p in (sl.get("phases") or [])][:3]
    names = _sm_icons(sl, 4)
    lights = [.1 + i * .22 for i in range(len(phases))]
    review_at = (lights[-1] if lights else .1) + .16
    marks = ("generico/documento", "generico/ia", "generico/check")
    art, text = [glow(x + w * .1, y + h * .4, w * .3, "var(--brand)", .3)], []
    bh = h * .24
    gap = 16 * k
    sx = x + 28 * k                         # the route's spine
    cx0 = x + 64 * k
    cw = w - (cx0 - x)
    ys = [y + i * (bh + gap) for i in range(len(phases))]
    if ys:
        spine = f"M{sx:.1f} {ys[0] + bh / 2:.1f} V{ys[-1] + bh / 2:.1f}"
        art.append(land(f'<path d="{spine}" stroke="var(--c2)" stroke-width="2" stroke-dasharray="3 7" opacity=".6"/>', .1, .4, 0))
        for i in range(len(ys) - 1):
            seg = f"M{sx:.1f} {ys[i] + bh / 2:.1f} V{ys[i + 1] + bh / 2:.1f}"
            art.append(f'<path d="{seg}" stroke="var(--c4)" stroke-width="3" opacity="0">{_sm_on(lights[i + 1])}</path>'
                       + _sm_ride(seg, lights[i] + .04, lights[i + 1], 6 * k))
    for i, ((head, what, when, *_r), by) in enumerate(zip(phases, ys)):
        at = lights[i]
        ny = by + bh / 2
        node = (f'<circle cx="{sx:.1f}" cy="{ny:.1f}" r="{20 * k:.1f}" fill="var(--card)" stroke="var(--c2)" stroke-width="1.6"/>'
                + f'<g opacity="0">{_sm_on(at)}<circle cx="{sx:.1f}" cy="{ny:.1f}" r="{20 * k:.1f}" fill="var(--c4)"/></g>'
                + _sm_ping(sx, ny, 20 * k, 44 * k, at))
        c = (card(cx0, by, cw, bh, "var(--card)", "var(--line)", 16, 1.4)
             + f'<g opacity="0">{_sm_on(at)}' + card(cx0, by, cw, bh, "color-mix(in srgb, var(--c4) 9%, var(--card))", "var(--c4)", 16, 2) + '</g>')
        r = min(28 * k, bh * .22)
        c += _sm_badge(marks[i], cx0 + 18 * k + r, by + 20 * k + r, r, "var(--c2)") + _sm_lit_badge(marks[i], cx0 + 18 * k + r, by + 20 * k + r, r, at)
        # what each step touches of their operation
        if i == 0:
            c += _sm_badge(names[0], cx0 + cw - 44 * k, by + bh - 40 * k, 22 * k, "var(--c2)") + _sm_q(cx0 + cw - 26 * k, by + bh - 60 * k, 11 * k, at, k)
        elif i == 1:
            for m, nm in enumerate(names[:4]):
                ix = cx0 + cw - (36 + (3 - m) * 44) * k
                c += icon(nm, ix, by + bh - 34 * k, 28 * k, "var(--c2)")
                c += f'<g opacity="0">{_sm_on(at + .03 + m * .025)}' + icon(nm, ix, by + bh - 34 * k, 28 * k, "var(--c4)") + '</g>'
        else:
            c += _sm_ok(cx0 + cw - 40 * k, by + bh - 38 * k, 16 * k, at + .04, ok)
        art.append(land(node, .15 + i * .1, .4, 0) + land(c, .15 + i * .1, .5, 14))
        text.append(land(f'<g>{_sm_off(at)}' + TC(f"{sx:.1f}", f"{ny + 7 * k:.1f}", str(i + 1), int(19 * k), "var(--white)", W6) + '</g>'
                    + f'<g opacity="0">{_sm_on(at)}' + TC(f"{sx:.1f}", f"{ny + 7 * k:.1f}", str(i + 1), int(19 * k), ctx.brand.on("var(--c4)"), W6) + '</g>'
                    + _sm_text(cx0 + 36 * k + 2 * r, by + 20 * k + r, head, 22 * k, cw * .5, lines_max=1)
                    + _sm_text(cx0 + 18 * k, by + bh * .72, what, 18 * k, cw * .56, "var(--white)", lines_max=2)
                    + pill(cx0 + cw - 20 * k - 80 * k, by + 20 * k + r, when, "var(--dim)", ctx, int(16 * k), 160 * k, "path when"), .15 + i * .1, .5, 14))
    # both teams and the person who reviews
    ty = (ys[-1] + bh + gap + 8 * k) if ys else y
    th = y + h - ty
    team = card(x, ty, w, th, "color-mix(in srgb, var(--c1) 12%, var(--card))", "var(--line)", 18, 1.2)
    bust_s = min(1.5 * k, th / 60)
    team += (_sm_bust(x + 40 * k, ty + th * .44, bust_s, SKIN_BROWN, "var(--accent)")
             + _sm_bust(x + 86 * k, ty + th * .44, bust_s, SKIN_LIGHT, "var(--c1)")
             + icon("generico/equipo", x + 132 * k, ty + th * .44, 30 * k, "var(--c2)"))
    rx = x + w * .52
    team += (f'<rect x="{rx:.1f}" y="{ty + 12 * k:.1f}" width="{x + w - rx - 12 * k:.1f}" height="{th - 24 * k:.1f}" rx="12" fill="var(--card)" stroke="var(--line)"/>'
             + f'<g opacity="0">{_sm_on(review_at)}<rect x="{rx:.1f}" y="{ty + 12 * k:.1f}" width="{x + w - rx - 12 * k:.1f}" height="{th - 24 * k:.1f}" rx="12" fill="none" stroke="{ok}" stroke-width="2"/></g>'
             + _sm_ok(rx + 26 * k, ty + th / 2, 13 * k, review_at, ok)
             + f'<circle cx="{rx + 26 * k:.1f}" cy="{ty + th / 2:.1f}" r="{13 * k:.1f}" fill="none" stroke="var(--c2)" stroke-width="1.5"/>')
    art.append(land(team, .45, .5, 12))
    text.append(land(_sm_text(x + 160 * k, ty + th / 2, sl.get("team", ""), 18 * k, rx - x - 176 * k, lines_max=2)
                     + _sm_text(rx + 50 * k, ty + th / 2, sl.get("review", ""), 18 * k, x + w - rx - 70 * k, lines_max=2), .45, .5, 12))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 8 · el próximo paso: the invitation, signed
@register("scene", "sm08_next")
@register("scene", "simple-next")
def sc_sm08_next(sl, ctx):
    """The invitation with its date on a calendar and its button; their operation of the cover, lit again; their three
    worries resolved; the signer. Loop: the button beats, the operation lights station by station, each worry gets its
    check. Frozen: the operation lit, the worries resolved, the invitation open."""
    x, y, w, h, P, k = _sm_zone(sl)
    ok = ctx.brand.c("dark.ok")
    stations = list(sl.get("stations") or [])[:4]
    worries = list(sl.get("worries") or _SM_WORRIES)[:3]
    names = _sm_icons(sl, len(stations))
    times = [.1 + i * .1 for i in range(len(stations))]
    solves = [(times[-1] if times else .1) + .1 + i * .07 for i in range(len(worries))]
    art, text = [], []
    # the operation sized to its stations; the invitation takes the rest
    goal = sl.get("goal", "")
    gh = 46 * k if goal else 0
    chain_h = 2 * 44 * k + 70 * k + 10 * k          # one row, as on the cover's desktop: the invitation keeps its room
    oh = chain_h + (gh + 16 * k if goal else 0) + 24 * k
    sig_h, wh = 72 * k, 100 * k
    ch = h - oh - wh - sig_h - 16 * k - 14 * k - 12 * k
    # the invitation: a calendar and its button
    cal_w = min(ch * .78, w * .3)
    inv = card(x, y, w, ch, "color-mix(in srgb, var(--c1) 14%, var(--card))", "var(--c4)", 18, 1.8)
    cx_, cy_ = x + 20 * k, y + 20 * k
    cw_, chh = cal_w, ch - 40 * k
    inv += (card(cx_, cy_, cw_, chh, "var(--card)", "var(--c2)", 12, 1.4)
            + f'<rect x="{cx_:.1f}" y="{cy_:.1f}" width="{cw_:.1f}" height="{chh * .24:.1f}" rx="12" fill="var(--c2)" opacity=".35"/>'
            + "".join(f'<circle cx="{cx_ + cw_ * f_:.1f}" cy="{cy_:.1f}" r="{5 * k:.1f}" fill="none" stroke="var(--c2)" stroke-width="2"/>' for f_ in (.3, .7)))
    for r_ in range(3):
        for c_ in range(5):
            dx = cx_ + 10 * k + c_ * (cw_ - 20 * k) / 5
            dy = cy_ + chh * .32 + r_ * chh * .22
            hot = (r_, c_) == (1, 2)
            inv += (f'<rect x="{dx:.1f}" y="{dy:.1f}" width="{(cw_ - 20 * k) / 5 - 5:.1f}" height="{chh * .16:.1f}" rx="4" '
                    f'fill="{"var(--c4)" if hot else "var(--dim)"}"/>')
    inv += icon("generico/reloj", cx_ + cw_ - 18 * k, cy_ + chh * .12, 20 * k, "var(--white)")
    tx = cx_ + cw_ + 22 * k
    room = x + w - tx - 20 * k
    by_ = y + ch - 44 * k
    cta = sl.get("cta", "")
    art.append(land(inv, .1, .5, 12))
    text.append(land(_sm_text(tx, y + ch * .4, cta, 27 * k, room, lines_max=3), .1, .5, 12))
    when = sl.get("when", "")
    btn_w = min(room, bold_width(_(str(when)), 17 * k, current_factor()) + 64 * k)
    art.append(f'<rect x="{tx - 6:.1f}" y="{by_ - 24 * k:.1f}" width="{btn_w + 12:.1f}" height="{48 * k:.1f}" rx="{24 * k:.1f}" fill="none" stroke="var(--c4)" stroke-width="2">'
               f'{loop("stroke-opacity", "0;.8;0", 2.4)}</rect>')
    text.append(land(card(tx, by_ - 18 * k, btn_w, 36 * k, "var(--c4)", "var(--c4)", 18 * k, 0)
                     + icon("generico/check", tx + 22 * k, by_, 20 * k, ctx.brand.on("var(--c4)"))
                     + _sm_text(tx + 42 * k, by_, when, 17 * k, btn_w - 52 * k, ctx.brand.on("var(--c4)"), lines_max=1), .3, .45, 8))
    # their operation, lit again, and the promise of the cover where it arrives
    oy = y + ch + 16 * k
    wy = oy + oh + 14 * k
    art.append(land(card(x, oy, w, oh, "var(--card)", "var(--line)", 18, 1.2), .2, .5, 12))
    chain, labels, pts, R = _sm_chain(names, stations, x + 12, oy + 12 * k, w - 24, chain_h, k, P, times, cols=len(stations) or 1)
    art.append(land(chain, .3, .5, 10))
    text.append(land(labels, .3, .5, 10))
    if goal:
        goal_at = (times[-1] if times else .1) + .06
        gw = min(w - 48, bold_width(_(str(goal)), 19 * k, current_factor()) + 86 * k)
        gx, gy = x + w / 2 - gw / 2, oy + oh - gh - 14 * k
        art.append(land(card(gx, gy, gw, gh, "var(--card)", "var(--c4)", gh / 2, 1.6)
                        + f'<g opacity="0">{_sm_on(goal_at)}' + card(gx, gy, gw, gh, "color-mix(in srgb, var(--c4) 18%, var(--card))", "var(--c4)", gh / 2, 2.4) + '</g>'
                        + icon("generico/check", gx + gh * .62, gy + gh / 2, gh * .5, "var(--c4)"), .4, .5, 10))
        text.append(land(_sm_text(gx + gh * 1.1, gy + gh / 2, goal, 19 * k, gw - gh * 1.3, lines_max=1), .4, .5, 10))
    # their worries, resolved
    n = max(1, len(worries))
    ww = (w - (n - 1) * 12 * k) / n
    marks = ("generico/documento", "generico/meta", "generico/dato")
    for i, t in enumerate(worries):
        wx = x + i * (ww + 12 * k)
        c = (card(wx, wy, ww, wh, "var(--card)", "var(--line)", 14, 1.2)
             + f'<rect x="{wx:.1f}" y="{wy:.1f}" width="{ww:.1f}" height="{wh:.1f}" rx="14" fill="none" stroke="{ok}" stroke-width="2" opacity="0">{_sm_on(solves[i])}</rect>'
             + icon(marks[i], wx + 16 * k + 13 * k, wy + wh / 2, 26 * k, "var(--c2)")
             + _sm_ok(wx + ww - 18 * k, wy + 18 * k, 10 * k, solves[i], ok))
        art.append(land(c, .35 + i * .06, .45, 10))
        text.append(land(_sm_text(wx + 52 * k, wy + wh / 2, t, 17 * k, ww - 80 * k, lines_max=3), .35 + i * .06, .45, 10))
    # the signer
    sy = y + h - sig_h
    art.append(land(_sm_bust(x + 30 * k, sy + sig_h * .34, 1.15 * k, SKIN_BROWN, "var(--c1)"), .45, .45, 8))
    text.append(land(_sm_text(x + 66 * k, sy + sig_h * .32, sl.get("name", ""), 19 * k, w * .45, lines_max=1)
                     + _sm_text(x + 66 * k, sy + sig_h * .68, sl.get("role", ""), 15 * k, w * .45, "var(--muted)", lines_max=1)
                     + _sm_text(x + w, sy + sig_h / 2, sl.get("sign", ""), 17 * k, w * .5, "var(--c2)", "end", 2), .45, .45, 8))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE
