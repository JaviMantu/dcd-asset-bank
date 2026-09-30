"""The banca deck, slides 7 and 10 (embudo, capacidad). Each scene is one 12-second story timed with beat(); the
reduced-motion frame (0.9 of the loop, 10.8 s) is its resolved state. Runs in the shared namespace of module/ext.py and
reuses the harvested helpers _n13_on/_n13_off/_n13_lit (energía), _n01_tr (energía) and _b14_ok_dot/_b14_ping (salud).

- d07_embudo: ten candidate cards drop into a funnel; week by week one or two go down its neck past a small KPI check
  and land on the «Validadas» shelf, tagged «Retorno claro» or «Habilitador»; one goes, quietly, to «Por ahora, no».
  Frozen frame: five validated on the shelf, one set aside, four still waiting in the funnel, week 4 lit.
- d10_capacidad: a queue of five requests waits, clocks ticking, at a small lab with two people; three AI-augmented
  engineers walk in from the right; the queue moves: each request crosses the lab and comes out as a prototype with
  a check and a green clock. Frozen frame: the queue empty, five prototypes out, five people in the lab.
"""

_D07_R = .965   # = _N13_RESET: every resolved state holds until 11.6 s, after the frozen frame


# ---------------------------------------------------------------- 7 · embudo: ten hypotheses, a funnel that decides fast
def _d07_glyph(k, x, y):
    """Tag glyphs around (x, y): 0 «Retorno claro» (an arrow up, c4), 1 «Habilitador» (two linked rings, c2)."""
    if k == 0:
        return (f'<path d="M{x - 6} {y + 5} L{x} {y - 6} L{x + 6} {y + 5} M{x} {y - 6} V{y + 7}" fill="none" stroke="var(--c4)" '
                'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    return (f'<circle cx="{x - 3.5}" cy="{y}" r="4.5" fill="none" stroke="var(--c2)" stroke-width="1.8"/>'
            f'<circle cx="{x + 3.5}" cy="{y}" r="4.5" fill="none" stroke="var(--c2)" stroke-width="1.8"/>')


def _d07_card(name, w, h, line2="", col2="var(--muted)", fill="var(--dim)", stroke="var(--line)"):
    """A candidate card drawn at 0,0: its name and a second line (pending by default)."""
    return (card(0, 0, w, h, fill, stroke, 12, 1.2)
            + T(14, 23, name, fit(name, 15, w - 26, "embudo candidate"), "var(--white)", W6)
            + (T(14, 44, line2, fit(line2, 15, w - 26, "embudo pending"), col2, W6) if line2 else ""))


def _pd07_card(name, w, h, line2="", col2="var(--muted)"):
    """_d07_card at phone size: name and second line at 20+."""
    return (card(0, 0, w, h, "var(--dim)", "var(--line)", 12, 1.2)
            + T(16, 26, name, fit(name, 21, w - 30, "embudo candidate", floor=20), "var(--white)", W6)
            + (T(16, 50, line2, fit(line2, 20, w - 30, "embudo pending", floor=20), col2, W6) if line2 else ""))


def _pd07_twin(sl, ctx):
    """d07 on the 900x1600 stage: the weeks rail on top, the ten candidates in a 2x5 bowl, the neck with its KPI check
    in the middle, the «Validadas» shelf (3 + 2 slots) and the «Por ahora, no» tray under it, the legend at the bottom.
    Same schedule and frozen frame as the desktop."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    names, weeks, tags = sl["candidates"], sl["weeks"], sl["tags"]
    W, H = 380, 60
    cx0, cx1, ry0, rp = zx + 20, zx + 420, zy + 70, 66
    slot = [(cx0 if k % 2 == 0 else cx1, ry0 + (k // 2) * rp) for k in range(len(names))]
    nx, ny_in, ny_out = zx + zw / 2 - W / 2, zy + 410, zy + 484
    sensor_y = zy + 468
    shy = zy + 566
    shelf = [(cx0, shy + j * 66) for j in range(3)] + [(cx1, shy + j * 66) for j in range(2)]
    tx, ty = cx1, shy + 2 * 66 + 34
    rail_y, wx = zy + 44, [zx + 100 + k * 207 for k in range(4)]
    route = sl["route"]
    wk_t, times, t, last = {}, [], .17, None
    for cand, wk, tag in route:
        if wk != last:
            t = t + (.02 if last is not None else 0)
            wk_t[wk], last = t, wk
        a = t + .02
        times.append(a)
        t = a + .08
    art, text = [glow(zx + zw / 2, zy + 360, 460, "var(--brand)", .42)], []
    # the weeks
    rail = f'<path d="M{zx + 20} {rail_y} H{zx + zw - 20}" stroke="var(--line)" stroke-width="1.5"/>'
    wl = ""
    for k, (lab, x) in enumerate(zip(weeks, wx)):
        at = wk_t.get(k, 2)
        z = fit(lab, 22, 190, "embudo week", floor=20)
        rail += f'<circle cx="{x}" cy="{rail_y}" r="5" fill="var(--card)" stroke="var(--c2)" stroke-width="1.4"/>'
        wl += TC(x, rail_y - 14, lab, z, "var(--muted)", W6)
        if at < 1:
            wl += (f'<g opacity="0">{_n13_on(at)}<circle cx="{x}" cy="{rail_y}" r="5.5" fill="var(--c4)"/>'
                   + TC(x, rail_y - 14, lab, z, "var(--c4)", W6) + '</g>')
    ring_pairs = [(0, f"{wx[0]} {rail_y}")]
    for k in sorted(wk_t):
        ring_pairs += [(wk_t[k], ring_pairs[-1][1]), (wk_t[k] + .02, f"{wx[k]} {rail_y}")]
    ring_pairs += [(_D07_R, ring_pairs[-1][1]), (min(_D07_R + .02, .999), f"{wx[0]} {rail_y}"), (1, f"{wx[0]} {rail_y}")]
    rail += (f'<g opacity="0">{_n13_on(wk_t[min(wk_t)])}<g>{_n01_tr(ring_pairs)}'
             '<circle r="12" fill="none" stroke="var(--c4)" stroke-width="1.6"/></g></g>')
    art.append(land(rail, .1, .5, 0))
    text.append(land(wl, .1, .5, 0))
    # the funnel, the neck and its KPI check
    by1 = ry0 + 4 * rp + H + 10
    nl, nr = nx - 12, nx + W + 12
    left = f"M{zx} {rail_y + 12} V{by1} L{nl:.0f} {by1 + 50} V{ny_out + 20}"
    right = f"M{zx + zw} {rail_y + 12} V{by1} L{nr:.0f} {by1 + 50} V{ny_out + 20}"
    art.append(f'<path d="M{zx} {rail_y + 12} V{by1} L{nl:.0f} {by1 + 50} V{ny_out + 20} H{nr:.0f} V{by1 + 50} L{zx + zw} {by1} V{rail_y + 12} Z" '
               f'fill="color-mix(in srgb, var(--c1) 8%, transparent)"/>'
               + trace(left, "var(--c2)", 1.8, .1, .8) + trace(right, "var(--c2)", 1.8, .1, .8))
    passes = [a + .045 for (c, w, tag), a in zip(route, times) if tag >= 0]
    lit = [(0, 0)]
    for p in passes:
        lit += [(p, 0), (p + .005, 1), (p + .035, 1), (p + .045, 0)]
    lit.append((1, 0))
    kc = nr + 28
    art.append(land(f'<path d="M{nl:.0f} {sensor_y} H{nr:.0f}" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="4 5" opacity=".7"/>'
                    f'<path d="M{nl:.0f} {sensor_y} H{nr:.0f}" stroke="{ok}" stroke-width="2" opacity="0">{beat("opacity", lit)}</path>'
                    f'<circle cx="{kc:.0f}" cy="{sensor_y}" r="15" fill="var(--card)" stroke="var(--c2)" stroke-width="1.5"/>'
                    + check(kc, sensor_y + 1, .75, "var(--c2)")
                    + f'<g opacity="0">{beat("opacity", lit)}<circle cx="{kc:.0f}" cy="{sensor_y}" r="15" fill="{ok}"/>{check(kc, sensor_y + 1, .75, "var(--ink)")}</g>'
                    + pill(kc + 64, sensor_y, sl["kpi"], "var(--dim)", ctx, 20, 96, "embudo kpi", 14)
                    + "".join(_b14_ping(f"{kc:.0f}", sensor_y, 15, 40, p, ok) for p in passes), .7, .45, 0))
    # the shelf «Validadas» and the tray «Por ahora, no»
    rack = "".join(f'<rect x="{x}" y="{y}" width="{W}" height="{H}" rx="12" fill="none" stroke="var(--line)" stroke-width="1.2" stroke-dasharray="4 5"/>'
                   for x, y in shelf + [(tx, ty)])
    art.append(land(rack, .5, .45, 10))
    text.append(land(T(cx0, shy - 16, sl["shelf"], fit(sl["shelf"], 22, W, "embudo shelf", floor=20), "var(--white)", W6)
                     + T(tx, ty - 14, sl["aside"], fit(sl["aside"], 21, W, "embudo aside", floor=20), "var(--muted)", W6), .6, .45, 10))
    # the legend
    leg = ""
    for k, (tag, why) in enumerate(tags):
        y = zy + 850 + k * 38
        wt = bold_width(_(str(tag)), 21, current_factor())
        leg += (f'<g transform="translate({cx0 + 8} {y - 7}) scale(1.4)">{_d07_glyph(k, 0, 0)}</g>'
                + T(cx0 + 28, y, tag, 21, "var(--c4)" if k == 0 else "var(--c2)", W6)
                + f'<circle cx="{cx0 + 28 + wt + 11:.0f}" cy="{y - 7}" r="2.5" fill="var(--muted)"/>'
                + T(f"{cx0 + 28 + wt + 22:.0f}", y, why, fit(why, 21, zw - 80 - wt, "embudo legend", floor=20), "var(--muted)", W6))
    text.append(land(leg, .9, .45, 8))
    # the ten candidates in the bowl
    moving = {c: (w, tag, a) for (c, w, tag), a in zip(route, times)}
    parts = []
    for k, name in enumerate(names):
        x, y = slot[k]
        inner = _pd07_card(name, W, H, sl["pending"])
        if k in moving:
            inner = f'<g>{_n13_off(moving[k][2], f=.004)}{inner}</g>'
        parts.append(f'<g transform="translate({x} {y})">{inner}</g>')
    art.append(seq(["".join(parts[i:i + 2]) for i in range(0, len(parts), 2)], .3, .5, -36))
    # the travelling copies
    shelf_j = 0
    for (cand, wk, tag), a in zip(route, times):
        x, y = slot[cand]
        k0, k1, k2, k4 = a + .012, a + .035, a + .055, a + .10
        if tag >= 0:
            end = [(k4, "{} {}".format(*shelf[shelf_j]))]
            shelf_j += 1
        else:
            end = [(k4 - .012, f"{tx} {ty}")]
        pairs = [(0, f"{x} {y}"), (k0, f"{x} {y}"), (k1, f"{nx:.0f} {ny_in}"), (k2, f"{nx:.0f} {ny_out}")] + end + [(1, end[-1][1])]
        col = "var(--c4)" if tag == 0 else "var(--c2)"
        body = card(0, 0, W, H, "var(--dim)", "var(--line)", 12, 1.2)
        name = T(16, 26, names[cand], fit(names[cand], 21, W - 30, "embudo candidate", floor=20), "var(--white)", W6)
        if tag >= 0:
            body += (f'<g>{_n13_off(k4)}' + T(16, 50, sl["pending"], 20, "var(--muted)", W6) + '</g>'
                     + f'<g opacity="0">{_n13_on(k4)}' + card(0, 0, W, H, f"color-mix(in srgb, {col} 12%, var(--card))", col, 12, 1.4)
                     + f'<g transform="translate(24 43) scale(1.3)">{_d07_glyph(tag, 0, 0)}</g>'
                     + T(40, 50, tags[tag][0], fit(tags[tag][0], 20, W - 100, "embudo tag", floor=20), col, W6)
                     + f'<circle cx="{W - 26}" cy="30" r="12" fill="{ok}"/>{check(W - 26, 31, .8, "var(--ink)")}</g>' + name)
        else:
            body += (T(16, 50, sl["pending"], 20, "var(--muted)", W6) + name
                     + f'<rect x="0" y="0" width="{W}" height="{H}" rx="12" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 4" opacity="0">{_n13_on(k4)}</rect>')
        body += (f'<rect x="0" y="0" width="{W}" height="{H}" rx="12" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">'
                 f'{beat("opacity", [(0, 0), (a, 0), (a + .006, 1), (k4, 1), (k4 + .01, 0), (1, 0)])}</rect>')
        art.append(f'<g opacity="0">{_n13_on(a, f=.004)}<g>{_n01_tr(pairs)}{body}</g></g>' + _b14_ping(x + W / 2, y + H / 2, 24, 80, a))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "d07_embudo")
def sc_d07_embudo(sl, ctx):
    """Ten candidate cards drop into the mouth of a funnel. A static rail of weeks runs above it. Each week one or two
    cards light, go down the neck past a small KPI check that turns green, slide out and land on the «Validadas» shelf
    with their tag («Retorno claro» or «Habilitador») and a check; in week 2 one card goes through without the check
    lighting and rests, quietly, in «Por ahora, no». Frozen frame: five on the shelf, one set aside, four waiting in the
    funnel, week 4 lit."""
    if ORIENT() == "portrait":
        return _pd07_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    names, weeks, tags = sl["candidates"], sl["weeks"], sl["tags"]
    W, H = 228, 54
    cx0, cx1, ry0, rp = 842, 1076, 168, 62                 # the bowl: two columns, five rows
    slot = [(cx0 if k % 2 == 0 else cx1, ry0 + (k // 2) * rp) for k in range(len(names))]
    nx, ny_in, ny_out = 958, 492, 616                      # the neck: card x, entry y, exit y
    sensor_y = 576
    shx, shy, shp = 1327, 186, 64                          # the shelf: card x, first slot y, pitch
    tx, ty = 842, 732                                      # the tray «Por ahora, no»
    rail_y, wx = 128, [912, 1090, 1268, 1446]
    # the schedule: [candidate, week, tag] with tag 0 «Retorno claro», 1 «Habilitador», -1 «Por ahora, no»
    route = sl["route"]
    wk_t, times, t, last = {}, [], .17, None
    for cand, wk, tag in route:
        if wk != last:
            t = t + (.02 if last is not None else 0)
            wk_t[wk], last = t, wk
        a = t + .02
        times.append(a)
        t = a + .08
    g = [glow(1072, 360, 420, "var(--brand)", .42)]

    # ---- the weeks: static labels on a rail; each lights when its week starts, a ring marks the current one
    rail = f'<path d="M850 {rail_y} H1540" stroke="var(--line)" stroke-width="1.5"/>'
    for k, (lab, x) in enumerate(zip(weeks, wx)):
        at = wk_t.get(k, 2)
        rail += (f'<circle cx="{x}" cy="{rail_y}" r="4" fill="var(--card)" stroke="var(--c2)" stroke-width="1.4"/>'
                 + TC(x, rail_y - 14, lab, fit(lab, 15, 150, "embudo week"), "var(--muted)", W6))
        if at < 1:
            rail += (f'<g opacity="0">{_n13_on(at)}<circle cx="{x}" cy="{rail_y}" r="4.5" fill="var(--c4)"/>'
                     + TC(x, rail_y - 14, lab, fit(lab, 15, 150, "embudo week"), "var(--c4)", W6) + '</g>')
    ring_pairs = [(0, f"{wx[0]} {rail_y}")]
    for k in sorted(wk_t):
        ring_pairs += [(wk_t[k], ring_pairs[-1][1]), (wk_t[k] + .02, f"{wx[k]} {rail_y}")]
    ring_pairs += [(_D07_R, ring_pairs[-1][1]), (min(_D07_R + .02, .999), f"{wx[0]} {rail_y}"), (1, f"{wx[0]} {rail_y}")]
    rail += (f'<g opacity="0">{_n13_on(wk_t[min(wk_t)])}<g>{_n01_tr(ring_pairs)}'
             '<circle r="10" fill="none" stroke="var(--c4)" stroke-width="1.6"/></g></g>')
    g.append(land(rail, .1, .5, 0))

    # ---- the funnel, the neck and its KPI check
    left = f"M822 146 L834 160 V476 L952 552 V600"
    right = f"M1322 146 L1310 160 V476 L1192 552 V600"
    g.append(f'<path d="M834 160 V476 L952 552 V600 H1192 V552 L1310 476 V160 Z" fill="color-mix(in srgb, var(--c1) 8%, transparent)"/>'
             + trace(left, "var(--c2)", 1.8, .1, .8) + trace(right, "var(--c2)", 1.8, .1, .8))
    passes = [a + .045 for (c, w, tag), a in zip(route, times) if tag >= 0]
    lit = [(0, 0)]
    for p in passes:
        lit += [(p, 0), (p + .005, 1), (p + .035, 1), (p + .045, 0)]
    lit.append((1, 0))
    kc = 1216
    sensor = (f'<path d="M952 {sensor_y} H1192" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="4 5" opacity=".7"/>'
              f'<path d="M952 {sensor_y} H1192" stroke="{ok}" stroke-width="2" opacity="0">{beat("opacity", lit)}</path>'
              f'<circle cx="{kc}" cy="{sensor_y}" r="12" fill="var(--card)" stroke="var(--c2)" stroke-width="1.5"/>'
              + check(kc, sensor_y + 1, .6, "var(--c2)")
              + f'<g opacity="0">{beat("opacity", lit)}<circle cx="{kc}" cy="{sensor_y}" r="12" fill="{ok}"/>{check(kc, sensor_y + 1, .6, "var(--ink)")}</g>'
              + pill(kc + 46, sensor_y, sl["kpi"], "var(--dim)", ctx, 15, 90, "embudo kpi", 14)
              + "".join(_b14_ping(kc, sensor_y, 12, 34, p, ok) for p in passes))
    g.append(land(sensor, .7, .45, 0))

    # ---- the shelf «Validadas» and the tray «Por ahora, no»
    n_ok = sum(1 for _c, _w, tag in route if tag >= 0)
    rack = (T(shx, shy - 16, sl["shelf"], fit(sl["shelf"], 17, W, "embudo shelf"), "var(--white)", W6)
            + f'<path d="M{shx - 6} {shy - 6} V{shy + shp * n_ok + 2}" stroke="var(--c2)" stroke-width="1.4" opacity=".6"/>')
    for j in range(n_ok):
        y = shy + j * shp
        rack += (f'<rect x="{shx}" y="{y}" width="{W}" height="{H}" rx="12" fill="none" stroke="var(--line)" stroke-width="1.2" stroke-dasharray="4 5"/>'
                 f'<path d="M{shx - 6} {y + H + 5} H{shx + W}" stroke="var(--c2)" stroke-width="1.4" opacity=".6"/>')
    tray = (T(tx, ty - 14, sl["aside"], fit(sl["aside"], 16, W, "embudo aside"), "var(--muted)", W6)
            + f'<rect x="{tx}" y="{ty}" width="{W}" height="{H}" rx="12" fill="none" stroke="var(--line)" stroke-width="1.2" stroke-dasharray="4 5"/>')
    g.append(land(rack, .5, .45, 10) + land(tray, .6, .45, 10))

    # ---- the legend: what each tag means
    leg = ""
    for k, (tag, why) in enumerate(tags):
        y = 740 + k * 38
        wt = bold_width(_(str(tag)), 15, current_factor())
        leg += (_d07_glyph(k, 1130, y - 5) + T(1146, y, tag, 15, "var(--c4)" if k == 0 else "var(--c2)", W6)
                + f'<circle cx="{1146 + wt + 9:.0f}" cy="{y - 5}" r="2" fill="var(--muted)"/>'
                + T(1146 + wt + 18, y, why, fit(why, 15, 372 - wt, "embudo legend"), "var(--muted)", W6))
    g.append(land(leg, .9, .45, 8))

    # ---- the ten candidates in the bowl (they drop in); the ones that move are covered by their travelling copy
    moving = {c: (w, tag, a) for (c, w, tag), a in zip(route, times)}
    parts = []
    for k, name in enumerate(names):
        x, y = slot[k]
        inner = _d07_card(name, W, H, sl["pending"])
        if k in moving:
            inner = f'<g>{_n13_off(moving[k][2], f=.004)}{inner}</g>'
        parts.append(f'<rect x="{x}" y="{y}" width="{W}" height="{H}" rx="12" fill="none" stroke="var(--line)" stroke-width="1" stroke-dasharray="3 5" opacity=".6"/>'
                     f'<g transform="translate({x} {y})">{inner}</g>')
    g.append(seq(parts, .3, .5, -36))

    # ---- the travelling copies: slot, neck, past the check, out, and onto the shelf (or the tray)
    shelf_j = 0
    for (cand, wk, tag), a in zip(route, times):
        x, y = slot[cand]
        k0, k1, k2, k3, k4 = a + .012, a + .035, a + .055, a + .078, a + .10
        if tag >= 0:
            sy = shy + shelf_j * shp
            shelf_j += 1
            end = [(k3, f"{shx} {ny_out}"), (k4, f"{shx} {sy}")]
        else:
            end = [(k4 - .012, f"{tx} {ty}")]
        pairs = ([(0, f"{x} {y}"), (k0, f"{x} {y}"), (k1, f"{nx} {ny_in}"), (k2, f"{nx} {ny_out}")] + end
                 + [(1, end[-1][1])])
        col = "var(--c4)" if tag == 0 else "var(--c2)"
        body = card(0, 0, W, H, "var(--dim)", "var(--line)", 12, 1.2)
        if tag >= 0:
            body += f'<g opacity="0">{_n13_on(k4)}' + card(0, 0, W, H, f"color-mix(in srgb, {col} 12%, var(--card))", col, 12, 1.4) + '</g>'
        body += T(14, 23, names[cand], fit(names[cand], 15, W - 26, "embudo candidate"), "var(--white)", W6)
        if tag >= 0:
            body += (f'<g opacity="0">{_n13_on(k4)}' + _d07_glyph(tag, 21, 39) + T(34, 44, tags[tag][0], fit(tags[tag][0], 15, W - 80, "embudo tag"), col, W6) + '</g>'
                     + f'<g>{_n13_off(k4)}' + T(14, 44, sl["pending"], 15, "var(--muted)", W6) + '</g>'
                     + _b14_ok_dot(W - 24, 27, k4, ok, 9))
        else:
            body += (T(14, 44, sl["pending"], 15, "var(--muted)", W6)
                     + f'<rect x="0" y="0" width="{W}" height="{H}" rx="12" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 4" opacity="0">{_n13_on(k4)}</rect>')
        body += (f'<rect x="0" y="0" width="{W}" height="{H}" rx="12" fill="none" stroke="var(--c4)" stroke-width="1.8" opacity="0">'
                 f'{beat("opacity", [(0, 0), (a, 0), (a + .006, 1), (k4, 1), (k4 + .01, 0), (1, 0)])}</rect>')
        g.append(f'<g opacity="0">{_n13_on(a, f=.004)}<g>{_n01_tr(pairs)}{body}</g></g>'
                 + _b14_ping(x + W / 2, y + H / 2, 20, 70, a))
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 10 · capacidad: AI engineers join their lab today
def _d10_bust(x, y, skin, shirt, rim="var(--c2)", long=False):
    """A faceless person from the chest up, head centered at (x, y); the shoulders end at y + 62 (the desk hides them)."""
    back = (f'<path d="M{x - 16} {y + 18} V{y - 4} C{x - 16} {y - 18} {x + 16} {y - 18} {x + 16} {y - 4} V{y + 18} Z" fill="{HAIR}"/>'
            if long else "")
    return (back + f'<path d="M{x - 27} {y + 62} C{x - 27} {y + 32} {x - 15} {y + 21} {x} {y + 21} C{x + 15} {y + 21} {x + 27} {y + 32} {x + 27} {y + 62} Z" fill="{shirt}"/>'
            f'<path d="M{x - 27} {y + 62} C{x - 27} {y + 32} {x - 15} {y + 21} {x} {y + 21} C{x + 15} {y + 21} {x + 27} {y + 32} {x + 27} {y + 62}" fill="none" stroke="{rim}" stroke-width="1.3" opacity=".7"/>'
            f'<rect x="{x - 6}" y="{y + 10}" width="12" height="13" fill="{shade(skin, 16)}"/>'
            f'<ellipse cx="{x}" cy="{y}" rx="14" ry="16" fill="{skin}"/>'
            f'<path d="M{x - 15} {y + 4} C{x - 17} {y - 14} {x - 9} {y - 19} {x} {y - 19} C{x + 9} {y - 19} {x + 17} {y - 14} {x + 15} {y + 4} '
            f'C{x + 13} {y - 4} {x + 8} {y - 8} {x} {y - 8} C{x - 8} {y - 8} {x - 13} {y - 4} {x - 15} {y + 4} Z" fill="{HAIR}"/>'
            f'<path d="M{x - 13} {y - 8} C{x - 11} {y - 17} {x - 4} {y - 19} {x} {y - 19} C{x + 5} {y - 19} {x + 11} {y - 17} {x + 13} {y - 8}" fill="none" stroke="var(--c2)" stroke-width="1.2" opacity=".55"/>')


def _d10_clock(x, y, col, tick=True):
    """A clock around (x, y), r 10; a waiting clock's hand turns."""
    hand = f'<path d="M{x} {y} L{x + 4} {y + 3}" stroke="{col}" stroke-width="1.8" stroke-linecap="round">'
    hand += (f'<animateTransform attributeName="transform" type="rotate" values="0 {x} {y};360 {x} {y}" dur="6s" repeatCount="indefinite"/></path>'
             if tick else '</path>')
    return (f'<circle cx="{x}" cy="{y}" r="10" fill="none" stroke="{col}" stroke-width="1.8"/>' + hand
            + f'<path d="M{x} {y} V{y - 6}" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>')


def _pd10_twin(sl, ctx):
    """d10 on the 900x1600 stage: the same left-to-right flow compressed to the phone width (queue column, lab, the
    engineers and the prototypes' column on the right), the platform under all of it. Same beats and frozen frame."""
    ok = ctx.brand.c("dark.ok")
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    n = int(sl.get("count", 5))
    req, proto = sl["request"], sl["proto"]
    W, H, P = 176, 54, 64
    qx, fy = zx, zy + 390
    ox = zx + zw - W
    lx0, lx1, ly0, ly1 = qx + W + 12, ox - 14, zy + 100, zy + 750
    head_y, desk_y = zy + 236, zy + 292
    stage = [ox + 28, ox + 84, ox + 140]
    dx_in = -258
    seats = [lx0 + 66, lx0 + 136] + [x + dx_in for x in stage]
    bx, by = (lx0 + lx1) / 2 - W / 2, fy
    JOIN0, JOIN1 = .20, .30
    SRV = [.33 + .105 * j for j in range(n)]
    art, text = [glow((lx0 + lx1) / 2, zy + 420, 460, "var(--brand)", .45)], []
    lab = (f'<rect x="{lx0}" y="{ly0}" width="{lx1 - lx0}" height="{ly1 - ly0}" rx="22" fill="color-mix(in srgb, var(--c1) 10%, var(--card))"/>'
           f'<path d="M{lx0} {fy - 10} V{ly0 + 22} Q{lx0} {ly0} {lx0 + 22} {ly0} H{lx1 - 22} Q{lx1} {ly0} {lx1} {ly0 + 22} V{head_y - 44}" fill="none" stroke="var(--c2)" stroke-width="1.6"/>'
           f'<path d="M{lx1} {fy + H + 10} V{ly1 - 22} Q{lx1} {ly1} {lx1 - 22} {ly1} H{lx0 + 22} Q{lx0} {ly1} {lx0} {ly1 - 22} V{fy + H + 10}" fill="none" stroke="var(--c2)" stroke-width="1.6"/>'
           + "".join(f'<path d="M{x - 6} {y} H{x + 6}" stroke="var(--c2)" stroke-width="1.6"/>'
                     for x, y in ((lx0, fy - 10), (lx0, fy + H + 10), (lx1, head_y - 44), (lx1, fy + H + 10))))
    door = (f'<path d="M{lx0} {fy - 10} V{fy + H + 10}" stroke="var(--c3)" stroke-width="2.4" stroke-dasharray="4 4">'
            f'{beat("opacity", [(0, 1), (JOIN1, 1), (JOIN1 + .02, 0), (_D07_R, 0), (min(_D07_R + .02, .999), 1), (1, 1)])}</path>')
    team = _d10_bust(seats[0], head_y, SKIN_BROWN, shade("var(--c1)", 10), long=True) + _d10_bust(seats[1], head_y, SKIN_LIGHT, shade("var(--c5)", 35))
    empty = f'<g>{_n13_off(JOIN1)}' + "".join(f'<path d="M{x - 27} {head_y + 62} C{x - 27} {head_y + 32} {x - 15} {head_y + 21} {x} {head_y + 21} C{x + 15} {head_y + 21} {x + 27} {head_y + 32} {x + 27} {head_y + 62}" '
                    f'fill="none" stroke="var(--line)" stroke-width="1.4" stroke-dasharray="4 4"/>'
                    f'<ellipse cx="{x}" cy="{head_y}" rx="14" ry="16" fill="none" stroke="var(--line)" stroke-width="1.4" stroke-dasharray="4 4"/>'
                    for x in seats[2:]) + '</g>'
    desk = f'<rect x="{lx0 + 16}" y="{desk_y}" width="{lx1 - lx0 - 32}" height="14" rx="4" fill="var(--card)" stroke="var(--c2)" stroke-width="1.4"/>'
    board = (card(bx - 14, fy - 14, W + 28, 160, "color-mix(in srgb, var(--c1) 14%, var(--card))", "var(--c2)", 14, 1.2, 'stroke-dasharray="5 5"')
             + spark(bx + W - 4, fy + 128, .55))
    fl = [(0, 0)] + [p for s in SRV for p in ((s + .025, 0), (s + .03, 1), (s + .055, 1), (s + .065, 0))] + [(1, 0)]
    board += f'<g opacity="0">{beat("opacity", fl)}{glow(bx + W - 4, fy + 128, 28, "var(--c4)", .7)}</g>'
    for i, L in enumerate((.9, .7, .8)):
        y = fy + H + 24 + i * 22
        wbar = W * L
        board += f'<rect x="{bx:.0f}" y="{y}" width="{wbar:.0f}" height="8" rx="4" fill="var(--line)" opacity=".7"/>'
        prs = [(0, 1)]
        for s in SRV:
            a0, a1 = s + .025 + i * .008, s + .055 + i * .004
            prs += [(a0, 1), (a1, 0), (s + .07, 0), (s + .075, 1)]
        prs.append((1, 1))
        board += (f'<path d="M{bx:.0f} {y + 4} H{bx + wbar:.0f}" pathLength="1" stroke-dasharray="1" stroke="var(--c4)" stroke-width="8" stroke-linecap="round">'
                  f'{beat("stroke-dashoffset", prs)}</path>')
    art.append(land(lab + team + empty + board, .1, .55, 12) + door)
    text.append(land(T(lx0 + 22, ly0 + 42, sl["lab"], fit(sl["lab"], 24, lx1 - lx0 - 44, "capacidad lab", floor=20), "var(--white)", W6), .1, .55, 12))
    # the three AI-augmented engineers walk in through the right door
    eng = "".join(_d10_bust(x, head_y, (SKIN_LIGHT, SKIN_BROWN, SKIN_LIGHT)[k], shade("var(--c1)", 45), "var(--c4)", k == 1)
                  + spark(x + 19, head_y - 18, .45) for k, x in enumerate(stage))
    sparks = f'<g opacity="0">{beat("opacity", fl)}' + "".join(glow(x + 19, head_y - 18, 22, "var(--c4)", .6) for x in stage) + '</g>'
    walk = [(0, "0 0"), (JOIN0, "0 0"), (JOIN1, f"{dx_in} 0"), (_D07_R, f"{dx_in} 0"), (min(_D07_R + .02, .999), "0 0"), (1, "0 0")]
    art.append(land(f'<g>{_n01_tr(walk)}{sparks}{eng}</g>', .5, .5, 0, 30) + land(desk, .1, .55, 12))
    lab_e = sl["engineers"]
    text.append(land(f'<g>{_n13_off(JOIN0)}' + TCW(stage[1], head_y - 80, lab_e, 13, 20, "var(--c4)", W6, 1.25) + '</g>', .7, .45, 8)
                + f'<g opacity="0">{_n13_on(JOIN1)}' + TCW(seats[3], desk_y + 42, lab_e, 30, 20, "var(--c4)", W6, 1.25) + '</g>'
                + _b14_ping(seats[3], head_y, 30, 90, JOIN1))
    # the platform everything stands on
    py = ly1 + 30
    art.append(land(card(zx, py, zw, 60, "color-mix(in srgb, var(--c1) 26%, var(--card))", "var(--c2)", 30, 1.4), .9, .45, 10))
    text.append(land(TC(zx + zw / 2, py + 38, sl["platform"], fit(sl["platform"], 24, zw - 60, "capacidad platform", floor=20), "var(--white)", W6), .9, .45, 10))
    # the queue
    slots = [fy + P * k for k in range(n)]
    outs = [slots[-1] - P * j for j in range(n)]
    qs = []
    for k in range(n):
        s = SRV[k]
        pairs = [(0, "0 0")]
        for j in range(k):
            prev = pairs[-1][1]
            pairs += [(SRV[j] + .005, prev), (SRV[j] + .025, f"0 {-P * (j + 1)}")]
        if k == 0:
            pairs += [(t, v) for t0 in (.08, .13, .18) for t, v in ((t0, "0 0"), (t0 + .01, "8 0"), (t0 + .02, "0 0"))]
        y0 = -P * k
        pairs += [(s, f"0 {y0}"), (s + .02, f"{bx - qx:.0f} {y0}"), (s + .065, f"{bx - qx:.0f} {y0}"),
                  (s + .08, f"{ox - qx} {y0}"), (s + .1, f"{ox - qx} {outs[k] - slots[k]}"),
                  (1, f"{ox - qx} {outs[k] - slots[k]}")]
        sw = s + .065
        body = (card(0, 0, W, H, "var(--dim)", "var(--line)", 10, 1.2)
                + f'<g>{_n13_off(sw)}' + _d10_clock(24, 27, "var(--c3)") + T(44, 34, req, fit(req, 20, W - 56, "capacidad request", floor=20), "var(--white)", W6) + '</g>'
                + f'<g opacity="0">{_n13_on(sw)}' + card(0, 0, W, H, f"color-mix(in srgb, {ok} 12%, var(--card))", ok, 10, 1.4)
                + _d10_clock(24, 27, ok, False) + T(44, 34, proto, fit(proto, 20, W - 80, "capacidad prototype", floor=20), "var(--white)", W6)
                + f'<circle cx="{W - 20}" cy="27" r="11" fill="{ok}"/>{check(W - 20, 28, .73, "var(--ink)")}</g>')
        qs.append(f'<g transform="translate({qx} {slots[k]})"><g>{_n01_tr(pairs)}'
                  f'<g>{beat("opacity", [(0, 1), (_D07_R, 1), (min(_D07_R + .02, .999), 0), (1, 0)])}{body}</g></g></g>'
                  + _b14_ping(f"{bx + W / 2:.0f}", fy + H / 2, 24, 80, sw, ok))
    art.append(seq(qs, .3, .5, 16))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


@register("scene", "d10_capacidad")
def sc_d10_capacidad(sl, ctx):
    """On the left a queue of five «Solicitud» cards waits, clocks ticking, at the door of a small lab («Su laboratorio»)
    where two faceless people work; the front one nudges the door. Three faceless AI-augmented engineers, each with a
    spark, wait on the right under their label and walk in through the right door. Then the queue moves: each request
    crosses into the lab, the board builds it, and it leaves through the right door as a «Prototipo» with a check and a
    green clock, stacking on the right. Everything stands on «Con su método y su plataforma». Frozen frame: the queue
    empty, five prototypes out, five people in the lab."""
    if ORIENT() == "portrait":
        return _pd10_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    n = int(sl.get("count", 5))
    req, proto = sl["request"], sl["proto"]
    W, H, P = 150, 44, 50
    qx, fy = 840, 400                     # the queue column and the flow row (the doors' row)
    ox = 1404                              # the prototypes' column
    lx0, lx1, ly0, ly1 = 1030, 1382, 150, 604
    head_y, desk_y = 262, 318
    stage = [1428, 1480, 1532]
    dx_in = -212
    seats = [1090, 1152] + [x + dx_in for x in stage]
    bx, by = 1136, fy                      # the card's place on the lab's board
    JOIN0, JOIN1 = .20, .30
    SRV = [.33 + .105 * j for j in range(n)]
    g = [glow(1206, 420, 440, "var(--brand)", .45)]

    # ---- the lab: walls with a door on each side, header, desk
    lab = (f'<rect x="{lx0}" y="{ly0}" width="{lx1 - lx0}" height="{ly1 - ly0}" rx="22" fill="color-mix(in srgb, var(--c1) 10%, var(--card))"/>'
           f'<path d="M{lx0} {fy - 10} V{ly0 + 22} Q{lx0} {ly0} {lx0 + 22} {ly0} H{lx1 - 22} Q{lx1} {ly0} {lx1} {ly0 + 22} V{head_y - 44}" fill="none" stroke="var(--c2)" stroke-width="1.6"/>'
           f'<path d="M{lx1} {fy + H + 10} V{ly1 - 22} Q{lx1} {ly1} {lx1 - 22} {ly1} H{lx0 + 22} Q{lx0} {ly1} {lx0} {ly1 - 22} V{fy + H + 10}" fill="none" stroke="var(--c2)" stroke-width="1.6"/>'
           + "".join(f'<path d="M{x - 6} {y} H{x + 6}" stroke="var(--c2)" stroke-width="1.6"/>'
                     for x, y in ((lx0, fy - 10), (lx0, fy + H + 10), (lx1, head_y - 44), (lx1, fy + H + 10)))
           + T(lx0 + 22, ly0 + 36, sl["lab"], fit(sl["lab"], 18, 300, "capacidad lab"), "var(--white)", W6))
    # the door on the left is closed by a dashed bar until the engineers have joined
    door = (f'<path d="M{lx0} {fy - 10} V{fy + H + 10}" stroke="var(--c3)" stroke-width="2" stroke-dasharray="4 4">'
            f'{beat("opacity", [(0, 1), (JOIN1, 1), (JOIN1 + .02, 0), (_D07_R, 0), (min(_D07_R + .02, .999), 1), (1, 1)])}</path>')
    team = (_d10_bust(seats[0], head_y, SKIN_BROWN, shade("var(--c1)", 10), long=True) + _d10_bust(seats[1], head_y, SKIN_LIGHT, shade("var(--c5)", 35)))
    empty = f'<g>{_n13_off(JOIN1)}' + "".join(f'<path d="M{x - 27} {head_y + 62} C{x - 27} {head_y + 32} {x - 15} {head_y + 21} {x} {head_y + 21} C{x + 15} {head_y + 21} {x + 27} {head_y + 32} {x + 27} {head_y + 62}" '
                    f'fill="none" stroke="var(--line)" stroke-width="1.4" stroke-dasharray="4 4"/>'
                    f'<ellipse cx="{x}" cy="{head_y}" rx="14" ry="16" fill="none" stroke="var(--line)" stroke-width="1.4" stroke-dasharray="4 4"/>'
                    for x in seats[2:]) + '</g>'
    desk = (f'<rect x="{lx0 + 16}" y="{desk_y}" width="{lx1 - lx0 - 32}" height="14" rx="4" fill="var(--card)" stroke="var(--c2)" stroke-width="1.4"/>')
    # the board where a request becomes a prototype: three bars build it
    board = (card(bx - 14, fy - 14, W + 28, 150, "color-mix(in srgb, var(--c1) 14%, var(--card))", "var(--c2)", 14, 1.2, 'stroke-dasharray="5 5"')
             + spark(bx + W - 2, fy + 120, .5)
             + "".join(f'<g opacity="0">{beat("opacity", [(0, 0), (s + .025, 0), (s + .03, 1), (s + .055, 1), (s + .065, 0), (1, 0)])}'
                       f'{glow(bx + W - 2, fy + 120, 26, "var(--c4)", .7)}</g>' for s in SRV))
    for i, L in enumerate((.9, .7, .8)):
        y = fy + H + 22 + i * 22
        wbar = (W) * L
        board += f'<rect x="{bx}" y="{y}" width="{wbar:.0f}" height="8" rx="4" fill="var(--line)" opacity=".7"/>'
        prs = [(0, 1)]
        for s in SRV:
            a0, a1 = s + .025 + i * .008, s + .055 + i * .004
            prs += [(a0, 1), (a1, 0), (s + .07, 0), (s + .075, 1)]
        prs.append((1, 1))
        board += (f'<path d="M{bx} {y + 4} H{bx + wbar:.0f}" pathLength="1" stroke-dasharray="1" stroke="var(--c4)" stroke-width="8" stroke-linecap="round">'
                  f'{beat("stroke-dashoffset", prs)}</path>')
    g.append(land(lab + team + empty + board, .1, .55, 12) + door)

    # ---- the three AI-augmented engineers: they wait on the right and walk in through the right door
    eng = ""
    for k, x in enumerate(stage):
        eng += (_d10_bust(x, head_y, (SKIN_LIGHT, SKIN_BROWN, SKIN_LIGHT)[k], shade("var(--c1)", 45), "var(--c4)", k == 1)
                + spark(x + 19, head_y - 18, .45))
    sparks = "".join(f'<g opacity="0">{beat("opacity", [(0, 0), (s + .025, 0), (s + .03, 1), (s + .055, 1), (s + .065, 0), (1, 0)])}'
                     f'{glow(x + 19, head_y - 18, 22, "var(--c4)", .6)}</g>' for s in SRV for x in stage)
    walk = [(0, "0 0"), (JOIN0, "0 0"), (JOIN1, f"{dx_in} 0"), (_D07_R, f"{dx_in} 0"), (min(_D07_R + .02, .999), "0 0"), (1, "0 0")]
    g.append(land(f'<g>{_n01_tr(walk)}{sparks}{eng}</g>', .5, .5, 0, 30) + land(desk, .1, .55, 12))
    lab_e = sl["engineers"]
    out_lab = (f'<g>{_n13_off(JOIN0)}' + TCW(stage[1], head_y - 72, lab_e, 17, 15, "var(--c4)", W6, 1.25) + '</g>')
    in_lab = (f'<g opacity="0">{_n13_on(JOIN1)}' + TCW(seats[3], desk_y + 38, lab_e, 17, 15, "var(--c4)", W6, 1.25) + '</g>')
    g.append(land(out_lab, .7, .45, 8) + in_lab + _b14_ping(seats[3], head_y, 30, 90, JOIN1))

    # ---- the platform everything stands on
    plat = (card(836, 672, 720, 48, "color-mix(in srgb, var(--c1) 26%, var(--card))", "var(--c2)", 24, 1.4)
            + TC(1196, 702, sl["platform"], fit(sl["platform"], 17, 660, "capacidad platform"), "var(--white)", W6))
    g.append(land(plat, .9, .45, 10))

    # ---- the queue: each request moves up to the door, crosses the lab and leaves as a prototype
    slots = [fy + P * k for k in range(n)]
    outs = [slots[-1] - P * j for j in range(n)]          # the prototypes stack from the bottom up
    qs = []
    for k in range(n):
        s = SRV[k]
        pairs = [(0, "0 0")]
        for j in range(k):                                  # the queue moves up one place at each service
            prev = pairs[-1][1]
            pairs += [(SRV[j] + .005, prev), (SRV[j] + .025, f"0 {-P * (j + 1)}")]
        if k == 0:                                          # the front one nudges the closed door
            pairs += [(t, v) for t0 in (.08, .13, .18) for t, v in ((t0, "0 0"), (t0 + .01, "8 0"), (t0 + .02, "0 0"))]
        y0 = -P * k
        pairs += [(s, f"0 {y0}"), (s + .02, f"{bx - qx} {y0}"), (s + .065, f"{bx - qx} {y0}"),
                  (s + .08, f"{ox - qx} {y0}"), (s + .1, f"{ox - qx} {outs[k] - slots[k]}"),
                  (1, f"{ox - qx} {outs[k] - slots[k]}")]
        sw = s + .065
        body = (card(0, 0, W, H, "var(--dim)", "var(--line)", 10, 1.2)
                + f'<g>{_n13_off(sw)}' + _d10_clock(22, 22, "var(--c3)") + T(42, 27, req, fit(req, 15, W - 54, "capacidad request"), "var(--white)", W6) + '</g>'
                + f'<g opacity="0">{_n13_on(sw)}' + card(0, 0, W, H, f"color-mix(in srgb, {ok} 12%, var(--card))", ok, 10, 1.4)
                + _d10_clock(22, 22, ok, False) + T(42, 27, proto, fit(proto, 15, W - 76, "capacidad prototype"), "var(--white)", W6) + '</g>'
                + _b14_ok_dot(W - 20, 22, sw, ok, 9))
        qs.append(f'<g transform="translate({qx} {slots[k]})"><g>{_n01_tr(pairs)}'
                  f'<g>{beat("opacity", [(0, 1), (_D07_R, 1), (min(_D07_R + .02, .999), 0), (1, 0)])}{body}</g></g></g>'
                  + _b14_ping(bx + W / 2, fy + H / 2, 24, 80, sw, ok))
    g.append(seq(qs, .3, .5, 16))
    return "".join(g), D, FREEZE
