"""Bench e of the class «Presentaciones de prospección de alto impacto»: slides 13 (escena), 14 (demo) and 15 (en-vivo).
Runs in the shared namespace (module/ext.py): lib helpers (land, pop, seq, beat, loop, card, pill, _woman, _lock, SKIN_*,
HAIR, shade…) are at hand without imports. Every loop is one 12-second story timed with beat(); the reduced-motion frame
(0.9 of the loop, 10.8 s) is its resolved state. Figures never animate."""

_V13_END = .98   # every resolved state holds until here, then the loop resets


def _v13_on(a, b=_V13_END, f=.02, hi=1):
    """Hidden until a, shown from a + f until b, hidden again by the end of the loop."""
    return beat("opacity", [(0, 0), (a, 0), (a + f, hi), (b, hi), (min(b + f, .999), 0), (1, 0)])


def _v13_lit(a, lo=.4, b=_V13_END, f=.02):
    """Dimmed until a, full from a + f until b."""
    return beat("opacity", [(0, lo), (a, lo), (a + f, 1), (b, 1), (min(b + f, .999), lo), (1, lo)])


def _v13_ping(x, y, r0, r1, col, a, span=.07):
    """One ring that opens at a and fades (gone in the frozen frame)."""
    return (f'<circle cx="{x}" cy="{y}" r="{r0}" fill="none" stroke="{col}" stroke-width="1.5" opacity="0">'
            f'{beat("r", [(0, r0), (a, r0), (a + span, r1), (1, r1)])}'
            f'{beat("opacity", [(0, 0), (a, 0), (a + .005, .9), (a + span, 0), (1, 0)])}</circle>')


def _v13_ride(path, a, b, inner):
    """inner (drawn around 0,0) rides path between a and b and is hidden the rest of the loop."""
    return (f'<g opacity="0">{beat("opacity", [(0, 0), (a, 0), (a + .004, 1), (b, 1), (b + .004, 0), (1, 0)])}'
            f'{move(path, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{inner}</g>')


def _v13_tick(x, y, a, ok, r=11):
    """An empty ring that fills with a check at a."""
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="var(--line)" stroke-width="1.5"/>'
            f'<g opacity="0">{_v13_on(a)}<circle cx="{x}" cy="{y}" r="{r}" fill="{ok}"/>{check(x, y + 1, r / 20, "var(--ink)")}</g>')


def _v13_lines(text, size, room, where):
    """text split into lines that each fit room at size (measured, never under 15 px)."""
    words, out, cur = _(str(text)).split(), [], ""
    for w in words:
        t = f"{cur} {w}".strip()
        if cur and bold_width(t, size, current_factor()) > room:
            out.append(cur)
            cur = w
        else:
            cur = t
    out.append(cur)
    for ln in out:
        fit(ln, size, room, where, floor=15)
    return out


def _v13_block(x, y, text, size, room, where, fill="var(--white)", lh=1.25, anchor=""):
    """A measured, wrapped label; returns (svg, number of lines)."""
    ls = _v13_lines(text, size, room, where)
    return "".join(T(x, f"{y + k * size * lh:.1f}", ln, size, fill, f'{anchor} {W6}') for k, ln in enumerate(ls)), len(ls)


def _v13_host(x, y, s, skin, jacket):
    """Faceless, three-quarter view facing right, short hair; the near arm reaches forward, hand at (122, 66)."""
    rim = 'fill="none" stroke="var(--c2)" stroke-width="1.2" opacity=".55"'
    torso = "M-70 178 C-72 102 -54 52 -20 38 C-8 34 12 34 26 38 C58 52 74 104 76 178 Z"
    arm = "M50 54 L78 104 L116 72"
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="{torso}" fill="{jacket}"/><path d="{torso}" {rim}/>'
            f'<path d="M-16 38 L2 56 L20 38 L11 31 L2 44 L-7 31 Z" fill="var(--white)" opacity=".92"/>'
            f'<path d="M-11 -6 C-10 12 -10 24 -12 40 C-2 46 10 46 16 40 C12 24 12 10 12 -6 Z" fill="{shade(skin, 14)}"/>'
            f'<g><g>{bob(0, 2, 4)}'
            f'<path d="M-22 -58 C-24 -94 2 -108 26 -99 C44 -92 48 -74 44 -55 C42 -40 36 -28 26 -21 C13 -13 -5 -15 -15 -26 C-22 -35 -22 -46 -22 -58 Z" fill="{skin}"/>'
            f'<ellipse cx="-13" cy="-52" rx="5" ry="8" fill="{shade(skin, 14)}"/>'
            f'<path d="M-26 -56 C-30 -98 6 -116 32 -101 C43 -94 46 -84 44 -77 C35 -86 20 -89 8 -87 C-2 -85 -9 -79 -12 -68 C-14 -62 -17 -57 -21 -51 Z" fill="{HAIR}"/>'
            f'<path d="M-26 -56 C-30 -98 6 -116 32 -101 C43 -94 46 -84 44 -77" {rim}/></g></g>'
            f'<path d="{arm}" fill="none" stroke="{shade(jacket, 12)}" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{arm}" {rim}/><circle cx="122" cy="66" r="8" fill="{skin}"/></g>')


def _v13_back(x, y, s, jacket, hair=HAIR, skin=SKIN_LIGHT):
    """An attendee seen from behind, looking at their laptop: back of the head and shoulders, faceless by construction."""
    rim = 'fill="none" stroke="var(--c2)" stroke-width="1.2" opacity=".5"'
    sh = "M-64 42 C-62 12 -42 0 -16 -2 H16 C42 0 62 12 64 42 Z"
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="{sh}" fill="{jacket}"/><path d="{sh}" {rim}/>'
            f'<rect x="-9" y="-14" width="18" height="16" fill="{shade(skin, 18)}"/>'
            f'<ellipse cx="-23" cy="-30" rx="4" ry="7" fill="{skin}"/><ellipse cx="23" cy="-30" rx="4" ry="7" fill="{skin}"/>'
            f'<ellipse cx="0" cy="-32" rx="23" ry="26" fill="{hair}"/><ellipse cx="0" cy="-32" rx="23" ry="26" {rim}/></g>')


# ---------------------------------------------------------------- portrait twins (the mobile build, DCD_ORIENT=portrait)
def _pv13_escena(sl, ctx):
    """v13 on the 900x1600 stage: the stopwatch (left) beside the projector screen (right) on top, the presenter and the
    room under them. The mini slide assembles in under 2 s, its little story plays, «12.000» never moves."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    sx, sy, sw, sh = zx + 250, zy + 50, zw - 250, 470
    t2 = 2 / D
    g = [glow(sx + sw / 2, sy + 240, 460, "var(--brand)", .5)]
    g.append(land(f'<path d="M{sx + 40} {sy + sh} L{sx + sw - 40} {sy + sh} L{zx + zw} {zy + zh - 10} L{sx - 30} {zy + zh - 10} Z" fill="var(--c2)" opacity=".06">'
                  f'{loop("opacity", ".04;.09;.04", 5)}</path>', .2, .5, 0))
    scr = (f'<path d="M{sx + 60} {zy + 6} V{sy - 12} M{sx + sw - 60} {zy + 6} V{sy - 12}" stroke="var(--line)" stroke-width="1.5"/>'
           f'<rect x="{sx - 12}" y="{sy - 16}" width="{sw + 24}" height="14" rx="7" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.2"/>'
           + card(sx, sy, sw, sh, "var(--card)", "var(--c2)", 10, 1.4))
    g.append(land(scr, .05, .45, 12))
    title = (f'<g opacity="0">{_v13_on(.01)}<rect x="{sx + 24}" y="{sy + 24}" width="{sw * .6:.0f}" height="16" rx="8" fill="var(--c2)" opacity=".85"/>'
             f'<rect x="{sx + 24}" y="{sy + 50}" width="{sw * .4:.0f}" height="10" rx="5" fill="var(--c2)" opacity=".45"/></g>')
    px, py, pw, ph = sx + 20, sy + 80, 290, sh - 100
    story, nl = _v13_block(px + 18, py + 38, sl["story"], 21, pw - 36, "v13 story", "var(--muted)")
    ny0 = py + 38 + nl * 26
    nodes = ((px + 54, py + ph - 50), (px + 146, ny0 + 60), (px + 236, py + ph - 110))
    path = f"M{nodes[0][0]} {nodes[0][1]} C{nodes[0][0] + 20} {nodes[0][1] - 90} {nodes[1][0] - 60} {nodes[1][1]} {nodes[1][0]} {nodes[1][1]}"
    path2 = f"M{nodes[1][0]} {nodes[1][1]} C{nodes[1][0] + 50} {nodes[1][1]} {nodes[2][0] - 10} {nodes[2][1] - 70} {nodes[2][0]} {nodes[2][1]}"
    hits = (.22, .36, .52)
    panel = (card(px, py, pw, ph, "var(--dim)", "var(--line)", 12, 1.2) + story
             + f'<path d="{path}" fill="none" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 6"/>'
             + f'<path d="{path2}" fill="none" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 6"/>'
             + f'<path d="{path}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="2.5">'
             f'{beat("stroke-dashoffset", [(0, 1), (hits[0], 1), (hits[1], 0), (_V13_END, 0), (1, 1)])}</path>'
             + f'<path d="{path2}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="2.5">'
             f'{beat("stroke-dashoffset", [(0, 1), (hits[1] + .02, 1), (hits[2], 0), (_V13_END, 0), (1, 1)])}</path>')
    for (nx, ny), a in zip(nodes, hits):
        panel += (f'<circle cx="{nx}" cy="{ny}" r="20" fill="var(--card)" stroke="var(--c2)" stroke-width="1.5"/>'
                  f'<g opacity="0">{_v13_on(a)}<circle cx="{nx}" cy="{ny}" r="20" fill="var(--c1)" stroke="var(--c4)" stroke-width="2"/>'
                  f'<circle cx="{nx}" cy="{ny}" r="7" fill="var(--c4)"/></g>' + _v13_ping(nx, ny, 20, 44, "var(--c4)", a))
    panel += _v13_ride(path, hits[0], hits[1], token("var(--c4)", 7)) + _v13_ride(path2, hits[1] + .02, hits[2], token("var(--c4)", 7))
    panel += f'<g opacity="0">{_v13_on(hits[2] + .03)}<circle cx="{nodes[2][0]}" cy="{nodes[2][1]}" r="30" fill="none" stroke="{ok}" stroke-width="2.5"/></g>'
    g.append(f'<g opacity="0">{_v13_on(.05)}{panel}</g>' + title)
    fx, fy = px + pw + 16, py
    fw, fh = sx + sw - 20 - fx, 170
    fig = (card(fx, fy, fw, fh, "var(--dim)", "var(--c2)", 12, 1.4)
           + TC(fx + fw / 2, fy + 110, sl["number"], fit(sl["number"], 52, fw - 40, "v13 figure", floor=20), "var(--white)", 'font-weight="700"')
           + f'<g transform="translate({fx + fw - 28} {fy + 30}) scale(1.3) translate({-(fx + fw - 28)} {-(fy + 30)})">{_lock(fx + fw - 28, fy + 30, "var(--c4)")}</g>')
    g.append(land(fig, .15, .45, 10))
    still, _n = _v13_block(fx + fw / 2, fy + fh + 44, sl["still"], 21, fw - 4, "v13 still", anchor='text-anchor="middle"')
    g.append(f'<g>{_v13_lit(.6, .55)}{still}</g>' + _v13_ping(fx + fw - 28, fy + 34, 14, 40, "var(--c4)", .6))
    # the stopwatch, left of the screen
    cx, cy, r = zx + 104, zy + 130, 76
    ticks = "".join(f'<path d="M{cx + (r - 7) * math.sin(math.radians(a)):.1f} {cy - (r - 7) * math.cos(math.radians(a)):.1f} '
                    f'L{cx + (r - 17) * math.sin(math.radians(a)):.1f} {cy - (r - 17) * math.cos(math.radians(a)):.1f}" '
                    f'stroke="var(--c2)" stroke-width="{2.4 if a % 90 == 0 else 1.4}" opacity=".7"/>' for a in range(0, 360, 30))
    ar = r - 28
    arc = f"M{cx} {cy - ar} A{ar} {ar} 0 0 1 {cx + ar * math.sin(math.radians(60)):.1f} {cy - ar * math.cos(math.radians(60)):.1f}"
    watch = (f'<rect x="{cx - 12}" y="{cy - r - 20}" width="24" height="14" rx="3" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.4"/>'
             f'<path d="M{cx + 52} {cy - r + 6} L{cx + 64} {cy - r - 6}" stroke="var(--c2)" stroke-width="5" stroke-linecap="round"/>'
             f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="var(--card)" stroke="var(--c2)" stroke-width="1.8"/>' + ticks
             + f'<path d="{arc}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{ok}" stroke-width="9" stroke-linecap="round">'
             f'{beat("stroke-dashoffset", [(0, 1), (t2, 0), (_V13_END, 0), (1, 1)])}</path>'
             + f'<g><animateTransform attributeName="transform" type="rotate" values="0 {cx} {cy};60 {cx} {cy};60 {cx} {cy};0 {cx} {cy}" '
             f'keyTimes="0;{t2:.3f};{_V13_END};1" dur="{D}s" repeatCount="indefinite"/>'
             f'<path d="M{cx} {cy + 10} V{cy - r + 16}" stroke="var(--white)" stroke-width="3" stroke-linecap="round"/></g>'
             f'<circle cx="{cx}" cy="{cy}" r="6" fill="var(--white)"/>'
             + TC(cx, cy + r + 40, sl["clock"], 28, "var(--c4)", 'font-weight="700"'))
    g.append(land(watch, .1, .45, 10))
    done, _n = _v13_block(cx, cy + r + 124, sl["done"], 21, 190, "v13 done", anchor='text-anchor="middle"')
    g.append(f'<g opacity="0">{_v13_on(t2)}<circle cx="{cx}" cy="{cy + r + 78}" r="16" fill="{ok}"/>'
             + check(cx, cy + r + 79, .8, "var(--ink)") + done + '</g>' + _v13_ping(cx, cy, r, r + 36, ok, t2))
    # the presenter, bottom left, points up at the screen; the room watches it
    wx, wy = zx + 130, zy + zh - 200
    waves = "".join(f'<path d="M{wx + 50 + k * 13:.1f} {wy - 84 - k * 10} Q{wx + 64 + k * 16:.1f} {wy - 52} {wx + 50 + k * 13:.1f} {wy - 20 + k * 10}" '
                    f'fill="none" stroke="var(--c4)" stroke-width="2.5" stroke-linecap="round">{loop("opacity", ".15;1;.15", 1.5, k * .3)}</path>'
                    for k in range(3))
    talk = pill(wx - 20, wy - 170, sl["talk"], "var(--card)", ctx, fit(sl["talk"], 22, 200, "v13 talk", floor=18), 220, "v13 talk")
    g.append(f'<g opacity="0">{_v13_on(t2 + .02)}{waves}{talk}</g>')
    g.append(land(_woman(wx, wy, 1.05, SKIN_BROWN, "var(--accent)"), .25, .6, 30))
    room = "".join(_user(zx + 360 + k * 108, zy + zh - 40, 1.5, "var(--c2)") for k in range(5))
    g.append(land(f'<g opacity=".55">{_v13_lit(t2, .6)}{room}</g>', .3, .5, 12))
    return portrait_mark("".join(g)), D, FREEZE


# ---------------------------------------------------------------- 13 · Cada diapositiva se entiende en dos segundos
@register("scene", "v13_escena")
def sc_v13_escena(sl, ctx):
    """A mini slide on a projector screen. Each loop a stopwatch starts: in under two seconds the title, the scene and
    the figure are all there, and the hand stops on «2 s», «Diapositiva completa». Then, while the faceless presenter
    talks (speech waves), a short story plays inside the mini slide: a token lights three steps in order. The figure
    «12.000» never moves: it sits there from the first frame with its lock, «La cifra no se mueve». Frozen frame: the
    slide complete, its little story resolved, the figure locked, the hand on «2 s»."""
    if ORIENT() == "portrait":
        return _pv13_escena(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    sx, sy, sw, sh = 1010, 146, 530, 400
    t2 = 2 / D                                   # the stopwatch stops at 2 s
    g = [glow(1275, 350, 420, "var(--brand)", .5)]
    # the light of the projector falls on the room
    g.append(land(f'<path d="M{sx + 40} {sy + sh} L{sx + sw - 40} {sy + sh} L1560 830 L1030 830 Z" fill="var(--c2)" opacity=".06">'
                  f'{loop("opacity", ".04;.09;.04", 5)}</path>', .2, .5, 0))
    # the screen, with its roller and cords
    scr = (f'<path d="M{sx + 60} 96 V{sy - 12} M{sx + sw - 60} 96 V{sy - 12}" stroke="var(--line)" stroke-width="1.5"/>'
           f'<rect x="{sx - 14}" y="{sy - 16}" width="{sw + 28}" height="14" rx="7" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.2"/>'
           + card(sx, sy, sw, sh, "var(--card)", "var(--c2)", 10, 1.4))
    g.append(land(scr, .05, .45, 12))
    # the mini slide, assembled in under two seconds on every loop: title, scene
    title = (f'<g opacity="0">{_v13_on(.01)}<rect x="{sx + 26}" y="{sy + 24}" width="320" height="14" rx="7" fill="var(--c2)" opacity=".85"/>'
             f'<rect x="{sx + 26}" y="{sy + 48}" width="210" height="9" rx="4.5" fill="var(--c2)" opacity=".45"/></g>')
    px, py, pw, ph = sx + 26, sy + 78, 268, 296
    nodes = ((px + 50, py + 236), (px + 136, py + 120), (px + 222, py + 196))
    path = f"M{nodes[0][0]} {nodes[0][1]} C{nodes[0][0] + 20} {nodes[0][1] - 90} {nodes[1][0] - 60} {nodes[1][1]} {nodes[1][0]} {nodes[1][1]}"
    path2 = f"M{nodes[1][0]} {nodes[1][1]} C{nodes[1][0] + 50} {nodes[1][1]} {nodes[2][0] - 10} {nodes[2][1] - 70} {nodes[2][0]} {nodes[2][1]}"
    hits = (.22, .36, .52)
    story, _n = _v13_block(px + 18, py + 32, sl["story"], 15, pw - 36, "v13 story", "var(--muted)")
    panel = (card(px, py, pw, ph, "var(--dim)", "var(--line)", 12, 1.2) + story
             + f'<path d="{path}" fill="none" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 6"/>'
             + f'<path d="{path2}" fill="none" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 6"/>'
             + f'<path d="{path}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="2">'
             f'{beat("stroke-dashoffset", [(0, 1), (hits[0], 1), (hits[1], 0), (_V13_END, 0), (1, 1)])}</path>'
             + f'<path d="{path2}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="2">'
             f'{beat("stroke-dashoffset", [(0, 1), (hits[1] + .02, 1), (hits[2], 0), (_V13_END, 0), (1, 1)])}</path>')
    for k, ((nx, ny), a) in enumerate(zip(nodes, hits)):
        panel += (f'<circle cx="{nx}" cy="{ny}" r="18" fill="var(--card)" stroke="var(--c2)" stroke-width="1.5"/>'
                  f'<g opacity="0">{_v13_on(a)}<circle cx="{nx}" cy="{ny}" r="18" fill="var(--c1)" stroke="var(--c4)" stroke-width="2"/>'
                  f'<circle cx="{nx}" cy="{ny}" r="6" fill="var(--c4)"/></g>' + _v13_ping(nx, ny, 18, 40, "var(--c4)", a))
    panel += _v13_ride(path, hits[0], hits[1], token("var(--c4)", 6)) + _v13_ride(path2, hits[1] + .02, hits[2], token("var(--c4)", 6))
    # the story resolved: the last step is ringed and stays
    panel += f'<g opacity="0">{_v13_on(hits[2] + .03)}<circle cx="{nodes[2][0]}" cy="{nodes[2][1]}" r="27" fill="none" stroke="{ok}" stroke-width="2"/></g>'
    g.append(f'<g opacity="0">{_v13_on(.05)}{panel}</g>' + title)
    # the figure: there from the first frame, never animated; its lock and its rule
    fx, fy, fw, fh = sx + 312, sy + 78, 192, 150
    fig = (card(fx, fy, fw, fh, "var(--dim)", "var(--c2)", 12, 1.4)
           + TC(fx + fw / 2, fy + 96, sl["number"], fit(sl["number"], 46, fw - 40, "v13 figure"), "var(--white)", 'font-weight="700"')
           + _lock(fx + fw - 24, fy + 26, "var(--c4)"))
    g.append(land(fig, .15, .45, 10))
    still, _n = _v13_block(fx + fw / 2, fy + fh + 34, sl["still"], 17, fw, "v13 still", anchor='text-anchor="middle"')
    g.append(f'<g>{_v13_lit(.6, .55)}{still}</g>' + _v13_ping(fx + fw - 24, fy + 30, 12, 34, "var(--c4)", .6))
    # the stopwatch: its hand runs from 0 and stops on the 2 s mark
    cx, cy, r = 902, 236, 58
    ticks = "".join(f'<path d="M{cx + (r - 6) * math.sin(math.radians(a)):.1f} {cy - (r - 6) * math.cos(math.radians(a)):.1f} '
                    f'L{cx + (r - 14) * math.sin(math.radians(a)):.1f} {cy - (r - 14) * math.cos(math.radians(a)):.1f}" '
                    f'stroke="var(--c2)" stroke-width="{2 if a % 90 == 0 else 1.2}" opacity=".7"/>' for a in range(0, 360, 30))
    ar = r - 22
    arc = f"M{cx} {cy - ar} A{ar} {ar} 0 0 1 {cx + ar * math.sin(math.radians(60)):.1f} {cy - ar * math.cos(math.radians(60)):.1f}"
    mx, my = cx + (r + 22) * math.sin(math.radians(60)), cy - (r + 22) * math.cos(math.radians(60))
    watch = (f'<rect x="{cx - 10}" y="{cy - r - 18}" width="20" height="12" rx="3" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.4"/>'
             f'<path d="M{cx + 40} {cy - r + 4} L{cx + 50} {cy - r - 6}" stroke="var(--c2)" stroke-width="4" stroke-linecap="round"/>'
             f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="var(--card)" stroke="var(--c2)" stroke-width="1.6"/>' + ticks
             + f'<path d="{arc}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{ok}" stroke-width="7" stroke-linecap="round">'
             f'{beat("stroke-dashoffset", [(0, 1), (t2, 0), (_V13_END, 0), (1, 1)])}</path>'
             + f'<g><animateTransform attributeName="transform" type="rotate" values="0 {cx} {cy};60 {cx} {cy};60 {cx} {cy};0 {cx} {cy}" '
             f'keyTimes="0;{t2:.3f};{_V13_END};1" dur="{D}s" repeatCount="indefinite"/>'
             f'<path d="M{cx} {cy + 8} V{cy - r + 12}" stroke="var(--white)" stroke-width="2.5" stroke-linecap="round"/></g>'
             f'<circle cx="{cx}" cy="{cy}" r="5" fill="var(--white)"/>'
             + T(f"{mx:.1f}", f"{my + 8:.1f}", sl["clock"], 22, "var(--c4)", 'font-weight="700"'))
    g.append(land(watch, .1, .45, 10))
    done, _n = _v13_block(cx, cy + r + 66, sl["done"], 17, 170, "v13 done", anchor='text-anchor="middle"')
    g.append(f'<g opacity="0">{_v13_on(t2)}<circle cx="{cx}" cy="{cy + r + 26}" r="13" fill="{ok}"/>'
             + check(cx, cy + r + 27, .65, "var(--ink)") + done + '</g>' + _v13_ping(cx, cy, r, r + 30, ok, t2))
    # the presenter points at the screen and talks; the room watches
    wx, wy = 902, 668
    waves = "".join(f'<path d="M{wx + 46 + k * 11:.1f} {wy - 76 - k * 9} Q{wx + 58 + k * 14:.1f} {wy - 48} {wx + 46 + k * 11:.1f} {wy - 20 + k * 9}" '
                    f'fill="none" stroke="var(--c4)" stroke-width="2" stroke-linecap="round">{loop("opacity", ".15;1;.15", 1.5, k * .3)}</path>'
                    for k in range(3))
    talk, _n = _v13_block(wx - 40, wy - 128, sl["talk"], 17, 140, "v13 talk", "var(--c4)")
    g.append(f'<g opacity="0">{_v13_on(t2 + .02)}{waves}{talk}</g>')
    g.append(land(_woman(wx, wy, .9, SKIN_BROWN, "var(--accent)"), .25, .6, 30))
    room = "".join(_user(x, 804, 1.15, "var(--c2)") for x in (1110, 1215, 1320, 1425, 1520))
    g.append(land(f'<g opacity=".55">{_v13_lit(t2, .6)}{room}</g>', .3, .5, 12))
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 14 · Demo en vivo: el facilitador te entrega el skill
def _v13_zip(s=1.0):
    """The skill as a zip package, drawn around 0,0 (64 x 52 at s 1)."""
    return (f'<g transform="scale({s})"><rect x="-32" y="-26" width="64" height="52" rx="8" '
            f'fill="color-mix(in srgb, var(--c1) 50%, var(--card))" stroke="var(--c2)" stroke-width="1.6"/>'
            f'<path d="M0 -26 V26" stroke="var(--c4)" stroke-width="2" stroke-dasharray="3 3"/>'
            f'<rect x="-7" y="-4" width="14" height="16" rx="3" fill="var(--card)" stroke="var(--c4)" stroke-width="1.6"/></g>')


def _pv14_demo(sl, ctx):
    """v14 on the 900x1600 stage: the facilitator with the package (left) and his screen (right) on top, the three
    laptops as full-width rows under them, each with its attendee seen from behind. Same flights, checks and swap."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    g = [glow(zx + zw / 2, zy + 360, 520, "var(--brand)", .45)]
    hx, hy = zx + 80, zy + 150
    px, py = hx + 142, hy + 38
    g.append(land(_v13_host(hx, hy, 1.0, SKIN_LIGHT, "var(--c1)"), .1, .55, 30))
    pkg = (f'<g transform="translate({px} {py})"><g>{bob(0, -3, 3)}{_v13_zip(1.3)}</g></g>'
           + _v13_ping(px, py, 34, 80, "var(--c4)", .05) + _v13_ping(px, py, 34, 80, "var(--c4)", .09) + _v13_ping(px, py, 34, 80, "var(--c4)", .13))
    lx0 = px + 60
    s = fit(sl["package"], 24, zx + zw - lx0, "v14 package", floor=18)
    g.append(land(pkg + T(lx0, py + 4, sl["package"], s, "var(--white)", 'font-weight="700"')
                  + T(lx0, py + 38, sl["hand"], fit(sl["hand"], 21, zx + zw - lx0, "v14 hand", floor=18), "var(--muted)", W6), .3, .5, 10))
    # his screen, top right
    mw, mh = 440, 150
    mx, my = zx + zw - mw, zy + 4
    swap = .8
    a_txt, _n = _v13_block(mx + 22, my + 76, sl["screen_a"], 21, mw - 44, "v14 screen a")
    b_txt, _n = _v13_block(mx + 22, my + 90, sl["screen_b"], 26, mw - 44, "v14 screen b", "var(--c4)")
    mon = (card(mx, my, mw, mh, "var(--card)", "var(--c2)", 14, 1.4)
           + f'<path d="M{mx} {my + 40} H{mx + mw}" stroke="var(--line)" stroke-width="1.2"/>'
           + "".join(f'<circle cx="{mx + 20 + k * 18}" cy="{my + 20}" r="5" fill="var(--line)"/>' for k in range(3))
           + T(mx + mw - 18, my + 28, sl["screen"], fit(sl["screen"], 20, 260, "v14 screen", floor=18), "var(--muted)", f'text-anchor="end" {W6}')
           + f'<g>{beat("opacity", [(0, 1), (swap, 1), (swap + .02, 0), (_V13_END, 0), (.999, 1), (1, 1)])}{a_txt}</g>'
           + f'<g opacity="0">{_v13_on(swap)}{b_txt}</g>'
           + f'<rect x="{mx - 5}" y="{my - 5}" width="{mw + 10}" height="{mh + 10}" rx="18" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">'
           f'{beat("opacity", [(0, 0), (swap, 0), (swap + .01, 1), (swap + .08, 0), (1, 0)])}</rect>')
    g.append(land(mon, .2, .5, 10))
    # the laptops, one per row, each with its attendee seen from behind on the left
    lx, lw, lh, pitch = zx + 130, zw - 130, 168, 190
    ly0 = zy + zh - 3 * pitch + 6
    jackets = ("var(--accent)", "var(--c3)", "var(--c1)")
    skins = (SKIN_BROWN, SKIN_LIGHT, SKIN_BROWN)
    lap_parts, rides = [], []
    for k in range(3):
        ly = ly0 + k * pitch
        arrive = .07 + k * .04 + .1
        steps = (arrive + .01, .34 + k * .04, .5 + k * .04)
        ready = .64 + k * .03
        zxp, zyp = lx + 84, ly + 20
        lap = (card(lx, ly, lw, lh, "var(--card)", "var(--c2)", 12, 1.4)
               + f'<path d="M{lx} {ly + 40} H{lx + lw}" stroke="var(--line)" stroke-width="1.2"/>'
               + "".join(f'<circle cx="{lx + 18 + j * 16}" cy="{ly + 20}" r="4.5" fill="var(--line)"/>' for j in range(3))
               + f'<g opacity="0">{_v13_on(arrive)}<g transform="translate({zxp} {zyp})">{_v13_zip(.46)}</g></g>')
        y = ly + 72
        for txt, a in zip(sl["install"], steps):
            block, n = _v13_block(lx + 50, y, txt, 21, lw - 66, "v14 step")
            lap += _v13_tick(lx + 26, y - 7, a, ok, 12) + f'<g>{_v13_lit(a, .45)}{block}</g>'
            y += n * 26 + 10
        lap += (f'<g opacity="0">{_v13_on(ready)}' + pill(lx + lw - 110, ly + 20, sl["ready"], ok, ctx, 20, 200, "v14 ready", 14) + '</g>'
                + f'<rect x="{lx - 4}" y="{ly - 4}" width="{lw + 8}" height="{lh + 8}" rx="15" fill="none" stroke="{ok}" stroke-width="2" opacity="0">'
                f'{beat("opacity", [(0, 0), (ready, 0), (ready + .01, 1), (ready + .08, 0), (1, 0)])}</rect>')
        lap_parts.append(_v13_back(zx + 56, ly + lh - 40, .82, jackets[k], skin=skins[k]) + lap)
        d = f"M{px} {py + 34} C{px + 40} {py + 140} {zxp + 60} {zyp - 120} {zxp} {zyp}"
        rides.append(_v13_ride(d, arrive - .1, arrive, _v13_zip(.6)))
    g.append(seq(lap_parts, .45, .5, 16))
    g.extend(rides)
    return portrait_mark("".join(g)), D, FREEZE


@register("scene", "v14_demo")
def sc_v14_demo(sl, ctx):
    """The facilitator hands the skill over. He holds the package «dynamic-commercial-decks.zip»; a copy flies to each
    attendee's laptop. On every laptop the three install steps check in order (you get the zip; Claude, Settings,
    Capabilities, Skills; you ask for it by name) and each laptop shows «Skill listo». Then the facilitator's screen
    moves to the demo: «Elegimos un prospecto real». Frozen frame: every laptop «Skill listo», his screen on the demo."""
    if ORIENT() == "portrait":
        return _pv14_demo(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    g = [glow(1190, 440, 440, "var(--brand)", .45)]
    # the facilitator and the package in his hand
    hx, hy = 892, 300
    px, py = hx + 142, hy + 38
    g.append(land(_v13_host(hx, hy, 1.0, SKIN_LIGHT, "var(--c1)"), .1, .55, 30))
    pkg = (f'<g transform="translate({px} {py})"><g>{bob(0, -3, 3)}{_v13_zip(1.15)}</g></g>'
           + _v13_ping(px, py, 30, 70, "var(--c4)", .05) + _v13_ping(px, py, 30, 70, "var(--c4)", .09) + _v13_ping(px, py, 30, 70, "var(--c4)", .13))
    s = fit(sl["package"], 17, 290, "v14 package")
    g.append(land(pkg + T(px + 48, py + 6, sl["package"], s, "var(--white)", 'font-weight="700"')
                  + T(px + 48, py + 30, sl["hand"], fit(sl["hand"], 15, 290, "v14 hand"), "var(--muted)", W6), .3, .5, 10))
    # his screen: first the zip goes out, then the demo starts
    mx, my, mw, mh = 1262, 96, 290, 150
    swap = .8
    a_txt, _n = _v13_block(mx + 22, my + 64, sl["screen_a"], 17, mw - 44, "v14 screen a")
    b_txt, _n = _v13_block(mx + 22, my + 72, sl["screen_b"], 24, 210, "v14 screen b", "var(--c4)")
    mon = (card(mx, my, mw, mh, "var(--card)", "var(--c2)", 14, 1.4)
           + f'<path d="M{mx + mw / 2} {my + mh} V{my + mh + 26} M{mx + mw / 2 - 40} {my + mh + 26} H{mx + mw / 2 + 40}" stroke="var(--c2)" stroke-width="2" stroke-linecap="round"/>'
           + f'<path d="M{mx} {my + 34} H{mx + mw}" stroke="var(--line)" stroke-width="1.2"/>'
           + "".join(f'<circle cx="{mx + 18 + k * 16}" cy="{my + 17}" r="4.5" fill="var(--line)"/>' for k in range(3))
           + T(mx + mw - 16, my + 23, sl["screen"], fit(sl["screen"], 15, 170, "v14 screen"), "var(--muted)", f'text-anchor="end" {W6}')
           + f'<g>{beat("opacity", [(0, 1), (swap, 1), (swap + .02, 0), (_V13_END, 0), (.999, 1), (1, 1)])}{a_txt}</g>'
           + f'<g opacity="0">{_v13_on(swap)}{b_txt}</g>'
           + f'<rect x="{mx - 5}" y="{my - 5}" width="{mw + 10}" height="{mh + 10}" rx="18" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">'
           f'{beat("opacity", [(0, 0), (swap, 0), (swap + .01, 1), (swap + .08, 0), (1, 0)])}</rect>')
    g.append(land(mon, .2, .5, 10))
    # the laptops, each with its attendee seen from behind
    lw, ly, lh = 236, 486, 232
    xs = (826, 1072, 1318)
    jackets = ("var(--accent)", "var(--c3)", "var(--c1)")
    skins = (SKIN_BROWN, SKIN_LIGHT, SKIN_BROWN)
    lap_parts, rides = [], []
    for k, lx in enumerate(xs):
        arrive = .07 + k * .04 + .1
        steps = (arrive + .01, .34 + k * .04, .5 + k * .04)
        ready = .64 + k * .03
        lap = (card(lx, ly, lw, lh, "var(--card)", "var(--c2)", 12, 1.4)
               + f'<path d="M{lx - 8} {ly + lh + 14} L{lx + 6} {ly + lh} H{lx + lw - 6} L{lx + lw + 8} {ly + lh + 14} Z" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.2"/>'
               + f'<path d="M{lx} {ly + 34} H{lx + lw}" stroke="var(--line)" stroke-width="1.2"/>'
               + "".join(f'<circle cx="{lx + 18 + j * 15}" cy="{ly + 17}" r="4" fill="var(--line)"/>' for j in range(3))
               + f'<g opacity="0">{_v13_on(arrive)}<g transform="translate({lx + lw - 26} {ly + 17})">{_v13_zip(.36)}</g></g>')
        y = ly + 62
        for j, (txt, a) in enumerate(zip(sl["install"], steps)):
            block, n = _v13_block(lx + 40, y, txt, 15, lw - 52, "v14 step")
            lap += _v13_tick(lx + 22, y - 5, a, ok, 10) + f'<g>{_v13_lit(a, .45)}{block}</g>'
            y += n * 19 + 12
        lap += (f'<g opacity="0">{_v13_on(ready)}' + pill(lx + lw / 2, ly + lh - 26, sl["ready"], ok, ctx, 16, lw - 30, "v14 ready") + '</g>'
                + f'<rect x="{lx - 4}" y="{ly - 4}" width="{lw + 8}" height="{lh + 8}" rx="15" fill="none" stroke="{ok}" stroke-width="2" opacity="0">'
                f'{beat("opacity", [(0, 0), (ready, 0), (ready + .01, 1), (ready + .08, 0), (1, 0)])}</rect>')
        lap_parts.append(lap + _v13_back(lx + lw / 2, 792, .9, jackets[k], skin=skins[k]))
        # the copy of the package that flies from his hand to this laptop
        tx, ty = lx + lw - 26, ly + 17
        d = f"M{px} {py + 30} C{px} {py + 110} {tx} {ty - 90} {tx} {ty}"
        rides.append(_v13_ride(d, arrive - .1, arrive, _v13_zip(.5)))
    g.append(seq(lap_parts, .45, .5, 16))
    g.extend(rides)
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 15 · Le das contexto, confirmas hechos y apruebas títulos
def _v13_page(x, y, col="var(--c2)"):
    """A web page glyph whose top-left is (x, y), 26 x 22."""
    return (f'<g fill="none" stroke="{col}" stroke-width="1.4"><rect x="{x}" y="{y}" width="26" height="22" rx="3"/>'
            f'<path d="M{x} {y + 6} H{x + 26}"/><path d="M{x + 5} {y + 12} H{x + 20} M{x + 5} {y + 17} H{x + 15}"/></g>')


def _v13_note(x, y, col="var(--c2)"):
    """A note glyph (folded corner) whose top-left is (x, y), 22 x 26."""
    return (f'<g fill="none" stroke="{col}" stroke-width="1.4" stroke-linejoin="round"><path d="M{x} {y} H{x + 15} L{x + 22} {y + 7} V{y + 26} H{x} Z"/>'
            f'<path d="M{x + 5} {y + 12} H{x + 17} M{x + 5} {y + 18} H{x + 14}"/></g>')


def _pv15_envivo(sl, ctx):
    """v15 on the 900x1600 stage: the same live screen, full width; each stage's name heads its frame and the rail of
    numbered checks runs down the left edge. Same flows, checks, answers and stamp; same frozen frame."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    sx, sy, sw, sh = zx, zy + 6, zw, zh - 10
    g = [glow(sx + sw / 2, sy + 420, 520, "var(--brand)", .45)]
    head = (card(sx, sy, sw, sh, "var(--card)", "var(--c2)", 16, 1.4)
            + f'<path d="M{sx} {sy + 52} H{sx + sw}" stroke="var(--line)" stroke-width="1.2"/>'
            + f'<circle cx="{sx + 28}" cy="{sy + 26}" r="8" fill="var(--c5)">{blink(1.4)}</circle>'
            + T(sx + 50, sy + 34, sl["screen"], fit(sl["screen"], 22, sw - 110, "v15 screen", floor=18), "var(--white)", W6)
            + f'<g>{loop("opacity", ".4;1;.4", 3)}{spark(sx + sw - 30, sy + 26, .75, "var(--c4)")}</g>')
    g.append(land(head, .05, .45, 12))
    tops, hs = (sy + 70, sy + 312, sy + 650), (226, 322, 224)
    span = ((.03, .27), (.29, .61), (.63, .83))
    cx0, x0 = sx + 34, sx + 64                 # the rail and the left edge of each stage's frame
    x1, xr = x0 + 22, sx + sw - 18             # the content box of every stage
    rail = f"M{cx0} {tops[0] + 30} V{tops[2] + 30}"
    g.append(land(f'<path d="{rail}" stroke="var(--line)" stroke-width="2"/>'
                  f'<path d="{rail}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{ok}" stroke-width="2.5">'
                  f'{beat("stroke-dashoffset", [(0, 1), (span[0][1], 1), (span[1][1], .5), (span[1][1] + .02, .5), (span[2][1], 0), (_V13_END, 0), (1, 1)])}</path>',
                  .2, .4, 0))
    for k, (top, h, (a, b), name) in enumerate(zip(tops, hs, span, sl["phases"])):
        cy = top + 30
        col = (f'<circle cx="{cx0}" cy="{cy}" r="20" fill="var(--card)" stroke="var(--c2)" stroke-width="1.5"/>'
               + f'<g>{beat("opacity", [(0, 1), (b, 1), (b + .02, 0), (_V13_END, 0), (.999, 1), (1, 1)])}'
               + TC(cx0, cy + 7, str(k + 1), 20, "var(--white)", 'font-weight="700"') + '</g>'
               + f'<g opacity="0">{_v13_on(b)}<circle cx="{cx0}" cy="{cy}" r="20" fill="{ok}"/>{check(cx0, cy + 1, .95, "var(--ink)")}</g>'
               + _v13_ping(cx0, cy, 20, 46, ok, b))
        frame = (card(x0, top, xr - x0, h, "var(--dim)", "var(--line)", 14, 1.2)
                 + f'<rect x="{x0}" y="{top}" width="{xr - x0}" height="{h}" rx="14" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">'
                 f'{_v13_on(a, b)}</rect>'
                 + f'<g>{_v13_lit(a, .5)}' + T(x1, cy + 8, name, fit(name, 24, 300, "v15 stage", floor=20), "var(--white)", 'font-weight="700"') + '</g>')
        g.append(land(col + frame, .25 + k * .12, .45, 12))
    # 1 · Contexto
    t, cw = tops[0] + 60, 270
    src = []
    for j, (lab, glyph) in enumerate(zip(sl["sources"], (_v13_page, _v13_note))):
        yy = t + j * 80
        src.append(card(x1, yy, cw, 62, "var(--card)", "var(--c2)", 12, 1.2)
                   + f'<g transform="translate({x1 + 14} {yy + 14}) scale(1.3) translate({-(x1 + 14)} {-(yy + 14)})">{glyph(x1 + 14, yy + 14)}</g>'
                   + T(x1 + 58, yy + 38, lab, fit(lab, 21, cw - 68, "v15 source", floor=18), "var(--white)", W6))
    bw = 200
    bx = xr - 16 - bw
    kx, ky = (x1 + cw + bx) / 2, t + 71
    skill = (card(kx - 38, ky - 30, 76, 60, "var(--card)", "var(--accent)", 14, 1.4) + spark(kx, ky, .95, "var(--accent)")
             + f'<rect x="{kx - 44}" y="{ky - 36}" width="88" height="72" rx="18" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">'
             f'{beat("opacity", [(0, 0), (.1, 0), (.11, 1), (.16, 1), (.17, 0), (1, 0)])}</rect>')
    bins = []
    for j, lab in enumerate(sl["sorted"]):
        yy = t + j * 80
        items = "".join(f'<g opacity="0">{_v13_on(.18 + j * .03 + i * .02)}<rect x="{bx + 18 + i * 26}" y="{yy + 46}" width="20" height="6" rx="3" fill="{("var(--c4)", "var(--c2)")[j]}"/></g>'
                        for i in range(3))
        bins.append(card(bx, yy, bw, 62, "var(--card)", ("var(--c4)", "var(--c2)")[j], 12, 1.2)
                    + T(bx + 18, yy + 33, lab, fit(lab, 21, bw - 36, "v15 bin", floor=18), "var(--white)", W6) + items)
    flows = []
    for j in range(2):
        yy = t + 31 + j * 80
        d_in = f"M{x1 + cw} {yy} C{x1 + cw + 30} {yy} {kx - 70} {ky} {kx - 38} {ky}"
        d_out = f"M{kx + 38} {ky} C{kx + 70} {ky} {bx - 30} {yy} {bx} {yy}"
        flows.append(f'<path d="{d_in}" fill="none" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 6"/>'
                     f'<path d="{d_out}" fill="none" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 6"/>'
                     + _v13_ride(d_in, .04 + j * .02, .1 + j * .02, token("var(--c4)", 6))
                     + _v13_ride(d_out, .15 + j * .02, .21 + j * .02, token(("var(--c4)", "var(--c2)")[j], 6)))
    g.append(land("".join(flows) + "".join(src) + skill + "".join(bins), .5, .45, 10))
    # 2 · Confirmas: the facts on the left, the five questions on the right
    t = tops[1]
    fw = 300
    tab = (T(x1, t + 92, sl["known_head"], fit(sl["known_head"], 20, fw, "v15 known head", floor=18), "var(--muted)", W6)
           + f'<path d="M{x1} {t + 106} H{x1 + fw}" stroke="var(--line)" stroke-width="1.2"/>')
    for j, fact in enumerate(sl["known"]):
        yy = t + 150 + j * 60
        a = .32 + j * .04
        tab += (f'<g>{_v13_lit(a, .5)}' + T(x1, yy, fact, fit(fact, 21, fw - 44, "v15 fact", floor=18), "var(--white)", W6) + '</g>'
                + _v13_tick(x1 + fw - 14, yy - 7, a, ok, 13)
                + f'<path d="M{x1} {yy + 22} H{x1 + fw}" stroke="var(--line)" stroke-width="1" opacity=".6"/>')
    qx = x1 + fw + 24
    qw = xr - 16 - qx
    qs = T(qx, t + 34, sl["ask_head"], fit(sl["ask_head"], 20, qw, "v15 ask head", floor=18), "var(--c4)", W6)
    for j, q in enumerate(sl["questions"][:5]):
        yy = t + 56 + j * 52
        a = .45 + j * .03
        qs += (card(qx, yy, qw, 44, "var(--card)", "var(--line)", 10, 1.2)
               + f'<g>{_v13_lit(a, .5)}' + T(qx + 16, yy + 29, q, fit(q, 21, qw - 60, "v15 question", floor=18), "var(--white)", W6) + '</g>'
               + _v13_tick(qx + qw - 24, yy + 22, a, ok, 11))
    g.append(land(tab + qs, .7, .45, 10))
    # 3 · Títulos: the titles light one by one, the stamp lands
    t = tops[2]
    tl = ""
    for j, title in enumerate(sl["titles"][:3]):
        yy = t + 98 + j * 50
        a = .66 + j * .04
        tl += (f'<g>{_v13_lit(a, .3)}<rect x="{x1}" y="{yy - 21}" width="7" height="30" rx="3.5" fill="var(--c4)"/>'
               + T(x1 + 22, yy + 1, title, fit(title, 21, 440, "v15 title", floor=18), "var(--white)", W6) + '</g>')
    stx, sty = xr - 16 - 96, t + 64
    stamp = (f'<g transform="translate({stx} {sty}) rotate(-8)">'
             f'<g opacity="0">{_v13_on(.78)}<g><animateTransform attributeName="transform" type="scale" values="1.6;1.6;1;1" '
             f'keyTimes="0;.78;.8;1" dur="{D}s" repeatCount="indefinite"/>'
             f'<rect x="-92" y="-32" width="184" height="64" rx="12" fill="none" stroke="{ok}" stroke-width="2.5"/>'
             + pill(0, 0, sl["approved"], ok, ctx, 24, 168, "v15 stamp") + '</g></g></g>'
             + _v13_ping(stx, sty, 44, 116, ok, .8, .08))
    g.append(land(tl, .85, .45, 10) + stamp)
    return portrait_mark("".join(g)), D, FREEZE


@register("scene", "v15_envivo")
def sc_v15_envivo(sl, ctx):
    """Your screen during the live demo, three stages lighting in order. Contexto: the prospect's site and your notes
    flow into the skill, which sorts them into facts and hypotheses. Confirmas: the facts table gets a check per row and
    the skill asks at most five questions (the room, the pain, the decision, the proof, who signs), each answered in
    turn. Títulos: the titles light one by one and the stamp «Aprobado» lands. Frozen frame: the three stages checked,
    every fact confirmed, the five questions answered, the titles «Aprobado»."""
    if ORIENT() == "portrait":
        return _pv15_envivo(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    sx, sy, sw, sh = 836, 96, 718, 724
    g = [glow(1195, 450, 460, "var(--brand)", .45)]
    head = (card(sx, sy, sw, sh, "var(--card)", "var(--c2)", 16, 1.4)
            + f'<path d="M{sx} {sy + 44} H{sx + sw}" stroke="var(--line)" stroke-width="1.2"/>'
            + f'<circle cx="{sx + 24}" cy="{sy + 22}" r="7" fill="var(--c5)">{blink(1.4)}</circle>'
            + T(sx + 42, sy + 28, sl["screen"], fit(sl["screen"], 17, 420, "v15 screen"), "var(--white)", W6)
            + f'<g>{loop("opacity", ".4;1;.4", 3)}{spark(sx + sw - 26, sy + 22, .6, "var(--c4)")}</g>')
    g.append(land(head, .05, .45, 12))
    # the three stages: when each starts and when it is checked
    tops, hs = (sy + 60, sy + 246, sy + 520), (174, 262, 190)
    span = ((.03, .27), (.29, .61), (.63, .83))
    cx0, x1 = sx + 34, sx + 186            # the stage column and the start of each stage's content
    rail = f"M{cx0} {tops[0] + 30} V{tops[2] + 30}"
    g.append(land(f'<path d="{rail}" stroke="var(--line)" stroke-width="2"/>'
                  f'<path d="{rail}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{ok}" stroke-width="2">'
                  f'{beat("stroke-dashoffset", [(0, 1), (span[0][1], 1), (span[1][1], .5), (span[1][1] + .02, .5), (span[2][1], 0), (_V13_END, 0), (1, 1)])}</path>',
                  .2, .4, 0))
    for k, (top, h, (a, b), name) in enumerate(zip(tops, hs, span, sl["phases"])):
        cy = top + 30
        col = (f'<circle cx="{cx0}" cy="{cy}" r="17" fill="var(--card)" stroke="var(--c2)" stroke-width="1.5"/>'
               + f'<g>{beat("opacity", [(0, 1), (b, 1), (b + .02, 0), (_V13_END, 0), (.999, 1), (1, 1)])}'  # the number gives way to the check
               + TC(cx0, cy + 6, str(k + 1), 17, "var(--white)", 'font-weight="700"') + '</g>'
               + f'<g opacity="0">{_v13_on(b)}<circle cx="{cx0}" cy="{cy}" r="17" fill="{ok}"/>{check(cx0, cy + 1, .8, "var(--ink)")}</g>'
               + _v13_ping(cx0, cy, 17, 40, ok, b)
               + f'<g>{_v13_lit(a, .5)}' + T(cx0 + 28, cy + 7, name, fit(name, 19, x1 - cx0 - 36, "v15 stage"), "var(--white)", 'font-weight="700"') + '</g>')
        frame = (card(x1 - 12, top, sx + sw - 16 - x1 + 12, h, "var(--dim)", "var(--line)", 14, 1.2)
                 + f'<rect x="{x1 - 12}" y="{top}" width="{sx + sw - 16 - x1 + 12}" height="{h}" rx="14" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">'
                 f'{_v13_on(a, b)}</rect>')
        g.append(land(col + frame, .25 + k * .12, .45, 12))
    # 1 · Contexto: the prospect's site and your notes flow into the skill, which sorts facts from hypotheses
    t, cw = tops[0], 220
    src = []
    for j, (lab, glyph) in enumerate(zip(sl["sources"], (_v13_page, _v13_note))):
        yy = t + 26 + j * 70
        src.append(card(x1, yy, cw, 52, "var(--card)", "var(--c2)", 12, 1.2) + glyph(x1 + 14, yy + 14)
                   + T(x1 + 50, yy + 32, lab, fit(lab, 16, cw - 62, "v15 source"), "var(--white)", W6))
    kx, ky = x1 + 290, t + 88
    skill = (card(kx - 34, ky - 26, 68, 52, "var(--card)", "var(--accent)", 14, 1.4) + spark(kx, ky, .8, "var(--accent)")
             + f'<rect x="{kx - 40}" y="{ky - 32}" width="80" height="64" rx="18" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">'
             f'{beat("opacity", [(0, 0), (.1, 0), (.11, 1), (.16, 1), (.17, 0), (1, 0)])}</rect>')
    bx, bw = sx + sw - 30 - 150, 150
    bins = []
    for j, lab in enumerate(sl["sorted"]):
        yy = t + 26 + j * 70
        items = "".join(f'<g opacity="0">{_v13_on(.18 + j * .03 + i * .02)}<rect x="{bx + 16 + i * 22}" y="{yy + 38}" width="16" height="5" rx="2.5" fill="{("var(--c4)", "var(--c2)")[j]}"/></g>'
                        for i in range(3))
        bins.append(card(bx, yy, bw, 52, "var(--card)", ("var(--c4)", "var(--c2)")[j], 12, 1.2)
                    + T(bx + 16, yy + 28, lab, fit(lab, 16, bw - 32, "v15 bin"), "var(--white)", W6) + items)
    flows = []
    for j in range(2):
        yy = t + 52 + j * 70
        d_in = f"M{x1 + cw} {yy} C{x1 + cw + 40} {yy} {kx - 70} {ky} {kx - 34} {ky}"
        d_out = f"M{kx + 34} {ky} C{kx + 70} {ky} {bx - 40} {yy} {bx} {yy}"
        flows.append(f'<path d="{d_in}" fill="none" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 6"/>'
                     f'<path d="{d_out}" fill="none" stroke="var(--line)" stroke-width="1.5" stroke-dasharray="3 6"/>'
                     + _v13_ride(d_in, .04 + j * .02, .1 + j * .02, token("var(--c4)", 5))
                     + _v13_ride(d_out, .15 + j * .02, .21 + j * .02, token(("var(--c4)", "var(--c2)")[j], 5)))
    g.append(land("".join(src) + skill + "".join(bins), .5, .45, 10) + "".join(flows))
    # 2 · Confirmas: the facts table gets its checks, then at most five questions, each answered in turn
    t = tops[1]
    fw = 290
    tab = (T(x1, t + 30, sl["known_head"], 15, "var(--muted)", W6)
           + f'<path d="M{x1} {t + 42} H{x1 + fw}" stroke="var(--line)" stroke-width="1.2"/>')
    for j, fact in enumerate(sl["known"]):
        yy = t + 76 + j * 50
        a = .32 + j * .04
        tab += (f'<g>{_v13_lit(a, .5)}' + T(x1, yy, fact, fit(fact, 16, fw - 44, "v15 fact"), "var(--white)", W6) + '</g>'
                + _v13_tick(x1 + fw - 14, yy - 6, a, ok, 11)
                + f'<path d="M{x1} {yy + 18} H{x1 + fw}" stroke="var(--line)" stroke-width="1" opacity=".6"/>')
    qx, qw = x1 + fw + 26, sx + sw - 30 - (x1 + fw + 26)
    qs = T(qx, t + 30, sl["ask_head"], fit(sl["ask_head"], 15, qw, "v15 ask head"), "var(--c4)", W6)
    for j, q in enumerate(sl["questions"][:5]):
        yy = t + 48 + j * 41
        a = .45 + j * .03
        qs += (card(qx, yy, qw, 34, "var(--card)", "var(--line)", 10, 1.2)
               + f'<g>{_v13_lit(a, .5)}' + T(qx + 14, yy + 23, q, fit(q, 16, qw - 56, "v15 question"), "var(--white)", W6) + '</g>'
               + _v13_tick(qx + qw - 20, yy + 17, a, ok, 9))
    g.append(land(tab + qs, .7, .45, 10))
    # 3 · Títulos: the titles light one by one, you read them aloud, the stamp lands
    t = tops[2]
    tl = ""
    for j, title in enumerate(sl["titles"][:3]):
        yy = t + 48 + j * 50
        a = .66 + j * .04
        tl += (f'<g>{_v13_lit(a, .3)}<rect x="{x1}" y="{yy - 18}" width="6" height="26" rx="3" fill="var(--c4)"/>'
               + T(x1 + 20, yy + 1, title, fit(title, 17, 330, "v15 title"), "var(--white)", W6) + '</g>')
    stx, sty = sx + sw - 30 - 90, t + 100
    stamp = (f'<g transform="translate({stx} {sty}) rotate(-8)">'
             f'<g opacity="0">{_v13_on(.78)}<g><animateTransform attributeName="transform" type="scale" values="1.6;1.6;1;1" '
             f'keyTimes="0;.78;.8;1" dur="{D}s" repeatCount="indefinite"/>'
             f'<rect x="-86" y="-30" width="172" height="60" rx="12" fill="none" stroke="{ok}" stroke-width="2.5"/>'
             + pill(0, 0, sl["approved"], ok, ctx, 22, 156, "v15 stamp") + '</g></g></g>'
             + _v13_ping(stx, sty, 40, 110, ok, .8, .08))
    g.append(land(tl, .85, .45, 10) + stamp)
    return "".join(g), D, FREEZE
