"""Group D, slides 10-12 of the energía deck: who we are, how we decide, how to start. Each scene lands once inside 2 s
and then tells a 12-second story in loop with beat() (explicit keyTimes), like sc_controlroom. The frame at 0.9 of the
loop (reduced motion) is the resolved one, and the static markup holds that same pose. The resolved state stays until
the loop ends and the next cycle clears it in its first half second, so the story always holds to the last frame; on the
first pass that clearing happens under the entrance and the stage starts empty."""


def _n10_tr(pairs, period=D):
    """A translate loop with explicit times: pairs = [(fraction of the period, (dx, dy))], eased between stops."""
    kt = ";".join(f"{t:.3f}" for t, v in pairs)
    vals = ";".join(f"{v[0]:.1f} {v[1]:.1f}" for t, v in pairs)
    spl = ";".join(["0.45 0 0.55 1"] * (len(pairs) - 1))
    return (f'<animateTransform attributeName="transform" type="translate" values="{vals}" keyTimes="{kt}" dur="{period}s" '
            f'repeatCount="indefinite" calcMode="spline" keySplines="{spl}"/>')


_N10_CLEAR = .04  # the fraction of the loop in which a new cycle clears the resolved state of the last one (0.48 s)


def _n10_on(a):
    """Opacity pairs: on at the loop's start (the last cycle's resolved state), cleared by _N10_CLEAR, on again from a."""
    return [(0, 1), (_N10_CLEAR, 0), (a, 0), (a + .008, 1), (1, 1)]


def _n10_ping(x, y, r0, r1, a, color="var(--c4)", width=2):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r0}" fill="none" stroke="{color}" stroke-width="{width}" opacity="0">'
            f'{beat("r", [(0, r0), (a, r0), (a + .06, r1), (1, r1)])}'
            f'{beat("opacity", [(0, 0), (a - .002, 0), (a, .9), (a + .06, 0), (1, 0)])}</circle>')


# ---------------------------------------------------------------- faceless people, in the control-room style
_N10_SKIN_MID = f"color-mix(in srgb, {SKIN_BROWN} 50%, {SKIN_LIGHT})"
_N10_HAIR2 = "color-mix(in srgb, var(--c3) 26%, var(--ink))"
_N10_DISC = "color-mix(in srgb, var(--c2) 24%, var(--card))"
_N10_RIM = 'fill="none" stroke="var(--c2)" stroke-width="1.2" opacity=".55"'


def _n10_bust(skin, jacket, hair, kind):
    """A faceless bust, three-quarter view facing right, drawn around (0, 0) for a badge of radius 46 (the caller clips
    it). kind «long»: long hair and an earring; «short»: short hair and a thin headset."""
    g = []
    if kind == "long":
        g.append(f'<path d="M-18 -21 C-23 -45 3 -56 17 -43 C23 -37 22 -27 20 -21 L14 -26 C5 -33 -5 -32 -9 -23 C-11 -12 -10 2 -13 14 '
                 f'C-15 24 -25 31 -29 23 C-32 14 -23 1 -21 -8 C-20 -13 -19 -17 -18 -21 Z" fill="{hair}"/>'
                 f'<path d="M-9 -23 C-11 -12 -10 2 -13 14 C-15 24 -25 31 -29 23" {_N10_RIM}/>')
    jd = "M-46 60 C-46 32 -31 16 -9 13 C-3 12 7 12 13 13 C35 16 50 32 50 60 Z"
    g.append(f'<path d="{jd}" fill="{jacket}"/><path d="{jd}" {_N10_RIM}/>')
    g.append('<path d="M-5 13 L3 26 L11 13 Z" fill="var(--white)" opacity=".92"/>')
    g.append(f'<path d="M-6 -6 C-5 2 -5 8 -6 14 C-1 17 6 17 10 14 C8 8 8 2 8 -6 Z" fill="{shade(skin, 14)}"/>')
    g.append(f'<path d="M-10 -22 C-11 -39 2 -45 13 -40.5 C21 -37 23 -28 21 -20 C20 -13.5 17 -7.5 12 -4 C6.5 -.5 -1.5 -1.5 -6.5 -7 '
             f'C-10 -11.5 -10 -16.5 -10 -22 Z" fill="{skin}"/>')
    g.append(f'<ellipse cx="-5.5" cy="-19" rx="2.5" ry="4" fill="{shade(skin, 14)}"/>')
    if kind == "long":
        g.append('<circle cx="-5.5" cy="-13.5" r="1.6" fill="var(--c4)"/>')
        g.append(f'<path d="M-11 -25 C-10 -42 7 -48 18 -39 C21.5 -35.5 21.5 -32 20.5 -29 C15 -35.5 6 -37 -1 -33.5 C-5.5 -31 -8 -27 -9.5 -21.5 Z" fill="{hair}"/>')
        g.append(f'<path d="M-6 -39 C2 -44.5 12 -42.5 16.5 -37" {_N10_RIM}/>')
    else:
        g.append(f'<path d="M-13 -20 C-15 -41 3 -50 16 -42.5 C21.5 -39 23 -34 22 -30.5 C17.5 -35 10 -36.5 4 -35.5 C-1 -34.5 -4.5 -31.5 -6 -26 '
                 f'C-7 -23 -8.5 -20.5 -10.5 -17.5 Z" fill="{hair}"/><path d="M-12 -28 C-10 -41 4 -46 15 -41.5" {_N10_RIM}/>')
        g.append('<path d="M-15 -22 C-13 -45 14 -49 20.5 -32" fill="none" stroke="var(--c4)" stroke-width="1.6" stroke-linecap="round"/>'
                 '<rect x="-10.5" y="-24" width="6" height="11" rx="2.5" fill="var(--c4)"/>'
                 '<path d="M-6 -14 C0 -7 7 -6 13.5 -7" fill="none" stroke="var(--c4)" stroke-width="1.2" stroke-linecap="round"/>')
    return "".join(g)


def _n10_face(clip, skin, jacket, hair, kind, r=46):
    """The bust inside its round badge (clip: the id of a clipPath circle of radius 46 in this slide's svg)."""
    return (f'<circle r="{r}" fill="{_N10_DISC}" stroke="var(--line)" stroke-width="1.5"/>'
            f'<g transform="scale({r / 46:.3f})"><g clip-path="url(#{clip})"><g transform="translate(-4 9)">{_n10_bust(skin, jacket, hair, kind)}</g></g></g>')


_N10_PEOPLE = ((SKIN_BROWN, "var(--accent)", HAIR, "long"), (SKIN_LIGHT, "var(--c1)", HAIR, "short"),
               (_N10_SKIN_MID, "var(--c3)", _N10_HAIR2, "long"), (SKIN_BROWN, "var(--c2)", HAIR, "short"),
               (SKIN_LIGHT, "var(--c1)", _N10_HAIR2, "long"), (_N10_SKIN_MID, "var(--accent)", HAIR, "short"))


# ---------------------------------------------------------------- portrait (0.5.0): the mobile build draws on 900x1600
# Under ORIENT() == "portrait" these scenes recompose on CANVAS() inside ART_ZONE() and return portrait_mark(svg); the
# desktop branch is untouched. A piece drawn in desktop units is placed with _pz at a scale that keeps its smallest
# label at 18 canvas units or more (10 px at 1440x900, where the 900x1600 stage is scaled 0.5625).
def _pz(inner, s, x, y, ox=0, oy=0):
    """inner, drawn in desktop units from its origin (ox, oy), placed at (x, y) of the portrait canvas at scale s."""
    return f'<g transform="translate({x:.1f} {y:.1f}) scale({s:.4f}) translate({-ox:.1f} {-oy:.1f})">{inner}</g>'


def _pz_clip(art, cid):
    """The art of a portrait scene, clipped under the text zone (a glow never climbs behind the title)."""
    zx, zy, zw, zh = ART_ZONE("left")
    return portrait_mark(f'<clipPath id="{cid}"><rect x="0" y="{zy - 30}" width="900" height="{zh + 50}"/></clipPath>'
                         f'<g clip-path="url(#{cid})">{art}</g>')


def _pz_fit(svg, box, cid):
    """A desktop composition that is already vertical, its art inside box (x, y, w, h): scaled into the portrait art
    zone as large as it fits, centred."""
    zx, zy, zw, zh = ART_ZONE("left")
    bx, by, bw, bh = box
    s = min(zw / bw, zh / bh)
    return _pz_clip(_pz(svg, s, zx + (zw - bw * s) / 2, zy + (zh - bh * s) / 2, bx, by), cid)


# ---------------------------------------------------------------- 10 · who we are
@register("scene", "m10_quienes")
def m10_quienes(sl, ctx):
    """12.000 people, augmented by AI and connected across countries. The figure never moves. Six faceless colleagues
    sit on the orbit of slides 6 and 9; an AI spark travels the orbit and reaches them one by one: each lights up with
    its spark (augmented) and the trail it leaves joins them (connected). The halo behind the figure grows with every
    one reached (that is where the value is). The frozen frame: all six augmented, the ring closed, the halo full."""
    P = ORIENT() == "portrait"
    cx, cy, R, rb = 1190, 452, 300, 46
    ring = ellipse_path(cx, cy, R, R)
    arrive = [.12 + k * .125 for k in range(7)]  # node k reached at arrive[k]; arrive[6]: back at the top, ring closed
    halo_pts = [(0, .455), (_N10_CLEAR, .14)]
    for k, a in enumerate(arrive):
        halo_pts += [(a, .14 + k * .045), (a + .02, .14 + (k + 1) * .045)]
    halo_pts.append((1, .455))
    g = ['<defs><clipPath id="n10-badge"><circle r="46"/></clipPath></defs>', "" if P else glow(cx, cy, 430, "var(--brand)", .5)]  # portrait: no glow under the figure
    halo = f'<circle cx="{cx}" cy="{cy}" r="236" fill="var(--brand)" opacity=".455">{beat("opacity", halo_pts)}{loop("r", "232;246;232", 5)}</circle>'
    g.append(land(halo, .1, .6, 0))
    base = f'<path d="{ring}" fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="3 14" opacity=".6"/>'
    dots = "".join(f'<circle cx="{cx + R * math.cos(math.radians(-90 + 20 * j)):.1f}" cy="{cy + R * math.sin(math.radians(-90 + 20 * j)):.1f}" r="3.5" fill="var(--c2)"/>'
                   for j in range(18) if j % 3)
    g.append(land(base + dots, .05, .6, 0))
    # the trail the spark leaves: drawn as it goes, fully closed at arrive[6]
    off = [(0, 0), (_N10_CLEAR, 0), (_N10_CLEAR + .002, 1), (arrive[0] + .02, 1)]
    for k in range(1, 7):
        off += [(arrive[k], 1 - k / 6)] + ([(arrive[k] + .02, 1 - k / 6)] if k < 6 else [])
    off.append((1, 0))
    trail = (f'<path d="{ring}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="2.5" stroke-linecap="round">'
             f'{beat("stroke-dashoffset", off)}{beat("opacity", [(0, 1), (_N10_CLEAR, 0), (_N10_CLEAR + .002, 0), (_N10_CLEAR + .004, 1), (1, 1)])}</path>')
    g.append(land(trail, .5, .3, 0))
    closed = f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="var(--c4)" stroke-width="3" opacity="0">{beat("r", [(0, R), (arrive[6], R), (arrive[6] + .03, R + 22), (1, R + 22)])}{beat("opacity", [(0, 0), (arrive[6] - .002, 0), (arrive[6], .8), (arrive[6] + .03, 0), (1, 0)])}</circle>'
    g.append(closed)
    # the figure and its unit: static, never animated
    fig = TC(cx, cy + 20, sl["figure"], fit(sl["figure"], 130, 440, "who figure"), "var(--c4)", W6)
    unit = TC(cx, cy + 72, sl["label"], fit(sl["label"], 28, 440, "who label"), "var(--white)", W6)
    reach = TC(cx, cy + 108, sl["reach"], fit(sl["reach"], 22, 400, "who reach"), "var(--c2)", W6)
    g.append(land(fig + unit + reach, .3, .6, 14))
    # the AI spark, travelling the ring from one colleague to the next (hidden under each badge while it stops there)
    stops = [(0, 0), (arrive[0] + .02, 0)]
    for k in range(1, 7):
        stops += [(arrive[k], k / 6)] + ([(arrive[k] + .02, k / 6)] if k < 6 else [])
    stops.append((1, 1))
    g.append(f'<g opacity="0">{beat("opacity", [(0, 0), (arrive[0] - .03, 0), (arrive[0] - .01, 1), (arrive[6], 1), (arrive[6] + .02, 0), (1, 0)])}'
             f'{move(ring, stops, D)}{token("var(--c4)", 5)}{spark(0, 0, .55, "var(--c4)")}</g>')
    # six colleagues: each lights up (ring and spark badge) when the spark reaches it
    for k, (skin, jacket, hair, kind) in enumerate(_N10_PEOPLE):
        a = math.radians(-90 + 60 * k)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        c = f'<circle r="{rb + 9}" fill="none" stroke="var(--c2)" stroke-width="1" stroke-dasharray="2 6" opacity=".5"/>'
        c += _n10_face("n10-badge", skin, jacket, hair, kind, rb)
        c += (f'<g>{beat("opacity", _n10_on(arrive[k]))}<circle r="{rb + 3}" fill="none" stroke="var(--c4)" stroke-width="2.5"/>'
              f'<circle cx="{rb * .74:.1f}" cy="{-rb * .74:.1f}" r="13" fill="var(--c4)"/>{spark(rb * .74, -rb * .74, .5, "var(--ink)")}</g>')
        c += _n10_ping(0, 0, rb + 3, rb + 28, arrive[k])
        g.append(pop(c, x, y, .4 + k * .12, .45))
        if sl.get("roles"):  # the discipline of each colleague: multidisciplinary, one team
            role = sl["roles"][k]
            ly = y - rb - 24 if k == 3 else y + rb + 24
            g.append(land(pill(x, ly, role, "var(--dim)", ctx, 18 if P else 15, 190 if P else 170, "who role"), .9 + k * .08, .4, 8))
    if P:  # the orbit is already square: the same story, scaled to the art zone (roles 18 -> 21 units)
        return _pz_fit("".join(g), (835, 97, 710, 710), "pz-m10"), D, FREEZE
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 11 · how we decide
def _n11_bulb(color="var(--c4)"):
    return (f'<path d="M-6 3 C-10 0 -10 -9 -5 -12 C-2 -14 2 -14 5 -12 C10 -9 10 0 6 3 L5 6 H-5 Z" fill="none" stroke="{color}" stroke-width="1.8" stroke-linejoin="round"/>'
            f'<path d="M-4 9 H4 M-2.5 12 H2.5" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/>')


def _n11_idea(text, x, y, verdict, t, lane, w=300, h=56):
    """One idea card at the evaluation spot (x, y). verdict: «ok» (it passes: a check and a stripe in the color of its reason) or
    «aside» (a pause mark, set aside politely); t: the fraction of the loop at which the verdict shows."""
    c = card(x, y, w, h, "var(--card)", "var(--c2)", 14, 1.5)
    ix, iy = x + 30, y + h / 2
    c += f'<circle cx="{ix}" cy="{iy}" r="16" fill="var(--dim)" stroke="var(--line)" stroke-width="1.2"/>'
    c0, c1 = _N10_CLEAR, _N10_CLEAR + .004
    before, after = [(0, 0), (c0, 0), (c1, 1), (t, 1), (t + .008, 0), (1, 0)], [(0, 1), (c0, 1), (c1, 0), (t, 0), (t + .008, 1), (1, 1)]
    c += f'<g opacity="0">{beat("opacity", before)}<g transform="translate({ix} {iy + 1})">{_n11_bulb()}</g></g>'
    if verdict == "ok":
        c += (f'<g>{beat("opacity", after)}<circle cx="{ix}" cy="{iy}" r="16" fill="{lane}"/>{check(ix, iy + 1, .62, "var(--ink)")}'
              f'<rect x="{x + 1.5}" y="{y + 12}" width="4" height="{h - 24}" rx="2" fill="{lane}"/></g>')
    else:
        c += (f'<g>{beat("opacity", after)}<rect x="{ix - 6}" y="{iy - 7}" width="4" height="14" rx="1.5" fill="var(--muted)"/>'
              f'<rect x="{ix + 2}" y="{iy - 7}" width="4" height="14" rx="1.5" fill="var(--muted)"/></g>')
    c += T(x + 58, y + h / 2 + 6.5, text, fit(text, 18, w - 74, "idea card"), "var(--white)", W6)
    return c


@register("scene", "m11_criterio")
def m11_criterio(sl, ctx):
    """How we decide, as a sorting loop. Ideas arrive one by one under the two criteria. The first («Priorizar
    alarmas») lights «Retorno claro» and goes to «Construimos»; the second («Una demo vistosa») lights neither and is
    set aside, politely, under «Por ahora, no»; the third («TI que entrega más rápido») lights «Habilitador clave» and
    is built too. Between ideas the empty spot asks «¿Retorno o habilitador?». The frozen frame: two ideas built, each
    checked in the color of its reason, one set aside, an empty slot and the question waiting for the next idea."""
    P = ORIENT() == "portrait"
    ok = ctx.brand.c("dark.ok")
    cols = (ok, "var(--c2)")
    cw, ch, cy0, cxs = 334, 222, 96, (846, 1208)
    mid = 1194
    ex, ey, ew, eh = 1044, 372, 300, 56           # the evaluation spot, under the «o»
    zy, zh = 506, 290                             # «Construimos»; the tray for the rest is shorter (it starts at ay)
    ay = 640
    slot = lambda k: 684 - k * 70                 # slots stack upwards from the zone's base
    g = [] if P else [glow(1194, 440, 440, "var(--brand)", .45)]  # portrait: no glow under the ask
    ideas = sl["ideas"]                           # [[text, verdict («retorno» | «habilitador» | «no»)], ...]
    starts = (.10, .36, .62)
    lock = {"retorno": 0, "habilitador": 1}
    # criteria: the matching card glows while its idea is judged, and keeps its check once one has passed through it
    cards = []
    for k, ((name, text), col) in enumerate(zip(sl["criteria"], cols)):
        x = cxs[k]
        c = card(x, cy0, cw, ch, "var(--card)", col, 18, 2)
        if k == 0:
            c += "".join(f'<rect x="{x + 28 + j * 26}" y="{cy0 + 86 - hh}" width="17" height="{hh}" rx="4" fill="{col}"/>' for j, hh in enumerate((22, 38, 56)))
        else:
            c += (f'<rect x="{x + 28}" y="{cy0 + 74}" width="84" height="12" rx="4" fill="{col}"/>'
                  + "".join(f'<rect x="{x + 33 + j * 42}" y="{cy0 + 36}" width="32" height="32" rx="4" fill="none" stroke="{col}" stroke-width="2.5"/>' for j in range(2)))
        c += T(x + 28, cy0 + 128, name, fit(name, 26, cw - 56, "criterion name"), "var(--white)", W6)
        c += TCW(x + 28, cy0 + 164, text, 30, 18, "var(--muted)", W6, 1.35, "start")
        cards.append(c)
    g.append(seq(cards, .1, .5, 16))
    orb = (f'<circle cx="{mid}" cy="{cy0 + ch / 2}" r="28" fill="var(--dim)" stroke="var(--c4)" stroke-width="2">{loop("stroke-opacity", ".3;1;.3", 3)}</circle>'
           + TC(mid, cy0 + ch / 2 + 8, sl["or"], 22, "var(--white)", W6))
    marks = []
    for k, col in enumerate(cols):
        x = cxs[k]
        t = next((starts[j] + .09 for j, (_t, v) in enumerate(ideas) if lock.get(v) == k), None)
        if t is None:
            continue
        marks.append(f'<rect x="{x}" y="{cy0}" width="{cw}" height="{ch}" rx="18" fill="none" stroke="{col}" stroke-width="4" opacity="0">'
                     f'{beat("opacity", [(0, 0), (t - .01, 0), (t, 1), (t + .14, 1), (t + .17, 0), (1, 0)])}</rect>')
        marks.append(f'<g>{beat("opacity", _n10_on(t + .015))}<circle cx="{x + cw - 34}" cy="{cy0 + 34}" r="17" fill="{col}"/>{check(x + cw - 34, cy0 + 35, .7, "var(--ink)")}</g>')
        marks.append(_n10_ping(x + cw - 34, cy0 + 34, 17, 40, t + .015, col))
    g.append(land("".join(marks) + orb, .7, .4, 0))
    # beams from the evaluation spot up to each criterion, and the two lanes down to the outcomes
    beam = [f"M{ex + 76} {ey} C{ex + 76} {ey - 28} {cxs[0] + cw / 2} {cy0 + ch + 26} {cxs[0] + cw / 2} {cy0 + ch + 2}",
            f"M{ex + ew - 76} {ey} C{ex + ew - 76} {ey - 28} {cxs[1] + cw / 2} {cy0 + ch + 26} {cxs[1] + cw / 2} {cy0 + ch + 2}"]
    lane = [f"M{ex + 56} {ey + eh} C{ex + 56} {ey + eh + 44} {cxs[0] + cw / 2} {zy - 40} {cxs[0] + cw / 2} {zy}",
            f"M{ex + ew - 56} {ey + eh} C{ex + ew - 56} {ey + eh + 44} {cxs[1] + cw / 2} {ay - 70} {cxs[1] + cw / 2} {ay}"]
    rails = "".join(f'<path d="{d}" fill="none" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 7"/>' for d in beam + lane)
    spot = (f'<rect x="{ex}" y="{ey}" width="{ew}" height="{eh}" rx="14" fill="none" stroke="var(--c4)" stroke-width="1.5" stroke-dasharray="6 7" opacity=".7">'
            f'{loop("stroke-opacity", ".35;1;.35", 3)}</rect>')
    away = [(0, 1)] + [p for s in starts for p in ((s + .02, 1), (s + .04, 0), (s + .19, 0), (s + .22, 1))] + [(1, 1)]
    spot += f'<g>{beat("opacity", away)}' + TC(ex + ew / 2, ey + eh / 2 + 6, sl["ask"], fit(sl["ask"], 17, ew - 40, "criterion ask"), "var(--muted)", W6) + '</g>'
    g.append(land(rails + spot, .75, .5, 0))
    lit = []
    for j, ((text, verdict), s) in enumerate(zip(ideas, starts)):
        if verdict in lock:
            k = lock[verdict]
            lit.append(f'<path d="{beam[k]}" fill="none" stroke="{cols[k]}" stroke-width="3" stroke-linecap="round" opacity="0">'
                       f'{beat("opacity", [(0, 0), (s + .07, 0), (s + .09, 1), (s + .2, 1), (s + .23, 0), (1, 0)])}</path>')
            lit.append(f'<path d="{lane[0]}" fill="none" stroke="{ok}" stroke-width="3" stroke-linecap="round" opacity="0">'
                       f'{beat("opacity", [(0, 0), (s + .16, 0), (s + .17, 1), (s + .23, 1), (s + .25, 0), (1, 0)])}</path>')
        else:  # it is judged against both, and neither holds
            for k in range(2):
                a = s + .07 + k * .03
                lit.append(f'<path d="{beam[k]}" fill="none" stroke="var(--c4)" stroke-width="2.5" stroke-linecap="round" opacity="0">'
                           f'{beat("opacity", [(0, 0), (a, 0), (a + .01, .75), (a + .025, .75), (a + .035, 0), (1, 0)])}</path>')
            lit.append(f'<path d="{lane[1]}" fill="none" stroke="var(--muted)" stroke-width="2.5" stroke-linecap="round" opacity="0">'
                       f'{beat("opacity", [(0, 0), (s + .16, 0), (s + .17, .8), (s + .23, .8), (s + .25, 0), (1, 0)])}</path>')
    g.append("".join(lit))
    # the outcome zones: built ideas stack on «Construimos»; the rest rest under «Por ahora, no»
    zones = (card(cxs[0], zy, cw, zh, "none", ok, 18, 1.2, 'stroke-opacity=".55"')
             + f'<rect x="{cxs[0] + 17}" y="{slot(2)}" width="{ew}" height="{eh}" rx="14" fill="none" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="6 7" opacity=".55"/>'
             + pill(cxs[0] + cw / 2, zy + zh - 26, sl["build"], ok, ctx, 18, cw - 40, "criterion build")
             + card(cxs[1], ay, cw, zy + zh - ay, "none", "var(--line)", 18, 1.2)
             + pill(cxs[1] + cw / 2, zy + zh - 26, sl["aside"], "var(--dim)", ctx, 18, cw - 40, "criterion aside"))
    g.append(land(zones, .9, .5, 12))
    built, flow = 0, []
    for (text, verdict), s in zip(ideas, starts):
        if verdict in lock:
            dx, dy, fade, vt = cxs[0] + 17 - ex, slot(built) - ey, 1, s + .09
            built += 1
        else:
            dx, dy, fade, vt = cxs[1] + 17 - ex, slot(0) - ey, .6, s + .14
        c0 = _N10_CLEAR
        pos = [(0, (dx, dy)), (c0, (dx, dy)), (c0 + .004, (-190, 0)), (s, (-190, 0)), (s + .06, (0, 0)), (s + .17, (0, 0)), (s + .23, (dx, dy)), (1, (dx, dy))]
        op = [(0, fade), (c0, 0), (s, 0), (s + .03, 1), (s + .19, 1), (s + .23, fade), (1, fade)]
        flow.append(f'<g transform="translate({dx} {dy})" opacity="{fade}">{_n10_tr(pos)}{beat("opacity", op)}'
                     + _n11_idea(text, ex, ey, "ok" if verdict in lock else "aside", vt, cols[lock.get(verdict, 0)]) + '</g>')
    g.append(land("".join(flow), .5, .3, 0))
    if P:  # criteria over the verdict over the trays: already a stack; scaled to the art zone (ask 17 -> 20 units)
        return _pz_fit("".join(g), (844, 92, 700, 706), "pz-m11"), D, FREEZE
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 12 · how to start
@register("scene", "m12_formas")
def m12_formas(sl, ctx):
    """Four ways to start, and a need that picks its way. Under the columns a chip asks «¿Qué necesitan hoy?»; it
    becomes one need at a time (probar, velocidad, control, continuidad) and a spark climbs its branch to the way that
    answers it: the column lights and its promise is underlined. The frozen frame: the question back at the root and
    all four branches lit, every promise underlined: any of them is a way in, and they combine."""
    if ORIENT() == "portrait":
        return _pz_formas(sl, ctx, .18, .86, .855, "n12-badge"), D, FREEZE
    cols = ("var(--c1)", "var(--accent)", "var(--c3)", "var(--c2)")
    n, gap, y0, h = len(sl["models"]), 24, 404, 282
    w = (1408 - gap * (n - 1)) / n
    xs = [96 + k * (w + gap) for k in range(n)]
    rx, ry, rw, rh = 800, 788, 400, 50             # the root chip, centered at (rx, ry)
    starts = [.14 + k * .18 for k in range(n)]
    arrive = [s + .08 for s in starts]
    g = ['<defs><clipPath id="n12-badge"><circle r="46"/></clipPath></defs>', glow(800, 600, 560, "var(--brand)", .4)]
    parts, lines = [], []
    for k, (x, (name, promise, items), col) in enumerate(zip(xs, sl["models"], cols)):
        c = card(x, y0, w, h, "var(--card)", col, 18, 2)
        c += pill(x + 24 + min(w / 2 - 24, bold_width(_(str(name)), 17, current_factor()) / 2 + 18), y0 + 36, name, col, ctx, 17, w - 48, "model name")
        ps = fit(promise, 20, w - 48, "model promise")
        c += T(x + 24, y0 + 88, promise, ps, "var(--c4)", W6)
        for j, it in enumerate(items[:4]):
            c += f'<circle cx="{x + 30:.1f}" cy="{y0 + 130 + j * 40}" r="5" fill="{col}"/>' + T(x + 46, y0 + 136 + j * 40, it, fit(it, 17, w - 70, "model item"), "var(--white)")
        parts.append(c)
        uw = min(w - 48, bold_width(_(str(promise)), ps, current_factor()))
        lines.append(f'<rect x="{x + 24:.1f}" y="{y0 + 97}" width="{uw:.1f}" height="3" rx="1.5" fill="var(--c4)">{beat("opacity", _n10_on(arrive[k]))}</rect>')
    g.append(seq(parts, .1, .5, 20))
    g.append(land("".join(lines), .5, .3, 0))
    # the tree: one root, four branches up to the columns
    ends = [(x + w / 2, y0 + h + 4) for x in xs]
    branch = [f"M{rx} {ry - rh / 2} C{rx} {ry - rh / 2 - 40} {ex:.1f} {ey + 40} {ex:.1f} {ey}" for ex, ey in ends]
    base = "".join(f'<path d="{d}" fill="none" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 7"/>' for d in branch)
    base += "".join(f'<circle cx="{ex:.1f}" cy="{ey}" r="7" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>' for ex, ey in ends)
    g.append(land(base, .8, .5, 0))
    live = []
    for k, (d, (ex, ey), s, a) in enumerate(zip(branch, ends, starts, arrive)):
        live.append(f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="2.5" stroke-linecap="round">'
                    f'{beat("stroke-dashoffset", [(0, 0), (_N10_CLEAR, 0), (_N10_CLEAR + .002, 1), (s + .03, 1), (a, 0), (1, 0)])}'
                    f'{beat("opacity", [(0, 1), (_N10_CLEAR, 0), (_N10_CLEAR + .002, 0), (_N10_CLEAR + .004, 1), (1, 1)])}</path>')
        live.append(f'<circle cx="{ex:.1f}" cy="{ey}" r="7" fill="var(--c4)">{beat("opacity", _n10_on(a))}</circle>' + _n10_ping(ex, ey, 7, 30, a))
        live.append(f'<g opacity="0">{beat("opacity", [(0, 0), (s + .025, 0), (s + .03, 1), (a, 1), (a + .015, 0), (1, 0)])}'
                    f'{move(d, [(0, 0), (s + .03, 0), (a, 1), (1, 1)], D)}{token("var(--c4)", 5)}{spark(0, 0, .5, "var(--c4)")}</g>')
        e = arrive[k + 1] - .02 if k + 1 < n else .855
        live.append(f'<rect x="{xs[k] - 6:.1f}" y="{y0 - 6}" width="{w + 12:.1f}" height="{h + 12}" rx="22" fill="none" stroke="var(--c4)" stroke-width="3" opacity="0">'
                    f'{beat("opacity", [(0, 0), (a, 0), (a + .01, 1), (e, 1), (e + .015, 0), (1, 0)])}</rect>')
    g.append(land("".join(live), .5, .3, 0))
    # the root: one of their people (the operator of slide 14, headset on) and the question, which becomes one need at a time
    root = (card(rx - rw / 2, ry - rh / 2, rw, rh, "var(--dim)", "var(--c4)", rh / 2, 1.5)
            + f'<g transform="translate({rx - rw / 2 + 27} {ry})">{_n10_face("n12-badge", SKIN_LIGHT, "var(--c1)", HAIR, "short", 20)}</g>')
    tx = rx + 16
    q = sl["ask"]
    root += f'<g>{beat("opacity", [(0, 1), (starts[0], 1), (starts[0] + .01, 0), (.86, 0), (.87, 1), (1, 1)])}' + TC(tx, ry + 6.5, q, fit(q, 18, rw - 76, "need ask"), "var(--c4)", W6) + '</g>'
    for k, need in enumerate(sl["needs"][:n]):
        s = starts[k]
        e = starts[k + 1] if k + 1 < n else .86
        root += (f'<g opacity="0">{beat("opacity", [(0, 0), (s + .005, 0), (s + .015, 1), (e - .01, 1), (e, 0), (1, 0)])}'
                 + TC(tx, ry + 6.5, need, fit(need, 18, rw - 76, "need"), "var(--white)", W6) + '</g>')
    g.append(land(root, 1.0, .45, 12))
    return "".join(g), D, FREEZE


def _pz_formas(sl, ctx, step, back, e_last, clip, nxt=None, t_next=.80):
    """ways (m12) and ways-b (n12) in portrait: the four ways in a 2x2 grid (each column drawn as on desktop, scaled
    x1.19: items 17 -> 20 units), the root chip between the rows with a branch up or down to each way. The same beats:
    the question becomes one need at a time, a spark climbs its branch, the way lights and its promise is underlined; back
    is when the question returns. nxt (ways-b): the hand-off to the discovery, under the grid, reached down the gutter."""
    cols = ("var(--c1)", "var(--accent)", "var(--c3)", "var(--c2)")
    n, h = len(sl["models"]), 282
    w = (1408 - 24 * (n - 1)) / n                  # the desktop column
    zx, zy, zw, zh = ART_ZONE("top")
    gap, gm = 24, 150
    s = (zw - gap) / 2 / w
    cw, ch = w * s, h * s
    X, Y = (zx, zx + cw + gap), (zy + 8, zy + 8 + ch + gm)
    pos = [(X[k % 2], Y[k // 2]) for k in range(n)]
    starts = [.14 + k * step for k in range(n)]
    arrive = [a + .08 for a in starts]
    rx, ry, rw, rh = zx + zw / 2, Y[0] + ch + gm / 2, 480, 62
    g, cells = [f'<defs><clipPath id="{clip}"><circle r="46"/></clipPath></defs>'], []
    for k, ((name, promise, items), col, (px_, py_)) in enumerate(zip(sl["models"], cols, pos)):
        c = card(0, 0, w, h, "var(--card)", col, 18, 2)
        c += pill(24 + min(w / 2 - 24, bold_width(_(str(name)), 17, current_factor()) / 2 + 18), 36, name, col, ctx, 17, w - 48, "model name")
        ps = fit(promise, 20, w - 48, "model promise", floor=15)
        c += T(24, 88, promise, ps, "var(--c4)", W6)
        for j, it in enumerate(items[:4]):
            c += f'<circle cx="30" cy="{130 + j * 40}" r="5" fill="{col}"/>' + T(46, 136 + j * 40, it, fit(it, 17, w - 70, "model item", floor=15), "var(--white)")
        uw = min(w - 48, bold_width(_(str(promise)), ps, current_factor()))
        c += f'<rect x="24" y="97" width="{uw:.1f}" height="3" rx="1.5" fill="var(--c4)">{beat("opacity", _n10_on(arrive[k]))}</rect>'
        e = arrive[k + 1] - .02 if k + 1 < n else e_last
        c += (f'<rect x="-6" y="-6" width="{w + 12:.1f}" height="{h + 12}" rx="22" fill="none" stroke="var(--c4)" stroke-width="3" opacity="0">'
              f'{beat("opacity", [(0, 0), (arrive[k], 0), (arrive[k] + .01, 1), (e, 1), (e + .015, 0), (1, 0)])}</rect>')
        cells.append(_pz(c, s, px_, py_))
    g.append(seq(cells, .1, .5, 20))
    # the tree: from the root, two branches up to the first row and two down to the second
    top, bot = ry - rh / 2, ry + rh / 2
    ends = [(px_ + cw / 2, py_ + ch + 6) if k < 2 else (px_ + cw / 2, py_ - 6) for k, (px_, py_) in enumerate(pos)]
    branch = [f"M{rx:.1f} {top:.1f} C{rx:.1f} {top - 30:.1f} {ex:.1f} {ey + 30:.1f} {ex:.1f} {ey:.1f}" if k < 2 else
              f"M{rx:.1f} {bot:.1f} C{rx:.1f} {bot + 30:.1f} {ex:.1f} {ey - 30:.1f} {ex:.1f} {ey:.1f}" for k, (ex, ey) in enumerate(ends)]
    base = "".join(f'<path d="{d}" fill="none" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 7"/>' for d in branch)
    base += "".join(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="8" fill="var(--card)" stroke="var(--c4)" stroke-width="1.5"/>' for ex, ey in ends)
    g.append(land(base, .8, .5, 0))
    live = []
    for k, (d, (ex, ey), a0, a) in enumerate(zip(branch, ends, starts, arrive)):
        live.append(f'<path d="{d}" pathLength="1" stroke-dasharray="1" fill="none" stroke="var(--c4)" stroke-width="3" stroke-linecap="round">'
                    f'{beat("stroke-dashoffset", [(0, 0), (_N10_CLEAR, 0), (_N10_CLEAR + .002, 1), (a0 + .03, 1), (a, 0), (1, 0)])}'
                    f'{beat("opacity", [(0, 1), (_N10_CLEAR, 0), (_N10_CLEAR + .002, 0), (_N10_CLEAR + .004, 1), (1, 1)])}</path>')
        live.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="8" fill="var(--c4)">{beat("opacity", _n10_on(a))}</circle>' + _n10_ping(ex, ey, 8, 34, a))
        live.append(f'<g opacity="0">{beat("opacity", [(0, 0), (a0 + .025, 0), (a0 + .03, 1), (a, 1), (a + .015, 0), (1, 0)])}'
                    f'{move(d, [(0, 0), (a0 + .03, 0), (a, 1), (1, 1)], D)}{token("var(--c4)", 6)}{spark(0, 0, .6, "var(--c4)")}</g>')
    g.append(land("".join(live), .5, .3, 0))
    # the hand-off (ways-b): under the grid, reached down the gutter between the columns of the second row
    if nxt:
        ny = Y[1] + ch + 34
        z = fit(nxt, 22, zw - 100, "formas next", floor=18)
        nw = bold_width(_(str(nxt)), z, current_factor()) + 84
        nx0 = rx - nw / 2
        hand = (f'<path d="M{rx:.1f} {bot:.1f} V{ny - rh / 2:.1f}" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 7"/>'
                + f'<g>{beat("opacity", _n10_on(t_next))}' + card(nx0, ny - rh / 2, nw, rh, "var(--card)", "var(--c4)", rh / 2, 1.5)
                + spark(nx0 + 32, ny, .65, "var(--c4)") + T(f"{nx0 + 56:.1f}", f"{ny + z * .36:.1f}", nxt, z, "var(--white)", W6)
                + f'<path d="M{nx0 + nw - 28:.1f} {ny - 8:.1f} L{nx0 + nw - 19:.1f} {ny:.1f} L{nx0 + nw - 28:.1f} {ny + 8:.1f}" fill="none" stroke="var(--c4)" stroke-width="2.4" stroke-linecap="round"/></g>'
                + _q10_ride(f"M{rx:.1f} {bot:.1f} V{ny - rh / 2 + 6:.1f}", back, t_next, r=6)
                + _n10_ping(nx0 + 32, ny, 12, 42, t_next))
        g.append(land(hand, 1.1, .45, 12))
    # the root: one of their people and the question, which becomes one need at a time (painted last: labels on top)
    root = (card(rx - rw / 2, top, rw, rh, "var(--dim)", "var(--c4)", rh / 2, 1.5)
            + f'<g transform="translate({rx - rw / 2 + 33:.1f} {ry:.1f})">{_n10_face(clip, SKIN_LIGHT, "var(--c1)", HAIR, "short", 24)}</g>')
    tx, room = rx + 22, rw - 100
    q = sl["ask"]
    root += (f'<g>{beat("opacity", [(0, 1), (starts[0], 1), (starts[0] + .01, 0), (back, 0), (back + .01, 1), (1, 1)])}'
             + TC(f"{tx:.1f}", f"{ry + 8:.1f}", q, fit(q, 22, room, "need ask", floor=18), "var(--c4)", W6) + '</g>')
    for k, need in enumerate(sl["needs"][:n]):
        e = starts[k + 1] if k + 1 < n else back
        root += (f'<g opacity="0">{beat("opacity", [(0, 0), (starts[k] + .005, 0), (starts[k] + .015, 1), (e - .01, 1), (e, 0), (1, 0)])}'
                 + TC(f"{tx:.1f}", f"{ry + 8:.1f}", need, fit(need, 22, room, "need", floor=18), "var(--white)", W6) + '</g>')
    g.append(land(root, 1.0, .45, 12))
    return _pz_clip("".join(g), "pz-" + clip)
