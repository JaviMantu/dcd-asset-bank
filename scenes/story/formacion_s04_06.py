"""Bench b · slides 4 and 6 of the class «Presentaciones de prospección de alto impacto» (slide 5 keeps `outside`).

- v04_meta: the consultative turn. A faceless client manager at her desk; above her, three worries appear one by one
  and each gets resolved: the proposal bar fits inside her budget, the quarter bar reaches the target line, the KPI
  gauge enters its green zone and her boss gets his check. The Amaris lockup waits small and dim at the side and only
  lights at the end: «Amaris: la prueba de que se puede». Frozen: three worries solved, Amaris lit, small.
- v06_hechos: sentences fall from the dossier into three columns: fact with its source (check and source tag),
  hypothesis to validate («podría»), and what is not said (people, providers, other companies' figures), struck.
  Then a figure with no source tries to enter your slide, hits its edge and is stopped: «Sin confirmar».
  Frozen: three columns filled, the unconfirmed figure outside the slide.

Timing helpers come from the harvested energía scenes (_n01_on: lit from a fraction to the reset; _n01_tr: a translate
keyed on fractions) and the faceless bust from _n07_bust; private helpers here are _v04_*.
"""


def _v04_split(s, n):
    """The wrap rule of aula.svg.wrap, so the line count here matches the tspans TCW writes."""
    out, cur = [], ""
    for w in s.split():
        if len(cur) + len(w) + 1 > n and cur:
            out.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    return out + [cur]


def _v04_label(x, cy, text, size, room, fill="var(--white)", anchor="start", where="v04 label", extra=W6):
    """A label wrapped into lines that fit room, centered on cy; it shrinks only until its longest word fits, never
    under 15 px. Returns (svg, lines, size, line height)."""
    s = _(str(text))
    longest = max(s.split(), key=lambda w: bold_width(w, size, current_factor()))
    size = fit(longest, size, room, where, floor=15)
    for n in range(48, 5, -1):
        lines = _v04_split(s, n)
        if all(bold_width(ln, size, current_factor()) <= room for ln in lines):
            break
    lh = round(size * 1.2, 1)
    y0 = cy - (len(lines) - 1) * lh / 2 + size * .36
    return TCW(x, f"{y0:.1f}", text, n, size, fill, extra, 1.2, anchor), lines, size, lh


def _v04_key(attr, pairs):
    """beat() with its values rounded: pairs = [(fraction, number)]."""
    return beat(attr, [(t, f"{v:.1f}") for t, v in pairs])


def _v04_rot(pairs, cx, cy):
    """A rotation keyed on fractions of the loop: pairs = [(fraction, degrees)] around (cx, cy)."""
    kt = ";".join(f"{t:.3f}" for t, _v in pairs)
    vals = ";".join(f"{a} {cx} {cy}" for _t, a in pairs)
    return (f'<animateTransform attributeName="transform" type="rotate" values="{vals}" keyTimes="{kt}" dur="{D}s" '
            f'repeatCount="indefinite"/>')


def _v04_off(a, f=.02):
    """Visible until a, hidden to the reset, visible again for the next lap: the pending state."""
    return beat("opacity", [(0, 1), (a, 1), (a + f, 0), (.97, 0), (1, 1)])


# ---------------------------------------------------------------- slide 4 · the three worries
def _v04_budget(x0, x1, cy, a, s, tag, ok):
    """Her budget is the dashed frame; the proposal bar grows and stops inside it; at s the frame turns ok."""
    w, full = x1 - x0, (x1 - x0 - 8) * .76
    return (T(x1, cy - 14, tag, fit(tag, 15, 160, "meta budget tag", floor=15), "var(--muted)", 'text-anchor="end" font-weight="600"')
            + f'<rect x="{x0}" y="{cy - 4}" width="{w}" height="30" rx="9" fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="6 5"/>'
            + f'<rect x="{x0 + 4}" y="{cy}" width="0" height="22" rx="6" fill="var(--c2)">{_v04_key("width", [(0, 0), (a + .05, 0), (s - .01, full), (.97, full), (1, 0)])}</rect>'
            + f'<g>{_n01_on(s)}<rect x="{x0}" y="{cy - 4}" width="{w}" height="30" rx="9" fill="none" stroke="{ok}" stroke-width="2"/>'
            f'<rect x="{x0 + 4}" y="{cy}" width="{full:.1f}" height="22" rx="6" fill="{ok}"/></g>')


def _v04_goal(x0, x1, cy, a, s, tag, ok):
    """The quarter as a bar in three months; it fills until it touches the target line, which turns ok."""
    w = x1 - x0
    xt = x0 + w * .86
    ticks = "".join(f'<path d="M{x0 + w * k / 3:.1f} {cy + 2} V{cy + 22}" stroke="var(--c2)" stroke-width="1.2" opacity=".45"/>' for k in (1, 2))
    return (f'<rect x="{x0}" y="{cy + 4}" width="{w}" height="16" rx="8" fill="var(--line)"/>' + ticks
            + f'<rect x="{x0}" y="{cy + 4}" width="0" height="16" rx="8" fill="var(--c2)">{_v04_key("width", [(0, 0), (a + .05, 0), (s - .01, xt - x0), (.97, xt - x0), (1, 0)])}</rect>'
            + f'<path d="M{xt:.1f} {cy - 6} V{cy + 30}" stroke="var(--c4)" stroke-width="2" stroke-dasharray="4 3"/>'
            + TC(f"{xt:.1f}", cy - 13, tag, fit(tag, 15, 120, "meta goal tag", floor=15), "var(--c4)", W6)
            + f'<g>{_n01_on(s)}<rect x="{x0}" y="{cy + 4}" width="{xt - x0:.1f}" height="16" rx="8" fill="{ok}"/>'
            f'<path d="M{xt:.1f} {cy - 6} V{cy + 30}" stroke="{ok}" stroke-width="3" stroke-linecap="round"/></g>')


def _v04_kpi(x0, cy, a, s, ok):
    """The KPI gauge: its needle climbs into the green zone; next to it, her boss, who gets his check at s."""
    gx, gy, r = x0 + 48, cy + 30, 38
    pt = lambda deg, rr=r: (gx + rr * math.cos(math.radians(deg)), gy - rr * math.sin(math.radians(deg)))
    (zx, zy) = pt(48)
    arc = (f'<path d="M{gx - r} {gy} A{r} {r} 0 0 1 {gx + r} {gy}" fill="none" stroke="var(--line)" stroke-width="9" stroke-linecap="round"/>'
           f'<path d="M{zx:.1f} {zy:.1f} A{r} {r} 0 0 1 {gx + r} {gy}" fill="none" stroke="{ok}" stroke-width="9" stroke-linecap="round" opacity=".85"/>')
    needle = (f'<g transform="rotate(-62 {gx} {gy})">{_v04_rot([(0, -62), (a + .05, -62), (s - .01, 64), (.97, 64), (1, -62)], gx, gy)}'
              f'<path d="M{gx} {gy} V{gy - r + 8}" stroke="var(--white)" stroke-width="3" stroke-linecap="round"/></g>'
              f'<circle cx="{gx}" cy="{gy}" r="5" fill="var(--white)"/>')
    bx, by = x0 + 176, cy - 6
    boss = (_n07_bust(bx, by, 1.5, SKIN_LIGHT, "var(--c1)")
            + f'<path d="M{bx} {by + 19} l-4 5 l4 15 l4 -15 Z" fill="var(--c4)"/>')
    badge = (f'<g>{_n01_on(s)}<circle cx="{bx + 28}" cy="{by - 16}" r="12" fill="{ok}"/>' + check(bx + 28, by - 15.5, .55, "var(--ink)") + '</g>')
    return arc + needle + boss + badge


def _v04_manager():
    """A faceless manager at her desk, behind her laptop, with a mug: seen from the front, no features."""
    desk = (f'<rect x="850" y="700" width="330" height="10" rx="4" fill="var(--line)"/>'
            f'<path d="M872 710 V812 M1158 710 V812" stroke="var(--line)" stroke-width="6" stroke-linecap="round"/>')
    who = f'<g>{bob(0, 2.5, 5)}{_n07_bust(1000, 604, 3.1, SKIN_BROWN, "var(--accent)", True)}</g>'
    laptop = (f'<path d="M958 640 H1042 L1048 700 H952 Z" fill="var(--card)" stroke="var(--c2)" stroke-width="1.5" stroke-linejoin="round"/>'
              f'<circle cx="1000" cy="668" r="5" fill="var(--c2)" opacity=".5"/>')
    mug = (f'<path d="M1106 668 H1132 V696 Q1132 700 1128 700 H1110 Q1106 700 1106 696 Z" fill="none" stroke="var(--c2)" stroke-width="1.6"/>'
           f'<path d="M1132 674 Q1144 676 1144 684 Q1144 692 1132 692" fill="none" stroke="var(--c2)" stroke-width="1.6"/>'
           f'<path d="M1114 660 Q1110 652 1116 646 M1124 660 Q1120 652 1126 646" fill="none" stroke="var(--c2)" stroke-width="1.3" opacity=".6">{loop("opacity", ".2;.7;.2", 3)}</path>')
    return desk + who + laptop + mug


@register("scene", "v04_meta")
def sc_v04_meta(sl, ctx):
    """What the client cares about: her budget, her quarter, her boss. Amaris comes last, as the proof."""
    if ORIENT() == "portrait":
        return _pv04_meta(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    X, Wd, H = 850, 680, 108
    ys = [96, 218, 340]
    shows, solves = [.02, .27, .51], [.21, .45, .69]
    lit = .76
    g = [glow(1190, 290, 460, "var(--brand)", .5)]
    # the manager and the trail of her thoughts up to the three worries
    trail = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="var(--card)" stroke="var(--c2)" stroke-width="1.5"/>'
                    for x, y, r in ((1046, 556, 5), (1068, 528, 7), (1094, 494, 9)))
    g.append(land(_v04_manager(), .1, .6, 16) + land(trail, .3, .45, 0))
    # the three worries: each appears, then gets solved
    for k, (y, text) in enumerate(zip(ys, sl["worries"])):
        a, s = shows[k], solves[k]
        cy = y + H / 2
        dot = X + 30
        inner = card(X, y, Wd, H, "var(--card)", "var(--c2)", 16, 1.2)
        inner += (f'<g>{_v04_off(s)}<circle cx="{dot}" cy="{cy}" r="8" fill="var(--c5)"/>'
                  f'<circle cx="{dot}" cy="{cy}" r="8" fill="none" stroke="var(--c5)" stroke-width="1.5">{loop("r", "8;16;8", 1.6)}{loop("opacity", "1;0;1", 1.6)}</circle></g>'
                  f'<g>{_n01_on(s)}<circle cx="{dot}" cy="{cy}" r="13" fill="{ok}"/>' + check(dot, cy + .5, .6, "var(--ink)") + '</g>')
        inner += _v04_label(X + 58, cy, text, 19, 290, where="meta worry")[0]
        vx0, vx1 = X + 366, X + 620
        if k == 0:
            inner += _v04_budget(vx0, vx1, cy, a, s, sl["budget"], ok)
        elif k == 1:
            inner += _v04_goal(vx0, vx1, cy, a, s, sl["goal"], ok)
        else:
            inner += _v04_kpi(vx0, cy, a, s, ok)
        inner += f'<g>{_n01_on(s)}<rect x="{X}" y="{y}" width="{Wd}" height="{H}" rx="16" fill="none" stroke="{ok}" stroke-width="1.8"/></g>'
        g.append(f'<g>{_n01_on(a, 1, .03)}<g>{_n01_tr([(0, "0 26"), (a, "0 26"), (a + .045, "0 0"), (1, "0 0")])}{inner}</g></g>')
    # Amaris: small and dim at the side, it only lights once her three worries are solved
    lx, ly, lw, lh = 1300, 596, 150, 28
    g.append(f'<g>{_n01_on(lit, 1, .03)}{glow(lx + lw / 2, ly + lh / 2, 150, "var(--brand)", .7)}</g>')
    # one Amaris mark per slide: the footer lockup; here Amaris is only the line that proves it
    g.append(f'<g>{_n01_on(lit + .03)}' + pill(lx + lw / 2, ly + lh / 2, sl["proof"], "var(--c4)", ctx, 16, 340, "meta proof") + '</g>')
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- slide 6 · facts, hypotheses and what is not said
def _v06_fact(x, y, w, h, text, src, ok):
    body = _v04_label(x + 16, y + 32, text, 16, w - 58, where="hechos fact")[0]
    tag_s = fit(src, 15, w - 52, "hechos source", floor=15)
    tw = bold_width(_(str(src)), tag_s, current_factor()) + 22
    tag = (card(x + 14, y + h - 34, tw, 24, "var(--dim)", "var(--c2)", 12, 1) + T(x + 25, y + h - 17, src, tag_s, "var(--c2)", W6))
    badge = f'<circle cx="{x + w - 20}" cy="{y + 20}" r="11" fill="{ok}"/>' + check(x + w - 20, y + 20.5, .5, "var(--ink)")
    return body, tag + badge


def _v06_hyp(x, y, w, h, text):
    body = _v04_label(x + 16, y + h / 2, text, 16, w - 54, where="hechos hypothesis")[0]
    q = f'<circle cx="{x + w - 20}" cy="{y + 20}" r="11" fill="none" stroke="var(--c4)" stroke-width="1.6"/>' + TC(x + w - 20, y + 26, "?", 16, "var(--c4)", W6)
    return body, q


def _v06_not(x, y, w, h, text, at):
    """What is not said: the sentence lands and a red stroke strikes each of its lines."""
    svg, lines, size, lh = _v04_label(x + 16, y + h / 2, text, 16, w - 32, "var(--muted)", where="hechos not said")
    y0 = y + h / 2 - (len(lines) - 1) * lh / 2
    strikes = ""
    for j, ln in enumerate(lines):
        lw = bold_width(ln, size, current_factor())
        yy = y0 + j * lh
        strikes += (f'<path d="M{x + 12} {yy:.1f} H{x + 20 + lw:.1f}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" '
                    f'stroke="var(--c5)" stroke-width="2.4" stroke-linecap="round">'
                    f'{beat("stroke-dashoffset", [(0, 1), (at, 1), (at + .03, 0), (.97, 0), (1, 1)])}</path>')
    return svg, strikes


@register("scene", "v06_hechos")
def sc_v06_hechos(sl, ctx):
    """Every sentence of the dossier lands in its column; a figure with no source never enters your slide."""
    if ORIENT() == "portrait":
        return _pv06_hechos(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    g = [glow(1190, 400, 470, "var(--brand)", .5)]
    # the dossier the sentences fall from
    dx, dy, dw, dh = 1040, 92, 300, 58
    rings = "".join(f'<circle cx="{dx + 16}" cy="{dy + 16 + k * 13}" r="4" fill="none" stroke="var(--c2)" stroke-width="1.5"/>' for k in range(3))
    dossier = (card(dx, dy, dw, dh, "var(--card)", "var(--c2)", 12, 1.6) + rings
               + T(dx + 34, dy + 36, sl["dossier"], fit(sl["dossier"], 18, 140, "hechos dossier", floor=15), "var(--white)", W6)
               + bars(dx + 186, dy + 18, 96, 3, 10))
    # three columns: header and empty slots
    cw, xs = 216, [850, 1082, 1314]
    tone = [ok, "var(--c4)", "var(--c5)"]
    heads = []
    for x, col, c in zip(xs, sl["columns"], tone):
        hd = (card(x, 166, cw, 68, "var(--card)", c, 14, 1.6) + f'<rect x="{x + 14}" y="166" width="{cw - 28}" height="4" rx="2" fill="{c}"/>'
              + TC(x + cw / 2, 196, col["head"], fit(col["head"], 19, cw - 24, "hechos head", floor=15), "var(--white)", W6)
              + TC(x + cw / 2, 220, col["tag"], fit(col["tag"], 15, cw - 24, "hechos head tag", floor=15), c if c != "var(--c5)" else "var(--muted)", W6))
        heads.append(hd)
    sy, sh = [246, 342, 438], 88
    # the sentences fall one by one into their columns; each one's empty slot waits for it
    facts, hyps, nots = sl["facts"], sl["hyps"], sl["nots"]
    order = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
    slots = "".join(f'<rect x="{xs[c] + 4}" y="{sy[j]}" width="{cw - 8}" height="{sh}" rx="12" fill="none" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="5 6" opacity=".4"/>'
                    for c, j in order)
    g.append(land(slots, .5, .4, 0))
    t0, step, fly = .04, .066, .04
    for i, (c, j) in enumerate(order):
        a = t0 + i * step
        x, y = xs[c] + 4, sy[j]
        w = cw - 8
        if c == 0:
            body, after = _v06_fact(x, y, w, sh, facts[j]["text"], facts[j]["src"], ok)
            after = f'<g>{_n01_on(a + fly + .01)}{after}</g>'
        elif c == 1:
            body, after = _v06_hyp(x, y, w, sh, hyps[j])
            after = f'<g>{_n01_on(a + fly)}{after}</g>'
        else:
            body, after = _v06_not(x, y, w, sh, nots[j], a + fly + .01)
        box = card(x, y, w, sh, "var(--card)", tone[c], 12, 1.4)
        ox, oy = dx + dw / 2 - (x + w / 2), dy + dh - y - 10
        g.append(f'<g>{_n01_on(a, 1, .015)}<g>{_n01_tr([(0, f"{ox:.0f} {oy:.0f}"), (a, f"{ox:.0f} {oy:.0f}"), (a + fly, "0 0"), (1, "0 0")])}'
                 f'{box}{body}</g></g>' + after)
    # drawn after the sentences, so each one slips out from under the dossier and behind the headers into its slot
    g.append(seq(heads, .2, .45, 12) + land(dossier, .1, .45, 12))
    # your slide: what you confirmed goes in
    fx, fy, fw, fh = 850, 578, 380, 222
    frame = (card(fx, fy, fw, fh, "var(--card)", "var(--c2)", 14, 1.6)
             + T(fx + 22, fy + 36, sl["slide_label"], fit(sl["slide_label"], 17, fw - 44, "hechos slide", floor=15), "var(--white)", W6)
             + f'<path d="M{fx + 22} {fy + 52} H{fx + fw - 22}" stroke="var(--line)" stroke-width="1.2"/>')
    rows = ""
    for k, (yy, wd) in enumerate(((fy + 84, 250), (fy + 122, 210), (fy + 160, 230))):
        rows += f'<rect x="{fx + 22}" y="{yy - 5}" width="{wd}" height="10" rx="5" fill="var(--c2)" opacity=".55"/>'
        rows += f'<g>{_n01_on(.52 + k * .02)}<circle cx="{fx + fw - 40}" cy="{yy}" r="10" fill="{ok}"/>' + check(fx + fw - 40, yy + .5, .45, "var(--ink)") + '</g>'
    g.append(land(frame + rows, .35, .5, 14))
    # a figure with no source tries to enter your slide and is stopped at its edge
    cw2, ch2, cyc = 176, 54, fy + 128
    hold_x, hit_x = 1412, fx + fw + 4 + cw2 / 2
    chip = (card(-cw2 / 2, -ch2 / 2, cw2, ch2, "var(--card)", "var(--c5)", 14, 1.8, 'stroke-dasharray="6 4"')
            + TC(0, 7, sl["unsourced"], fit(sl["unsourced"], 20, cw2 - 28, "hechos figure", floor=15), "var(--white)", W6))
    a0, hit, back = .60, .68, .74
    g.append(f'<g>{_n01_on(a0, 1, .02)}<g transform="translate(0 {cyc})">'
             + _n01_tr([(0, "1470 0"), (a0, "1470 0"), (hit, f"{hit_x:.0f} 0"), (hit + .01, f"{hit_x + 8:.0f} 0"), (hit + .02, f"{hit_x:.0f} 0"),
                        (back, f"{hold_x} 0"), (1, f"{hold_x} 0")]).replace("<animateTransform ", '<animateTransform additive="sum" ')
             + chip + '</g></g>')
    wall = f'<path d="M{fx + fw} {fy + 20} V{fy + fh - 20}" stroke="var(--c5)" stroke-width="4" stroke-linecap="round"/>'
    g.append(f'<g>{_n01_on(hit)}{wall}</g>')
    g.append(f'<g>{_n01_on(hit + .02)}' + pill(hold_x, cyc - 58, sl["stop"], "var(--c5)", ctx, 16, 200, "hechos stop") + '</g>')
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- portrait twins (the mobile build, DCD_ORIENT=portrait)
def _pv04_budget(x0, x1, cy, a, s, tag, ok):
    """_v04_budget at phone size."""
    w, full = x1 - x0, (x1 - x0 - 8) * .76
    return (T(x1, cy - 16, tag, fit(tag, 22, 260, "meta budget tag", floor=20), "var(--muted)", 'text-anchor="end" font-weight="600"')
            + f'<rect x="{x0}" y="{cy - 4}" width="{w}" height="40" rx="10" fill="none" stroke="var(--c2)" stroke-width="1.6" stroke-dasharray="6 5"/>'
            + f'<rect x="{x0 + 5}" y="{cy + 1}" width="0" height="30" rx="7" fill="var(--c2)">{_v04_key("width", [(0, 0), (a + .05, 0), (s - .01, full), (.97, full), (1, 0)])}</rect>'
            + f'<g>{_n01_on(s)}<rect x="{x0}" y="{cy - 4}" width="{w}" height="40" rx="10" fill="none" stroke="{ok}" stroke-width="2.4"/>'
            f'<rect x="{x0 + 5}" y="{cy + 1}" width="{full:.1f}" height="30" rx="7" fill="{ok}"/></g>')


def _pv04_goal(x0, x1, cy, a, s, tag, ok):
    """_v04_goal at phone size."""
    w = x1 - x0
    xt = x0 + w * .86
    ticks = "".join(f'<path d="M{x0 + w * k / 3:.1f} {cy + 6} V{cy + 34}" stroke="var(--c2)" stroke-width="1.4" opacity=".45"/>' for k in (1, 2))
    return (f'<rect x="{x0}" y="{cy + 8}" width="{w}" height="22" rx="11" fill="var(--line)"/>' + ticks
            + f'<rect x="{x0}" y="{cy + 8}" width="0" height="22" rx="11" fill="var(--c2)">{_v04_key("width", [(0, 0), (a + .05, 0), (s - .01, xt - x0), (.97, xt - x0), (1, 0)])}</rect>'
            + f'<path d="M{xt:.1f} {cy - 6} V{cy + 44}" stroke="var(--c4)" stroke-width="2.4" stroke-dasharray="4 3"/>'
            + TC(f"{xt:.1f}", cy - 14, tag, fit(tag, 22, 160, "meta goal tag", floor=20), "var(--c4)", W6)
            + f'<g>{_n01_on(s)}<rect x="{x0}" y="{cy + 8}" width="{xt - x0:.1f}" height="22" rx="11" fill="{ok}"/>'
            f'<path d="M{xt:.1f} {cy - 6} V{cy + 44}" stroke="{ok}" stroke-width="3.5" stroke-linecap="round"/></g>')


def _pv04_kpi(x0, cy, a, s, ok):
    """_v04_kpi at phone size: the gauge climbs into the green zone, her boss gets his check."""
    gx, gy, r = x0 + 60, cy + 40, 48
    pt = lambda deg, rr=r: (gx + rr * math.cos(math.radians(deg)), gy - rr * math.sin(math.radians(deg)))
    (zx, zy) = pt(48)
    arc = (f'<path d="M{gx - r} {gy} A{r} {r} 0 0 1 {gx + r} {gy}" fill="none" stroke="var(--line)" stroke-width="11" stroke-linecap="round"/>'
           f'<path d="M{zx:.1f} {zy:.1f} A{r} {r} 0 0 1 {gx + r} {gy}" fill="none" stroke="{ok}" stroke-width="11" stroke-linecap="round" opacity=".85"/>')
    needle = (f'<g transform="rotate(-62 {gx} {gy})">{_v04_rot([(0, -62), (a + .05, -62), (s - .01, 64), (.97, 64), (1, -62)], gx, gy)}'
              f'<path d="M{gx} {gy} V{gy - r + 10}" stroke="var(--white)" stroke-width="3.5" stroke-linecap="round"/></g>'
              f'<circle cx="{gx}" cy="{gy}" r="6" fill="var(--white)"/>')
    bx, by = x0 + 250, cy + 2
    boss = (_n07_bust(bx, by, 1.8, SKIN_LIGHT, "var(--c1)")
            + f'<path d="M{bx} {by + 23} l-5 6 l5 18 l5 -18 Z" fill="var(--c4)"/>')
    badge = (f'<g>{_n01_on(s)}<circle cx="{bx + 36}" cy="{by - 20}" r="14" fill="{ok}"/>' + check(bx + 36, by - 19.5, .65, "var(--ink)") + '</g>')
    return arc + needle + boss + badge


def _pv04_meta(sl, ctx):
    """v04 on the 900x1600 stage: the three worries as full-width cards, the manager at her desk under them, the proof
    beside her; same beats, same frozen frame."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    X, Wd, H = zx, zw, 170
    ys = [zy + 8 + k * 188 for k in range(3)]
    shows, solves = [.02, .27, .51], [.21, .45, .69]
    lit = .76
    g = [glow(zx + zw / 2, zy + 280, 480, "var(--brand)", .5)]
    mdx, mdy = zx + 220 - 1000, ys[2] + H + 16 - 485
    trail = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="var(--card)" stroke="var(--c2)" stroke-width="1.5"/>'
                    for x, y, r in ((1046, 556, 5), (1068, 528, 7), (1094, 494, 9)))
    g.append(land(f'<g transform="translate({mdx} {mdy})">{_v04_manager()}</g>', .1, .6, 16)
             + land(f'<g transform="translate({mdx} {mdy})">{trail}</g>', .3, .45, 0))
    for k, (y, text) in enumerate(zip(ys, sl["worries"])):
        a, s = shows[k], solves[k]
        ty = y + 46
        dot = X + 36
        inner = card(X, y, Wd, H, "var(--card)", "var(--c2)", 16, 1.2)
        inner += (f'<g>{_v04_off(s)}<circle cx="{dot}" cy="{ty}" r="10" fill="var(--c5)"/>'
                  f'<circle cx="{dot}" cy="{ty}" r="10" fill="none" stroke="var(--c5)" stroke-width="1.6">{loop("r", "10;19;10", 1.6)}{loop("opacity", "1;0;1", 1.6)}</circle></g>'
                  f'<g>{_n01_on(s)}<circle cx="{dot}" cy="{ty}" r="16" fill="{ok}"/>' + check(dot, ty + .5, .75, "var(--ink)") + '</g>')
        inner += _v04_label(X + 68, ty, text, 26, Wd - 300 if k == 0 else Wd - 100, where="meta worry")[0]
        vx0, vx1, vcy = X + 68, X + Wd - 40, y + 108
        if k == 0:
            inner += _pv04_budget(vx0, vx1, vcy, a, s, sl["budget"], ok)
        elif k == 1:
            inner += _pv04_goal(vx0, vx1, vcy, a, s, sl["goal"], ok)
        else:
            inner += _pv04_kpi(vx0, vcy - 20, a, s, ok)
        inner += f'<g>{_n01_on(s)}<rect x="{X}" y="{y}" width="{Wd}" height="{H}" rx="16" fill="none" stroke="{ok}" stroke-width="2.2"/></g>'
        g.append(f'<g>{_n01_on(a, 1, .03)}<g>{_n01_tr([(0, "0 26"), (a, "0 26"), (a + .045, "0 0"), (1, "0 0")])}{inner}</g></g>')
    px, py = zx + zw - 230, zy + zh - 150
    g.append(f'<g>{_n01_on(lit, 1, .03)}{glow(px, py, 180, "var(--brand)", .7)}</g>')
    g.append(f'<g>{_n01_on(lit + .03)}' + pill(px, py, sl["proof"], "var(--c4)", ctx, 24, 440, "meta proof") + '</g>')
    return portrait_mark("".join(g)), D, FREEZE


def _pv06_fact(x, y, w, h, text, src, ok):
    body = _v04_label(x + 16, y + 34, text, 22, w - 60, where="hechos fact")[0]
    tag_s = fit(src, 20, w - 44, "hechos source", floor=18)
    tw = bold_width(_(str(src)), tag_s, current_factor()) + 20
    tag = (card(x + 12, y + h - 38, tw, 30, "var(--dim)", "var(--c2)", 14, 1) + T(x + 22, y + h - 16, src, tag_s, "var(--c2)", W6))
    badge = f'<circle cx="{x + w - 22}" cy="{y + 22}" r="14" fill="{ok}"/>' + check(x + w - 22, y + 22.5, .65, "var(--ink)")
    return body, tag + badge


def _pv06_hyp(x, y, w, h, text):
    body = _v04_label(x + 16, y + h / 2, text, 22, w - 58, where="hechos hypothesis")[0]
    q = f'<circle cx="{x + w - 22}" cy="{y + 22}" r="14" fill="none" stroke="var(--c4)" stroke-width="1.8"/>' + TC(x + w - 22, y + 30, "?", 21, "var(--c4)", W6)
    return body, q


def _pv06_not(x, y, w, h, text, at):
    svg, lines, size, lh = _v04_label(x + 16, y + h / 2, text, 22, w - 32, "var(--muted)", where="hechos not said")
    y0 = y + h / 2 - (len(lines) - 1) * lh / 2
    strikes = ""
    for j, ln in enumerate(lines):
        lw = bold_width(ln, size, current_factor())
        yy = y0 + j * lh
        strikes += (f'<path d="M{x + 12} {yy:.1f} H{x + 20 + lw:.1f}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" '
                    f'stroke="var(--c5)" stroke-width="3" stroke-linecap="round">'
                    f'{beat("stroke-dashoffset", [(0, 1), (at, 1), (at + .03, 0), (.97, 0), (1, 1)])}</path>')
    return svg, strikes


def _pv06_hechos(sl, ctx):
    """v06 on the 900x1600 stage: the dossier on top, the three columns under it, your slide at the bottom with the
    unconfirmed figure stopped at its edge; same beats, same frozen frame."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    g = [glow(zx + zw / 2, zy + 380, 480, "var(--brand)", .5)]
    dw, dh = 380, 68
    dx, dy = zx + (zw - dw) / 2, zy + 6
    rings = "".join(f'<circle cx="{dx + 18}" cy="{dy + 18 + k * 16}" r="5" fill="none" stroke="var(--c2)" stroke-width="1.6"/>' for k in range(3))
    dossier = (card(dx, dy, dw, dh, "var(--card)", "var(--c2)", 12, 1.6) + rings
               + T(dx + 40, dy + 43, sl["dossier"], fit(sl["dossier"], 24, 190, "hechos dossier", floor=20), "var(--white)", W6)
               + bars(dx + 250, dy + 20, 110, 3, 12))
    cw, gp = 264, 14
    xs = [zx + k * (cw + gp) for k in range(3)]
    tone = [ok, "var(--c4)", "var(--c5)"]
    hy0, hh0 = dy + dh + 20, 82
    heads = []
    for x, col, c in zip(xs, sl["columns"], tone):
        heads.append(card(x, hy0, cw, hh0, "var(--card)", c, 14, 1.6) + f'<rect x="{x + 14}" y="{hy0}" width="{cw - 28}" height="5" rx="2.5" fill="{c}"/>'
                     + TC(x + cw / 2, hy0 + 36, col["head"], fit(col["head"], 26, cw - 24, "hechos head", floor=20), "var(--white)", W6)
                     + TC(x + cw / 2, hy0 + 66, col["tag"], fit(col["tag"], 21, cw - 24, "hechos head tag", floor=20), c if c != "var(--c5)" else "var(--muted)", W6))
    sh = 100
    sy = [hy0 + hh0 + 12 + j * (sh + 10) for j in range(3)]
    facts, hyps, nots = sl["facts"], sl["hyps"], sl["nots"]
    order = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
    g.append(land("".join(f'<rect x="{xs[c] + 4}" y="{sy[j]}" width="{cw - 8}" height="{sh}" rx="12" fill="none" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="5 6" opacity=".4"/>'
                          for c, j in order), .5, .4, 0))
    t0, step, fly = .04, .066, .04
    for i, (c, j) in enumerate(order):
        a = t0 + i * step
        x, y = xs[c] + 4, sy[j]
        w = cw - 8
        if c == 0:
            body, after = _pv06_fact(x, y, w, sh, facts[j]["text"], facts[j]["src"], ok)
            after = f'<g>{_n01_on(a + fly + .01)}{after}</g>'
        elif c == 1:
            body, after = _pv06_hyp(x, y, w, sh, hyps[j])
            after = f'<g>{_n01_on(a + fly)}{after}</g>'
        else:
            body, after = _pv06_not(x, y, w, sh, nots[j], a + fly + .01)
        box = card(x, y, w, sh, "var(--card)", tone[c], 12, 1.4)
        ox, oy = dx + dw / 2 - (x + w / 2), dy + dh - y - 10
        g.append(f'<g>{_n01_on(a, 1, .015)}<g>{_n01_tr([(0, f"{ox:.0f} {oy:.0f}"), (a, f"{ox:.0f} {oy:.0f}"), (a + fly, "0 0"), (1, "0 0")])}'
                 f'{box}{body}</g></g>' + after)
    g.append(seq(heads, .2, .45, 12) + land(dossier, .1, .45, 12))
    fx, fw = zx, 460
    fy = sy[2] + sh + 30
    fh = zy + zh - 16 - fy
    frame = (card(fx, fy, fw, fh, "var(--card)", "var(--c2)", 14, 1.6)
             + T(fx + 24, fy + 44, sl["slide_label"], fit(sl["slide_label"], 24, fw - 48, "hechos slide", floor=20), "var(--white)", W6)
             + f'<path d="M{fx + 24} {fy + 64} H{fx + fw - 24}" stroke="var(--line)" stroke-width="1.2"/>')
    rows = ""
    step_r = (fh - 110) / 3
    for k, wd in enumerate((310, 260, 290)):
        yy = fy + 110 + k * step_r
        rows += f'<rect x="{fx + 24}" y="{yy - 6:.1f}" width="{wd}" height="12" rx="6" fill="var(--c2)" opacity=".55"/>'
        rows += f'<g>{_n01_on(.52 + k * .02)}<circle cx="{fx + fw - 44}" cy="{yy:.1f}" r="13" fill="{ok}"/>' + check(fx + fw - 44, f"{yy + .5:.1f}", .6, "var(--ink)") + '</g>'
    g.append(land(frame + rows, .35, .5, 14))
    cw2, ch2, cyc = 220, 66, fy + fh / 2 + 20
    hold_x, hit_x = fx + fw + 4 + cw2 / 2 + 110, fx + fw + 4 + cw2 / 2
    chip = (card(-cw2 / 2, -ch2 / 2, cw2, ch2, "var(--card)", "var(--c5)", 16, 2, 'stroke-dasharray="6 4"')
            + TC(0, 9, sl["unsourced"], fit(sl["unsourced"], 26, cw2 - 30, "hechos figure", floor=20), "var(--white)", W6))
    a0, hit, back = .60, .68, .74
    start = zx + zw - cw2 / 2 - 4
    g.append(f'<g>{_n01_on(a0, 1, .02)}<g transform="translate(0 {cyc:.0f})">'
             + _n01_tr([(0, f"{start:.0f} 0"), (a0, f"{start:.0f} 0"), (hit, f"{hit_x:.0f} 0"), (hit + .01, f"{hit_x + 10:.0f} 0"), (hit + .02, f"{hit_x:.0f} 0"),
                        (back, f"{hold_x:.0f} 0"), (1, f"{hold_x:.0f} 0")]).replace("<animateTransform ", '<animateTransform additive="sum" ')
             + chip + '</g></g>')
    g.append(f'<g>{_n01_on(hit)}<path d="M{fx + fw} {fy + 24} V{fy + fh - 24}" stroke="var(--c5)" stroke-width="5" stroke-linecap="round"/></g>')
    g.append(f'<g>{_n01_on(hit + .02)}' + pill(hold_x, cyc - 74, sl["stop"], "var(--c5)", ctx, 24, 250, "hechos stop") + '</g>')
    return portrait_mark("".join(g)), D, FREEZE
