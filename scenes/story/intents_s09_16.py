"""Catalog scenes for the intents of 0.6.0 (2/2): funnel, timeline, org and map, two compositions each.

Same contract as intents_s01_08.py (its _ix_* pieces and simple_s01_08.py's _sm_* ones share this namespace):
portrait-aware from birth, icons from the slide's `vertical`, labels on opaque cards painted last, entrances done by
2 s, the story resolved before 10.8 s, no figure moves and no number is invented.

- ix09_funnel_stages · funnel-stages: a funnel of stages; the flow falls through, some leave at each stage; the stage
  that loses the most gets the question.
- ix10_funnel_gates · funnel-gates: ideas cross three questions; the ones that stop wait aside, the rest reach «build».
- ix11_timeline_milestones · timeline-milestones: dated milestones along one line; a cursor runs and each one pops.
- ix12_timeline_tracks · timeline-tracks: parallel workstreams as bars over periods; today's line sweeps, bars grow.
- ix13_org_tree · org-tree: a sponsor, three leads and their roles; a spark flows down the tree lighting each seat.
- ix14_org_squad · org-squad: their roles and ours paired across a shared goal; each pair talks through it in turn.
- ix15_map_hub · map-hub: an abstract dotted land (never a real border), a hub and its regions, linked one by one.
- ix16_map_lines · map-lines: two routes drawn like a transit map, crossing at one shared station.
"""


# ---------------------------------------------------------------- 9 · funnel: stages that leak
@register("scene", "ix09_funnel_stages")
@register("scene", "funnel-stages")
def sc_ix09_funnel_stages(sl, ctx):
    """A funnel of stages, each with its icon and name; to the left, what leaves. Loop: the flow falls through; at
    each stage a share leaves by the side and the stage lights; the stage named in `focus` gets its «?»; the result
    lights at the bottom. Frozen: every stage lit, the question on its stage, the result on."""
    x, y, w, h, P, k = _sm_zone(sl)
    stages = list(sl.get("levels") or [])[:5]
    n = max(1, len(stages))
    names = _sm_icons(sl, n)
    focus = int(sl.get("focus", -1))
    bot = 80 * k
    fx0, fw = x + 70 * k, w * .5
    fcx = fx0 + fw / 2
    top, fh = y + 20 * k, h - bot - 40 * k
    lh = fh / n
    wid = lambda i: fw * (1 - .7 * i / n)
    times = [.08 + .13 * i for i in range(n)]
    art, text = [glow(fcx, y + h * .4, fw * .8, "var(--brand)", .35)], []
    layers, labs = [], []
    for i, lab in enumerate(stages):
        y0, y1 = top + i * lh, top + (i + 1) * lh
        w0, w1 = wid(i), wid(i + 1)
        poly = f"M{fcx - w0 / 2:.1f} {y0 + 3:.1f} H{fcx + w0 / 2:.1f} L{fcx + w1 / 2:.1f} {y1 - 3:.1f} H{fcx - w1 / 2:.1f} Z"
        layers.append(f'<path d="{poly}" fill="color-mix(in srgb, var(--c1) {30 + 10 * i}%, var(--card))" stroke="var(--c2)" stroke-width="1.4"/>'
                      f'<path d="{poly}" fill="none" stroke="var(--c4)" stroke-width="2.4" opacity="0">{_sm_on(times[i])}</path>')
        r = min(22 * k, lh * .26)
        cy = (y0 + y1) / 2
        layers.append(_sm_badge(names[i], fcx, cy, r) + _sm_lit_badge(names[i], fcx, cy, r, times[i]))
        # the label card to the right, joined by a thin line
        lx = fx0 + fw + 22 * k
        lw = x + w - lx
        layers.append(f'<path d="M{fcx + (w0 + w1) / 4 + 4:.1f} {cy:.1f} H{lx:.1f}" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="3 5" opacity=".7"/>')
        ca, cl = _ix_tag(lx, cy - 24 * k, lw, 48 * k, lab, "", k, times[i])
        layers.append(ca)
        labs.append(cl)
        # the leak: a share leaves by the left side at the end of this stage
        if i < n - 1:
            ex, ey = fcx - (w1 / 2) - 2, y1 - 6
            leak = f"M{fcx:.1f} {y0 + lh * .2:.1f} Q{fcx - w1 * .3:.1f} {y1 - lh * .3:.1f} {ex:.1f} {ey:.1f} T{x + 10 * k:.1f} {ey + lh * .45:.1f}"
            art.append(_sm_ride(leak, times[i] + .02, times[i] + .1, 5 * k, "var(--muted)"))
            art.append(f'<path d="M{ex:.1f} {ey:.1f} q{-24 * k:.1f} {4 * k:.1f} {-36 * k:.1f} {22 * k:.1f}" fill="none" stroke="var(--muted)" stroke-width="1.8" stroke-dasharray="3 4"/>')
        if i == focus:
            qx = fcx + (w0 + w1) / 4 - 16 * k
            layers.append(f'<g opacity="0">{_sm_on(times[-1] + .08)}' + _sm_q(qx, cy - lh * .24, 14 * k, times[-1] + .08, k) + '</g>')
    art.append(seq(layers, .1, .5, 10))
    text.append(seq(labs, .15, .5, 10))
    # the flow that falls through: three drops per loop, staggered
    fall = f"M{fcx:.1f} {top - 16 * k:.1f} V{top + fh + 8 * k:.1f}"
    for j in range(3):
        a = .05 + j * .22
        art.append(_sm_ride(fall, a, a + .24, 5 * k))
    if sl.get("out"):
        text.append(land(_sm_text(x, top + fh + 14 * k, sl["out"], 16 * k, fw * .7, "var(--muted)", lines_max=1, extra=""), .3, .45, 0))
    ga, gl = _ix_goal(x + w / 2, y + h - 26 * k, sl.get("result", ""), times[-1] + .06, k, w - 20)
    art.append(land(ga, .4, .45, 8))
    text.append(land(gl, .4, .45, 8))
    if focus >= 0 and sl.get("focus_label"):
        text.append(f'<g opacity="0">{_sm_on(times[-1] + .08)}' + _sm_text(x + w, top - 4 * k, sl["focus_label"], 17 * k, w * .6, "var(--c4)", "end", 1) + '</g>')
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 10 · funnel: ideas through three questions
@register("scene", "ix10_funnel_gates")
@register("scene", "funnel-gates")
def sc_ix10_funnel_gates(sl, ctx):
    """Ideas in a column, three questions as gates, «Por ahora no» below and «Construimos» at the end. Loop: each idea
    runs toward the end; where a gate says no it drops aside, without drama; the rest reach the end with a check.
    Frozen: each idea marked (built or aside, with the question that stopped it)."""
    x, y, w, h, P, k = _sm_zone(sl)
    ok = ctx.brand.c("dark.ok")
    ideas = list(sl.get("ideas") or [])[:5]
    gates = list(sl.get("gates") or [])[:3]
    stops = list(sl.get("stops") or [])
    ni, ng = max(1, len(ideas)), max(1, len(gates))
    names = _sm_icons(sl, ni)
    lw = w * (.36 if P else .4)
    head = 84 * k
    aside_h = 70 * k
    ry0 = y + head
    rh = (h - head - aside_h - 24 * k) / ni
    gx0, gx1 = x + lw + 30 * k, x + w - 70 * k
    gxs = [gx0 + (gx1 - gx0) * (j + .5) / ng for j in range(ng)]
    endx = x + w - 30 * k
    ay = y + h - aside_h / 2
    runs = [.08 + .13 * i for i in range(ni)]
    art, text = [], []
    # the gates: a bar with its question on top
    gw = (gx1 - gx0) / ng
    for j, g in enumerate(gates):
        gx = gxs[j]
        art.append(land(card(gx - gw / 2 + 6, y, gw - 12, head - 12 * k, "var(--card)", "var(--c2)", 10, 1.2)
                        + f'<path d="M{gx:.1f} {ry0:.1f} V{ry0 + ni * rh:.1f}" stroke="var(--c2)" stroke-width="{5 * k:.1f}" stroke-linecap="round" opacity=".6"/>', .1 + j * .06, .45, 10))
        text.append(land(_sm_text(gx, y + (head - 12 * k) / 2, g, 16 * k, gw - 16, anchor="middle", lines_max=2), .1 + j * .06, .45, 10))
    # the end and the aside tray
    art.append(land(f'<path d="M{endx:.1f} {ry0:.1f} V{ry0 + ni * rh:.1f}" stroke="{ok}" stroke-width="{5 * k:.1f}" stroke-linecap="round"/>'
                    + card(gx0 - 10 * k, ay - aside_h / 2 + 6, gx1 - gx0 + 20 * k, aside_h - 12, "var(--ink)", "var(--line)", 12, 1.2, 'stroke-dasharray="5 6"'), .2, .45, 0))
    text.append(land(_sm_text(gx0 + 6 * k, ay, sl.get("aside", ""), 17 * k, (gx1 - gx0) * .5, "var(--muted)", lines_max=1)
                     + f'<g transform="rotate(-90 {endx + 22 * k:.1f} {ry0 + ni * rh / 2:.1f})">'
                     + _sm_text(endx + 22 * k, ry0 + ni * rh / 2, sl.get("keep", ""), 17 * k, ni * rh - 10, ok, "middle", 1) + '</g>', .2, .45, 0))
    rows, labs = [], []
    parked = 0
    for i, idea in enumerate(ideas):
        cy = ry0 + (i + .5) * rh
        r = min(18 * k, rh * .3)
        st = int(stops[i]) if i < len(stops) else -1
        a = runs[i]
        rows.append(card(x, cy - rh / 2 + 4, lw, rh - 8, "var(--card)", "var(--line)", 10, 1.2) + _sm_badge(names[i], x + 10 * k + r, cy, r))
        labs.append(_sm_text(x + 20 * k + 2 * r, cy, idea, 17 * k, lw - 60 * k - 2 * r, lines_max=2))
        mx = x + lw - 20 * k
        if 0 <= st < ng:
            sx = gxs[st] - 10 * k
            px = gx0 + 20 * k + parked * 34 * k + (gx1 - gx0) * .5
            parked += 1
            path = f"M{x + lw:.1f} {cy:.1f} H{sx:.1f} Q{sx:.1f} {ay:.1f} {px:.1f} {ay:.1f}"
            art.append(_sm_ride(path, a, a + .1, 6 * k, "var(--c2)"))
            art.append(f'<g opacity="0">{_sm_on(a + .1)}<circle cx="{px:.1f}" cy="{ay:.1f}" r="{9 * k:.1f}" fill="var(--c2)" opacity=".7"/></g>')
            art.append(f'<path d="M{x + lw:.1f} {cy:.1f} H{sx:.1f}" stroke="var(--c2)" stroke-width="2" stroke-dasharray="4 5" opacity="0">{_sm_on(a + .1)}</path>')
            text.append(f'<g opacity="0">{_sm_on(a + .1)}<circle cx="{mx:.1f}" cy="{cy:.1f}" r="{12 * k:.1f}" fill="var(--dim)" stroke="var(--c2)" stroke-width="1.4"/></g>')
            text.append(f'<g opacity="0">{_sm_on(a + .1)}' + TC(f"{mx:.1f}", f"{cy + 6 * k:.1f}", str(st + 1), int(16 * k), "var(--white)", W6) + '</g>')
            art.append(_sm_ping(gxs[st], cy, 6, 22 * k, a + .06, "var(--c2)"))
        else:
            path = f"M{x + lw:.1f} {cy:.1f} H{endx:.1f}"
            art.append(_sm_ride(path, a, a + .12, 6 * k))
            art.append(f'<path d="{path}" stroke="var(--c4)" stroke-width="2.4" opacity="0">{_sm_on(a + .12)}</path>')
            text.append(_sm_ok(mx, cy, 12 * k, a + .12, ok))
            art.append(_sm_ping(endx, cy, 6, 24 * k, a + .12, ok))
    art.append(seq(rows, .15, .45, 10))
    text.append(seq(labs, .15, .45, 10))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 11 · timeline: milestones on one line
@register("scene", "ix11_timeline_milestones")
@register("scene", "timeline-milestones")
def sc_ix11_timeline_milestones(sl, ctx):
    """Dated milestones on one line (across on desktop, down the phone), alternating sides. Loop: a cursor runs from
    «Hoy», each milestone pops and its card lights as it passes. Frozen: every milestone reached."""
    x, y, w, h, P, k = _sm_zone(sl)
    evs = [list(e) + [""] for e in (sl.get("events") or [])][:6]
    n = max(1, len(evs))
    names = _sm_icons(sl, n)
    t0, t1 = .06, .76
    art, text = [glow(x + w / 2, y + h / 2, w * .5, "var(--brand)", .3)], []
    R = 22 * k
    if P:
        ax = x + w / 2
        a0, a1 = y + 60 * k, y + h - 20 * k
        pts = [(ax, a0 + (a1 - a0) * (i + .5) / n) for i in range(n)]
        line = f"M{ax:.1f} {a0 - 30 * k:.1f} V{a1:.1f}"
        start = (ax, a0 - 30 * k)
    else:
        ay = y + h / 2
        a0, a1 = x + 30, x + w - 10
        pts = [(a0 + (a1 - a0) * (i + .5) / n, ay) for i in range(n)]
        line = f"M{a0 - 20:.1f} {ay:.1f} H{a1:.1f}"
        start = (a0 - 20, ay)
    art.append(land(f'<path d="{line}" stroke="var(--line)" stroke-width="{8 * k:.1f}" stroke-linecap="round"/>', .1, .45, 0))
    art.append(f'<path d="{line}" pathLength="1" stroke="var(--c4)" stroke-width="{4 * k:.1f}" stroke-linecap="round" stroke-dasharray="1" stroke-dashoffset="1">'
               f'{beat("stroke-dashoffset", [(0, 1), (t0, 1), (t1, 0), (_IX_END, 0), (1, 1)])}</path>')
    art.append(_sm_ride(line, t0, t1, 9 * k))
    L = (a1 - (a0 - 30 * k)) if P else (a1 - (a0 - 20))
    times = [t0 + (t1 - t0) * (((p[1] - start[1]) if P else (p[0] - start[0])) / L) for p in pts]
    marks, labs = [], []
    for i, ((px, py), (when, what, *_r)) in enumerate(zip(pts, evs)):
        side = 1 if i % 2 == 0 else -1
        marks.append(_sm_badge(names[i], px, py, R) + _sm_lit_badge(names[i], px, py, R, times[i]))
        if P:
            cw, ch = w / 2 - R - 26 * k, min(76 * k, (a1 - a0) / n - 8 * k)
            cx0 = px + R + 14 * k if side > 0 else px - R - 14 * k - cw
            cy0 = py - ch / 2
            stem = f'<path d="M{px + side * R:.1f} {py:.1f} H{px + side * (R + 14 * k):.1f}" stroke="var(--c2)" stroke-width="1.6"/>'
        else:
            cw, ch = min(2 * (a1 - a0) / n - 40, 216), 76
            cx0 = max(x, min(x + w - cw, px - cw / 2))
            cy0 = py - R - 40 - ch if side > 0 else py + R + 40
            stem = f'<path d="M{px:.1f} {py - side * R:.1f} V{py - side * (R + 40):.1f}" stroke="var(--c2)" stroke-width="1.6"/>'
        ca, cl = _ix_tag(cx0, cy0, cw, ch, what, when, k, times[i])
        marks.append(stem + ca)
        labs.append(cl)
    art.append(seq(marks, .15, .45, 10))
    text.append(seq(labs, .15, .45, 10))
    now = sl.get("now", "")
    if now:
        sx, sy = start
        art.append(land(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{8 * k:.1f}" fill="var(--c4)"/>', .1, .4, 0))
        if P:
            text.append(land(_sm_text(sx + 20 * k, sy, now, 18 * k, w * .4, "var(--c4)", lines_max=1), .1, .4, 0))
        else:
            text.append(land(_sm_text(sx, sy + 34, now, 17, 120, "var(--c4)", "middle", 1), .1, .4, 0))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 12 · timeline: parallel tracks over periods
@register("scene", "ix12_timeline_tracks")
@register("scene", "timeline-tracks")
def sc_ix12_timeline_tracks(sl, ctx):
    """Workstreams as rows, periods as columns; each bar spans its periods. Loop: today's line sweeps across and every
    bar grows as the line passes it, its label lighting when done; the decision gate lights at the end. Frozen: every
    bar complete, the gate lit."""
    x, y, w, h, P, k = _sm_zone(sl)
    ok = ctx.brand.c("dark.ok")
    periods = list(sl.get("periods") or [])[:6]
    tracks = [list(t) + [0, 1, ""] for t in (sl.get("tracks") or [])][:5]
    npd, nt = max(1, len(periods)), max(1, len(tracks))
    names = _sm_icons(sl, nt)
    lw = 0 if P else w * .26
    head = 50 * k
    bot = 116 * k
    px0, px1 = x + lw, x + w
    cw = (px1 - px0) / npd
    rh = (h - head - bot) / nt
    t0, t1 = .06, .78
    tx = lambda c: t0 + (t1 - t0) * c / npd
    art, text = [], []
    grid = "".join(f'<path d="M{px0 + cw * c:.1f} {y + head:.1f} V{y + head + nt * rh:.1f}" stroke="var(--line)" stroke-width="1" stroke-dasharray="3 6"/>' for c in range(npd + 1))
    art.append(land(grid, .1, .45, 0))
    hl = "".join(card(px0 + cw * c + 3, y, cw - 6, head - 10 * k, "var(--card)", "var(--line)", 8, 1)
                 + _sm_text(px0 + cw * (c + .5), y + (head - 10 * k) / 2, p, 16 * k, cw - 14, anchor="middle", lines_max=1)
                 for c, p in enumerate(periods))
    text.append(land(hl, .1, .45, 8))
    rows, labs = [], []
    for i, (name, s, e, what, *_r) in enumerate(tracks):
        s, e = max(0, int(s)), min(npd, int(e))
        ry = y + head + i * rh
        bx, bw = px0 + cw * s + 4, cw * (e - s) - 8
        bh = min(40 * k, rh * .42)
        if P:
            by = ry + rh * .5
            r = 14 * k
            rows.append(icon(names[i], x + r, ry + rh * .24, 2 * r, "var(--c2)"))
            labs.append(_sm_text(x + 2 * r + 10 * k, ry + rh * .24, name, 18 * k, w - 2 * r - 20 * k, "var(--muted)", lines_max=1))
        else:
            by = ry + (rh - bh) / 2
            r = 16
            rows.append(card(x, ry + 6, lw - 12, rh - 12, "var(--card)", "var(--line)", 10, 1) + icon(names[i], x + 12 + r, ry + rh / 2, 2 * r, "var(--c2)"))
            labs.append(_sm_text(x + 20 + 2 * r, ry + rh / 2, name, 17, lw - 44 - 2 * r, lines_max=2))
        a, b = tx(s), tx(e)
        rows.append(f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="{bh / 2:.1f}" fill="none" stroke="var(--c2)" stroke-width="1.2" stroke-dasharray="4 5" opacity=".6"/>'
                    f'<rect x="{bx:.1f}" y="{by:.1f}" width="0" height="{bh:.1f}" rx="{bh / 2:.1f}" fill="color-mix(in srgb, var(--c1) 70%, var(--card))" stroke="var(--c4)" stroke-width="1.6">'
                    f'{beat("width", [(0, 0), (a, 0), (b, round(bw, 1)), (_IX_END, round(bw, 1)), (1, 0)])}</rect>')
        text.append(f'<g opacity="0">{_sm_on(b)}' + _sm_text(bx + 14 * k, by + bh / 2, what, 16 * k, bw - 24 * k, lines_max=1) + '</g>')
    art.append(seq(rows, .15, .45, 8))
    text.append(seq(labs, .15, .45, 8))
    # today's line sweeps across
    ly0, ly1 = y + head - 6, y + head + nt * rh + 6
    art.append(f'<g>{beat("opacity", [(0, 0), (t0, 0), (t0 + .01, 1), (t1, 1), (t1 + .03, 0), (1, 0)])}'
               f'<animateTransform attributeName="transform" type="translate" values="0 0;0 0;{px1 - px0:.1f} 0;{px1 - px0:.1f} 0" keyTimes="0;{t0:.3f};{t1:.3f};1" dur="{D}s" repeatCount="indefinite"/>'
               f'<path d="M{px0:.1f} {ly0:.1f} V{ly1:.1f}" stroke="var(--c4)" stroke-width="2.4"/>'
               f'<circle cx="{px0:.1f}" cy="{ly0:.1f}" r="{6 * k:.1f}" fill="var(--c4)"/></g>')
    if sl.get("today"):
        text.append(land(_sm_text(px0, ly1 + 22 * k, sl["today"], 16 * k, cw * 1.5, "var(--c4)", lines_max=1), .2, .4, 0))
    ga, gl = _ix_goal(x + w / 2, y + h - 26 * k, sl.get("gate", ""), t1 + .02, k, w - 20, "generico/meta")
    art.append(land(ga, .4, .45, 8))
    text.append(land(gl, .4, .45, 8))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 13 · org: a tree of roles
def _ix_seat(cx, y, w, h, role, k, at, mark=None, head=False):
    """(art, label): a card with a faceless bust (and the area's icon for a lead), lit from at."""
    art = (card(cx - w / 2, y, w, h, "var(--card)", "var(--c2)" if head else "var(--line)", 12, 1.4)
           + f'<rect x="{cx - w / 2:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="12" fill="color-mix(in srgb, var(--c4) 10%, transparent)" stroke="var(--c4)" stroke-width="2" opacity="0">{_sm_on(at)}</rect>'
           + _sm_bust(cx - w / 2 + 26 * k, y + h / 2 - 4 * k, .95 * k, SKIN_LIGHT if head else SKIN_BROWN, "var(--c1)"))
    room = w - 62 * k
    if mark:
        art += icon(mark, cx + w / 2 - 20 * k, y + 20 * k, 22 * k, "var(--c4)")
        room -= 26 * k
    return art, _sm_text(cx - w / 2 + 52 * k, y + h / 2, role, (18 if head else 17) * k, room, lines_max=2)


@register("scene", "ix13_org_tree")
@register("scene", "org-tree")
def sc_ix13_org_tree(sl, ctx):
    """A sponsor on top, three leads (each with the icon of an area of their business) and the roles under each
    lead. Loop: a spark flows down from the sponsor to each lead and on to their roles, each seat lights; the shared
    goal lights at the end. Frozen: every seat lit, the goal on."""
    x, y, w, h, P, k = _sm_zone(sl)
    teams = list(sl.get("teams") or [])[:3]
    nt = max(1, len(teams))
    names = _sm_icons(sl, nt)
    gap = 14 * k
    cw = (w - (nt - 1) * gap) / nt
    th, lh, mh = 70 * k, 76 * k, 62 * k
    bot = 70 * k
    ty, ly = y, y + th + 60 * k
    my0 = ly + lh + 30 * k
    mmax = max([len(list(t.get("members") or [])[:3]) for t in teams] + [1])
    mh = min(96 * k, (y + h - bot - 20 * k - my0 - (mmax - 1) * 16 * k) / mmax)
    art, text = [glow(x + w / 2, y + h * .4, w * .5, "var(--brand)", .3)], []
    top_at = .06
    a, b = _ix_seat(x + w / 2, ty, min(w * .6, 380 * k), th, sl.get("top", ""), k, top_at, head=True)
    art.append(land(a, .1, .45, 10))
    text.append(land(b, .1, .45, 10))
    bus_y = ty + th + 30 * k
    art.append(land(f'<path d="M{x + w / 2:.1f} {ty + th:.1f} V{bus_y:.1f} M{x + cw / 2:.1f} {bus_y:.1f} H{x + w - cw / 2:.1f}" stroke="var(--c2)" stroke-width="1.8" fill="none"/>', .15, .45, 0))
    seats, labs = [], []
    for i, tm in enumerate(teams):
        cx = x + i * (cw + gap) + cw / 2
        la = .14 + .16 * i
        down = f"M{x + w / 2:.1f} {ty + th:.1f} V{bus_y:.1f} H{cx:.1f} V{ly:.1f}"
        art.append(f'<path d="M{cx:.1f} {bus_y:.1f} V{ly:.1f}" stroke="var(--c2)" stroke-width="1.8"/>')
        art.append(_sm_ride(down, la - .07, la, 6 * k))
        sa, sb_ = _ix_seat(cx, ly, cw, lh, tm.get("lead", ""), k, la, names[i])
        seats.append(sa)
        labs.append(sb_)
        members = list(tm.get("members") or [])[:3]
        mw = cw - 22 * k
        mx = cx + 11 * k
        for j, m in enumerate(members):
            my = my0 + j * (mh + 16 * k)
            ma = la + .05 + .04 * j
            spine = f"M{cx - cw / 2 + 10 * k:.1f} {ly + lh:.1f} V{my + mh / 2:.1f} H{mx - mw / 2:.1f}"
            art.append(f'<path d="{spine}" fill="none" stroke="var(--c2)" stroke-width="1.4" opacity=".7"/>')
            art.append(_sm_ride(spine, ma - .04, ma, 5 * k))
            sa, sb_ = _ix_seat(mx, my, mw, mh, m, k, ma)
            seats.append(sa)
            labs.append(sb_)
    art.append(seq(seats, .15, .45, 10))
    text.append(seq(labs, .15, .45, 10))
    ga, gl = _ix_goal(x + w / 2, y + h - 26 * k, sl.get("goal", ""), .7, k, w - 20, "generico/meta")
    art.append(land(ga, .4, .45, 8))
    text.append(land(gl, .4, .45, 8))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 14 · org: two teams paired around a goal
@register("scene", "ix14_org_squad")
@register("scene", "org-squad")
def sc_ix14_org_squad(sl, ctx):
    """Their roles and ours (columns facing each other on desktop, rows above and below on the phone), paired through
    a shared goal in the middle. Loop: each pair talks in turn, a pulse goes from their role to the goal and on to
    ours and back, and the bridge stays lit; with every bridge lit, the goal and the rhythm light. Frozen: one team."""
    x, y, w, h, P, k = _sm_zone(sl)
    ok = ctx.brand.c("dark.ok")
    left = list(sl.get("their_roles") or [])[:3]
    right = list(sl.get("our_roles") or [])[:3]
    n = max(1, len(left), len(right))
    names = _sm_icons(sl, n)
    bot = 70 * k
    art, text = [], []
    hub_r = 70 * k
    if P:
        cx, cy = x + w / 2, y + (h - bot) / 2
        gap = 12 * k
        cw, ch = (w - (n - 1) * gap) / n, 110 * k
        ly, ry = y + 40 * k, y + h - bot - ch - 40 * k
        lpos = [(x + i * (cw + gap) + cw / 2, ly + ch / 2) for i in range(n)]
        rpos = [(x + i * (cw + gap) + cw / 2, ry + ch / 2) for i in range(n)]
        heads = [(x, ly - 20 * k, "start"), (x, ry + ch + 22 * k, "start")]
    else:
        cx, cy = x + w / 2, y + (h - bot) / 2
        cw, ch = w * .32, 92
        rh = (h - bot - 60) / n
        lpos = [(x + cw / 2, y + 50 + rh * (i + .5)) for i in range(n)]
        rpos = [(x + w - cw / 2, y + 50 + rh * (i + .5)) for i in range(n)]
        heads = [(x, y + 20, "start"), (x + w, y + 20, "end")]
    turns = [.1 + .18 * i for i in range(n)]
    done = turns[-1] + .14
    hub_art = (land(glow(cx, cy, hub_r * 2, "var(--c4)", .18)
                    + f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{hub_r:.1f}" fill="var(--card)" stroke="var(--c4)" stroke-width="2"/>'
                    + f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{hub_r:.1f}" fill="color-mix(in srgb, var(--c4) 16%, var(--card))" stroke="{ok}" stroke-width="3" opacity="0">{_sm_on(done)}</circle>'
                    + icon("generico/meta", cx, cy - hub_r * .38, 30 * k, "var(--c4)") + _sm_ping(cx, cy, hub_r, hub_r * 1.5, done, ok), .1, .5, 0))
    hub_txt = (land(_sm_text(cx, cy + hub_r * .22, sl.get("center", ""), 18 * k, hub_r * 1.7, anchor="middle", lines_max=2), .1, .5, 0))
    for side, (pos, roles, (hx, hy, anc)) in enumerate(((lpos, left, heads[0]), (rpos, right, heads[1]))):
        cards, labs = [], []
        lab = sl.get("their_team" if side == 0 else "our_team", "")
        text.append(land(_sm_text(hx, hy, str(lab).upper(), 15 * k, w * .5, "var(--c4)", anc, 1, 'font-weight="600" letter-spacing="2"'), .1, .4, 0))
        for i, role in enumerate(roles):
            px, py = pos[i]
            r = 18 * k
            if P:
                ex, ey = px, (py + ch / 2 if side == 0 else py - ch / 2)
            else:
                ex, ey = (px + cw / 2 if side == 0 else px - cw / 2), py
            bridge = _ix_curve((ex, ey), (cx, cy), P)
            art.append(f'<path d="{bridge}" fill="none" stroke="var(--c2)" stroke-width="1.6" stroke-dasharray="4 6" opacity=".7"/>'
                       f'<path d="{bridge}" fill="none" stroke="var(--c4)" stroke-width="2.6" opacity="0">{_sm_on(turns[i] + (.04 if side == 0 else .08))}</path>')
            t = turns[i]
            if side == 0:
                art.append(_sm_ride(bridge, t, t + .04, 6 * k))
            else:
                back = _ix_curve((cx, cy), (ex, ey), P)
                art.append(_sm_ride(back, t + .04, t + .08, 6 * k))
                art.append(_sm_ride(bridge, t + .09, t + .13, 6 * k, "var(--c2)"))
            c = (card(px - cw / 2, py - ch / 2, cw, ch, "var(--card)", "var(--line)", 12, 1.3)
                 + f'<rect x="{px - cw / 2:.1f}" y="{py - ch / 2:.1f}" width="{cw:.1f}" height="{ch:.1f}" rx="12" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">{_sm_on(t + (0 if side == 0 else .08))}</rect>')
            if P:
                c += _sm_bust(px, py - ch * .18, .95 * k, SKIN_BROWN if side == 0 else SKIN_LIGHT, "var(--c1)" if side else "var(--c2)")
                labs.append(_sm_text(px, py + ch * .28, role, 17 * k, cw - 16 * k, anchor="middle", lines_max=2))
            else:
                c += _sm_bust(px - cw / 2 + 28, py - 4, 1.05, SKIN_BROWN if side == 0 else SKIN_LIGHT, "var(--c1)" if side else "var(--c2)")
                c += icon(names[i], px + cw / 2 - 20, py - ch / 2 + 20, 22, "var(--c2)")
                labs.append(_sm_text(px - cw / 2 + 56, py + 4, role, 17, cw - 90, lines_max=2))
            cards.append(c)
        art.append(seq(cards, .15 + side * .1, .45, 10))
        text.append(seq(labs, .15 + side * .1, .45, 10))
    art.append(hub_art)          # the goal over its bridges
    text.insert(0, hub_txt)
    ga, gl = _ix_goal(x + w / 2, y + h - 26 * k, sl.get("rhythm", ""), done + .03, k, w - 20, "uso/calendario")
    art.append(land(ga, .4, .45, 8))
    text.append(land(gl, .4, .45, 8))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 15 · map: a hub and its regions
def _ix_land(cx, cy, rx, ry, step, seed=0):
    """An abstract dotted land (never a real border): rows of round dots inside a wobbly ellipse."""
    def inside(px, py):
        dx, dy = (px - cx) / rx, (py - cy) / ry
        a = math.atan2(dy, dx)
        r = 1 + .1 * math.sin(3 * a + seed) + .07 * math.cos(5 * a + 2 * seed) + .05 * math.sin(7 * a)
        return dx * dx + dy * dy <= r * r
    out = []
    yy = cy - ry * 1.2
    while yy <= cy + ry * 1.2:
        xs = [xx for xx in range(int(cx - rx * 1.25), int(cx + rx * 1.25), 4) if inside(xx, yy)]
        if xs:
            x0 = xs[0] + (step - (xs[0] - int(cx - rx * 1.25)) % step) % step
            if xs[-1] > x0:
                out.append(f"M{x0} {yy:.0f} H{xs[-1]}")
        yy += step
    return (f'<path d="{" ".join(out)}" stroke="var(--c2)" stroke-width="{step * .28:.1f}" stroke-linecap="round" '
            f'stroke-dasharray="0 {step}" opacity=".35"/>')


@register("scene", "ix15_map_hub")
@register("scene", "map-hub")
def sc_ix15_map_hub(sl, ctx):
    """An abstract land of dots, their hub in the middle and a pin per region. Loop: a line draws from the hub to each
    region in turn, a token rides it and the region lights with its icon; with every region linked, the note lights.
    Frozen: every region linked and lit."""
    x, y, w, h, P, k = _sm_zone(sl)
    regions = list(sl.get("regions") or [])[:6]
    n = max(1, len(regions))
    names = _sm_icons(sl, n)
    bot = 70 * k
    cx, cy = x + w / 2, y + (h - bot) / 2
    rx, ry = w * .44, (h - bot) * .44
    art, text = [glow(cx, cy, rx, "var(--brand)", .35)], []
    art.append(land(_ix_land(cx, cy, rx, ry, 18 * k, 1.3), .1, .6, 0))
    times = [.1 + .12 * i for i in range(n)]
    note_at = times[-1] + .1
    R = 22 * k
    pins, labs = [], []
    for i, lab in enumerate(regions):
        a = math.radians(-100 + 360 * i / n)
        px, py = cx + rx * .72 * math.cos(a), cy + ry * .72 * math.sin(a)
        link = f"M{cx:.1f} {cy:.1f} Q{(cx + px) / 2 + (py - cy) * .25:.1f} {(cy + py) / 2 - (px - cx) * .25:.1f} {px:.1f} {py:.1f}"
        art.append(f'<path d="{link}" fill="none" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="3 6" opacity=".6"/>'
                   f'<path d="{link}" pathLength="1" fill="none" stroke="var(--c4)" stroke-width="2.6" stroke-dasharray="1" stroke-dashoffset="1">'
                   f'{beat("stroke-dashoffset", [(0, 1), (times[i] - .06, 1), (times[i], 0), (_IX_END, 0), (1, 1)])}</path>')
        art.append(_sm_ride(link, times[i] - .06, times[i], 6 * k))
        pins.append(_sm_badge(names[i], px, py, R) + _sm_lit_badge(names[i], px, py, R, times[i]))
        lw = min(bold_width(_(str(lab)), 18 * k, current_factor()) + 30 * k, w * .4)
        lx = max(x, min(x + w - lw, px - lw / 2))
        ly = py + R + 8 * k if math.sin(a) > -.3 else py - R - 8 * k - 36 * k
        ca, cl = _ix_tag(lx, ly, lw, 36 * k, lab, "", k, times[i])
        pins.append(ca)
        labs.append(cl)
    art.append(seq(pins, .2, .45, 8))
    text.append(seq(labs, .2, .45, 8))
    # the hub
    hr = 30 * k
    art.append(land(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{hr:.1f}" fill="var(--c4)"/>' + icon("publico/edificio", cx, cy, hr * 1.1, ctx.brand.on("var(--c4)"))
                    + f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{hr:.1f}" fill="none" stroke="var(--c4)" stroke-width="2">{loop("r", f"{hr:.0f};{hr * 1.6:.0f};{hr:.0f}", 2.6)}{loop("opacity", "1;0;1", 2.6)}</circle>', .1, .45, 0))
    hub = sl.get("hub", "")
    hw = min(bold_width(_(str(hub)), 18 * k, current_factor()) + 30 * k, w * .5)
    text.append(land(card(cx - hw / 2, cy + hr + 8 * k, hw, 36 * k, "var(--card)", "var(--c4)", 10, 1.4)
                     + _sm_text(cx, cy + hr + 26 * k, hub, 18 * k, hw - 16 * k, anchor="middle", lines_max=1), .1, .45, 0))
    ga, gl = _ix_goal(x + w / 2, y + h - 26 * k, sl.get("note", ""), note_at, k, w - 20)
    art.append(land(ga, .4, .45, 8))
    text.append(land(gl, .4, .45, 8))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 16 · map: two routes like a transit map
@register("scene", "ix16_map_lines")
@register("scene", "map-lines")
def sc_ix16_map_lines(sl, ctx):
    """Two routes drawn like a transit map: one across, one down with a bend, crossing at the shared station. Loop:
    the first route lights stop by stop, then the second, a token riding each; the shared station lights last with the
    note. Frozen: both routes lit, the shared station on."""
    x, y, w, h, P, k = _sm_zone(sl)
    lines = list(sl.get("routes") or [])[:2]
    hub = sl.get("hub", "")
    if len(lines) < 2:
        lines = lines + [{"name": "", "stops": [hub]}] * (2 - len(lines))
    A, B = [list(l.get("stops") or [hub]) for l in lines]
    ha = A.index(hub) if hub in A else len(A) // 2
    hb = B.index(hub) if hub in B else len(B) // 2
    bot = 70 * k
    art, text = [], []
    na, nb = len(A), len(B)
    sa = (w - 80 * k) / max(1, na - 1)
    hx = x + 40 * k + sa * ha
    sb_ = (h - bot - 150 * k) / max(1, nb - 1)
    hy = y + 90 * k + sb_ * hb
    pa = [(x + 40 * k + sa * i, hy) for i in range(na)]
    pb = [(hx, y + 90 * k + sb_ * j) for j in range(nb)]
    if hb >= 1:   # the first stop of the second route bends in from the left
        pb[0] = (hx - sb_ * .8, pb[0][1])
    cols = ("var(--c4)", "var(--accent)")
    ta = [.06 + .08 * i for i in range(na)]
    tb = [ta[-1] + .08 + .08 * j for j in range(nb)]
    hub_at = max(tb[-1], ta[-1]) + .06
    names = _sm_icons(sl, na + nb)
    for li, (pts, times, col) in enumerate(((pa, ta, cols[0]), (pb, tb, cols[1]))):
        d = "M" + " L".join(f"{px:.1f} {py:.1f}" for px, py in pts)
        art.append(land(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{12 * k:.1f}" stroke-linecap="round" stroke-linejoin="round" opacity=".25"/>', .1 + li * .1, .5, 0))
        art.append(f'<path d="{d}" pathLength="1" fill="none" stroke="{col}" stroke-width="{8 * k:.1f}" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1" stroke-dashoffset="1">'
                   f'{beat("stroke-dashoffset", [(0, 1), (times[0], 1), (times[-1], 0), (_IX_END, 0), (1, 1)])}</path>')
        art.append(_sm_ride(d, times[0], times[-1], 8 * k, "var(--white)"))
    # stations: white dots with a ring; labels on cards (above/below across, to the right down)
    R = 13 * k
    st, labs = [], []
    hub_idx = {(0, ha), (1, hb)}
    for li, (pts, stops, times, col) in enumerate(((pa, A, ta, cols[0]), (pb, B, tb, cols[1]))):
        for i, ((px, py), s) in enumerate(zip(pts, stops)):
            if (li, i) in hub_idx:
                continue
            st.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{R:.1f}" fill="var(--ink)" stroke="{col}" stroke-width="{4 * k:.1f}"/>'
                      f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{R * .55:.1f}" fill="{col}" opacity="0">{_sm_on(times[i])}</circle>')
            ic = names[(i if li == 0 else na + i) % len(names)]
            if li == 0:
                lw = min(sa - 12 * k, 230 * k)
                below = i < ha and (ha - i) % 2 == 1   # the stops after the shared one keep above: its card is below
                ly = py + R + 12 * k if below else py - R - 12 * k - 64 * k
                lx = max(x, min(x + w - lw, px - lw / 2))
            else:
                lw = min(x + w - px - R - 20 * k, 330 * k)
                lx, ly = px + R + 14 * k, py - 32 * k
            ca, cl = _ix_tag(lx, ly, lw, 64 * k, s, "", k, times[i], lead=36 * k)
            st.append(ca + icon(ic, lx + 26 * k, ly + 32 * k, 26 * k, col))
            labs.append(cl)
    art.append(seq(st, .2, .45, 8))
    text.append(seq(labs, .2, .45, 8))
    # the shared station
    hr = 24 * k
    art.append(land(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="{hr:.1f}" fill="var(--ink)" stroke="var(--white)" stroke-width="{5 * k:.1f}"/>'
                    + f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="{hr * .6:.1f}" fill="var(--white)" opacity="0">{_sm_on(hub_at)}</circle>'
                    + _sm_ping(hx, hy, hr, hr * 2.4, hub_at, "var(--white)"), .2, .45, 0))
    hw = min(bold_width(_(str(hub)), 18 * k, current_factor()) + 30 * k, w * .45)
    hlx = min(x + w - hw, hx + hr + 10 * k)
    text.append(land(card(hlx, hy + hr + 6 * k, hw, 38 * k, "var(--card)", "var(--white)", 10, 1.6)
                     + _sm_text(hlx + hw / 2, hy + hr + 25 * k, hub, 18 * k, hw - 16 * k, anchor="middle", lines_max=1), .2, .45, 0))
    # the legend: the two routes' names
    lg = ""
    for li, l in enumerate(lines):
        ly = y + 14 * k + li * 34 * k
        lg += (f'<path d="M{x:.1f} {ly:.1f} h{36 * k:.1f}" stroke="{cols[li]}" stroke-width="{8 * k:.1f}" stroke-linecap="round"/>'
               + _sm_text(x + 50 * k, ly, l.get("name", ""), 17 * k, w * .7, lines_max=1))
    text.append(land(lg, .1, .45, 0))
    ga, gl = _ix_goal(x + w / 2, y + h - 26 * k, sl.get("note", ""), hub_at + .02, k, w - 20)
    art.append(land(ga, .4, .45, 8))
    text.append(land(gl, .4, .45, 8))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE
