"""The banca «Datos e IA» deck, slides 1, 5 and 6 (portada, caso-dato, caso-reporte). Each scene is one 12-second story
timed with beat(); the reduced-motion frame (0.9 of the loop, 10.8 s) is its resolved state. Runs in the shared namespace
of module/ext.py and reuses the harvested helpers _n13_on/_n13_off/_n13_ride and _N14_RIM (energía), _n01_tr (energía),
_b04_draw/_b04_ping (salud) and _b14_ok_dot/_b14_ping (salud).

- d01_portada: ten hypothesis cards, each with its «?», flow one by one through a funnel into «Su laboratorio»; each
  comes out validated, its card gets a check and a check lands on the quarter timeline (Oct, Nov, Dic), which fills to
  «10 de 10 validadas».
- d05_dato: a four-stage data pipeline (ingesta, calidad, documentación, catálogo); at each stage an agent (a spark) does
  its work and a faceless data person approves it from the tablet: the pulse flies up and the stage turns «Aprobado».
- d06_reporte: two static figures side by side, «20 min» (dim) and «160 s» (lit); on the left a person crawls through the
  manual steps, on the right the agent ticks the same steps, the report is ready and the person taps «Revisado».
"""


def _d01_wrap(x, y, s, room, size, fill, where, anchor="start", lh=1.2):
    """A label wrapped to room px: its longest word fits at >= 15 px, the rest wraps (TCW)."""
    word = max(_(str(s)).split(), key=len)
    z = fit(word, size, room, where, floor=15)
    chars, n = max(4, int(room / (z * .56))), len(_(str(s)))
    lines = -(-n // chars)
    return TCW(x, y, s, max(len(word), -(-n // lines) + 1) if lines > 1 else chars, z, fill, W6, lh, anchor)


def _d01_win(a, b, lo=0, hi=1):
    """beat() pairs: lo until a, hi from a to b, lo again after."""
    return beat("opacity", [(0, lo), (a, lo), (a + .01, hi), (b, hi), (b + .01, lo), (1, lo)])


# ---------------------------------------------------------------- portrait (the mobile build, DCD_ORIENT=portrait)
def _pd01_ring(x, y, r0, r1, times, span=.05, col="var(--c4)"):
    """One ring that opens at each time in times and fades (two animations for all of them, not two each)."""
    rs, op = [(0, r0)], [(0, 0)]
    for a in times:
        rs += [(a, r0), (a + span, r1), (a + span + .001, r0)]
        op += [(a, 0), (a + .005, .6), (a + span, 0)]
    rs.append((1, r0))
    op.append((1, 0))
    return (f'<circle cx="{x}" cy="{y}" r="{r0}" fill="none" stroke="{col}" stroke-width="1.5" opacity="0">'
            f'{beat("r", rs)}{beat("opacity", op)}</circle>')


def _pd01_twin(sl, ctx):
    """d01 on the 900x1600 stage: the ten cards as a 2x5 grid, the funnel and the lab under them, the quarter timeline
    at the bottom. Same beats as the desktop (each card lights, rides down to the lab, lands checked on its slot)."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    W, H, GX, P = 400, 64, 20, 74
    cards = [(zx + (k % 2) * (W + GX), zy + 50 + (k // 2) * P) for k in range(10)]
    A = [.15 + k * .066 for k in range(10)]
    E = [a + .055 for a in A]
    cx = zx + zw / 2
    FY0, FY1 = zy + 430, zy + 510
    lw, lh = 300, 70
    lx, ly = cx - lw / 2, FY1 + 10
    LY = zy + 760
    sx = [zx + 50 + i * 80 for i in range(10)]
    DONE = .82
    art, text = [glow(cx, zy + 420, 480, "var(--brand)", .45)], []
    cnt = sl["count"]
    text.append(land(T(zx, zy + 30, cnt, fit(cnt, 26, 500, "portada count", floor=20), "var(--white)", W6), .1, .5, 8))
    parts = []
    for k, ((x, y), lab) in enumerate(zip(cards, sl["hypotheses"])):
        a, e = A[k], E[k]
        qx, qy = x + W - 28, y + H / 2
        parts.append(card(x, y, W, H, "var(--card)", "var(--line)", 12, 1.2)
                     + f'<rect x="{x}" y="{y}" width="{W}" height="{H}" rx="12" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_d01_win(a - .02, e)}</rect>'
                     + T(x + 16, y + 41, str(k + 1), 22, "var(--c4)", W6)
                     + T(x + 50, y + 40, lab, fit(lab, 22, W - 110, "portada hypothesis", floor=20), "var(--white)", W6)
                     + f'<g>{_n13_off(e)}<circle cx="{qx}" cy="{qy}" r="15" fill="var(--card)" stroke="var(--c4)" stroke-width="1.6"/>'
                     + TC(qx, qy + 7.5, "?", 21, "var(--c4)", W6) + '</g>'
                     + f'<g opacity="0">{_n13_on(e)}<rect x="{x}" y="{y}" width="{W}" height="{H}" rx="12" fill="none" stroke="{ok}" stroke-width="1.5"/>'
                     + f'<circle cx="{qx}" cy="{qy}" r="15" fill="{ok}"/>{check(qx, qy + 1, 1, "var(--ink)")}</g>')
    art.append(seq(["".join(parts[i:i + 2]) for i in range(0, 10, 2)], .15, .45, 14))
    fun = (f'<path d="M{zx + 10} {FY0} H{zx + zw - 10} L{cx + 70} {FY1} H{cx - 70} Z" fill="color-mix(in srgb, var(--c2) 8%, var(--card))" '
           f'stroke="var(--c2)" stroke-width="1.4" stroke-opacity=".6" stroke-linejoin="round"/>'
           f'<path d="M{cx} {ly + lh} V{LY - 70}" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="3 6" opacity=".6"/>')
    labc = card(lx, ly, lw, lh, "var(--card)", "var(--c4)", 14, 1.6) + spark(lx + 36, ly + lh / 2, .7)
    art.append(land(fun, .45, .5, 10) + land(labc, .6, .5, 10)
               + _pd01_ring(cx, ly + lh / 2, 40, 110, [a + .025 for a in A]))
    text.append(land(TC(cx + 20, ly + 44, sl["lab"], fit(sl["lab"], 24, lw - 90, "portada lab", floor=20), "var(--white)", W6), .6, .5, 10))
    # the quarter timeline: three months, ten slots
    edges = [sx[0] - 30, (sx[2] + sx[3]) / 2, (sx[6] + sx[7]) / 2, sx[-1] + 30]
    mx = [(sx[0] + sx[2]) / 2, (sx[3] + sx[6]) / 2, (sx[7] + sx[9]) / 2]
    last = (E[2], E[6], E[9])
    tl = f'<path d="M{edges[0]} {LY} H{edges[-1]}" stroke="var(--line)" stroke-width="2" stroke-linecap="round"/>'
    tl += "".join(f'<path d="M{x0:.0f} {LY - 20} V{LY + 20}" stroke="var(--line)" stroke-width="1.5"/>' for x0 in edges)
    tl += "".join(f'<circle cx="{x0}" cy="{LY}" r="18" fill="var(--card)" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="3 4"/>' for x0 in sx)
    months = ""
    for name, mcx, at in zip(sl["months"], mx, last):
        z = fit(name, 24, 200, "portada month", floor=20)
        months += (TC(f"{mcx:.0f}", LY - 40, name, z, "var(--muted)", W6)
                   + f'<g opacity="0">{_n13_on(at)}' + TC(f"{mcx:.0f}", LY - 40, name, z, "var(--c4)", W6) + '</g>')
    t0 = E[0] - (E[-1] - E[0]) * 30 / (sx[-1] - sx[0])
    fill = _b04_draw(f"M{edges[0]} {LY} H{sx[-1]}", "var(--c4)", t0, E[-1], 3)
    slots = "".join(_b14_ok_dot(x0, LY, e, ok, 18) for x0, e in zip(sx, E))
    pend = f'<g>{_n13_off(DONE)}' + TC(cx, LY + 90, sl["pending"], fit(sl["pending"], 24, 700, "portada pending", floor=20), "var(--muted)", W6) + '</g>'
    done = (f'<g opacity="0">{_n13_on(DONE)}' + TC(cx, LY + 94, sl["done"], fit(sl["done"], 32, 760, "portada done", floor=20), ok, W6) + '</g>'
            + _b14_ping(cx, LY + 82, 30, 160, DONE, ok, .06))
    rides = "".join(_n13_ride(f"M{x + W / 2} {y + H - 8} C{x + W / 2} {FY0 + 20} {cx} {FY0 + 6} {cx} {FY1} V{ly + lh / 2} "
                              f"C{cx} {LY - 70} {sx[k]} {LY - 90} {sx[k]} {LY}", A[k], E[k], 7)
                    for k, (x, y) in enumerate(cards))
    art.append(land(tl, .8, .5, 10) + fill)
    text.append(land(months + pend, 1.0, .45, 8))
    return portrait_mark("".join(art) + rides + slots + "".join(text) + done), D, FREEZE


# ---------------------------------------------------------------- 1 · portada: ten hypotheses validated this quarter
@register("scene", "d01_portada")
def sc_d01_portada(sl, ctx):
    """Ten hypothesis cards, numbered, each with its «?». Loop: one by one each card lights and sends a token down the
    funnel into «Su laboratorio»; it comes out validated: its «?» becomes a check and a check lands on its slot of the
    quarter timeline (three in October, four in November, three in December; each month lights once full). The counter
    is fixed text («10 hipótesis»); the state line reads «Por validar», then «10 de 10 validadas». Frozen frame: ten
    cards checked and ten checks on the timeline."""
    if ORIENT() == "portrait":
        return _pd01_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    W, H, GX = 134, 94, 13
    cards = [(834 + (k % 5) * (W + GX), (136, 244)[k // 5]) for k in range(10)]
    A = [.15 + k * .066 for k in range(10)]            # each hypothesis leaves its card
    E = [a + .055 for a in A]                          # ... and lands validated on the timeline
    FY0, FY1 = 356, 452
    lx, ly, lw, lh = 1060, 460, 260, 62
    LY = 690
    sx = [902 + i * 64 for i in range(10)]
    DONE = .82
    g = [glow(1190, 420, 460, "var(--brand)", .45)]
    cnt = sl["count"]
    g.append(land(T(834, 114, cnt, fit(cnt, 20, 360, "portada count"), "var(--white)", W6), .1, .5, 8))
    # the ten cards
    parts = []
    for k, ((x, y), lab) in enumerate(zip(cards, sl["hypotheses"])):
        a, e = A[k], E[k]
        qx, qy = x + W - 18, y + 22
        parts.append(card(x, y, W, H, "var(--card)", "var(--line)", 12, 1.2)
                     + f'<rect x="{x}" y="{y}" width="{W}" height="{H}" rx="12" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity="0">{_d01_win(a - .02, e)}</rect>'
                     + f'<rect x="{x}" y="{y}" width="{W}" height="{H}" rx="12" fill="none" stroke="{ok}" stroke-width="1.4" opacity="0">{_n13_on(e)}</rect>'
                     + T(x + 14, y + 28, str(k + 1), 17, "var(--c4)", W6)
                     + f'<g>{_n13_off(e)}<circle cx="{qx}" cy="{qy}" r="11" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>'
                     + TC(qx, qy + 5.5, "?", 15, "var(--c4)", W6) + '</g>'
                     + _b14_ok_dot(qx, qy, e, ok, 11)
                     + _d01_wrap(x + 14, y + 56, lab, W - 26, 15, "var(--white)", "portada hypothesis"))
    g.append(seq(parts, .15, .45, 14))
    # the funnel and the lab
    fun = (f'<path d="M846 {FY0} H1534 L1250 {FY1} H1130 Z" fill="color-mix(in srgb, var(--c2) 8%, var(--card))" '
           f'stroke="var(--c2)" stroke-width="1.4" stroke-opacity=".6" stroke-linejoin="round"/>')
    for f in (.34, .67):
        yy = FY0 + f * (FY1 - FY0)
        fun += (f'<path d="M{846 + f * 284:.0f} {yy:.0f} H{1534 - f * 284:.0f}" stroke="var(--c2)" stroke-width="1" '
                f'stroke-dasharray="3 6" opacity=".45"/>')
    lab = (card(lx, ly, lw, lh, "var(--card)", "var(--c4)", 14, 1.6) + spark(lx + 32, ly + lh / 2, .6)
           + TC(lx + lw / 2 + 16, ly + 39, sl["lab"], fit(sl["lab"], 20, lw - 84, "portada lab"), "var(--white)", W6))
    fun += f'<path d="M1190 {ly + lh} V{LY - 62}" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="3 6" opacity=".6"/>'
    g.append(land(fun, .45, .5, 10) + land(lab, .6, .5, 10)
             + _b04_ping(lx + lw / 2, ly + lh / 2, 34, 90, "var(--c4)", [a + .025 for a in A], .05, .6))
    # the quarter timeline: three months, ten slots
    edges, split, mx = [870, 1062, 1318, 1510], (3, 4, 3), (966, 1190, 1414)
    last = (E[2], E[6], E[9])
    tl = f'<path d="M870 {LY} H1510" stroke="var(--line)" stroke-width="2" stroke-linecap="round"/>'
    tl += "".join(f'<path d="M{x0} {LY - 16} V{LY + 16}" stroke="var(--line)" stroke-width="1.5"/>' for x0 in edges)
    for m, (name, cx, at) in enumerate(zip(sl["months"], mx, last)):
        z = fit(name, 18, 150, "portada month")
        tl += (f'<g>{_n13_off(at)}' + TC(cx, LY - 34, name, z, "var(--muted)", W6) + '</g>'
               + f'<g opacity="0">{_n13_on(at)}' + TC(cx, LY - 34, name, z, "var(--c4)", W6) + '</g>')
    tl += "".join(f'<circle cx="{x0}" cy="{LY}" r="14" fill="var(--card)" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="3 4"/>'
                  for x0 in sx)
    t0 = E[0] - (E[-1] - E[0]) * 32 / 576
    fill = _b04_draw(f"M870 {LY} H{sx[-1]}", "var(--c4)", t0, E[-1], 3)
    slots = "".join(_b14_ok_dot(x0, LY, e, ok, 14) + _b14_ping(x0, LY, 14, 34, e, ok) for x0, e in zip(sx, E))
    pend = f'<g>{_n13_off(DONE)}' + TC(1190, 774, sl["pending"], fit(sl["pending"], 20, 600, "portada pending"), "var(--muted)", W6) + '</g>'
    done = (f'<g opacity="0">{_n13_on(DONE)}' + TC(1190, 776, sl["done"], fit(sl["done"], 26, 600, "portada done"), ok, W6) + '</g>'
            + _b14_ping(1190, 766, 30, 160, DONE, ok, .06))
    rides = "".join(_n13_ride(f"M{x + W / 2} {y + H - 8} C{x + W / 2} {FY0 + 20} 1190 {FY0 + 6} 1190 {FY1} V{ly + lh / 2} "
                              f"C1190 {LY - 70} {sx[k]} {LY - 90} {sx[k]} {LY}", A[k], E[k], 6)
                    for k, (x, y) in enumerate(cards))
    g.append(land(tl, .8, .5, 10) + fill + land(pend, 1.0, .45, 8))
    return "".join(g) + rides + slots + done, D, FREEZE


# ---------------------------------------------------------------- 5 · caso-dato: agents along the data lifecycle
def _d05_agent(path, a, b):
    """The agent (a spark) working along path between a and b, hidden otherwise."""
    return (f'<g opacity="0">{beat("opacity", [(0, 0), (a, 0), (a + .01, 1), (b - .01, 1), (b, 0), (1, 0)])}'
            f'{move(path, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{glow(0, 0, 26, "var(--c4)", .35)}{spark(0, 0, .6)}</g>')


def _d05_dash(a, b):
    """A stroke that draws between a and b and stays drawn until the loop resets."""
    return beat("stroke-dashoffset", [(0, 1), (a, 1), (b, 0), (.965, 0), (.985, 1), (1, 1)])


def _d05_vignette(k, bx, by, bw, a, ok):
    """What the agent does at stage k, inside the box at (bx, by), bw wide and 160 high, starting at a:
    0 rows arrive and get checked; 1 a broken row gets fixed; 2 a field gets described; 3 an entry lands in the catalog."""
    rows = [by + 30 + i * 30 for i in range(4)]
    bar_w = bw - 58
    s = ""
    if k == 0:
        for i, y in enumerate(rows):
            t = a + .012 * i
            s += (f'<rect x="{bx + 14}" y="{y}" width="{bar_w}" height="10" rx="5" fill="none" stroke="var(--line)" stroke-width="1" stroke-dasharray="3 4"/>'
                  f'<g opacity="0">{_n13_on(t)}<g>{_n01_tr([(0, "-26 0"), (t, "-26 0"), (t + .02, "0 0"), (1, "0 0")])}'
                  f'<rect x="{bx + 14}" y="{y}" width="{bar_w}" height="10" rx="5" fill="var(--c2)" opacity=".75"/></g></g>'
                  f'<g opacity="0">{_n13_on(a + .055 + .01 * i)}{check(bx + bw - 26, y + 6, .45, ok)}</g>')
        return s + _d05_agent(f"M{bx + bw - 26} {rows[0] - 10} V{rows[-1] + 14}", a + .045, a + .095)
    if k == 1:
        fix = a + .07
        for i, y in enumerate(rows):
            if i != 1:
                s += f'<rect x="{bx + 14}" y="{y}" width="{bar_w}" height="10" rx="5" fill="var(--c2)" opacity=".6"/>'
                continue
            s += (f'<g>{_n13_off(fix)}<rect x="{bx + 14}" y="{y}" width="{bar_w}" height="10" rx="5" fill="none" stroke="var(--c5)" stroke-width="1.6" stroke-dasharray="7 5"/>'
                  f'<circle cx="{bx + bw - 26}" cy="{y + 5}" r="9" fill="var(--c5)"/>'
                  f'<path d="M{bx + bw - 26} {y} V{y + 5}" stroke="var(--ink)" stroke-width="2.2" stroke-linecap="round"/>'
                  f'<circle cx="{bx + bw - 26}" cy="{y + 9}" r="1.4" fill="var(--ink)"/></g>'
                  f'<g opacity="0">{_n13_on(fix)}<rect x="{bx + 14}" y="{y}" width="{bar_w}" height="10" rx="5" fill="var(--c2)" opacity=".85"/>'
                  f'{check(bx + bw - 26, y + 6, .45, ok)}</g>'
                  + _b14_ping(bx + bw - 26, y + 5, 9, 30, fix, ok))
        return s + _d05_agent(f"M{bx + 20} {by + 14} C{bx + 30} {rows[1] - 20} {bx + 40} {rows[1] - 10} {bx + bw - 44} {rows[1] - 10}", a + .005, a + .085)
    if k == 2:
        s += (f'<rect x="{bx + 14}" y="{by + 18}" width="78" height="22" rx="11" fill="none" stroke="var(--c4)" stroke-width="1.5"/>'
              f'<rect x="{bx + 26}" y="{by + 26}" width="54" height="6" rx="3" fill="var(--c4)" opacity=".8"/>')
        for i, L in enumerate((.92, .78, .86, .55)):
            y, w0 = by + 62 + i * 22, (bw - 28) * L
            ta = a + .012 + i * .018
            s += (f'<path d="M{bx + 14} {y} h{w0:.0f}" stroke="var(--line)" stroke-width="2" stroke-dasharray="3 5"/>'
                  f'<path d="M{bx + 14} {y} h{w0:.0f}" pathLength="1" stroke-dasharray="1" stroke="var(--c2)" stroke-width="4" stroke-linecap="round">'
                  f'{_d05_dash(ta, ta + .018)}</path>')
        return s + _d05_agent(f"M{bx + 14} {by + 54} H{bx + bw - 16} L{bx + 14} {by + 76} H{bx + bw - 30} L{bx + 14} {by + 98} "
                              f"H{bx + bw - 22} L{bx + 14} {by + 120} H{bx + 14 + (bw - 28) * .55:.0f}", a + .01, a + .085)
    # k == 3: the catalog, three entries and a free slot where the new one lands
    cw, ch = (bw - 40) / 2, 52
    spots = [(bx + 14 + (i % 2) * (cw + 12), by + 18 + (i // 2) * (ch + 14)) for i in range(4)]
    for i, (x, y) in enumerate(spots[:3]):
        s += card(x, y, cw, ch, "var(--card)", "var(--line)", 8, 1.2) + bars(x + 10, y + 14, cw - 20, 2, 14, "var(--c2)", ".45")
    x, y = spots[3]
    lands = a + .06
    entry = (card(x, y, cw, ch, "color-mix(in srgb, var(--c4) 14%, var(--card))", "var(--c4)", 8, 1.6)
             + bars(x + 10, y + 14, cw - 20, 2, 14, "var(--c4)", ".8"))
    s += (f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="8" fill="none" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="4 4" opacity=".7"/>'
          f'<g opacity="0">{_n13_on(lands)}<g>{_n01_tr([(0, "0 -30"), (lands, "0 -30"), (lands + .02, "0 0"), (1, "0 0")])}{entry}</g></g>'
          + _b14_ping(x + cw / 2, y + ch / 2, 20, 50, lands + .02)
          + f'<g opacity="0">{_n13_on(lands + .02)}<circle cx="{x + cw - 4}" cy="{y + 4}" r="9" fill="{ok}"/>{check(x + cw - 4, y + 5, .45, "var(--ink)")}</g>')
    return s + _d05_agent(f"M{bx + bw / 2} {by + 150} C{bx + bw / 2} {by + 120} {x + cw / 2} {y + ch + 30} {x + cw / 2} {y + ch / 2}", a + .005, a + .07)


def _d05_person(x, y, skin, shirt, tap):
    """_n14_man without the headset (a data person, not a call center): faceless, seen from behind at three quarters,
    head bowed to the tablet held out to the right, where tap is drawn. (x, y) is the base of the neck."""
    tablet = (f'<g transform="translate(112 62) rotate(-10)">'
              f'<rect x="-66" y="-44" width="132" height="90" rx="11" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.5"/>'
              f'<rect x="-58" y="-36" width="116" height="74" rx="6" fill="var(--card)"/>'
              + bars(-48, -27, 92, 2, 12, "var(--c2)", ".5") + tap + '</g>')
    head = (f'<ellipse cx="6" cy="-32" rx="25" ry="30" fill="{skin}"/>'
            f'<ellipse cx="26" cy="-29" rx="4.5" ry="7" fill="{shade(skin, 14)}"/>'
            f'<path d="M-19 -36 C-21 -66 4 -78 24 -70 C35 -65 39 -54 35 -44 C31 -48 27 -48 24 -44 C21 -36 19 -26 15 -18 C10 -10 2 -6 -6 -6 C-14 -8 -19 -18 -19 -36 Z" fill="{HAIR}"/>'
            f'<path d="M4 -73 C18 -74 30 -66 34 -52" {_N14_RIM}/>')
    body = (f'<path d="M-80 160 C-82 98 -72 52 -48 34 C-32 24 -16 20 0 20 C18 20 36 24 52 34 C76 52 84 98 84 160 Z" fill="{shirt}"/>'
            f'<path d="M-80 160 C-82 98 -72 52 -48 34 C-42 30 -36 27 -30 25 C-46 54 -52 104 -50 160 Z" fill="{shade(shirt, 20)}"/>'
            f'<path d="M20 21 C38 25 54 34 62 46 C76 66 84 104 84 160" {_N14_RIM}/>'
            f'<path d="M-12 -6 L12 -6 L14 22 L-14 22 Z" fill="{shade(skin, 22)}"/>'
            f'<g transform="rotate(16 6 -20)"><g>{bob(0, 2.5, 4)}{head}</g></g>'
            f'<path d="M58 44 C74 62 70 86 58 100" fill="none" stroke="{shade(shirt, 12)}" stroke-width="16" stroke-linecap="round"/>'
            + tablet
            + f'<circle cx="54" cy="98" r="8.5" fill="{skin}"/><path d="M58 92 L64 84" stroke="{skin}" stroke-width="4.5" stroke-linecap="round"/>')
    return f'<g transform="translate({x} {y})">{body}</g>'


def _pd05_twin(sl, ctx):
    """d05 on the 900x1600 stage: the four stages as full-width rows down a vertical data line (the vignette on the
    right of each row, scaled), the data person with the tablet and the label under them. Same beats as the desktop."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    PX, X0, X1, RH, GAP = zx + 22, zx + 58, zx + zw - 22, 150, 12
    ys = [zy + 14 + k * (RH + GAP) for k in range(4)]
    mids = [y + RH / 2 for y in ys]
    A = [.16 + .18 * k for k in range(4)]
    WORK = [a + .09 for a in A]
    TAP = [a + .11 for a in A]
    AP = [a + .14 for a in A]
    VW, VS = 340, .8                                   # the vignette: drawn 340 wide, scaled to 272 x 128
    vx = X1 - 14 - VW * VS
    mnx, mny, desk = zx + 520, zy + 770, zy + 890
    art, text = [glow(zx + zw / 2, zy + 360, 480, "var(--brand)", .45)], []
    # the data line, down the left edge, with a node per stage
    pipe = (f'<path d="M{PX} {zy} V{mids[-1]}" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 6"/>'
            + "".join(f'<path d="M{PX + 8} {m} H{X0}" stroke="var(--line)" stroke-width="1.5"/>'
                      f'<circle cx="{PX}" cy="{m}" r="9" fill="var(--card)" stroke="var(--c2)" stroke-width="1.5"/>' for m in mids))
    segs = [f"M{PX} {zy} V{mids[0] - 9}"] + [f"M{PX} {mids[k] + 9} V{mids[k + 1] - 9}" for k in range(3)]
    spans = [(A[0] - .05, A[0])] + [(AP[k] + .005, A[k + 1]) for k in range(3)]
    lit = "".join(_b04_draw(d, "var(--c4)", a, b, 2.5) + _n13_ride(d, a, b, 7) for d, (a, b) in zip(segs, spans))
    for k, m in enumerate(mids):
        lit += (f'<g opacity="0">{_n13_on(AP[k])}<circle cx="{PX}" cy="{m}" r="11" fill="{ok}"/>{check(PX, m + 1, .5, "var(--ink)")}</g>')
    art.append(land(pipe, .1, .5, 0) + lit)
    # the four stages
    rows, words = [], []
    rw = X1 - X0
    for k, (y, name, res) in enumerate(zip(ys, sl["phases"], sl["results"])):
        a = A[k]
        rows.append(card(X0, y, rw, RH, "var(--card)", "var(--line)", 16, 1.2)
                    + f'<rect x="{X0}" y="{y}" width="{rw}" height="{RH}" rx="16" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_d01_win(a - .01, AP[k])}</rect>'
                    + card(vx, y + 11, VW * VS, 128, "var(--dim)", "var(--line)", 12, 1)
                    + f'<g transform="translate({vx:.0f} {y + 11}) scale({VS})">{_d05_vignette(k, 0, 0, VW, a, ok)}</g>'
                    + spark(X0 + 30, y + 80, .5))
        room = vx - X0 - 30
        words.append(T(X0 + 20, y + 42, str(k + 1), 24, "var(--c4)", W6)
                     + T(X0 + 50, y + 42, name, fit(name, 24, room - 30, "dato stage", floor=20), "var(--white)", W6)
                     + f'<g>{_n13_off(WORK[k])}' + T(X0 + 50, y + 88, sl["wait"], fit(sl["wait"], 22, room - 30, "dato wait", floor=20), "var(--muted)", W6) + '</g>'
                     + f'<g opacity="0">{_n13_on(WORK[k])}' + T(X0 + 50, y + 88, res, fit(res, 22, room - 30, "dato result", floor=20), "var(--c4)", W6) + '</g>'
                     + f'<g>{_n13_off(AP[k])}' + pill(X0 + 110, y + 122, sl["approve"][0], "var(--dim)", ctx, 20, 190, "dato pending", 14) + '</g>'
                     + f'<g opacity="0">{_n13_on(AP[k])}<rect x="{X0}" y="{y}" width="{rw}" height="{RH}" rx="16" fill="none" stroke="{ok}" stroke-width="1.5"/>'
                     + pill(X0 + 110, y + 122, sl["approve"][1], ok, ctx, 20, 190, "dato approved", 14) + '</g>')
    art.append(seq([r + w for r, w in zip(rows, words)], .2, .5, 16))
    # the data person with the tablet: «Aprobar», tapped once per stage
    fl = [(0, 0)] + [p for t in TAP for p in ((t, 0), (t + .005, 1), (t + .035, 1), (t + .045, 0))] + [(1, 0)]
    flashes = (f'<g opacity="0">{beat("opacity", fl)}'
               f'<rect x="-50" y="-7" width="100" height="38" rx="19" fill="{ok}"/>{check(0, 13, .8, "var(--ink)")}</g>')
    tap = pill(0, 12, sl["tap"], "var(--c4)", ctx, 20, 112, "dato tap", 10) + flashes
    art.append(f'<clipPath id="pd05-desk"><rect x="{zx}" y="{zy}" width="{zw}" height="{desk - zy + 2}"/></clipPath>'
               f'<g clip-path="url(#pd05-desk)">' + land(_d05_person(mnx, mny, SKIN_LIGHT, "var(--c1)", tap), .5, .6, 40) + '</g>'
               + land(f'<path d="M{zx + 360} {desk} H{X1}" stroke="var(--c2)" stroke-width="1.5" opacity=".7"/>', .3, .5, 0))
    tx, ty = mnx + 112 + 20, mny + 20                  # the top of the tablet
    for k, m in enumerate(mids):
        d = f"M{tx} {ty} C{tx} {ty - 60} {X1 + 10} {ty - 60} {X1 + 10} {ty - 120} V{m} H{X1 - 4}"
        art.append(f'<g opacity="0">{beat("opacity", [(0, 0), (TAP[k], 0), (TAP[k] + .003, .9), (AP[k], .9), (AP[k] + .03, 0), (1, 0)])}'
                   f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="1.8" stroke-linecap="round">'
                   f'{beat("stroke-dashoffset", [(0, 1), (TAP[k], 1), (AP[k], 0), (1, 0)])}</path></g>')
    ly = desk - 190
    text.append(land(f'<circle cx="{zx + 22}" cy="{ly - 8}" r="17" fill="{ok}"/>{check(zx + 22, ly - 7, .7, "var(--ink)")}'
                     + TCW(zx + 52, ly, sl["label"], 22, 26, "var(--white)", W6, 1.25, "start"), 1.2, .5, 10))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "d05_dato")
def sc_d05_dato(sl, ctx):
    """A data pipeline of four stages (Ingesta, Calidad, Documentación, Catálogo) under a line where the data travels.
    Loop: the data enters; at each stage an agent (a spark) does its work (the rows arrive and get checked, a broken row
    gets fixed, a field gets described, an entry lands in the catalog) and the stage says so; a faceless data person
    below taps «Aprobar» on the tablet, the pulse flies up to the stage and it turns «Aprobado»; the data moves on.
    Frozen frame: the four stages done and approved."""
    if ORIENT() == "portrait":
        return _pd05_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    W, GX, Y, H = 166, 16, 150, 322
    xs = [834 + k * (W + GX) for k in range(4)]
    cxs = [x + W / 2 for x in xs]
    A = [.16 + .18 * k for k in range(4)]            # the agent starts at stage k
    WORK = [a + .09 for a in A]                        # its result shows
    TAP = [a + .11 for a in A]                         # the person taps «Aprobar»
    AP = [a + .14 for a in A]                          # the stage turns «Aprobado»
    PY = 118
    mnx, mny, desk = 930, 652, 800
    g = [glow(1190, 330, 470, "var(--brand)", .45)]
    # the pipeline line, where the data travels from stage to stage
    pipe = (f'<path d="M824 {PY} H{cxs[-1]}" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 6"/>'
            + "".join(f'<path d="M{cx} {PY + 8} V{Y}" stroke="var(--line)" stroke-width="1.5"/>'
                      f'<circle cx="{cx}" cy="{PY}" r="8" fill="var(--card)" stroke="var(--c2)" stroke-width="1.5"/>' for cx in cxs))
    lit = _b04_draw(f"M824 {PY} H{cxs[0] - 8}", "var(--c4)", A[0] - .05, A[0], 2.5)
    lit += _n13_ride(f"M824 {PY} H{cxs[0]}", A[0] - .05, A[0], 6)
    for k in range(3):
        seg = f"M{cxs[k] + 8} {PY} H{cxs[k + 1] - 8}"
        lit += _b04_draw(seg, "var(--c4)", AP[k] + .005, A[k + 1], 2.5) + _n13_ride(seg, AP[k] + .005, A[k + 1], 6)
    for k, cx in enumerate(cxs):
        lit += (f'<circle cx="{cx}" cy="{PY}" r="8" fill="var(--c4)" opacity="0">{_d01_win(A[k], AP[k])}</circle>'
                f'<g opacity="0">{_n13_on(AP[k])}<circle cx="{cx}" cy="{PY}" r="9" fill="{ok}"/>{check(cx, PY + 1, .4, "var(--ink)")}</g>')
    g.append(land(pipe, .1, .5, 0) + lit)
    # the four stages
    stages = []
    for k, (x, name, res) in enumerate(zip(xs, sl["phases"], sl["results"])):
        a = A[k]
        c = (card(x, Y, W, H, "var(--card)", "var(--line)", 16, 1.2)
             + f'<rect x="{x}" y="{Y}" width="{W}" height="{H}" rx="16" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity="0">{_d01_win(a - .01, AP[k])}</rect>'
             + f'<rect x="{x}" y="{Y}" width="{W}" height="{H}" rx="16" fill="none" stroke="{ok}" stroke-width="1.5" opacity="0">{_n13_on(AP[k])}</rect>'
             + T(x + 14, Y + 32, str(k + 1), 17, "var(--c4)", W6)
             + T(x + 32, Y + 32, name, fit(name, 17, W - 44, "dato stage"), "var(--white)", W6)
             + card(x + 12, Y + 48, W - 24, 160, "var(--dim)", "var(--line)", 12, 1)
             + _d05_vignette(k, x + 12, Y + 48, W - 24, a, ok)
             + spark(x + 24, Y + 238, .42)
             + f'<g>{_n13_off(WORK[k])}' + T(x + 40, Y + 244, sl["wait"], fit(sl["wait"], 15, W - 52, "dato wait"), "var(--muted)", W6) + '</g>'
             + f'<g opacity="0">{_n13_on(WORK[k])}' + T(x + 40, Y + 244, res, fit(res, 15, W - 52, "dato result"), "var(--c4)", W6) + '</g>'
             + f'<g>{_n13_off(AP[k])}' + pill(x + W / 2, Y + 288, sl["approve"][0], "var(--dim)", ctx, 15, W - 24, "dato pending", 14) + '</g>'
             + f'<g opacity="0">{_n13_on(AP[k])}' + pill(x + W / 2, Y + 288, sl["approve"][1], ok, ctx, 15, W - 24, "dato approved", 14) + '</g>'
             + _b14_ping(x + W / 2, Y + 288, 20, 70, AP[k], ok))
        stages.append(c)
    g.append(seq(stages, .2, .5, 16))
    # the data person with the tablet: «Aprobar», tapped once per stage
    flashes = "".join(f'<g opacity="0">{beat("opacity", [(0, 0), (t, 0), (t + .005, 1), (t + .035, 1), (t + .045, 0), (1, 0)])}'
                      f'<rect x="-44" y="-5" width="88" height="34" rx="17" fill="{ok}"/>{check(0, 13, .7, "var(--ink)")}</g>'
                      f'<circle cx="30" cy="12" r="6" fill="none" stroke="var(--white)" stroke-width="1.5" opacity="0">{beat("r", [(0, 6), (t - .012, 6), (t + .05, 34), (1, 34)])}'
                      f'{beat("opacity", [(0, 0), (t - .012, 0), (t - .008, 1), (t + .05, 0), (1, 0)])}</circle>' for t in TAP)
    tap = pill(0, 12, sl["tap"], "var(--c4)", ctx, 15, 104, "dato tap", 12) + flashes
    people = (f'<clipPath id="d05-desk"><rect x="760" y="0" width="840" height="{desk + 2}"/></clipPath>'
              f'<g clip-path="url(#d05-desk)">' + land(_d05_person(mnx, mny, SKIN_LIGHT, "var(--c1)", tap), .5, .6, 40) + '</g>')
    console = land(f'<path d="M820 {desk} H1170 L1160 828 H830 Z" fill="var(--card)"/>'
                   f'<path d="M820 {desk} H1170" stroke="var(--c2)" stroke-width="1.5" opacity=".7"/>', .3, .5, 20)
    beams = ""
    for k, cx in enumerate(cxs):
        d = f"M1046 668 C1046 560 {cx} 560 {cx} {Y + H - 14}"
        beams += (f'<g opacity="0">{beat("opacity", [(0, 0), (TAP[k], 0), (TAP[k] + .003, .9), (AP[k], .9), (AP[k] + .03, 0), (1, 0)])}'
                  f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="1.5" stroke-linecap="round">'
                  f'{beat("stroke-dashoffset", [(0, 1), (TAP[k], 1), (AP[k], 0), (1, 0)])}</path></g>'
                  + _n13_ride(d, TAP[k], AP[k], 5))
    lab = sl["label"]
    label = (f'<circle cx="1196" cy="690" r="15" fill="{ok}"/>{check(1196, 691, .6, "var(--ink)")}'
             + _d01_wrap(1224, 698, lab, 326, 22, "var(--white)", "dato label"))
    return "".join(g) + people + console + beams + land(label, 1.2, .5, 10), D, FREEZE


# ---------------------------------------------------------------- 6 · caso-reporte: 20 minutes by hand, 160 seconds with an agent
def _d06_clock(x, y):
    """A small clock whose hand keeps turning: the manual path takes its time."""
    s = 'fill="none" stroke="var(--muted)" stroke-width="1.8" stroke-linecap="round"'
    return (f'<circle cx="{x}" cy="{y}" r="12" {s}/><path d="M{x} {y} V{y - 7}" {s}>'
            f'<animateTransform attributeName="transform" type="rotate" values="0 {x} {y};360 {x} {y}" dur="6s" repeatCount="indefinite"/></path>'
            f'<path d="M{x} {y} H{x + 5}" {s}/>')


def _pd06_twin(sl, ctx):
    """d06 on the 900x1600 stage: the two panels stacked (before on top, after below), each with its fixed figure and
    sheet on the left, the steps in the middle and the person with the tablet on the right. Same beats as the desktop."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    PW, PH = zw, 420
    PYS = (zy + 44, zy + 44 + PH + 16)
    tasks = sl["tasks"]
    SLOW = [.06 + .15 * i for i in range(6)]
    FAST = [.10 + .012 * i for i in range(len(tasks))]
    READY, TAP, REV = .22, .34, .36
    art, text = [glow(zx + zw / 2, PYS[1] + 200, 360, "var(--c4)", .14), glow(zx + zw / 2, PYS[0] + 200, 380, "var(--brand)", .35)], []
    tag = sl["tag"]
    text.append(land(T(zx, zy + 26, tag, fit(tag, 22, zw, "reporte tag", floor=20), "var(--muted)", W6), .1, .5, 8))
    rides, top = [], []
    for side, (y0, (cap, fig, how)) in enumerate(zip(PYS, sl["sides"])):
        after = side == 1
        x0 = zx
        col = "var(--c4)" if after else "var(--muted)"
        panel = (card(x0, y0, PW, PH, "color-mix(in srgb, var(--c4) 6%, var(--card))" if after else "var(--dim)",
                      "var(--c4)" if after else "var(--line)", 18, 1.6 if after else 1.2)
                 + (spark(x0 + PW - 32, y0 + 34, .7) if after else _d06_clock(x0 + PW - 32, y0 + 34)))
        words = (T(x0 + 24, y0 + 42, cap, fit(cap, 24, PW - 90, "reporte caption", floor=20), col, W6)
                 + TC(x0 + 150, y0 + 138, fig, fit(fig, 80, 260, "reporte figure", floor=20), col, W6)
                 + TCW(x0 + 150, y0 + 180, how, 25, 20, "var(--white)" if after else "var(--muted)", W6, 1.2))
        # the sheet the steps fill, under the figure
        dx, dy, dw, dh = x0 + 24, y0 + 262, 96, 142
        sheet = (card(dx, dy, dw, dh, "var(--card)", "var(--line)", 8, 1.2)
                 + f'<path d="M{dx + dw - 18} {dy} V{dy + 18} H{dx + dw}" fill="none" stroke="var(--line)" stroke-width="1.2"/>')
        rows = ""
        for i, name in enumerate(tasks):
            y = y0 + 90 + i * 32
            mx = x0 + 316
            by_ = dy + 22 + i * 14
            bw_ = (dw - 24) * (.9, .7, .82, .6, .88, .74, .8, .5)[i]
            sheet += f'<rect x="{dx + 12}" y="{by_}" width="{bw_:.0f}" height="6" rx="3" fill="none" stroke="var(--line)" stroke-width="1" stroke-dasharray="2 3"/>'
            z = fit(name, 20, 220, "reporte task", floor=20)
            ring = f'<circle cx="{mx}" cy="{y - 7}" r="9" fill="none" stroke="var(--c2)" stroke-width="1.3" stroke-dasharray="2 3"/>'
            if after:
                t = FAST[i]
                rows += (ring + T(mx + 20, y, name, z, "var(--muted)", W6)
                         + f'<g opacity="0">{_n13_on(t)}' + T(mx + 20, y, name, z, "var(--white)", W6)
                         + f'<circle cx="{mx}" cy="{y - 7}" r="10" fill="{ok}"/>{check(mx, y - 6, .67, "var(--ink)")}</g>')
                sheet += f'<rect x="{dx + 12}" y="{by_}" width="{bw_:.0f}" height="6" rx="3" fill="var(--c4)" opacity="0">{_n13_on(t + .004, hi=.85)}</rect>'
                continue
            rows += ring + T(mx + 20, y, name, z, "var(--muted)", W6)
            if i >= len(SLOW):
                continue
            s0, s1 = SLOW[i], SLOW[i] + .15
            rows += (f'<g opacity="0">{_n13_on(s0, s1)}<circle cx="{mx}" cy="{y - 7}" r="9" fill="none" stroke="var(--c4)" stroke-width="1.8">'
                     f'{loop("r", "7;10;7", 1.2)}</circle>' + T(mx + 20, y, name, z, "var(--c4)", W6) + '</g>'
                     f'<g opacity="0">{_n13_on(s1)}{check(mx, y - 6, .55, "var(--muted)")}' + T(mx + 20, y, name, z, "var(--white)", W6) + '</g>')
            sheet += f'<rect x="{dx + 12}" y="{by_}" width="{bw_:.0f}" height="6" rx="3" fill="var(--c2)" opacity="0">{_n13_on(s1, hi=.7)}</rect>'
        if after:
            sheet += (f'<rect x="{dx}" y="{dy}" width="{dw}" height="{dh}" rx="8" fill="none" stroke="{ok}" stroke-width="1.8" opacity="0">{_n13_on(READY)}</rect>'
                      + f'<g opacity="0">{_n13_on(READY)}' + pill(dx + dw + 90, dy + dh - 24, sl["ready"], ok, ctx, 20, 170, "reporte ready", 10) + '</g>')
            rides.append(_d05_agent(f"M{x0 + 316} {y0 + 64} V{y0 + 90 + 7 * 32} C{x0 + 316} {y0 + 380} {dx + 160} {dy + 40} {dx + dw / 2} {dy + dh / 2}",
                                    FAST[0] - .02, READY))
        # the person at the desk, on the right
        mnx, mny = x0 + 628, y0 + 236
        if after:
            tap = (f'<g>{_n13_off(REV)}' + pill(0, 12, sl["review"][0], "var(--c4)", ctx, 20, 112, "reporte review", 10) + '</g>'
                   + f'<g opacity="0">{_n13_on(REV)}' + pill(0, 12, sl["review"][1], ok, ctx, 20, 112, "reporte reviewed", 10) + '</g>')
            skin, shirt = SKIN_BROWN, "var(--c1)"
            rides.append(_n13_ride(f"M{dx + dw} {dy + dh / 2} C{dx + 300} {dy + dh} {mnx + 60} {mny + 140} {mnx + 112} {mny + 74}", READY + .02, TAP - .01, 7))
        else:
            grid = "".join(f'<path d="M-46 {y} H46" stroke="var(--c2)" stroke-width="1" opacity=".45"/>' for y in (0, 12, 24))
            grid += "".join(f'<path d="M{x} -4 V28" stroke="var(--c2)" stroke-width="1" opacity=".45"/>' for x in (-16, 16))
            tap = grid + f'<rect x="18" y="13" width="2" height="9" fill="var(--c4)">{blink(1.0)}</rect>'
            skin, shirt = SKIN_LIGHT, shade("var(--c1)", 35)
        clip = f"pd06-desk-{side}"
        top.append(f'<clipPath id="{clip}"><rect x="{x0 + 2}" y="{y0}" width="{PW - 4}" height="{PH - 26}"/></clipPath>'
                   f'<g clip-path="url(#{clip})">' + land(_d05_person(mnx, mny, skin, shirt, tap), .7 + .1 * side, .6, 30) + '</g>')
        art.append(land(panel, .2 + .15 * side, .5, 14) + land(sheet, .45 + .15 * side, .5, 10))
        text.append(land(words + rows, .45 + .15 * side, .5, 10))
    return portrait_mark("".join(art) + "".join(text) + "".join(top) + "".join(rides)), D, FREEZE


@register("scene", "d06_reporte")
def sc_d06_reporte(sl, ctx):
    """Two panels side by side with their static figures: «20 min» (before, dim) and «160 s» (after, lit). The figures
    never move. Left: a faceless person assembles the report by hand, one small step at a time (the current step pulses,
    the sheet fills a line per step) and the loop ends with the path still going. Right: the agent ticks the same steps in
    a breath, the report is ready, it goes down to a faceless person's tablet and the person taps «Revisado». Frozen
    frame: the report ready and reviewed on the right; on the left the sixth step still in progress."""
    if ORIENT() == "portrait":
        return _pd06_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    PXS, PW, PY, PH = (832, 1208), 344, 138, 662
    tasks = sl["tasks"]
    SLOW = [.06 + .15 * i for i in range(6)]          # the manual path: a step every 1.8 s; steps 7 and 8 never start
    FAST = [.10 + .012 * i for i in range(len(tasks))]
    READY, TAP, REV = .22, .34, .36
    g = [glow(1380, 330, 330, "var(--c4)", .14), glow(1000, 420, 360, "var(--brand)", .35)]
    tag = sl["tag"]
    g.append(land(T(832, 114, tag, fit(tag, 16, 700, "reporte tag"), "var(--muted)", W6), .1, .5, 8))
    rides, top = [], []
    for side, (x0, (cap, fig, how)) in enumerate(zip(PXS, sl["sides"])):
        after = side == 1
        col = "var(--c4)" if after else "var(--muted)"
        panel = (card(x0, PY, PW, PH, "color-mix(in srgb, var(--c4) 6%, var(--card))" if after else "var(--dim)",
                      "var(--c4)" if after else "var(--line)", 18, 1.6 if after else 1.2)
                 + T(x0 + 22, PY + 40, cap, fit(cap, 18, PW - 90, "reporte caption"), col, W6)
                 + (spark(x0 + PW - 32, PY + 34, .6) if after else _d06_clock(x0 + PW - 32, PY + 34))
                 + TC(x0 + PW / 2, PY + 124, fig, fit(fig, 76, PW - 44, "reporte figure"), col, W6)
                 + _d01_wrap(x0 + PW / 2, PY + 162, how, PW - 44, 16, "var(--white)" if after else "var(--muted)", "reporte how", "middle"))
        # the steps and the sheet they fill
        rows, sheet = "", ""
        dx, dy, dw, dh = x0 + 226, PY + 214, 94, 150
        sheet += (card(dx, dy, dw, dh, "var(--card)", "var(--line)", 8, 1.2)
                  + f'<path d="M{dx + dw - 18} {dy} V{dy + 18} H{dx + dw}" fill="none" stroke="var(--line)" stroke-width="1.2"/>')
        for i, name in enumerate(tasks):
            y = PY + 226 + i * 27
            mx = x0 + 30
            by_ = dy + 26 + i * 15
            bw_ = (dw - 24) * (.9, .7, .82, .6, .88, .74, .8, .5)[i]
            sheet += f'<rect x="{dx + 12}" y="{by_}" width="{bw_:.0f}" height="6" rx="3" fill="none" stroke="var(--line)" stroke-width="1" stroke-dasharray="2 3"/>'
            z = fit(name, 15, 176, "reporte task")
            if after:
                t = FAST[i]
                rows += (f'<circle cx="{mx}" cy="{y - 5}" r="7" fill="none" stroke="var(--c2)" stroke-width="1.3" stroke-dasharray="2 3"/>'
                         f'<g>{_n13_off(t)}' + T(mx + 16, y, name, z, "var(--muted)", W6) + '</g>'
                         f'<g opacity="0">{_n13_on(t)}' + T(mx + 16, y, name, z, "var(--white)", W6) + '</g>'
                         + _b14_ok_dot(mx, y - 5, t, ok, 8))
                sheet += f'<rect x="{dx + 12}" y="{by_}" width="{bw_:.0f}" height="6" rx="3" fill="var(--c4)" opacity="0">{_n13_on(t + .004, hi=.85)}</rect>'
                continue
            if i >= len(SLOW):
                rows += (f'<circle cx="{mx}" cy="{y - 5}" r="7" fill="none" stroke="var(--line)" stroke-width="1.3" stroke-dasharray="2 3"/>'
                         + T(mx + 16, y, name, z, "var(--muted)", W6))
                continue
            s0, s1 = SLOW[i], SLOW[i] + .15
            rows += (f'<circle cx="{mx}" cy="{y - 5}" r="7" fill="none" stroke="var(--line)" stroke-width="1.3" stroke-dasharray="2 3"/>'
                     f'<g opacity="0">{_n13_on(s0, s1)}<circle cx="{mx}" cy="{y - 5}" r="7" fill="none" stroke="var(--c4)" stroke-width="1.8">'
                     f'{loop("r", "5;8;5", 1.2)}</circle></g>'
                     f'<g opacity="0">{_n13_on(s1)}{check(mx, y - 4, .42, "var(--muted)")}</g>'
                     f'<g>{_n13_off(s0)}' + T(mx + 16, y, name, z, "var(--muted)", W6) + '</g>'
                     f'<g opacity="0">{_n13_on(s0, s1)}' + T(mx + 16, y, name, z, "var(--c4)", W6) + '</g>'
                     f'<g opacity="0">{_n13_on(s1)}' + T(mx + 16, y, name, z, "var(--white)", W6) + '</g>')
            sheet += f'<rect x="{dx + 12}" y="{by_}" width="{bw_:.0f}" height="6" rx="3" fill="var(--c2)" opacity="0">{_n13_on(s1, hi=.7)}</rect>'
        if after:
            sheet += (f'<rect x="{dx}" y="{dy}" width="{dw}" height="{dh}" rx="8" fill="none" stroke="{ok}" stroke-width="1.8" opacity="0">{_n13_on(READY)}</rect>'
                      + f'<g opacity="0">{_n13_on(READY)}' + pill(dx + dw / 2, dy + dh + 22, sl["ready"], ok, ctx, 15, dw + 30, "reporte ready", 12) + '</g>'
                      + _b14_ping(dx + dw / 2, dy + dh / 2, 30, 90, READY, ok))
            rides.append(_d05_agent(f"M{x0 + 30} {PY + 200} V{PY + 226 + 7 * 27} C{x0 + 30} {PY + 460} {dx - 30} {dy + 40} {dx + dw / 2} {dy + dh / 2}",
                                    FAST[0] - .02, READY))
            rides.append(_n13_ride(f"M{dx + dw / 2} {dy + dh + 40} C{dx + dw / 2} {dy + dh + 110} {x0 + 250} 640 {x0 + 222} 690", READY + .02, TAP - .01, 6))
        # the person at the desk
        mnx, mny = x0 + 110, 668
        if after:
            tap = (f'<g>{_n13_off(REV)}' + pill(0, 12, sl["review"][0], "var(--c4)", ctx, 15, 104, "reporte review", 12) + '</g>'
                   + f'<g opacity="0">{_n13_on(REV)}' + pill(0, 12, sl["review"][1], ok, ctx, 15, 108, "reporte reviewed", 12) + '</g>'
                   + f'<circle cx="30" cy="12" r="6" fill="none" stroke="var(--white)" stroke-width="1.5" opacity="0">{beat("r", [(0, 6), (TAP, 6), (TAP + .06, 34), (1, 34)])}'
                     f'{beat("opacity", [(0, 0), (TAP, 0), (TAP + .004, 1), (TAP + .06, 0), (1, 0)])}</circle>')
            skin, shirt = SKIN_BROWN, "var(--c1)"
        else:
            grid = "".join(f'<path d="M-46 {y} H46" stroke="var(--c2)" stroke-width="1" opacity=".45"/>' for y in (0, 12, 24))
            grid += "".join(f'<path d="M{x} -4 V28" stroke="var(--c2)" stroke-width="1" opacity=".45"/>' for x in (-16, 16))
            tap = grid + f'<rect x="18" y="13" width="2" height="9" fill="var(--c4)">{blink(1.0)}</rect>'
            skin, shirt = SKIN_LIGHT, shade("var(--c1)", 35)
        clip = f"d06-desk-{side}"
        top.append(f'<clipPath id="{clip}"><rect x="{x0 + 2}" y="{PY}" width="{PW - 4}" height="{782 - PY}"/></clipPath>'
                   f'<g clip-path="url(#{clip})">' + land(_d05_person(mnx, mny, skin, shirt, tap), .7 + .1 * side, .6, 30) + '</g>'
                   + land(f'<path d="M{x0 + 16} 782 H{x0 + PW - 16}" stroke="var(--c2)" stroke-width="1.5" opacity=".6"/>', .6, .4, 0))
        g.append(land(panel, .2 + .15 * side, .5, 14) + land(sheet + rows, .45 + .15 * side, .5, 10))
    return "".join(g) + "".join(top) + "".join(rides), D, FREEZE
