"""Bench a: slide 1 of the salud deck (slides 2 and 3 reuse n02_afuera and n03_respuesta).
b01_portada - the promise as a region at dusk: four people seen from behind, each with their phone; on the horizon,
              their homes and, far behind, the homes of the whole region. A consultation leaves the phone (telemedicine,
              vital signs, e-prescription, psychology), rides the care pulse, opens the care that answers it (a doctor,
              a clinic of the network, a reminder, an appointment) and comes back down as a heart: that home lights up.
Reuses the pagos helpers _q01_arc_y, _q01_sw, _q01_person and the energía helpers _n01_on, _n01_tr (loaded before)."""


def _b01_home(k):
    """Home k on its baseline, smallest to tallest: 0 a small house, 1 a two-storey house, 2 a house with a porch,
    3 an apartment block. Returns (outline with dim windows, lit windows, half width, height)."""
    st = 'stroke="var(--c2)" stroke-width="1.6" stroke-linejoin="round"'
    sw = _q01_sw("var(--c2)")
    if k == 0:
        body = (f'<rect x="-40" y="-44" width="80" height="44" rx="2" fill="var(--card)" {st}/>'
                f'<path d="M-48 -42 L0 -70 L48 -42" fill="var(--card)" {st}/><rect x="-9" y="-26" width="18" height="26" rx="2" {sw}/>')
        win, hw, h = [(-32, -34, 16, 14), (16, -34, 16, 14)], 48, 70
    elif k == 1:
        body = (f'<rect x="-50" y="-72" width="100" height="72" rx="2" fill="var(--card)" {st}/>'
                f'<path d="M-58 -70 L0 -100 L58 -70" fill="var(--card)" {st}/><path d="M28 -88 V-104 H38 V-82" {sw}/>'
                f'<rect x="-10" y="-30" width="20" height="30" rx="2" {sw}/>')
        win, hw, h = [(-40, -62, 22, 18), (18, -62, 22, 18), (-40, -30, 22, 18), (18, -30, 22, 18)], 58, 104
    elif k == 2:
        body = (f'<rect x="-62" y="-66" width="124" height="66" rx="2" fill="var(--card)" {st}/>'
                f'<path d="M-70 -64 L-30 -96 H30 L70 -64" fill="var(--card)" {st}/>'
                f'<path d="M-62 -24 H62 M-50 -24 V0 M50 -24 V0" {sw}/><rect x="-11" y="-24" width="22" height="24" rx="2" {sw}/>')
        win, hw, h = [(-52, -54, 26, 20), (-13, -54, 26, 20), (26, -54, 26, 20)], 70, 96
    else:
        body = (f'<rect x="-66" y="-138" width="132" height="138" rx="3" fill="var(--card)" {st}/>'
                f'<path d="M-72 -138 H72" {sw}/><rect x="-14" y="-32" width="28" height="32" rx="2" {sw}/>')
        win, hw, h = [(x0, y0, 26, 18) for y0 in (-124, -96, -68) for x0 in (-54, -13, 28)] + [(-54, -38, 26, 18), (28, -38, 26, 18)], 72, 138
    dim = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{hh}" rx="2" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.2" opacity=".8"/>' for x, y, w, hh in win)
    lit = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{hh}" rx="2" fill="var(--c4)" opacity=".85"/>' for x, y, w, hh in win)
    return body + dim, lit, hw, h


def _b01_heart(s=1.0, fill="var(--ink)"):
    return (f'<path transform="scale({s})" d="M0 7 C-11 -1 -11 -10 -5 -10 C-2 -10 0 -7.5 0 -6 C0 -7.5 2 -10 5 -10 '
            f'C11 -10 11 -1 0 7 Z" fill="{fill}"/>')


def _b01_care(k, col):
    """The care that arrives, drawn around 0,0 in ~22 px: 0 a doctor (stethoscope), 1 a clinic of the network,
    2 a reminder (bell), 3 an appointment (calendar)."""
    sw = _q01_sw(col, 1.8)
    if k == 0:
        return (f'<path d="M-9 -10 V-3 A7 7 0 0 0 5 -3 V-10 M-2 4 V6 A6 6 0 0 0 10 6 V1" {sw}/>'
                f'<circle cx="10" cy="-2" r="3" {sw}/>')
    if k == 1:
        return (f'<path d="M-11 10 V-8 H11 V10 Z M-14 10 H14" {sw}/><path d="M0 -5 V5 M-5 0 H5" {sw}/>')
    if k == 2:
        return f'<path d="M-9 6 H9 L7 3 V-2 A7 7 0 0 0 -7 -2 V3 Z M-2.5 9 A2.5 2.5 0 0 0 2.5 9 M0 -9 V-11" {sw}/>'
    return (f'<rect x="-11" y="-8" width="22" height="19" rx="3" {sw}/><path d="M-11 -2 H11 M-5 -11 V-6 M5 -11 V-6" {sw}/>'
            f'<path d="M-4 5 L-1 8 L5 2" {sw}/>')


def _b01_pulse(xs, yf, blip=True):
    """The care pulse: the arc yf(x) from 850 to 1530, with a heartbeat blip above each home when blip."""
    pts, x = [], 850
    beat_at = sorted(xs)
    while x <= 1530:
        near = next((c for c in beat_at if abs(x - c) < 22), None) if blip else None
        if near is not None:
            for dx, dy in ((-22, 0), (-12, 0), (-7, 7), (-2, -26), (4, 15), (9, 0), (22, 0)):
                pts.append((near + dx, yf(near + dx) + dy))
            x = near + 26
            continue
        pts.append((x, yf(x)))
        x += 10
    return "M" + " L".join(f"{a:.1f} {b:.1f}" for a, b in pts)


# ---------------------------------------------------------------- portrait (the mobile build, DCD_ORIENT=portrait)
import re as _pb01_re


def _pb01_win(markup, fill):
    """The window rects of fill in markup merged into one path (same pose, a third of the bytes)."""
    rx = r'<rect x="(-?\d+)" y="(-?\d+)" width="(\d+)" height="(\d+)" rx="2" fill="' + _pb01_re.escape(fill) + r'"([^>]*)/>'
    found = _pb01_re.findall(rx, markup)
    d = "".join(f"M{x} {y}h{w}v{h}h-{w}Z" for x, y, w, h, _a in found)
    return _pb01_re.sub(rx, "", markup) + (f'<path d="{d}" fill="{fill}"{found[0][4]}/>' if found else "")


def _pb01_twin(sl, ctx):
    """b01 on the 900x1600 stage: the same sky of cares, care pulse, homes on the horizon and four people from behind,
    stacked down the art zone. Same four consultations, same frozen frame (four cares open and joined, four homes lit)."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    cx = zx + zw / 2
    xs = [cx - 285, cx - 95, cx + 95, cx + 285]
    ay = lambda x, r, cy: cy - math.sqrt(r * r - (x - cx) ** 2)
    hy = lambda x: ay(x, 1400, zy + 1890)       # horizon: 490 below the zone top at the center
    by = lambda x: ay(x, 1300, zy + 1560)       # the care pulse, 260 below the zone top
    ny = [zy + 70, zy + 150, zy + 70, zy + 150]
    hs = 1.2
    homes = [(_pb01_win(b, "var(--dim)"), _pb01_win(l, "var(--c4)"), hw, h) for b, l, hw, h in map(_b01_home, range(4))]
    base = [hy(x) for x in xs]
    tops = [b - h[3] * hs for b, h in zip(base, homes)]
    art = [glow(cx, zy + 340, 480, "var(--brand)", .6)]
    # far away: the homes of the whole region, a faint skyline; a few windows breathing
    far, lights, x, j = [], [], zx + 10, 0
    while x < zx + zw - 30:
        w, h = 22 + (j * 7) % 13, 12 + (j * 37) % 23
        yb = hy(x + w / 2) - 10
        far.append(f"{'M' if j == 0 else 'L'}{x:.0f} {yb - h:.0f}" + (f" L{x + w / 2:.0f} {yb - h - 8:.0f}" if j % 3 != 1 else "") + f" L{x + w:.0f} {yb - h:.0f}")
        if j % 6 == 0:
            lights.append(f'<rect x="{x + w / 2 - 2:.0f}" y="{yb - h + 6:.0f}" width="4" height="4" fill="var(--c4)">'
                          f'{loop("opacity", ".1;.9;.1", 3 + j % 5 * .7, (j * 1.3) % 4)}</rect>')
        x += w
        j += 1
    sil = "".join(far) + f" L{x:.0f} {hy(x):.0f} A1400 1400 0 0 0 {zx + 10} {hy(zx + 10):.0f} Z"
    art.append(land(f'<path d="{sil}" fill="var(--dim)" stroke="var(--c2)" stroke-width="1" stroke-opacity=".35" opacity=".85"/>' + "".join(lights)
                    + f'<path d="M{zx} {hy(zx):.0f} A1400 1400 0 0 1 {zx + zw} {hy(zx + zw):.0f}" fill="none" stroke="var(--c2)" stroke-width="1.4" opacity=".45"/>', .15, .6, 0))
    # the care that can arrive: dim nodes and links
    sky = "".join(f'<path d="M{xs[k]:.0f} {ny[k]} L{xs[k + 1]:.0f} {ny[k + 1]}" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="3 6" opacity=".45"/>' for k in range(3))
    sky += "".join(f'<circle cx="{x:.0f}" cy="{y}" r="6" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.6"/>' for x, y in zip(xs, ny))
    art.append(land(sky, .3, .6, 10))
    # the care pulse with a heartbeat blip above each home, and the threads from each roof up to the sky
    pts, x = [], zx + 20
    while x <= zx + zw - 20:
        near = next((c for c in xs if abs(x - c) < 24), None)
        if near is not None:
            pts += [(near + dx, by(near + dx) + dy) for dx, dy in ((-24, 0), (-13, 0), (-8, 8), (-2, -30), (4, 17), (10, 0), (24, 0))]
            x = near + 30
            continue
        pts.append((x, by(x)))
        x += 16
    pulse = "M" + " L".join(f"{a:.0f} {b:.0f}" for a, b in pts)
    bus = (f'<path d="{pulse}" fill="none" stroke="var(--c2)" stroke-width="1.8" stroke-linejoin="round" opacity=".55"/>'
           f'<path d="{pulse}" fill="none" stroke="var(--c4)" stroke-width="2.4" stroke-dasharray="2 14" opacity=".85">{loop("stroke-dashoffset", "0;-32", 1.8)}</path>')
    threads = "".join(f'<path d="M{x:.0f} {t - 4:.0f} V{y + 7}" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="2 5" opacity=".5"/>' for x, t, y in zip(xs, tops, ny))
    link = TC(f"{cx:.0f}", f"{by(cx) - 40:.0f}", sl["link"], fit(sl["link"], 22, 260, "portada link", floor=20), "var(--c4)", W6)
    art.append(land(bus + threads + link, .45, .6, 0))   # the link label rides in the same entrance, clear of the roofs
    text = []
    # their homes on the horizon
    for k, (x, b) in enumerate(zip(xs, base)):
        art.append(pop(f'<g transform="scale({hs})">{homes[k][0]}</g>', x, b, .5 + k * .1, .45))
    # the people, from behind, each holding up their phone
    people = [(SKIN_BROWN, "var(--accent)", 1), (SKIN_LIGHT, "var(--c1)", 0), (SKIN_LIGHT, "var(--c3)", 2), (SKIN_BROWN, "var(--c2)", 0)]
    devs = []
    for k, ((skin, jacket, hair), x, s) in enumerate(zip(people, xs, (.98, 1.04, .94, 1.02))):
        m, dev = _q01_person(round(x - 60 * s), zy + 890, s, "currentColor", jacket, hair, 3)
        art.append(land(f'<g style="color:{skin}">{m}</g>', .7 + k * .1, .6, 30))   # the skin mix written once
        devs.append(dev)
    lab = sl["region"]
    size = fit(lab, 24, 640, "portada region", floor=20)
    lw = bold_width(_(str(lab)), size, current_factor())
    hx, ry = cx - lw / 2 - 16, zy + 560
    text.append(land(TC(f"{cx + 12:.0f}", ry, lab, size, "var(--c4)", W6)
                     + f'<g transform="translate({hx:.0f} {ry - 7})">{_b01_heart(1.1, ok)}</g>'
                     + f'<circle cx="{hx:.0f}" cy="{ry - 8}" r="9" fill="none" stroke="{ok}" stroke-width="1.8">{loop("r", "9;18;9", 2.4)}{loop("opacity", "1;0;1", 2.4)}</circle>',
                     1.3, .5, 10))
    # the loop: four consultations, each opens the care that answers it and lights that home
    loops, joins = [], []
    for k, (x, b, (dx, dy), t0) in enumerate(zip(xs, base, devs, (.10, .26, .42, .58))):
        rise_end, bloom, back0, done = t0 + .05, t0 + .09, t0 + .095, t0 + .135
        b_ = by(x)
        up = f"M{dx:.0f} {dy - 24:.0f} C{dx:.0f} {dy - 130:.0f} {x:.0f} {b_ + 160:.0f} {x:.0f} {b_:.0f} V{ny[k]}"
        down = f"M{x:.0f} {ny[k]} V{tops[k] - 4:.0f}"
        loops.append(f'<g>{_n01_on(t0, t0 + .06)}<circle cx="{dx:.0f}" cy="{dy:.0f}" r="32" fill="none" stroke="var(--c4)" stroke-width="2.2"/>'
                     + pill(dx, dy - 58, sl["services"][k], "var(--c4)", ctx, 20, 186, "portada service", 14) + '</g>')
        loops.append(f'<g>{_n01_on(t0 + .005, bloom, .005)}{token("var(--c4)", 7)}{move(up, [(0, 0), (t0, 0), (bloom, 1), (1, 1)], D)}</g>')
        blip = " L".join(f"{x + ddx:.0f} {by(x + ddx) + ddy:.0f}" for ddx, ddy in ((-24, 0), (-13, 0), (-8, 8), (-2, -30), (4, 17), (10, 0), (24, 0)))
        loops.append(f'<g>{_n01_on(rise_end)}<path d="M{blip}" fill="none" stroke="{ok}" stroke-width="2.8" stroke-linejoin="round"/></g>')
        care = sl["cares"][k]
        s_ = fit(care, 22, 176, "portada care", floor=20)
        w_ = bold_width(_(str(care)), s_, current_factor()) + 58
        h_ = s_ + 22
        chip = (card(-w_ / 2, -h_ / 2, w_, h_, "var(--card)", ok, h_ / 2, 1.8)
                + f'<g transform="translate({-w_ / 2 + 24:.0f} 0) scale(.85)">{_b01_care(k, ok)}</g>'
                + T(f"{-w_ / 2 + 42:.0f}", f"{s_ * .36:.1f}", care, s_, "var(--white)", W6))
        loops.append(f'<g>{_n01_on(bloom, 1, .02)}<g transform="translate({x:.0f} {ny[k]})">{chip}</g></g>')
        if k:
            joins.append(f'<g>{_n01_on(bloom)}<path d="M{xs[k - 1]:.0f} {ny[k - 1]} L{x:.0f} {ny[k]}" stroke="{ok}" stroke-width="1.8" opacity=".8"/></g>')
        loops.append(f'<g>{_n01_on(back0, done, .005)}<g>{_b01_heart(1, ok)}{move(down, [(0, 0), (back0, 0), (done, 1), (1, 1)], D)}</g></g>')
        hw = homes[k][2] * hs
        loops.append(f'<g>{_n01_on(done)}<g transform="translate({x:.0f} {b:.0f})"><g transform="scale({hs})">{homes[k][1]}</g></g>'
                     f'<circle cx="{x + hw - 10:.0f}" cy="{tops[k] + 26:.0f}" r="14" fill="{ok}"/>'
                     f'<g transform="translate({x + hw - 10:.0f} {tops[k] + 28:.0f})">{_b01_heart(.72)}</g>'
                     f'<rect x="{dx - 14:.0f}" y="{dy - 23:.0f}" width="28" height="46" rx="5" fill="none" stroke="{ok}" stroke-width="2.2"/></g>')
    return portrait_mark("".join(art) + "".join(joins) + "".join(text) + "".join(loops)), D, FREEZE


# ---------------------------------------------------------------- slide 1: the promise, alive
@register("scene", "b01_portada")
def sc_b01_portada(sl, ctx):
    """A region at dusk seen from behind four people, each with their phone. On the horizon, four homes of every kind
    and, far behind, the homes of the whole region, their windows coming on. Above the roofs, one care pulse; above it,
    the care that can arrive. Loop: each person opens a consultation in the app, it rides the pulse (a heartbeat above
    their home), opens the care that answers it, and care comes back down as a heart: that home lights up.
    Frozen frame: four consultations made, four cares open and joined, four homes lit with a heart."""
    if ORIENT() == "portrait":
        return _pb01_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    cx, R_H, R_BUS = 1190, 1100, 1030
    xs = [905, 1095, 1285, 1475]
    base = [_q01_arc_y(x, R_H) for x in xs]
    homes = [_b01_home(k) for k in range(4)]
    tops = [b - h[3] for b, h in zip(base, homes)]
    bus_y = lambda x: _q01_arc_y(x, R_BUS, cy=1330)
    ny = [214, 148, 214, 148]
    arc = lambda r, x0, x1, cy=1570: f"M{x0} {_q01_arc_y(x0, r, cy=cy):.1f} A{r} {r} 0 0 1 {x1} {_q01_arc_y(x1, r, cy=cy):.1f}"
    g = [glow(cx, 420, 500, "var(--brand)", .6), glow(cx, 520, 380, "var(--c4)", .1)]
    # the ground: curved lines and rays toward the horizon, faint
    ground = "".join(f'<path d="{arc(r, x0, 2 * cx - x0)}" fill="none" stroke="var(--c2)" stroke-width="1.2" opacity="{op}"/>'
                     for r, x0, op in ((1000, 830, .14), (900, 850, .1), (800, 880, .07)))
    ground += "".join(f'<path d="M{cx + (bx - cx) * .2:.0f} 500 L{bx} 830" stroke="var(--c2)" stroke-width="1" opacity=".07"/>' for bx in range(640, 1760, 112))
    g.append(land(ground, .1, .6, 0))
    # far away: the homes of the whole region, small roofs, their windows coming on out of step
    far, lights, x = [], [], 832
    for j in range(80):
        w, h = 12 + (j * 7) % 9, 10 + (j * 37) % 19
        if x + w > 1548:
            break
        yb = _q01_arc_y(x + w / 2, R_H) - 8
        far.append(f"{'M' if j == 0 else 'L'}{x} {yb - h:.1f}" + (f" L{x + w / 2:.1f} {yb - h - 7:.1f}" if j % 3 != 1 else "") + f" L{x + w} {yb - h:.1f}")
        lights.append(f'<rect x="{x + w / 2 - 1.5:.1f}" y="{yb - h + 5:.1f}" width="3" height="3" fill="var(--c4)">'
                      f'{loop("opacity", ".1;.9;.9;.1", 3 + j % 5 * .7, (j * 1.3) % 4)}</rect>')
        x += w
    sil = "".join(far) + f" L{x} {_q01_arc_y(x, R_H):.1f} A{R_H} {R_H} 0 0 0 832 {_q01_arc_y(832, R_H):.1f} Z"
    g.append(land(f'<path d="{sil}" fill="var(--dim)" stroke="var(--c2)" stroke-width="1" stroke-opacity=".35" opacity=".85"/>' + "".join(lights)
                  + f'<path d="{arc(R_H, 820, 1560)}" fill="none" stroke="var(--c2)" stroke-width="1.4" opacity=".45"/>', .15, .6, 0))
    # the care that can arrive: dim nodes and links, always there
    sky = "".join(f'<path d="M{xs[k]} {ny[k]} L{xs[k + 1]} {ny[k + 1]}" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="3 6" opacity=".45"/>' for k in range(3))
    sky += "".join(f'<circle cx="{x}" cy="{y}" r="5" fill="var(--ink)" stroke="var(--c2)" stroke-width="1.5"/>' for x, y in zip(xs, ny))
    sky += "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="var(--c2)" opacity=".6"/>' for x, y in ((1000, 118), (1190, 196), (1380, 118), (860, 150), (1530, 214)))
    g.append(land(sky, .3, .6, 10))
    # the care pulse, and the threads from each roof up to the sky
    pulse = _b01_pulse(xs, bus_y)
    bus = (f'<path d="{pulse}" fill="none" stroke="var(--c2)" stroke-width="16" stroke-linejoin="round" opacity=".05"/>'
           f'<path d="{pulse}" fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-linejoin="round" opacity=".55"/>'
           f'<path d="{pulse}" fill="none" stroke="var(--c4)" stroke-width="2" stroke-dasharray="2 14" opacity=".85">{loop("stroke-dashoffset", "0;-32", 1.8)}</path>')
    threads = "".join(f'<path d="M{x} {t - 4:.1f} V{y + 6}" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="2 5" opacity=".5"/>' for x, t, y in zip(xs, tops, ny))
    link = TC(cx, 282, sl["link"], fit(sl["link"], 16, 190, "portada link"), "var(--c4)", W6)
    g.append(land(bus + threads + link, .45, .6, 0))
    # their homes on the horizon
    lit_homes = []
    for k, (x, b) in enumerate(zip(xs, base)):
        body, lit, hw, h = homes[k]
        g.append(pop(body, x, b, .5 + k * .1, .45))
        lit_homes.append((x, b, lit, hw))
    # the people, from behind, each holding up their phone
    people = [(xs[0] - 62, 826, .9, SKIN_BROWN, "var(--accent)", 1), (xs[1] - 64, 826, .98, SKIN_LIGHT, "var(--c1)", 0),
              (xs[2] - 62, 826, .86, SKIN_LIGHT, "var(--c3)", 2), (xs[3] - 66, 826, .96, SKIN_BROWN, "var(--c2)", 0)]
    devs = []
    for k, (px, py, s, skin, jacket, hair) in enumerate(people):
        m, dev = _q01_person(px, py, s, skin, jacket, hair, 3)
        g.append(land(m, .7 + k * .1, .6, 30))
        devs.append(dev)
    lab = sl["region"]
    size = fit(lab, 17, 470, "portada region")
    lw = bold_width(_(str(lab)), size, current_factor())
    hx = cx - lw / 2 - 14
    g.append(land(TC(cx + 10, 552, lab, size, "var(--c4)", W6)
                  + f'<g transform="translate({hx:.1f} 546)">{_b01_heart(.85, ok)}</g>'
                  + f'<circle cx="{hx:.1f}" cy="545" r="7" fill="none" stroke="{ok}" stroke-width="1.5">{loop("r", "7;15;7", 2.4)}{loop("opacity", "1;0;1", 2.4)}</circle>',
                  1.3, .5, 10))
    # the loop: four consultations, each opens the care that answers it and lights that home
    loops, joins = [], []
    for k, ((x, b, lit, hw), (dx, dy), t0) in enumerate(zip(lit_homes, devs, (.10, .26, .42, .58))):
        rise_end, bloom, back0, done = t0 + .05, t0 + .09, t0 + .095, t0 + .135
        by_ = bus_y(x)
        up = f"M{dx:.1f} {dy - 22:.1f} C{dx:.1f} {dy - 120:.1f} {x} {by_ + 150:.1f} {x} {by_:.1f} V{ny[k]}"
        down = f"M{x} {ny[k]} V{tops[k] - 4:.1f}"
        loops.append(f'<g>{_n01_on(t0, t0 + .06)}<circle cx="{dx:.1f}" cy="{dy:.1f}" r="30" fill="none" stroke="var(--c4)" stroke-width="2">{loop("r", "24;36;24", 1)}</circle></g>')
        loops.append(f'<g>{_n01_on(t0)}' + pill(dx, dy - 50, sl["services"][k], "var(--c4)", ctx, 15, 150, "portada service", 12) + '</g>')
        loops.append(f'<g>{_n01_on(t0 + .005, bloom, .005)}{token("var(--c4)", 6)}{move(up, [(0, 0), (t0, 0), (bloom, 1), (1, 1)], D)}</g>')
        # the heartbeat above this home lights as the consultation passes
        blip = " L".join(f"{x + ddx:.1f} {bus_y(x + ddx) + ddy:.1f}" for ddx, ddy in ((-22, 0), (-12, 0), (-7, 7), (-2, -26), (4, 15), (9, 0), (22, 0)))
        loops.append(f'<g>{_n01_on(rise_end)}<path d="M{blip}" fill="none" stroke="{ok}" stroke-width="2.4" stroke-linejoin="round"/></g>')
        loops.append(f'<circle cx="{x}" cy="{by_:.1f}" r="6" fill="none" stroke="{ok}" stroke-width="2" opacity="0">'
                     f'{beat("r", [(0, 6), (rise_end - .01, 6), (rise_end + .025, 28), (1, 28)])}'
                     f'{beat("opacity", [(0, 0), (rise_end - .01, 0), (rise_end - .007, 1), (rise_end + .025, 0), (1, 0)])}</circle>')
        care = sl["cares"][k]
        s_ = fit(care, 16, 140, "portada care")
        w_ = bold_width(_(str(care)), s_, current_factor()) + 52
        h_ = s_ + 22
        chip = (glow(0, 0, 70, ok, .16) + card(-w_ / 2, -h_ / 2, w_, h_, "var(--card)", ok, h_ / 2, 1.6)
                + f'<g transform="translate({-w_ / 2 + 21:.1f} 0) scale(.72)">{_b01_care(k, ok)}</g>'
                + T(-w_ / 2 + 36, s_ * .36, care, s_, "var(--white)", W6))
        loops.append(f'<g>{_n01_on(bloom, 1, .02)}<g transform="translate({x} {ny[k]})"><g>{_n01_tr([(0, "0 10"), (bloom, "0 10"), (bloom + .02, "0 0"), (1, "0 0")])}{chip}</g></g></g>')
        if k:
            joins.append(f'<g>{_n01_on(bloom)}<path d="M{xs[k - 1]} {ny[k - 1]} L{x} {ny[k]}" stroke="{ok}" stroke-width="1.6" opacity=".8"/></g>')
        loops.append(f'<g>{_n01_on(back0, done, .005)}<g>{_b01_heart(.8, ok)}{move(down, [(0, 0), (back0, 0), (done, 1), (1, 1)], D)}</g></g>')
        loops.append(f'<g>{_n01_on(done)}<g transform="translate({x} {b:.1f})">{glow(0, -40, 110, "var(--c4)", .22)}{lit}</g></g>')
        loops.append(f'<g>{_n01_on(done)}<circle cx="{x + hw - 8}" cy="{tops[k] + 22:.1f}" r="12" fill="{ok}"/>'
                     f'<g transform="translate({x + hw - 8} {tops[k] + 23.5:.1f})">{_b01_heart(.6)}</g></g>')
        loops.append(f'<g>{_n01_on(done)}<rect x="{dx - 12:.1f}" y="{dy - 20:.1f}" width="24" height="40" rx="4" fill="none" stroke="{ok}" stroke-width="2"/></g>')
    return "".join(g) + "".join(joins) + "".join(loops), D, FREEZE  # the lit links under the chips
