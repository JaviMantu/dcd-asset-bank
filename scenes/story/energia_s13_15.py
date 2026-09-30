"""Group E of the energía deck: slide 13 (the next step), 14 (tomorrow's control room) and 15 (the optional open question).
Runs inside the shared ext namespace (module/ext.py), so every helper is at hand without imports. Every loop is one
12-second story timed with beat(); the reduced-motion frame (0.9 of the loop, 10.8 s) is its resolved state."""
from aula.svg import glow_fill as _n15_glow_fill


# ---------------------------------------------------------------- beats shared by the three scenes (fractions of D)
_N13_RESET = .965  # every story rewinds between 11.6 and 11.8 s, after the frozen frame


def _n13_on(a, b=_N13_RESET, f=.02, hi=1):
    """Hidden until a, shown from a + f until b, hidden again by b + f."""
    return beat("opacity", [(0, 0), (a, 0), (a + f, hi), (b, hi), (min(b + f, .999), 0), (1, 0)])


def _n13_off(a, b=_N13_RESET, f=.02):
    """Shown until a, hidden from a + f until b, shown again by b + f (a template that the story fills in)."""
    return beat("opacity", [(0, 1), (a, 1), (a + f, 0), (b, 0), (min(b + f, .999), 1), (1, 1)])


def _n13_lit(a, lo=.45, b=_N13_RESET, f=.02):
    """Dimmed until a, full from a + f until b."""
    return beat("opacity", [(0, lo), (a, lo), (a + f, 1), (b, 1), (min(b + f, .999), lo), (1, lo)])


def _n13_ride(path, a, b, r=6):
    """A token that rides path between a and b and is hidden otherwise: what one step hands to the next."""
    return (f'<g opacity="0">{beat("opacity", [(0, 0), (a, 0), (a + .004, 1), (b, 1), (b + .004, 0), (1, 0)])}'
            f'{move(path, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{token("var(--c4)", r)}</g>')


# ---------------------------------------------------------------- 13 · Empecemos con un discovery
@register("scene", "m13_discovery")
def sc_m13_discovery(sl, ctx):
    """The next step as one 12-second story along a time rail. Today (0-3 s) a frame weighs their options and settles on one
    pain. This week (3-6 s) the discovery workshop takes it, sees how to solve it with technology and agrees the KPI of the
    success case. A week later (6-9 s) the prototype comes alive: live data, the forecast crosses its limit, an early alert,
    the KPI on screen. Then (9-11.6 s) they decide, with a proposal fitted to them among the four ways to start.
    Frozen frame: the pain chosen, the workshop done, the prototype live and the proposal ready for their decision."""
    P = ORIENT() == "portrait"
    z15 = 17 if P else 15  # the 15-unit labels, larger where the portrait scale (x1.22) alone would leave them under 20
    ok = ctx.brand.c("dark.ok")
    cols = ("var(--c1)", "var(--c3)", "var(--c2)", "var(--accent)", "var(--c4)")
    y0, h = 420, 300
    X = ((96, 280), (416, 360), (816, 380), (1236, 268))
    (ax, aw), (bx, bw), (cx, cw), (dx, dw) = X
    opts = sl["cards"][:5]
    n, pick = len(opts), sl.get("pick", 0)
    t_pick, starts = .217, (0, .25, .5, .75)  # the frame settles at 2.6 s; the four steps start at 0, 3, 6 and 9 s

    # today: their options; a frame weighs each one, then settles on the pain they choose
    a = "".join(card(ax, y0 + k * 60, aw, 50, "var(--card)", col, 14, 1.5) + f'<circle cx="{ax + 26}" cy="{y0 + 25 + k * 60}" r="7" fill="{col}"/>'
                + T(ax + 44, y0 + 31 + k * 60, name, fit(name, 17, aw - 84, "m13 option"), "var(--white)", W6)
                for k, (name, col) in enumerate(zip(opts, cols)))
    yc = y0 + 25 + pick * 60
    chosen = (f'<g opacity="0">{_n13_on(t_pick)}<rect x="{ax}" y="{y0 + pick * 60}" width="{aw}" height="50" rx="14" fill="none" stroke="var(--c4)" stroke-width="2.5"/>'
              f'<circle cx="{ax + aw - 24}" cy="{yc}" r="11" fill="{ok}"/>' + check(ax + aw - 24, yc + 1, .55, "var(--ink)") + '</g>')
    order = [k for k in range(n) if k != pick] + [pick]
    hops = [.083 + i * (t_pick - .083) / (n - 1) for i in range(n)]  # 1.0 s, then every 0.4 s
    scan = (f'<rect x="{ax - 5}" y="{y0 - 5}" width="{aw + 10}" height="60" rx="17" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">'
            f'<animateTransform attributeName="transform" type="translate" values="0 {pick * 60};{";".join(f"0 {k * 60}" for k in order)}" '
            f'keyTimes="0;{";".join(f"{t:.3f}" for t in hops)}" dur="{D}s" repeatCount="indefinite" calcMode="discrete"/>'
            f'{beat("opacity", [(0, 0), (.08, 0), (.083, 1), (_N13_RESET, 1), (.985, 0), (1, 0)])}</rect>')

    # this week: the discovery workshop fills in the pain, how to solve it and the KPI, one check at a time
    wtitle, wrows = sl["workshop"]
    b = card(bx, y0, bw, h, "var(--card)", "var(--c2)", 18, 1.5) + pill(bx + bw / 2, y0 + 38, wtitle, "var(--c2)", ctx, 17, bw - 40, "m13 workshop")
    for j, (verb, text) in enumerate(wrows[:3]):
        y, t = y0 + 96 + j * 70, .3 + j * .067  # 3.6, 4.4 and 5.2 s
        room = bw - 84
        b += T(bx + 24, y, verb, z15, "var(--c4)", W6) + f'<circle cx="{bx + bw - 36}" cy="{y + 10}" r="13" fill="none" stroke="var(--line)" stroke-width="1.5"/>'
        if j == 0:  # the template line becomes the pain they chose
            b += (f'<g>{_n13_off(t)}' + T(bx + 24, y + 28, text, fit(text, 18, room, "m13 workshop row"), "var(--muted)", W6) + '</g>'
                  f'<g opacity="0">{_n13_on(t)}' + T(bx + 24, y + 28, opts[pick], fit(opts[pick], 18, room, "m13 workshop row"), "var(--white)", W6) + '</g>')
        else:
            b += f'<g>{_n13_lit(t, .6)}' + T(bx + 24, y + 28, text, fit(text, 18, room, "m13 workshop row"), "var(--white)", W6) + '</g>'
        b += f'<g opacity="0">{_n13_on(t)}<circle cx="{bx + bw - 36}" cy="{y + 10}" r="13" fill="{ok}"/>' + check(bx + bw - 36, y + 11, .6, "var(--ink)") + '</g>'

    # a week later: the prototype comes alive with live data, the forecast crosses its limit, an early alert, the KPI on screen
    live = .533
    c = (card(cx, y0, cw, h, "var(--card)", "var(--c3)", 18, 1.5) + f'<path d="M{cx} {y0 + 44} H{cx + cw}" stroke="var(--line)" stroke-width="1.5"/>'
         + "".join(f'<circle cx="{cx + 24 + k * 18}" cy="{y0 + 22}" r="5" fill="var(--line)"/>' for k in range(3))
         + f'<g opacity="0">{_n13_on(live)}' + "".join(f'<circle cx="{cx + 24 + k * 18}" cy="{y0 + 22}" r="5" fill="{col}"/>' for k, col in enumerate(("var(--c5)", "var(--c4)", ok))) + '</g>'
         + T(cx + 84, y0 + 28, sl["proto"], fit(sl["proto"], 17, cw - 200, "m13 prototype"), "var(--white)", W6)
         + f'<g opacity="0">{_n13_on(live)}' + pill(cx + cw - 64, y0 + 22, sl["live"], ok, ctx, z15, 110, "m13 live", 14) + '</g>')
    px, py, pw = cx + 16, y0 + 58, cw - 32
    c += (card(px, py, pw, 152, "var(--dim)", "var(--line)", 12, 1.2)
          + T(px + 16, py + 26, sl["chart"], fit(sl["chart"], z15, pw - 130, "m13 chart"), "var(--muted)", W6)
          + T(px + pw - 16, py + 26, sl["forecast"], fit(sl["forecast"], z15, 110, "m13 forecast"), "var(--c4)", 'text-anchor="end" font-weight="600"')
          + f'<path d="M{px + 16} {py + 62} H{px + pw - 16}" stroke="var(--c5)" stroke-width="1.2" stroke-dasharray="4 5" opacity=".85"/>')
    real = [(0, 122), (20, 114), (40, 124), (60, 110), (80, 118), (100, 104), (120, 110), (140, 98), (160, 92)]
    d = "M" + " L".join(f"{px + 16 + x} {py + y}" for x, y in real)
    ex, ey = px + 176, py + 92  # the live trace ends here; the forecast runs on to the right
    c += (f'<g opacity="0">{_n13_on(.63)}<path d="{d} L{ex} {py + 140} L{px + 16} {py + 140} Z" fill="var(--c3)" opacity=".14"/></g>'
          f'<path d="{d}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="0" fill="none" stroke="var(--c3)" stroke-width="2" stroke-linejoin="round">'
          f'{beat("stroke-dashoffset", [(0, 1), (.542, 1), (.642, 0), (_N13_RESET, 0), (.985, 1), (1, 1)])}</path>'
          f'<g opacity="0">{_n13_on(.542)}{move(d, [(0, 0), (.542, 0), (.642, 1), (1, 1)], D)}{token("var(--c4)", 5)}</g>'
          f'<g opacity="0">{_n13_on(.642)}<path d="M{ex} {ey} L{px + pw - 16} {py + 40}" fill="none" stroke="var(--c4)" stroke-width="1.8" stroke-dasharray="6 6"/></g>')
    hx = ex + (px + pw - 16 - ex) * (ey - 62 - py) / (ey - py - 40)  # where the forecast crosses the limit
    c += (f'<g opacity="0">{_n13_on(.683)}<circle cx="{hx:.1f}" cy="{py + 62}" r="9" fill="none" stroke="var(--c5)" stroke-width="1.5">{loop("r", "8;18;8", 2.4)}</circle>'
          + pill(px + pw - 88, py + 124, sl["alert"], "var(--c5)", ctx, z15, 172, "m13 alert", 14) + '</g>')
    ky = y0 + 230
    c += (card(px, ky, pw, 52, "none", "var(--line)", 12, 1.5, 'stroke-dasharray="6 6"')
          + f'<g opacity="0">{_n13_on(.6)}' + card(px, ky, pw, 52, "var(--dim)", ok, 12, 1.5)
          + T(px + 16, ky + 32, sl["kpi"], fit(sl["kpi"], 16, pw - 70, "m13 kpi"), "var(--white)", W6)
          + f'<circle cx="{px + pw - 26}" cy="{ky + 26}" r="12" fill="{ok}"/>' + check(px + pw - 26, ky + 27, .55, "var(--ink)") + '</g>')

    # the boot: a warm light behind the window and one scan line down its body as it goes live
    boot = (f'<g opacity="0">{beat("opacity", [(0, 0), (live, 0), (live + .03, 1), (.6, .45), (_N13_RESET, .45), (.985, 0), (1, 0)])}'
            + glow(cx + cw / 2, y0 + h / 2, 170 if P else 300, "var(--c3)", .5) + '</g>')
    c += (f'<rect x="{cx + 2}" y="{y0 + 46}" width="{cw - 4}" height="2" fill="var(--c3)" opacity="0">'
          f'{beat("opacity", [(0, 0), (live, 0), (live + .004, .8), (.585, .8), (.59, 0), (1, 0)])}'
          f'<animateTransform attributeName="transform" type="translate" values="0 0;0 0;0 {h - 50};0 {h - 50}" keyTimes="0;{live};.585;1" dur="{D}s" repeatCount="indefinite"/></rect>')

    # then: their call, with a proposal fitted to them among the four ways to start
    ask_, ways = sl["offer"]
    dd = card(dx, y0, dw, h, "var(--card)", ok, 18, 1.5) + T(dx + 22, y0 + 48, ask_, fit(ask_, 20, dw - 44, "m13 offer"), "var(--white)", W6)
    for j, way in enumerate(ways[:4]):
        y, t = y0 + 92 + j * 38, .783 + j * .025  # 9.4, 9.7, 10.0 and 10.3 s
        dd += (f'<circle cx="{dx + 30}" cy="{y}" r="6" fill="none" stroke="var(--line)" stroke-width="1.5"/>'
               f'<g opacity="0">{_n13_on(t)}<circle cx="{dx + 30}" cy="{y}" r="6" fill="{ok}"/></g>'
               f'<g>{_n13_lit(t)}' + T(dx + 46, y + 6, way, fit(way, 17, dw - 70, "m13 way"), "var(--white)", W6) + '</g>')
    s = fit(sl["decide"], 16, dw - 60, "m13 decision")
    qw = min(dw - 24, bold_width(_(str(sl["decide"])), s, current_factor()) + 36)
    dd += (f'<g>{_n13_off(.875)}' + card(dx + (dw - qw) / 2, y0 + 244, qw, s + 20, "none", "var(--line)", (s + 20) / 2, 1.5, 'stroke-dasharray="5 5"') + '</g>'
           + f'<g opacity="0">{_n13_on(.875)}' + pill(dx + dw / 2, y0 + 244 + (s + 20) / 2, sl["decide"], ok, ctx, 16, dw - 24, "m13 decision") + '</g>')

    # the step on stage lights up; what each step produces rides to the next one
    fstep = [f'<rect x="{x - 6}" y="{y0 - 6}" width="{w + 12}" height="{h + 12}" rx="22" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity="0">'
          f'{_n13_on(t0 + .01, (t1 if t1 < 1 else _N13_RESET) - .01, .02, .75)}</rect>'
          for (x, w), t0, t1 in zip(X[1:], starts[1:], starts[2:] + (1,))]
    frames = "".join(fstep)
    ya = y0 + 150
    link1 = f"M{ax + aw + 4} {yc} C{ax + aw + 26} {yc} {bx - 26} {ya} {bx - 8} {ya}"
    arrows = (f'<g opacity="0">{_n13_on(t_pick)}<path d="{link1}" fill="none" stroke="var(--c2)" stroke-width="2" stroke-dasharray="4 7">{loop("stroke-dashoffset", "0;-22", 1.6)}</path></g>'
              + "".join(f'<path d="M{x0 + 8} {ya} H{x1 - 10}" stroke="var(--c2)" stroke-width="2" stroke-dasharray="4 7">{loop("stroke-dashoffset", "0;-22", 1.6)}</path>'
                        for x0, x1 in ((bx + bw, cx), (cx + cw, dx)))
              + "".join(f'<path d="M{x1 - 14} {ya - 7} L{x1 - 5} {ya} L{x1 - 14} {ya + 7}" fill="none" stroke="var(--c2)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
                        for x1 in (bx, cx, dx)))
    rides = (_n13_ride(link1, .222, .283) + _n13_ride(f"M{bx + bw} {ya} H{cx - 6}", .483, .525)
             + _n13_ride(f"M{cx + cw} {ya} H{dx - 6}", .733, .775))

    # the time rail: today, this week, a week later, then their call
    yr = y0 + h + 34
    xm = [x + w / 2 for x, w in X]
    fr = [(m - xm[0]) / (xm[-1] - xm[0]) for m in xm]
    reach = (0, .292, .542, .792)
    rail = (f'<path d="M{xm[0]} {yr} H{xm[-1]}" stroke="var(--line)" stroke-width="2"/>'
            f'<path d="M{xm[0]} {yr} H{xm[-1]}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="0" fill="none" stroke="var(--c4)" stroke-width="2">'
            + beat("stroke-dashoffset", [(0, 1), (.25, 1), (reach[1], 1 - fr[1]), (.5, 1 - fr[1]), (reach[2], 1 - fr[2]), (.75, 1 - fr[2]), (reach[3], 0),
                                         (_N13_RESET, 0), (.985, 1), (1, 1)]) + '</path>')
    for k, (m, t, (x, w)) in enumerate(zip(xm, sl["when"], X)):
        rail += f'<circle cx="{m}" cy="{yr}" r="7" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>'
        rail += f'<circle cx="{m}" cy="{yr}" r="3.5" fill="var(--c4)"/>' if not k else f'<g opacity="0">{_n13_on(reach[k])}<circle cx="{m}" cy="{yr}" r="3.5" fill="var(--c4)"/></g>'
        lab = TC(m, yr + 36, t, fit(t, 17, w, "m13 when"), "var(--c4)", W6)
        rail += lab if not k else f'<g>{_n13_lit(reach[k], .5)}{lab}</g>'
    now = (f'<g>{move(f"M{xm[0]} {yr} H{xm[-1]}", [(0, 0), (.25, 0), (reach[1], fr[1]), (.5, fr[1]), (reach[2], fr[2]), (.75, fr[2]), (reach[3], 1), (_N13_RESET, 1), (.985, 0), (1, 0)], D)}'
           + token("var(--c4)", 7) + '</g>')
    if P:
        return _m13_portrait(sl, a, b, c, dd, boot, chosen + scan, fstep, X, y0, h, yc, ya, t_pick, reach), D, FREEZE
    return (glow(800, 580, 560, "var(--brand)", .4) + boot + seq([a, b, c, dd], .1, .5, 18) + land(arrows + chosen + scan + frames, .9, .4, 0)
            + rides + land(rail + now, .7, .45, 0)), D, FREEZE


def _m13_portrait(sl, a, b, c, dd, boot, pick, fstep, X, y0, h, yc, ya, t_pick, reach):
    """discovery in portrait: the four steps as a 2x2 read row by row (today, this week / a week later, their call),
    each drawn as on desktop and scaled (x1.24 and x1.22: the 17-unit labels land at 21), a time rail under each row
    and the hand-offs between the steps. a, b, c, dd: the desktop steps; pick: the choosing frame of today; fstep: the
    frames that light the steps on stage (b, c, d); reach: when the rail reaches each step."""
    zx, zy, zw, zh = ART_ZONE("top")
    (ax, aw), (bx, bw), (cx, cw), (dx, dw) = X
    gp = 28
    s1, s2 = (zw - gp) / (aw + bw), (zw - gp) / (cw + dw)
    Y1 = zy
    Y2 = Y1 + h * s1 + 78
    place = ((zx, Y1, s1), (zx + aw * s1 + gp, Y1, s1), (zx, Y2, s2), (zx + cw * s2 + gp, Y2, s2))

    def at(k, x, y):  # a desktop point of step k, on the portrait canvas
        px_, py_, sk = place[k]
        return px_ + (x - X[k][0]) * sk, py_ + (y - y0) * sk

    def put(k, inner):
        px_, py_, sk = place[k]
        return _pz(inner, sk, px_, py_, X[k][0], y0)

    def chev(x, y, down=False):
        d = f"M{x - 8:.1f} {y - 9:.1f} L{x:.1f} {y:.1f} L{x + 8:.1f} {y - 9:.1f}" if down else f"M{x - 9:.1f} {y - 8:.1f} L{x:.1f} {y:.1f} L{x - 9:.1f} {y + 8:.1f}"
        return f'<path d="{d}" fill="none" stroke="var(--c2)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'

    # the hand-offs: the chosen pain to the workshop, the workshop down to the prototype, the prototype to their call
    (p1x, p1y), (p2x, p2y) = at(0, ax + aw + 4, yc), at(1, bx - 4, ya)
    link1 = f"M{p1x:.1f} {p1y:.1f} C{p1x + 16:.1f} {p1y:.1f} {p2x - 16:.1f} {p2y:.1f} {p2x - 6:.1f} {p2y:.1f}"
    vx = at(1, bx + 22, 0)[0]
    vy0, vy1 = at(1, 0, y0 + h)[1] + 6, at(2, 0, y0)[1] - 6
    down = f"M{vx:.1f} {vy0:.1f} V{vy1 - 4:.1f}"
    (q1x, qy), q2x = at(2, cx + cw, ya), at(3, dx, ya)[0]
    across = f"M{q1x + 6:.1f} {qy:.1f} H{q2x - 8:.1f}"
    dash = lambda d: f'<path d="{d}" fill="none" stroke="var(--c2)" stroke-width="2.4" stroke-dasharray="4 7">{loop("stroke-dashoffset", "0;-22", 1.6)}</path>'
    arrows = (f'<g opacity="0">{_n13_on(t_pick)}{dash(link1)}</g>' + dash(down) + dash(across)
              + chev(p2x - 4, p2y) + chev(vx, vy1, True) + chev(q2x - 4, qy))
    rides = _n13_ride(link1, .222, .283, 7) + _n13_ride(down, .483, .525, 7) + _n13_ride(across, .733, .775, 7)

    # the time rail, one per row: today and this week, then a week later and their call
    xm = [at(k, x + w / 2, 0)[0] for k, (x, w) in enumerate(X)]
    ry = (at(1, 0, y0 + h)[1] + 24, at(3, 0, y0 + h)[1] + 24)
    rows = ((0, 1, .25), (2, 3, .75))
    rail, now = "", ""
    for r, (k0, k1, t0) in enumerate(rows):
        d = f"M{xm[k0]:.1f} {ry[r]:.1f} H{xm[k1]:.1f}"
        rail += (f'<path d="{d}" stroke="var(--line)" stroke-width="2.4"/>'
                 f'<path d="{d}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="0" fill="none" stroke="var(--c4)" stroke-width="2.4">'
                 + beat("stroke-dashoffset", [(0, 1), (t0, 1), (reach[k1], 0), (_N13_RESET, 0), (.985, 1), (1, 1)]) + '</path>')
        op = [(0, 1), (.5, 1), (.51, 0), (.97, 0), (.985, 1), (1, 1)] if not r else [(0, 0), (reach[2], 0), (reach[2] + .01, 1), (_N13_RESET, 1), (.985, 0), (1, 0)]
        mv = [(0, 0), (t0, 0), (reach[k1], 1), (.93, 1), (.96, 0), (1, 0)] if not r else [(0, 0), (t0, 0), (reach[k1], 1), (1, 1)]
        now += f'<g opacity="{r}">{beat("opacity", op)}{move(d, mv, D)}{token("var(--c4)", 8)}</g>'  # static: the 10.8 s pose'
    for k, t in enumerate(sl["when"][:4]):
        y = ry[k // 2]
        rail += f'<circle cx="{xm[k]:.1f}" cy="{y:.1f}" r="8" fill="var(--card)" stroke="var(--c4)" stroke-width="1.8"/>'
        dot = f'<circle cx="{xm[k]:.1f}" cy="{y:.1f}" r="4" fill="var(--c4)"/>'
        rail += dot if not k else f'<g opacity="0">{_n13_on(reach[k])}{dot}</g>'
        lab = TC(f"{xm[k]:.1f}", f"{y + 34:.1f}", t, fit(t, 21, X[k][1] * place[k][2], "m13 when", floor=18), "var(--c4)", W6)
        now += lab if not k else f'<g>{_n13_lit(reach[k], .5)}{lab}</g>'  # labels last, over the rail and its token
    steps = seq([put(0, a), put(1, b), put(2, boot + c), put(3, dd)], .1, .5, 18)
    marks = put(0, pick) + "".join(put(k, f) for k, f in zip((1, 2, 3), fstep))
    return _pz_clip(steps + land(arrows + marks, .9, .4, 0) + rides + land(rail + now, .7, .45, 0), "pz-m13")


# ---------------------------------------------------------------- 15 · ¿Dónde están hoy? (optional)
@register("scene", "m15_chain")
def sc_m15_chain(sl, ctx):
    """«¿Dónde están hoy?», one chain of four layers, each with the question that places the client in it. The loop asks
    layer by layer: a pulse walks the chain and the «?» lights each layer and its question in turn (0-9.6 s); then the whole
    chain lights up at once while the field, retyped at every turn, waits for their answer. The presenter taps the layer they
    name (module/deck.js): the ring and «Hoy» mark it, the ambient loop stops (data-hop) and the field fills with their
    answer and «empezamos por ahí». Frozen frame: the whole chain lit and the field waiting, cursor blinking."""
    P = ORIENT() == "portrait"
    ok = ctx.brand.c("dark.ok")
    cols = ("var(--c4)", "var(--c2)", "var(--c3)", "var(--accent)")
    n, gap, y0, h = len(sl["layers"]), 20, 444, 290
    w = (1408 - gap * (n - 1)) / n
    xs = [96 + k * (w + gap) for k in range(n)]
    step, whole = .8 / n, .8  # each layer holds the question 2.4 s; from 9.6 s the chain lights as one
    g = [glow(800, 600, 600, "var(--brand)", .45),
         land(card(96, 388, 1408, 40, "var(--dim)", "var(--line)", 20, 1.2)
              + TC(800, 414, sl["base"], fit(sl["base"], 15, 1320, "chain base"), "var(--muted)", W6), .1, .45, 0)]
    asks, picks, chevs = [], [], []
    for k, (x, (name, question, items), col) in enumerate(zip(xs, sl["layers"], cols)):
        c = (card(x, y0, w, h, "var(--card)", "var(--line)", 16, 1.2) + f'<rect x="{x:.1f}" y="{y0}" width="{w:.1f}" height="4" rx="2" fill="{col}"/>'
             + T(x + 18, y0 + 40, f"0{k + 1}", 18, "var(--c4)", W6) + T(x + 56, y0 + 40, name, fit(name, 18, w - 76, "chain layer"), "var(--white)", W6)
             + TCW(x + 18, y0 + 78, question, 34, 16, "var(--muted)", 'font-weight="600" font-style="italic"', 1.3, "start"))
        for j, it in enumerate(items[:3]):
            yy = y0 + 150 + j * 44
            c += f'<path d="M{x + 18:.1f} {yy} H{x + w - 18:.1f}" stroke="var(--line)" stroke-width="1"/>' + T(x + 18, yy + 30, it, fit(it, 16, w - 36, "chain item"), "var(--white)", W6)
        # marked by the presenter's tap (deck.css shows .pick-ring on .picked): the ring breathes and «Hoy» names it
        c += (f'<g class="pick-ring"><rect x="{x - 4:.1f}" y="{y0 - 4}" width="{w + 8:.1f}" height="{h + 8}" rx="20" fill="none" stroke="var(--c4)" stroke-width="3"/>'
              f'<rect x="{x - 10:.1f}" y="{y0 - 10}" width="{w + 20:.1f}" height="{h + 20}" rx="26" fill="none" stroke="var(--c4)" stroke-width="1.5">'
              f'{loop("stroke-opacity", ".05;.6;.05", 2.4)}</rect>'
              + pill(x + w - 50, y0 + 34, sl["today"], "var(--c4)", ctx, 17 if P else 15, 90, "chain today", 14) + '</g>')
        c += f'<rect x="{x:.1f}" y="{y0}" width="{w:.1f}" height="{h}" rx="16" fill="var(--ink)" opacity="0"/>'
        picks.append(f'<g data-pick="{k}">{c}</g>')
        g.append(land(picks[-1], .2 + k * .12, .5, 18))
        if k:
            chevs.append(f'<path d="M{x - 14:.1f} {y0 + 30} L{x - 6:.1f} {y0 + 36} L{x - 14:.1f} {y0 + 42}" fill="none" stroke="var(--c4)" stroke-width="1.8" stroke-linecap="round"/>')
            g.append(land(chevs[-1], .8, .4, 0))
        # the ambient ask: this layer holds the question for its turn, then the whole chain lights as one
        a0, a1, last = k * step, (k + 1) * step, k == n - 1
        on = ([(0, 1)] if not k else [(0, 0), (a0, 0), (a0 + .015, 1)]) + [(a1 - .015, 1), (a1, .7 if last else 0)]
        on += ([] if last else [(whole, 0)]) + [(whole + .02, .7), (_N13_RESET, .7), (.985, 0 if k else 1), (1, 0 if k else 1)]
        asks.append(f'<g>{beat("opacity", on)}'
                    f'<rect x="{x:.1f}" y="{y0}" width="{w:.1f}" height="{h}" rx="16" fill="none" stroke="{col}" stroke-width="1.5"/>'
                    f'<rect x="{x + 6:.1f}" y="{y0 + 60}" width="3" height="46" rx="1.5" fill="{col}"/>'
                    f'<rect x="{x + 12:.1f}" y="{y0 - 3}" width="{w - 24:.1f}" height="10" rx="5" fill="{col}" opacity=".35"/></g>')
    # the «?» visits each layer in its turn and leaves while the chain lights as one; a pulse walks the chain with it
    qs = [(x + w - 34, y0 + 34) for x in xs]
    hop = (f'<g><animateTransform attributeName="transform" type="translate" values="{";".join(f"{x - qs[0][0]:.1f} 0" for x, _ in qs)}" '
           f'keyTimes="{";".join(f"{k * step:.3f}" for k in range(n))}" dur="{D}s" repeatCount="indefinite" calcMode="discrete"/>'
           + beat("opacity", [(0, 1), (whole - .01, 1), (whole, 0), (.995, 0), (1, 1)])
           + f'<circle cx="{qs[0][0]:.1f}" cy="{qs[0][1]}" r="16" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5">{loop("r", "16;20;16", 2.4)}</circle>'
           + TC(f"{qs[0][0]:.1f}", qs[0][1] + 6, "?", 18, "var(--c4)", W6) + '</g>')
    pulse = (f'<g>{move(f"M96 {y0 + 2} H1504", [(0, 0), (whole, 1), (1, 1)], D)}'
             + beat("opacity", [(0, 1), (whole - .02, 1), (whole, 0), (.995, 0), (1, 1)]) + token("var(--c4)", 5) + '</g>')
    g.append(land(f'<g data-hop="">{"".join(asks)}{hop}{pulse}</g>', 1.2, .4, 0))
    if P:  # portrait: the layers in a 2x2 (scaled x1.19), the field under them at the art zone's width
        return _m15_portrait(sl, ctx, picks, asks, xs, w, y0, h, step, whole), D, FREEZE
    return "".join(g) + _m15_field(sl, ctx, 360, 752, 880, 22, 15, 200, 560), D, FREEZE


def _m15_field(sl, ctx, fx, fy, fw_, zph, zs, room, aroom):
    """The field of m15_chain: «Hoy estamos en…» types itself at every turn and waits; a light sweeps it. The tap fills it
    with their answer. (fx, fy, fw_): its box (60 high); zph: the placeholder and answer size; zs, room: the hint's
    (and «empezamos por ahí»); aroom: the answer's room."""
    ok = ctx.brand.c("dark.ok")
    fh = 60
    ph = sl["placeholder"]
    tw = bold_width(_(str(ph)), zph, current_factor())
    type_ = [(0, 0), (.1, 0), (.2, 1), (_N13_RESET, 1), (.985, 0), (1, 0)]
    clip = (f'<clipPath id="n15-type"><rect x="{fx + 60}" y="{fy}" width="{tw + 8:.1f}" height="{fh}">'
            f'{beat("width", [(t, f"{v * (tw + 8):.1f}") for t, v in type_])}</rect></clipPath>'
            f'<clipPath id="n15-field"><rect x="{fx}" y="{fy}" width="{fw_}" height="{fh}" rx="30"/></clipPath>')
    sweep = (f'<linearGradient id="n15-sweep" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="var(--c4)" stop-opacity="0"/>'
             f'<stop offset=".5" stop-color="var(--c4)" stop-opacity=".28"/><stop offset="1" stop-color="var(--c4)" stop-opacity="0"/></linearGradient>'
             f'<g clip-path="url(#n15-field)"><rect x="{fx - 140}" y="{fy - 20}" width="140" height="{fh + 40}" fill="url(#n15-sweep)" transform="skewX(-20)">'
             f'<animateTransform attributeName="transform" type="translate" additive="sum" values="0 0;0 0;{fw_ + 420} 0;{fw_ + 420} 0" keyTimes="0;.22;.42;1" dur="{D}s" repeatCount="indefinite"/></rect></g>')
    cur = (f'<rect x="{fx + 64}" y="{fy + 16}" width="3" height="28" fill="var(--c4)">'
           f'{beat("x", [(t, f"{fx + 64 + v * (tw + 8):.1f}") for t, v in type_])}'
           f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.2s" repeatCount="indefinite" calcMode="discrete"/></rect>')  # on at 10.8 s
    sparkle = f'<g>{spark(fx + 36, fy + 30, .6, "var(--c4)")}<animateTransform attributeName="transform" type="rotate" values="0 {fx + 36} {fy + 30};90 {fx + 36} {fy + 30};90 {fx + 36} {fy + 30}" keyTimes="0;.15;1" dur="4s" repeatCount="indefinite" calcMode="spline" keySplines=".4 0 .2 1;0 0 1 1"/></g>'
    nx = fx + fw_ - 28
    field = (clip + card(fx, fy, fw_, fh, "var(--card)", "var(--c4)", 30, 1.5) + sweep
             + f'<rect x="{fx}" y="{fy}" width="{fw_}" height="{fh}" rx="30" fill="none" stroke="var(--c4)" stroke-width="4" opacity=".5">{loop("stroke-opacity", ".1;.8;.1", 3)}</rect>'
             + sparkle
             + '<g data-placeholder="">' + f'<g clip-path="url(#n15-type)">' + T(fx + 64, fy + 38, ph, zph, "var(--muted)", W6) + '</g>' + cur
             + T(nx, fy + 37, sl["hint"], fit(sl["hint"], zs, room, "chain hint"), "var(--c4)", 'text-anchor="end" font-weight="600"') + '</g>'
             + "".join(f'<g data-answer="{k}" opacity="0" style="transition:opacity .45s">'
                       + spark(fx + 36, fy + 30, .6, ok)
                       + T(fx + 64, fy + 38, ans, fit(ans, zph, aroom, "chain answer"), "var(--white)", W6)
                       + f'<circle cx="{nx - 8}" cy="{fy + 30}" r="12" fill="{ok}"/>' + check(nx - 8, fy + 31, .55, "var(--ink)")
                       + T(nx - 30, fy + 37, sl["next"], fit(sl["next"], zs, room, "chain next"), ok, 'text-anchor="end" font-weight="600"') + '</g>'
                       for k, ans in enumerate(sl["answers"])))
    return land(field, 1.0, .5, 14)


def _m15_portrait(sl, ctx, picks, asks, xs, w, y0, h, step, whole):
    """chain-tap in portrait: the base bar, the four layers in a 2x2 read row by row (each drawn as on desktop and scaled
    x1.19: items 16 -> 19 units, «Hoy» 17 -> 20), the «?» and the pulse walking the rows, and the field under them. The
    taps work as on desktop: every layer is still a [data-pick] with its [data-answer] in the field."""
    zx, zy, zw, zh = ART_ZONE("top")
    n, gap = len(picks), 20
    s = (zw - gap) / 2 / w
    cw, ch = w * s, h * s
    by = zy + 4
    Y = (by + 60, by + 60 + ch + 18)
    pos = [(zx + (k % 2) * (cw + gap), Y[k // 2]) for k in range(n)]
    put = lambda k, inner: _pz(inner, s, pos[k][0], pos[k][1], xs[k], y0)
    g = [land(card(zx, by, zw, 48, "var(--dim)", "var(--line)", 24, 1.2)
              + TC(f"{zx + zw / 2:.1f}", f"{by + 31:.1f}", sl["base"], fit(sl["base"], 20, zw - 40, "chain base", floor=18), "var(--muted)", W6), .1, .45, 0)]
    for k in range(n):
        g.append(land(put(k, picks[k]), .2 + k * .12, .5, 18))
        if k % 2:  # the chain reads left to right in each row
            x, y = pos[k][0] - gap / 2 + 4, pos[k][1] + 36 * s
            g.append(land(f'<path d="M{x - 5:.1f} {y - 8:.1f} L{x + 3:.1f} {y:.1f} L{x - 5:.1f} {y + 8:.1f}" fill="none" stroke="var(--c4)" stroke-width="2.2" stroke-linecap="round"/>', .8, .4, 0))
    qs = [(px_ + cw - 34 * s, py_ + 34 * s) for px_, py_ in pos]
    hop = (f'<g><animateTransform attributeName="transform" type="translate" values="{";".join(f"{x - qs[0][0]:.1f} {y - qs[0][1]:.1f}" for x, y in qs)}" '
           f'keyTimes="{";".join(f"{k * step:.3f}" for k in range(n))}" dur="{D}s" repeatCount="indefinite" calcMode="discrete"/>'
           + beat("opacity", [(0, 1), (whole - .01, 1), (whole, 0), (.995, 0), (1, 1)])
           + f'<circle cx="{qs[0][0]:.1f}" cy="{qs[0][1]:.1f}" r="19" fill="var(--card)" stroke="var(--c4)" stroke-width="1.8">{loop("r", "19;23;19", 2.4)}</circle>'
           + TC(f"{qs[0][0]:.1f}", f"{qs[0][1] + 7:.1f}", "?", 21, "var(--c4)", W6) + '</g>')
    walk = "".join(f"M{zx:.1f} {y + 2:.1f} H{zx + zw:.1f} " for y in Y).strip()  # one row after the other
    pulse = (f'<g>{move(walk, [(0, 0), (whole, 1), (1, 1)], D)}'
             + beat("opacity", [(0, 1), (whole - .02, 1), (whole, 0), (.995, 0), (1, 1)]) + token("var(--c4)", 6) + '</g>')
    g.append(land(f'<g data-hop="">{"".join(put(k, a) for k, a in enumerate(asks))}{hop}{pulse}</g>', 1.2, .4, 0))
    g.append(_m15_field(sl, ctx, zx, Y[1] + ch + 16, zw, 24, 20, 230, 440))
    return _pz_clip("".join(g), "pz-m15")


# ---------------------------------------------------------------- 14 · Una operación que anticipa desviaciones
_N14_RIM = 'fill="none" stroke="var(--c2)" stroke-width="1.2" opacity=".6"'


def _n14_woman(x, y, s, skin, jacket):
    """Faceless, seen from behind at three quarters, turned up-right to the wall screen and pointing at it: long hair,
    earring, a thin rim of screen light on the side that faces it. (x, y) is the base of her neck."""
    arm = (f'<path d="M48 38 L88 -4 L112 -56" fill="none" stroke="{jacket}" stroke-width="17" stroke-linecap="round" stroke-linejoin="round"/>'
           f'<path d="M58 30 L92 -6 L114 -52" {_N14_RIM}/>'
           f'<circle cx="114" cy="-62" r="8.5" fill="{skin}"/><path d="M117 -68 L124 -84" stroke="{skin}" stroke-width="4.5" stroke-linecap="round"/>')
    body = (f'<path d="M-76 160 C-78 100 -70 54 -46 36 C-32 26 -16 22 0 22 C18 22 36 26 50 36 C72 52 80 100 80 160 Z" fill="{jacket}"/>'
            f'<path d="M-76 160 C-78 100 -70 54 -46 36 C-40 32 -34 29 -28 27 C-44 54 -50 104 -48 160 Z" fill="{shade(jacket, 20)}"/>'
            f'<path d="M22 23 C38 27 52 36 60 46 C74 64 80 104 80 160" {_N14_RIM}/>'
            f'<path d="M-12 -8 L12 -8 L14 24 L-14 24 Z" fill="{shade(skin, 22)}"/>'
            f'<g transform="rotate(-8 4 -36)"><ellipse cx="4" cy="-36" rx="26" ry="31" fill="{skin}"/>'
            f'<ellipse cx="24" cy="-33" rx="4.5" ry="7.5" fill="{shade(skin, 14)}"/><circle cx="25" cy="-23" r="2.6" fill="var(--c4)"/>'
            f'<path d="M-24 -40 C-26 -72 -2 -86 20 -78 C33 -73 38 -60 34 -48 C30 -54 25 -55 20 -50 C17 -42 16 -33 13 -25 C9 -16 3 -10 -4 -7 '
            f'C-6 10 -9 28 -20 42 C-31 50 -44 44 -45 32 C-41 16 -29 6 -27 -10 C-26 -20 -24 -30 -24 -40 Z" fill="{HAIR}"/>'
            f'<path d="M2 -77 C16 -79 29 -71 34 -56" {_N14_RIM}/></g>')
    return f'<g transform="translate({x} {y}) scale({s})">{body}<g>{sway(48, 38, 2.5, 5)}{arm}</g></g>'


def _n14_man(x, y, s, skin, shirt, tap):
    """Faceless, seen from behind at three quarters, head bowed to the tablet he holds out to his right, where he approves
    the move; thin headset. The tablet faces us over his shoulder, so its button reads. (x, y) is the base of his neck."""
    tablet = (f'<g transform="translate(112 62) rotate(-10)">'
              f'<rect x="-66" y="-44" width="132" height="90" rx="11" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.5"/>'
              f'<rect x="-58" y="-36" width="116" height="74" rx="6" fill="var(--card)"/>'
              + bars(-48, -27, 92, 2, 12, "var(--c2)", ".5") + tap + '</g>')
    head = (f'<ellipse cx="6" cy="-32" rx="25" ry="30" fill="{skin}"/>'
            f'<ellipse cx="26" cy="-29" rx="4.5" ry="7" fill="{shade(skin, 14)}"/>'
            f'<path d="M-19 -36 C-21 -66 4 -78 24 -70 C35 -65 39 -54 35 -44 C31 -48 27 -48 24 -44 C21 -36 19 -26 15 -18 C10 -10 2 -6 -6 -6 C-14 -8 -19 -18 -19 -36 Z" fill="{HAIR}"/>'
            f'<path d="M-22 -44 C-18 -78 30 -84 38 -50" fill="none" stroke="var(--c4)" stroke-width="3" stroke-linecap="round"/>'
            f'<rect x="21" y="-41" width="11" height="19" rx="4.5" fill="var(--c4)"/>'
            f'<path d="M27 -23 C30 -12 38 -6 46 -6" fill="none" stroke="var(--c4)" stroke-width="2" stroke-linecap="round"/><circle cx="47" cy="-6" r="2.8" fill="var(--c4)"/>'
            f'<path d="M4 -73 C18 -74 30 -66 34 -52" {_N14_RIM}/>')
    body = (f'<path d="M-80 160 C-82 98 -72 52 -48 34 C-32 24 -16 20 0 20 C18 20 36 24 52 34 C76 52 84 98 84 160 Z" fill="{shirt}"/>'
            f'<path d="M-80 160 C-82 98 -72 52 -48 34 C-42 30 -36 27 -30 25 C-46 54 -52 104 -50 160 Z" fill="{shade(shirt, 20)}"/>'
            f'<path d="M20 21 C38 25 54 34 62 46 C76 66 84 104 84 160" {_N14_RIM}/>'
            f'<path d="M-12 -6 L12 -6 L14 22 L-14 22 Z" fill="{shade(skin, 22)}"/>'
            f'<g transform="rotate(16 6 -20)"><g>{bob(0, 2.5, 4)}{head}</g></g>'
            f'<path d="M58 44 C74 62 70 86 58 100" fill="none" stroke="{shade(shirt, 12)}" stroke-width="16" stroke-linecap="round"/>'
            + tablet
            + f'<circle cx="54" cy="98" r="8.5" fill="{skin}"/><path d="M58 92 L64 84" stroke="{skin}" stroke-width="4.5" stroke-linecap="round"/>')
    return f'<g transform="translate({x} {y}) scale({s})">{body}</g>'


@register("scene", "m14_controlroom")
def sc_m14_controlroom(sl, ctx):
    """The close, tomorrow's control room, as one 12-second loop; the quality bar of the deck (ext.py `controlroom`) with
    three polishes. It opens as slide 13's prototype grown up: the wall screen zooms in with the same chart. The approval
    is visible as cause: when he taps «Aprobar», a pulse flies from his tablet to the warehouse, which pings, and the part
    leaves. The two operators are redrawn seen from behind at three quarters, facing the screen they work with, standing at
    a console that crops them above the footer. The beats: alert anticipated, AI suggestion, approval, the part travels,
    the station turns green (proactive maintenance). The frozen frame (0.9) is the resolved one."""
    P = ORIENT() == "portrait"
    ok = ctx.brand.c("dark.ok")
    sx, sy, sw, sh = 1000, 80, 550, 460
    alert_on = [(0, 1), (.56, 1), (.6, 0), (.97, 0), (1, 1)]
    done_on = [(0, 0), (.56, 0), (.6, 1), (.96, 1), (1, 0)]
    desk = 796  # the console's top edge: the operators stand behind it, nothing is drawn below 830
    g = [glow(1275, 300, 470, "var(--brand)", .55)]
    cone = (f'<path d="M{sx + 30} {sy + sh} L{sx + sw - 30} {sy + sh} L1560 {desk} L820 {desk} Z" fill="var(--c2)" opacity=".07">'
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
             + f'<g>{beat("opacity", [(0, 1), (.56, 1), (.62, .25), (.96, .25), (1, 1)])}{trace(fc, "var(--c4)", 1.8, 1.2, .5, " stroke-dasharray=" + chr(34) + "7 7" + chr(34))}</g>'
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
    # the approval reaches the warehouse (0.22-0.26), which pings, and the part leaves (0.28)
    wh_ping = f'<circle cx="{wx}" cy="{wy}" r="30" fill="none" stroke="var(--c4)" stroke-width="1.5">{beat("r", [(0, 30), (.26, 30), (.36, 56), (1, 56)])}{beat("opacity", [(0, 0), (.26, 0), (.265, 1), (.36, 0), (1, 0)])}</circle>'
    van = (f'<g>{beat("opacity", [(0, 0), (.25, 0), (.28, 1), (.57, 1), (.62, 0), (1, 0)])}{move(route, [(0, 0), (.28, 0), (.58, 1), (1, 1)], D)}'
           + token("var(--c4)", 6)
           + f'<rect x="-20" y="-11" width="26" height="18" rx="3" fill="var(--c4)" fill-opacity=".25" stroke="var(--c4)" stroke-width="1.5"/><rect x="6" y="-7" width="13" height="14" rx="3" fill="var(--c4)" fill-opacity=".25" stroke="var(--c4)" stroke-width="1.5"/>'
           f'<circle cx="-11" cy="9" r="3.5" fill="none" stroke="var(--c4)" stroke-width="1.5"/><circle cx="12" cy="9" r="3.5" fill="none" stroke="var(--c4)" stroke-width="1.5"/></g>')
    toast = (f'<g>{beat("opacity", [(0, 0), (.08, 0), (.11, 1), (.46, 1), (.5, 0), (1, 0)])}'
             + card(mx + 14, my + 12, 420, 44, "var(--card)", "var(--c2)", 12, 1.2) + spark(mx + 36, my + 34, .55, "var(--c4)")
             + T(mx + 56, my + 40, sl["suggest"], fit(sl["suggest"], 15, 360, "control room suggestion"), "var(--white)", W6) + '</g>')
    # the tablet: «Aprobar» until he taps it, then approved
    tap = (f'<g>{beat("opacity", [(0, 1), (.22, 1), (.25, 0), (.97, 0), (1, 1)])}' + pill(0, 16, sl["approve"], "var(--c4)", ctx, 18 if P else 14, 110, "control room approve", 12) + '</g>'
           f'<g>{beat("opacity", [(0, 0), (.23, 0), (.26, 1), (.96, 1), (1, 0)])}<rect x="-34" y="4" width="68" height="24" rx="12" fill="{ok}"/>' + check(0, 17, .6, "var(--ink)") + '</g>'
           f'<circle cx="30" cy="16" r="6" fill="none" stroke="var(--white)" stroke-width="1.5">{beat("r", [(0, 6), (.21, 6), (.3, 34), (1, 34)])}'
           f'{beat("opacity", [(0, 0), (.21, 0), (.22, 1), (.3, 0), (1, 0)])}</circle>')
    # people behind the console; the pulse from his tablet flies away from us to the warehouse, so it passes behind him
    wmx, wmy, mnx, mny = 905, 676, 1250, 690
    bx_, by_ = mnx + 112 + 16 * math.sin(math.radians(10)), mny + 62 + 16 * math.cos(math.radians(10))  # the tablet's button on stage
    beam_d = f"M{bx_:.0f} {by_ - 14:.0f} C{bx_ - 20:.0f} {by_ - 150:.0f} {wx + 40} {wy + 150} {wx} {wy + 32}"  # away from us: behind his head
    beam = (f'<g opacity="0">{beat("opacity", [(0, 0), (.22, 0), (.225, .9), (.27, .9), (.31, 0), (1, 0)])}'
            f'<path d="{beam_d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="1.5" stroke-linecap="round">'
            f'{beat("stroke-dashoffset", [(0, 1), (.222, 1), (.262, 0), (1, 0)])}</path></g>'
            + _n13_ride(beam_d, .222, .262, 6))
    people = (f'<clipPath id="n14-desk"><rect x="760" y="0" width="840" height="{desk + 2}"/></clipPath>'
              f'<g clip-path="url(#n14-desk)">' + land(_n14_woman(wmx, wmy, 1.1, SKIN_BROWN, "var(--accent)"), .25, .6, 40)
              + land(_n14_man(mnx, mny, 1.0, SKIN_LIGHT, "var(--c1)", tap), .4, .6, 40) + '</g>')
    leds = "".join(f'<circle cx="{860 + k * 26}" cy="{desk + 19}" r="2.2" fill="var(--c2)" opacity=".45"/>' for k in range(8))
    status = (f'<g>{beat("opacity", alert_on)}<rect x="1336" y="{desk + 15}" width="120" height="8" rx="4" fill="var(--c5)"/></g>'
              f'<g>{beat("opacity", done_on)}<rect x="1336" y="{desk + 15}" width="120" height="8" rx="4" fill="{ok}"/></g>')
    console = land(f'<path d="M820 {desk} H1560 L1548 830 H832 Z" fill="var(--card)"/>'
                   f'<path d="M820 {desk} H1560" stroke="var(--c2)" stroke-width="1.5" opacity=".7"/>'
                   f'<path d="M820 {desk + 1} H1560" stroke="var(--c2)" stroke-width="6" opacity=".08"/>' + leds + status, .2, .5, 20)
    sign = T(sx + sw, sy + sh + 34, sl["sign"], fit(sl["sign"], 20, 330, "control room sign"), "var(--c4)", 'text-anchor="end" font-weight="600"')
    wall = (screen + land(chart + mp, .3, .45, 10) + lines + land(alert + st_alert, .6, .4, 0) + st_ok + wh_ping + van + toast)
    ccx, ccy = sx + sw / 2, sy + sh / 2
    if P:
        return _m14_portrait(sl, ok, wall, (ccx, ccy), (wx, wy), tap, alert_on, done_on), D, FREEZE
    return (g[0] + land(cone, .2, .6, 0) + pop(f'<g transform="translate({-ccx} {-ccy})">{wall}</g>', ccx, ccy, .05, .6)
            + land(sign, 1.4, .45, 10) + beam + people + console), D, FREEZE


def _m14_portrait(sl, ok, wall, cc, wh, tap, alert_on, done_on):
    """controlroom-live in portrait: the same wall screen (chart, map, suggestion, the part in transit), scaled x1.36 so
    its 15-unit labels land at 19.5, full width under the sign; the two operators in front of it, seen from behind, at a
    console that crops them at the foot of the art zone. The approval flies from his tablet to the warehouse on the
    screen, behind his head, as on desktop. cc: the screen's centre and wh: the warehouse, in desktop units."""
    zx, zy, zw, zh = ART_ZONE("left")
    k, top = 1.30, zy + 52                          # the screen: 550x460 desktop units -> 715x598
    PX, PY = zx + zw / 2, top + 230 * k
    at = lambda x, y: (PX + (x - cc[0]) * k, PY + (y - cc[1]) * k)
    sb = top + 460 * k                              # the screen's bottom edge
    desk = zy + zh - 70                             # the console's top edge: the art ends 40 over the slide's footer line
    g = [glow(PX, PY, 400, "var(--brand)", .55)]
    cone = (f'<path d="M{PX - 320:.1f} {sb:.1f} L{PX + 320:.1f} {sb:.1f} L{zx + zw:.1f} {desk:.1f} L{zx:.1f} {desk:.1f} Z" fill="var(--c2)" opacity=".07">'
            f'{loop("opacity", ".04;.12;.04", 5)}</path>')
    g.append(land(cone, .2, .6, 0))
    g.append(pop(f'<g transform="scale({k})"><g transform="translate({-cc[0]} {-cc[1]})">{wall}</g></g>', PX, PY, .05, .6))
    sign = T(f"{PX + 358:.1f}", f"{top - 22:.1f}", sl["sign"], fit(sl["sign"], 22, zw - 60, "control room sign", floor=18), "var(--c4)", 'text-anchor="end" font-weight="600"')
    # the operators: she points up at the screen, he approves on the tablet he holds out (its button reads x1.05)
    sm, (wmx, wmy), (mnx, mny) = 1.05, (zx + 190, sb + 96), (zx + 560, desk - 118)
    bx_, by_ = mnx + sm * (112 + 16 * math.sin(math.radians(10))), mny + sm * (62 + 16 * math.cos(math.radians(10)))
    wx, wy = at(wh[0], wh[1] + 32)
    beam_d = f"M{bx_:.0f} {by_ - 16:.0f} C{bx_ - 30:.0f} {by_ - 200:.0f} {wx + 60:.0f} {wy + 190:.0f} {wx:.0f} {wy:.0f}"  # behind his head
    beam = (f'<g opacity="0">{beat("opacity", [(0, 0), (.22, 0), (.225, .9), (.27, .9), (.31, 0), (1, 0)])}'
            f'<path d="{beam_d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="2" stroke-linecap="round">'
            f'{beat("stroke-dashoffset", [(0, 1), (.222, 1), (.262, 0), (1, 0)])}</path></g>'
            + _n13_ride(beam_d, .222, .262, 7))
    people = (f'<clipPath id="n14-desk"><rect x="0" y="0" width="900" height="{desk + 2:.1f}"/></clipPath>'
              f'<g clip-path="url(#n14-desk)">' + land(_n14_woman(wmx, wmy, 1.0, SKIN_BROWN, "var(--accent)"), .25, .6, 40)
              + land(_n14_man(mnx, mny, sm, SKIN_LIGHT, "var(--c1)", tap), .4, .6, 40) + '</g>')
    leds = "".join(f'<circle cx="{zx + 40 + j * 26:.1f}" cy="{desk + 16:.1f}" r="2.4" fill="var(--c2)" opacity=".45"/>' for j in range(8))
    status = (f'<g>{beat("opacity", alert_on)}<rect x="{zx + zw - 150:.1f}" y="{desk + 12:.1f}" width="120" height="8" rx="4" fill="var(--c5)"/></g>'
              f'<g>{beat("opacity", done_on)}<rect x="{zx + zw - 150:.1f}" y="{desk + 12:.1f}" width="120" height="8" rx="4" fill="{ok}"/></g>')
    console = land(f'<path d="M{zx:.1f} {desk:.1f} H{zx + zw:.1f} L{zx + zw - 12:.1f} {desk + 30:.1f} H{zx + 12:.1f} Z" fill="var(--card)"/>'
                   f'<path d="M{zx:.1f} {desk:.1f} H{zx + zw:.1f}" stroke="var(--c2)" stroke-width="1.5" opacity=".7"/>'
                   f'<path d="M{zx:.1f} {desk + 1:.1f} H{zx + zw:.1f}" stroke="var(--c2)" stroke-width="6" opacity=".08"/>' + leds + status, .2, .5, 20)
    return _pz_clip("".join(g) + beam + people + console + land(sign, 1.4, .45, 10), "pz-m14")
