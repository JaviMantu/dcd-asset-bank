"""Catalog scenes for the intents of 0.6.0 (1/2): journey, roadmap, before-after and matrix, two compositions each.

Vertical-neutral and portrait-aware from birth, after simple_s01_08.py: each scene draws inside ART_ZONE(layout) on
CANVAS() and returns portrait_mark(svg); the mobile build stacks the same story with labels 1.3x larger. Icons come from
the slide's `vertical` (icons.py; «generico» when missing), in catalog order unless args.icons names them. Labels sit on
opaque cards and are painted after the art; every entrance ends by 2 s; the 12 s loop resolves before 10.8 s. No figure
moves and no number is invented: a period («Semana 1») is a label, never a KPI value.

- ix01_journey_path · journey-path: their customer walks a path of stations; one stop holds a question until it clears.
- ix02_journey_loop · journey-loop: touchpoints on a ring around the customer; a spark closes the loop, each lights.
- ix03_roadmap_phases · roadmap-phases: phases on a time axis with their deliverables; a progress bar fills each one.
- ix04_roadmap_road · roadmap-road: a winding road climbs past milestone flags to the goal at the top.
- ix05_before_split · before-after-split: «Antes» and «Después» panels; a sweep line turns the old steps into the new.
- ix06_before_lanes · before-after-lanes: the same stations in two lanes; the old token goes back, the new one arrives.
- ix07_matrix_quadrants · matrix-quadrants: ideas drop into a 2x2 of impact and effort; the first quadrant lights.
- ix08_matrix_table · matrix-table: options against criteria, qualitative marks fill cell by cell, one row is chosen.
"""

_IX_END = .97


# ---------------------------------------------------------------- shared pieces (the _ix prefix: used by intents_s09_16.py too)
def _ix_curve(a, b, vert=False):
    """A smooth cubic from a to b, with horizontal (or vertical) tangents."""
    (x0, y0), (x1, y1) = a, b
    if vert:
        m = (y1 - y0) / 2
        return f"M{x0:.1f} {y0:.1f} C{x0:.1f} {y0 + m:.1f} {x1:.1f} {y1 - m:.1f} {x1:.1f} {y1:.1f}"
    m = (x1 - x0) / 2
    return f"M{x0:.1f} {y0:.1f} C{x0 + m:.1f} {y0:.1f} {x1 - m:.1f} {y1:.1f} {x1:.1f} {y1:.1f}"


def _ix_goal(cx, cy, text, at, k, room, mark="generico/check"):
    """(art, label): the promise pill, lit from at."""
    gh = 46 * k
    gw = min(room, bold_width(_(str(text)), 20 * k, current_factor()) + 90 * k)
    gx, gy = cx - gw / 2, cy - gh / 2
    art = (card(gx, gy, gw, gh, "var(--card)", "var(--c4)", gh / 2, 1.6)
           + f'<g opacity="0">{_sm_on(at)}' + card(gx, gy, gw, gh, "color-mix(in srgb, var(--c4) 18%, var(--card))", "var(--c4)", gh / 2, 2.4) + '</g>'
           + icon(mark, gx + gh * .62, cy, gh * .5, "var(--c4)") + _sm_ping(cx, cy, gh / 2, gh * 1.6, at))
    return art, _sm_text(gx + gh * 1.1, cy, text, 20 * k, gw - gh * 1.3, lines_max=1)


def _ix_who(x, y, w, text, k, mark="generico/equipo"):
    """(art, label): a pill with the person or team the slide is about, at the top of the zone."""
    ph = 44 * k
    return (card(x, y, w, ph, "var(--card)", "var(--line)", ph / 2, 1.2) + icon(mark, x + ph * .6, y + ph / 2, ph * .56, "var(--c4)"),
            _sm_text(x + ph * 1.1, y + ph / 2, text, 19 * k, w - ph * 1.4, lines_max=1))


def _ix_tag(x, y, w, h, name, note, k, lit=None, col="var(--c4)", fill="var(--card)", lead=0):
    """(art, label): an opaque card with a name and a muted note; lit (a time) draws its lit border from then."""
    art = card(x, y, w, h, fill, "var(--line)", 12, 1.2)
    if lit is not None:
        art += f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="12" fill="none" stroke="{col}" stroke-width="2" opacity="0">{_sm_on(lit)}</rect>'
    pad = 12 * k
    x, w = x + lead, w - lead
    if note:
        lab = (_sm_text(x + pad, y + h * .32, name, 19 * k, w - 2 * pad, lines_max=1)
               + _sm_text(x + pad, y + h * .7, note, 16 * k, w - 2 * pad, "var(--muted)", lines_max=1, extra=""))
    else:
        lab = _sm_text(x + pad, y + h / 2, name, 19 * k, w - 2 * pad, lines_max=2)
    return art, lab


# ---------------------------------------------------------------- 1 · journey: a path with stations
@register("scene", "ix01_journey_path")
@register("scene", "journey-path")
def sc_ix01_journey_path(sl, ctx):
    """Their customer's path, station by station (a wave on desktop, a zigzag down the phone). Loop: a traveler walks
    it, each station lights; at the friction stop a «?» holds the walk until it turns into a check; the promise lights
    at the end. Frozen: every station lit, the friction cleared, the promise on."""
    x, y, w, h, P, k = _sm_zone(sl)
    ok = ctx.brand.c("dark.ok")
    steps = [list(s) + [""] for s in (sl.get("steps") or [])][:5]
    n = max(1, len(steps))
    names = _sm_icons(sl, n)
    fr = int(sl.get("friction", -1))
    times, t = [], .06
    for i in range(n):
        times.append(t)
        t += .12 + (.1 if i == fr else 0)
    goal_at = times[-1] + .08
    art, text = [glow(x + w / 2, y + h / 2, w * .5, "var(--brand)", .3)], []
    a, b = _ix_who(x, y, w, sl.get("who", ""), k)
    art.append(land(a, .1, .45, 10))
    text.append(land(b, .1, .45, 10))
    top, bot = y + 64 * k, y + h - 70 * k
    R = 34 * k if P else 36
    if P:   # a zigzag down the left, the cards to the right
        rh = (bot - top) / n
        pts = [(x + 70 * k + (i % 2) * 70 * k, top + rh * (i + .5)) for i in range(n)]
    else:   # a wave across
        cw = w / n
        mid, amp = (top + bot) / 2, (bot - top) * .2
        pts = [(x + cw * (i + .5), mid + (-amp if i % 2 == 0 else amp)) for i in range(n)]
    road = "".join(_ix_curve(pts[i], pts[i + 1], P) for i in range(n - 1))
    art.append(land(f'<path d="{road}" fill="none" stroke="var(--line)" stroke-width="{12 * k:.1f}" stroke-linecap="round"/>'
                    f'<path d="{road}" fill="none" stroke="var(--c2)" stroke-width="2" stroke-dasharray="3 8" opacity=".7"/>', .15, .5, 0))
    cards, labs = [], []
    for i, ((px, py), (name, note, *_r)) in enumerate(zip(pts, steps)):
        if i < n - 1:
            seg = _ix_curve(pts[i], pts[i + 1], P)
            start = times[i] + (.1 if i == fr else 0) + .01
            art.append(f'<path d="{seg}" fill="none" stroke="var(--c4)" stroke-width="3.5" stroke-linecap="round" opacity="0">{_sm_on(times[i + 1])}</path>')
            art.append(_sm_ride(seg, start, times[i + 1], 8 * k, "var(--c4)"))
        art.append(land(_sm_badge(names[i], px, py, R), .2 + i * .06, .45, 10) + _sm_lit_badge(names[i], px, py, R, times[i]))
        if i == fr:
            clear = times[i] + .1
            art.append(f'<g>{_sm_off(clear)}' + _sm_q(px + R * .8, py - R * .8, 13 * k, times[i], k) + '</g>'
                       + _sm_ok(px + R * .8, py - R * .8, 13 * k, clear, ok))
        if P:
            cx0 = x + 230 * k
            ca, cl = _ix_tag(cx0, py - rh * .4, x + w - cx0, rh * .8, name, note, k, times[i])
        else:
            cwid = min(2 * cw - 40, 214)
            ch = 70
            cy0 = py - R - 14 - ch if i % 2 == 0 else py + R + 14
            ca, cl = _ix_tag(max(x, min(x + w - cwid, px - cwid / 2)), cy0, cwid, ch, name, note, k, times[i])
        cards.append(ca)
        labs.append(cl)
    art.append(seq(cards, .25, .45, 10))
    text.append(seq(labs, .25, .45, 10))
    if fr >= 0 and sl.get("friction_label"):
        fx, fy = pts[fr]
        at, clear = times[fr], times[fr] + .1
        lab = sl["friction_label"]
        if P:
            px_, py_ = x + w - 10 * k, fy + (rh * .4 if fr < n - 1 else -rh * .4)
            pl = _sm_text(px_ - 10 * k, py_, lab, 17 * k, w * .6, "var(--c4)", "end", 1)
        else:
            py_ = fy + (R + 104 if fr % 2 == 0 else -R - 104)
            pl = _sm_text(fx, py_, lab, 17, min(2 * cw, 300), "var(--c4)", "middle", 1)
        text.append(f'<g opacity="0">{beat("opacity", [(0, 0), (at - .06, 0), (at - .04, 1), (clear, 1), (clear + .02, 0), (1, 0)])}{pl}</g>')
    ga, gl = _ix_goal(x + w / 2, y + h - 26 * k, sl.get("goal", ""), goal_at, k, w - 20)
    art.append(land(ga, .4, .45, 8))
    text.append(land(gl, .4, .45, 8))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 2 · journey: a loop of touchpoints
@register("scene", "ix02_journey_loop")
@register("scene", "journey-loop")
def sc_ix02_journey_loop(sl, ctx):
    """Touchpoints on a ring around their customer. Loop: a spark travels the ring once, the thread draws behind it and
    each touchpoint lights as it passes; closing the ring, the center gets its check and the loop's lesson lights.
    Frozen: the ring closed, every touchpoint lit."""
    x, y, w, h, P, k = _sm_zone(sl)
    ok = ctx.brand.c("dark.ok")
    tps = list(sl.get("touchpoints") or [])[:6]
    n = max(1, len(tps))
    names = _sm_icons(sl, n)
    bot = 64 * k
    cx, cy = x + w / 2, y + (h - bot) / 2
    Rr = min(w * .34, (h - bot) * .36)
    R = 32 * k if P else 34
    t0, t1 = .06, .7
    times = [t0 + (t1 - t0) * i / n for i in range(n)]
    close = t1 + .02
    ang = [-90 + 360 * i / n for i in range(n)]
    pts = [(cx + Rr * math.cos(math.radians(a)), cy + Rr * math.sin(math.radians(a))) for a in ang]
    art, text = [glow(cx, cy, Rr * 1.1, "var(--brand)", .4)], []
    ring = f"M{cx:.1f} {cy - Rr:.1f} A{Rr:.1f} {Rr:.1f} 0 1 1 {cx - .1:.1f} {cy - Rr:.1f}"
    art.append(land(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{Rr:.1f}" fill="none" stroke="var(--line)" stroke-width="{10 * k:.1f}"/>'
                    f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{Rr:.1f}" fill="none" stroke="var(--c2)" stroke-width="2" stroke-dasharray="3 8" opacity=".7"/>', .1, .5, 0))
    # the thread that follows the spark, then the spark
    art.append(f'<path d="{ring}" pathLength="1" fill="none" stroke="var(--c4)" stroke-width="3.5" stroke-linecap="round" stroke-dasharray="1" stroke-dashoffset="1">'
               f'{beat("stroke-dashoffset", [(0, 1), (t0, 1), (t1, 0), (_IX_END, 0), (1, 1)])}</path>')
    art.append(_sm_ride(ring, t0, t1, 8 * k))
    # the customer at the center
    cr = Rr * .42
    art.append(land(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{cr:.1f}" fill="var(--card)" stroke="var(--c2)" stroke-width="1.6"/>'
                    + _sm_bust(cx, cy - cr * .3, cr / 30, SKIN_BROWN, "var(--c1)")
                    + f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{cr:.1f}" fill="none" stroke="{ok}" stroke-width="2.4" opacity="0">{_sm_on(close)}</circle>'
                    + _sm_ok(cx + cr * .72, cy - cr * .72, 12 * k, close, ok) + _sm_ping(cx, cy, cr, cr * 1.5, close, ok), .15, .5, 0))
    cw_c = cr * 1.9
    text.append(land(card(cx - cw_c / 2, cy + cr * .28, cw_c, 34 * k, "var(--card)", "var(--line)", 10, 1)
                     + _sm_text(cx, cy + cr * .28 + 17 * k, sl.get("center", ""), 18 * k, cw_c - 12, anchor="middle", lines_max=1), .15, .5, 0))
    # the touchpoints: a badge on the ring, a label card outside it
    badges, labs = [], []
    lw = min(200 * k, w * .3)
    for i, ((px, py), a) in enumerate(zip(pts, ang)):
        badges.append(_sm_badge(names[i], px, py, R) + _sm_lit_badge(names[i], px, py, R, times[i]))
        ux, uy = math.cos(math.radians(a)), math.sin(math.radians(a))
        lh = 36 * k
        lx = px + ux * (R + 10) + (0 if abs(ux) < .3 else (lw / 2 if ux > 0 else -lw / 2)) - lw / 2
        ly = py + uy * (R + 10 + lh / 2) - lh / 2 if abs(ux) < .3 else py + (R * .9 if uy >= -.2 else -R * .9 - lh)
        lx = max(x, min(x + w - lw, lx))
        ca, cl = _ix_tag(lx, ly, lw, lh, tps[i], "", k, times[i])
        labs.append(land(ca + cl, .25 + i * .05, .45, 8))
    art.append(seq(badges, .2, .45, 8))
    text.extend(labs)
    ga, gl = _ix_goal(x + w / 2, y + h - 26 * k, sl.get("loop", ""), close + .04, k, w - 20, "uso/sincronizar")
    art.append(land(ga, .4, .45, 8))
    text.append(land(gl, .4, .45, 8))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 3 · roadmap: phases on a time axis
@register("scene", "ix03_roadmap_phases")
@register("scene", "roadmap-phases")
def sc_ix03_roadmap_phases(sl, ctx):
    """Phases on a time axis (columns on desktop, bands down the phone), each with its period and two deliverables;
    between phases, a decision gate. Loop: the progress bar fills the axis, each phase lights and its deliverables get
    their check, each gate opens; the goal lights at the end. Frozen: every phase done, the goal on."""
    x, y, w, h, P, k = _sm_zone(sl)
    ok = ctx.brand.c("dark.ok")
    phases = list(sl.get("phases") or [])[:4]
    n = max(1, len(phases))
    names = _sm_icons(sl, n)
    step = .72 / n
    starts = [.06 + step * i for i in range(n)]
    ends = [s + step * .85 for s in starts]
    goal_at = ends[-1] + .04
    art, text = [glow(x + w / 2, y + h * .45, w * .5, "var(--brand)", .3)], []
    gap = 14 * k
    bot = y + h - 70 * k
    if P:   # the axis down the left, a band per phase
        ax = x + 26 * k
        top = y + 10 * k
        bh = (bot - top - (n - 1) * gap) / n
        boxes = [(x + 70 * k, top + i * (bh + gap), w - 70 * k, bh) for i in range(n)]
        axis = f"M{ax:.1f} {top:.1f} V{bot:.1f}"
        prog = lambda f: f"M{ax:.1f} {top:.1f} V{top + (bot - top) * f:.1f}"
    else:   # the axis across the top, a column per phase
        ay = y + 16
        top = ay + 30
        bw = (w - (n - 1) * gap) / n
        mi = max([len(list(p.get("items") or [])[:3]) for p in phases] + [1])
        bh_d = min(bot - top - 34, 94 + mi * 92)   # as tall as its deliverables
        boxes = [(x + i * (bw + gap), top + 34, bw, bh_d) for i in range(n)]
        axis = f"M{x:.1f} {ay:.1f} H{x + w:.1f}"
    art.append(land(f'<path d="{axis}" stroke="var(--line)" stroke-width="{8 * k:.1f}" stroke-linecap="round"/>', .1, .45, 0))
    L = (bot - top) if P else w
    art.append(f'<path d="{axis}" pathLength="1" stroke="var(--c4)" stroke-width="{4 * k:.1f}" stroke-linecap="round" stroke-dasharray="1" stroke-dashoffset="1">'
               f'{beat("stroke-dashoffset", [(0, 1), (starts[0], 1), (ends[-1], 0), (_IX_END, 0), (1, 1)])}</path>')
    cards, labs = [], []
    for i, ph in enumerate(phases):
        bx, by, bw_, bh_ = boxes[i]
        items = list(ph.get("items") or [])[:3]
        r = 22 * k
        c = (card(bx, by, bw_, bh_, "var(--card)", "var(--line)", 14, 1.2)
             + f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bw_:.1f}" height="{bh_:.1f}" rx="14" fill="color-mix(in srgb, var(--c4) 8%, transparent)" stroke="var(--c4)" stroke-width="2" opacity="0">{_sm_on(starts[i])}</rect>'
             + _sm_badge(names[i], bx + 14 * k + r, by + 14 * k + r, r) + _sm_lit_badge(names[i], bx + 14 * k + r, by + 14 * k + r, r, starts[i]))
        l = (_sm_text(bx + 24 * k + 2 * r, by + 14 * k + r * .6, ph.get("name", ""), 20 * k, bw_ - 36 * k - 2 * r, lines_max=1)
             + _sm_text(bx + 24 * k + 2 * r, by + 14 * k + r * 1.5, ph.get("when", ""), 16 * k, bw_ - 36 * k - 2 * r, "var(--c4)", lines_max=1))
        # the deliverables: rows under the head, each checked in turn
        hy = by + 28 * k + 2 * r
        if P:
            ih = min(44 * k, (bh_ - (hy - by) - 10 * k) / max(1, len(items)))
            iw = bw_ - 28 * k
        else:
            ih = min(96, (bh_ - (hy - by) - 12) / max(2, len(items)))
            iw = bw_ - 24
        for j, it in enumerate(items):
            iy = hy + j * ih
            at = starts[i] + step * .25 * (j + 1)
            c += (f'<rect x="{bx + 12 * k:.1f}" y="{iy:.1f}" width="{iw:.1f}" height="{ih - 8 * k:.1f}" rx="8" fill="var(--ink)" opacity=".35"/>'
                  + f'<circle cx="{bx + 12 * k + 16 * k:.1f}" cy="{iy + (ih - 8 * k) / 2:.1f}" r="{8 * k:.1f}" fill="none" stroke="var(--c2)" stroke-width="1.6"/>'
                  + _sm_ok(bx + 12 * k + 16 * k, iy + (ih - 8 * k) / 2, 9 * k, at, ok))
            l += _sm_text(bx + 12 * k + 32 * k, iy + (ih - 8 * k) / 2, it, 17 * k, iw - 42 * k, lines_max=2 if not P else 1, extra="")
        # the period tick on the axis
        if P:
            tick = f'<circle cx="{ax:.1f}" cy="{by + 14 * k + r:.1f}" r="{7 * k:.1f}" fill="var(--card)" stroke="var(--c2)" stroke-width="2"/>'
            lit = f'<circle cx="{ax:.1f}" cy="{by + 14 * k + r:.1f}" r="{7 * k:.1f}" fill="var(--c4)" opacity="0">{_sm_on(starts[i])}</circle>'
        else:
            tick = f'<circle cx="{bx + 20:.1f}" cy="{ay:.1f}" r="7" fill="var(--card)" stroke="var(--c2)" stroke-width="2"/>'
            lit = f'<circle cx="{bx + 20:.1f}" cy="{ay:.1f}" r="7" fill="var(--c4)" opacity="0">{_sm_on(starts[i])}</circle>'
        cards.append(c + tick + lit)
        labs.append(l)
        # the decision gate between this phase and the next
        if i < n - 1:
            gx, gy = (ax, by + bh_ + gap / 2) if P else (bx + bw_ + gap / 2, top + 16)
            s = 9 * k
            dia = f"M{gx:.1f} {gy - s:.1f} L{gx + s:.1f} {gy:.1f} L{gx:.1f} {gy + s:.1f} L{gx - s:.1f} {gy:.1f} Z"
            art.append(f'<path d="{dia}" fill="var(--card)" stroke="var(--c2)" stroke-width="1.8"/>'
                       f'<path d="{dia}" fill="{ok}" opacity="0">{_sm_on(ends[i])}</path>')
    art.append(seq(cards, .15, .5, 12))
    text.append(seq(labs, .15, .5, 12))
    if sl.get("decide"):
        if P:
            dl = _sm_text(x + w, y + h - 70 * k + 10 * k, "◆ " + str(sl["decide"]), 16 * k, w * .5, "var(--muted)", "end", 1, extra="")
        else:
            dl = _sm_text(x + w, y + 16 - 24, "◆ " + str(sl["decide"]), 15, w * .5, "var(--muted)", "end", 1, extra="")
        text.append(land(dl, .3, .45, 0))
    ga, gl = _ix_goal(x + w / 2, y + h - 26 * k, sl.get("goal", ""), goal_at, k, w - 20, "generico/meta")
    art.append(land(ga, .4, .45, 8))
    text.append(land(gl, .4, .45, 8))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 4 · roadmap: a winding road to the goal
@register("scene", "ix04_roadmap_road")
@register("scene", "roadmap-road")
def sc_ix04_roadmap_road(sl, ctx):
    """A road winds up the left from «Hoy» to the goal at the top, a milestone flag at each bend, its card to the right. Loop: a vehicle
    climbs, each flag rises and lights as it passes, the goal flag lights at the top. Frozen: the road traveled, every
    milestone lit."""
    x, y, w, h, P, k = _sm_zone(sl)
    ms = [list(m) + [""] for m in (sl.get("milestones") or [])][:5]
    n = max(1, len(ms))
    names = _sm_icons(sl, n)
    art, text = [glow(x + w / 2, y + h * .2, w * .45, "var(--c4)", .15)], []
    # the road: from bottom center to top center, swinging left and right between milestones
    top, bot = y + 110 * k, y + h - 40 * k
    swing = w * .09
    rx = x + w * .17       # the road on the left, the cards to its right
    pts = [(rx, bot)]
    for i in range(n):
        pts.append((rx + (swing if i % 2 == 0 else -swing), bot - (bot - top) * (i + 1) / (n + 1)))
    pts.append((rx, top))
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}" + "".join(" C" + _ix_curve(pts[i], pts[i + 1], True).split(" C", 1)[1] for i in range(len(pts) - 1))
    wide = 30 * k
    art.append(land(f'<path d="{d}" fill="none" stroke="color-mix(in srgb, var(--c1) 22%, var(--ink))" stroke-width="{wide:.1f}" stroke-linecap="round"/>'
                    f'<path d="{d}" fill="none" stroke="var(--c2)" stroke-width="2" stroke-dasharray="10 12" opacity=".6"/>', .1, .55, 0))
    t0, t1 = .06, .74
    art.append(f'<path d="{d}" pathLength="1" fill="none" stroke="var(--c4)" stroke-width="4" stroke-linecap="round" stroke-dasharray="1" stroke-dashoffset="1">'
               f'{beat("stroke-dashoffset", [(0, 1), (t0, 1), (t1, 0), (_IX_END, 0), (1, 1)])}</path>')
    # the vehicle rides the whole road (paths share an even pace: the flags light at their share of it)
    art.append(_sm_ride(d, t0, t1, 10 * k))
    times = [t0 + (t1 - t0) * (i + 1) / (n + 1) for i in range(n)]
    flags, labs = [], []
    for i, ((px, py), (when, what, *_r)) in enumerate(zip(pts[1:-1], ms)):
        side = -1
        fx = px + side * (wide * .5 + 8 * k)
        pole = 46 * k
        fl = (f'<path d="M{fx:.1f} {py:.1f} V{py - pole:.1f}" stroke="var(--c2)" stroke-width="2.2"/>'
              f'<path d="M{fx:.1f} {py - pole:.1f} l{side * 26 * k:.1f} {8 * k:.1f} l{-side * 26 * k:.1f} {8 * k:.1f} Z" fill="var(--c2)"/>'
              f'<g opacity="0">{_sm_on(times[i])}<path d="M{fx:.1f} {py - pole:.1f} l{side * 26 * k:.1f} {8 * k:.1f} l{-side * 26 * k:.1f} {8 * k:.1f} Z" fill="var(--c4)"/></g>'
              + _sm_ping(fx, py - pole + 8 * k, 6, 30 * k, times[i]))
        ch = 64 * k
        r = 18 * k
        cx0 = rx + swing + wide / 2 + 24 * k
        cw = min(x + w - cx0, 460 * k)
        cy0 = py - ch / 2
        ca, cl = _ix_tag(cx0, cy0, cw, ch, what, when, k, times[i], lead=2 * r + 8 * k)
        ca += _sm_badge(names[i], cx0 + 10 * k + r, cy0 + ch / 2, r) + _sm_lit_badge(names[i], cx0 + 10 * k + r, cy0 + ch / 2, r, times[i])
        flags.append(fl + ca)
        labs.append(cl)
    art.append(seq(flags, .2, .45, 10))
    text.append(seq(labs, .2, .45, 10))
    # start and goal
    art.append(land(f'<circle cx="{pts[0][0]:.1f}" cy="{pts[0][1]:.1f}" r="{10 * k:.1f}" fill="var(--c2)"/>', .1, .4, 0))
    text.append(land(_sm_text(pts[0][0] + 24 * k, pts[0][1], sl.get("start", ""), 18 * k, w * .4, "var(--c2)", lines_max=1), .1, .4, 0))
    ga, gl = _ix_goal(x + w / 2, y + 30 * k, sl.get("goal", ""), t1 + .02, k, w - 20, "generico/meta")
    art.append(land(ga, .35, .45, -8))
    text.append(land(gl, .35, .45, -8))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 5 · before-after: two panels and a sweep
@register("scene", "ix05_before_split")
@register("scene", "before-after-split")
def sc_ix05_before_split(sl, ctx):
    """Two panels, «Antes» and «Después» (side by side on desktop, stacked on the phone). The old steps are there, each
    with its clock; the new panel waits, dashed. Loop: a sweep line crosses from the old panel to the new, the old steps
    dim one by one and the new ones light with their check. Frozen: the old panel dim, the new one lit."""
    x, y, w, h, P, k = _sm_zone(sl)
    ok = ctx.brand.c("dark.ok")
    before = list(sl.get("before") or [])[:4]
    after = list(sl.get("after") or [])[:4]
    names = _sm_icons(sl, max(len(before), len(after), 1))
    gap = 26 * k
    if P:
        pw, ph = w, (h - gap) / 2
        panes = [(x, y, pw, ph), (x, y + ph + gap, pw, ph)]
    else:
        m_ = max(len(before), len(after), 1)
        pw, ph = (w - gap) / 2, min(h, 70 + m_ * 120 + 16)
        y0 = y + (h - ph) / 2
        panes = [(x, y0, pw, ph), (x + pw + gap, y0, pw, ph)]
    dims = [.12 + .08 * i for i in range(len(before))]
    lits = [.44 + .1 * i for i in range(len(after))]
    art, text = [], []
    heads = [(sl.get("before_label", "Antes"), sl.get("before_note", ""), "var(--muted)"), (sl.get("after_label", "Después"), sl.get("after_note", ""), "var(--c4)")]
    for side, ((px, py, pw_, ph_), (lab, note, col), items) in enumerate(zip(panes, heads, (before, after))):
        dash = 'stroke-dasharray="6 6"' if side else ""
        pane = card(px, py, pw_, ph_, "var(--card)" if side else "color-mix(in srgb, var(--card) 70%, var(--ink))", "var(--line)", 16, 1.4, dash)
        if side:
            pane += f'<rect x="{px:.1f}" y="{py:.1f}" width="{pw_:.1f}" height="{ph_:.1f}" rx="16" fill="none" stroke="var(--c4)" stroke-width="2.2" opacity="0">{_sm_on(lits[0] if lits else .5)}</rect>'
        hh = 70 * k
        lab_t = (_sm_text(px + 18 * k, py + hh * .38, lab, 22 * k, pw_ - 36 * k, col, lines_max=1)
                 + _sm_text(px + 18 * k, py + hh * .8, note, 16 * k, pw_ - 36 * k, "var(--muted)", lines_max=1, extra=""))
        m = len(items) or 1
        ih = min((ph_ - hh - 16 * k) / m, 92 * k if P else 120)
        rows, rl = [], []
        for j, it in enumerate(items):
            iy = py + hh + j * ih
            r = min(20 * k, ih * .28)
            icx, icy = px + 18 * k + r, iy + ih / 2
            if side == 0:
                row = (card(px + 10 * k, iy + 4, pw_ - 20 * k, ih - 8, "var(--ink)", "var(--line)", 10, 1)
                       + _sm_badge(names[j % len(names)], icx + 4, icy, r, "var(--muted)")
                       + icon("generico/reloj", px + pw_ - 30 * k, icy, 22 * k, "var(--c5)")
                       + f'<rect x="{px + 10 * k:.1f}" y="{iy + 4:.1f}" width="{pw_ - 20 * k:.1f}" height="{ih - 8:.1f}" rx="10" fill="var(--ink)" opacity="0">'
                       f'{beat("opacity", [(0, 0), (dims[j], 0), (dims[j] + .03, .55), (_IX_END, .55), (1, 0)])}</rect>')
                rl.append(_sm_text(icx + r + 14 * k, icy, it, 18 * k, pw_ - 2 * r - 90 * k, "var(--muted)", lines_max=2, extra=""))
            else:
                row = (card(px + 10 * k, iy + 4, pw_ - 20 * k, ih - 8, "var(--ink)", "var(--c2)", 10, 1, 'stroke-dasharray="4 5"')
                       + f'<g opacity="0">{_sm_on(lits[j])}' + card(px + 10 * k, iy + 4, pw_ - 20 * k, ih - 8, "color-mix(in srgb, var(--c4) 12%, var(--card))", "var(--c4)", 10, 1.6) + '</g>'
                       + _sm_badge(names[j % len(names)], icx + 4, icy, r) + _sm_lit_badge(names[j % len(names)], icx + 4, icy, r, lits[j])
                       + _sm_ok(px + pw_ - 30 * k, icy, 11 * k, lits[j] + .02, ok))
                rl.append(_sm_text(icx + r + 14 * k, icy, it, 18 * k, pw_ - 2 * r - 90 * k, lines_max=2))
            rows.append(row)
        art.append(land(pane, .1 + side * .12, .5, 12) + seq(rows, .2 + side * .12, .45, 10))
        text.append(land(lab_t, .1 + side * .12, .5, 12) + seq(rl, .2 + side * .12, .45, 10))
    # the sweep: from the old panel's edge through the new one
    if P:
        sx0, sx1 = x, x + w
        yy0, yy1 = y, y + h
        line = (f'<g opacity="0">{beat("opacity", [(0, 0), (.1, 0), (.12, 1), (.82, 1), (.86, 0), (1, 0)])}'
                f'<path d="M{sx0:.1f} {yy0:.1f} H{sx1:.1f}" stroke="var(--c4)" stroke-width="3"/>'
                f'<animateTransform attributeName="transform" type="translate" values="0 0;0 0;0 {h:.1f};0 {h:.1f}" keyTimes="0;.1;.84;1" dur="{D}s" repeatCount="indefinite"/></g>')
    else:
        line = (f'<g opacity="0">{beat("opacity", [(0, 0), (.1, 0), (.12, 1), (.82, 1), (.86, 0), (1, 0)])}'
                f'<path d="M{x:.1f} {y0:.1f} V{y0 + ph:.1f}" stroke="var(--c4)" stroke-width="3"/>'
                f'<animateTransform attributeName="transform" type="translate" values="0 0;0 0;{w:.1f} 0;{w:.1f} 0" keyTimes="0;.1;.84;1" dur="{D}s" repeatCount="indefinite"/></g>')
    # the arrow between panels
    if P:
        ax_, ay_ = x + w / 2, y + h / 2
        arr = f'<circle cx="{ax_:.1f}" cy="{ay_:.1f}" r="{20 * k:.1f}" fill="var(--c4)"/><g transform="rotate(90 {ax_:.1f} {ay_:.1f})">' + icon("uso/flecha-der", ax_, ay_, 24 * k, ctx.brand.on("var(--c4)")) + '</g>'
    else:
        ax_, ay_ = x + pw + gap / 2, y + h / 2
        arr = f'<circle cx="{ax_:.1f}" cy="{ay_:.1f}" r="20" fill="var(--c4)"/>' + icon("uso/flecha-der", ax_, ay_, 24, ctx.brand.on("var(--c4)"))
    art.append(line)
    text.append(land(arr, .35, .45, 0))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 6 · before-after: two lanes, one goes back
@register("scene", "ix06_before_lanes")
@register("scene", "before-after-lanes")
def sc_ix06_before_lanes(sl, ctx):
    """The same stations in two lanes (rows on desktop, columns on the phone): today's and the one with the change.
    Loop: today's token goes back from the second station to the first (a loop marked with the detour label) and then
    goes on; the new token runs straight and reaches the end first, where the result lights. Frozen: both lanes
    traveled, the new one checked."""
    x, y, w, h, P, k = _sm_zone(sl)
    ok = ctx.brand.c("dark.ok")
    steps = list(sl.get("steps") or [])[:4]
    n = max(2, len(steps))
    names = _sm_icons(sl, n)
    labels = (sl.get("before_label", "Hoy"), sl.get("after_label", "Con el cambio"))
    gap = 22 * k
    bot = 70 * k
    if P:
        lw, lh = (w - gap) / 2, h - bot
        lanes = [(x, y, lw, lh), (x + lw + gap, y, lw, lh)]
    else:
        lw, lh = w, (h - bot - gap) / 2
        lanes = [(x, y, lw, lh), (x, y + lh + gap, lw, lh)]
    art, text = [], []
    R = 28 * k
    new_t = [.1 + .1 * i for i in range(n)]
    old_t = [.1, .24] + [.24 + .26 + .12 * (i - 1) for i in range(2, n)]
    old_t[1] = .22
    finish_new = new_t[-1] + .02
    for li, ((lx, ly, lw_, lh_), lab) in enumerate(zip(lanes, labels)):
        new = li == 1
        col = "var(--c4)" if new else "var(--muted)"
        art.append(land(card(lx, ly, lw_, lh_, "var(--card)" if new else "color-mix(in srgb, var(--card) 70%, var(--ink))", "var(--line)", 16, 1.3), .1 + li * .1, .5, 10))
        hh = 44 * k
        text.append(land(_sm_text(lx + 16 * k, ly + hh * .6, lab, 21 * k, lw_ - 32 * k, col, lines_max=1), .1 + li * .1, .5, 10))
        if P:
            pts = [(lx + lw_ / 2, ly + hh + 30 * k + (lh_ - hh - 60 * k) * (i + .3) / n) for i in range(n)]
        else:
            pts = [(lx + 40 + (lw_ - 80) * (i + .5) / n, ly + hh + (lh_ - hh) * .36) for i in range(n)]
        line = "M" + " L".join(f"{px:.1f} {py:.1f}" for px, py in pts)
        art.append(land(f'<path d="{line}" stroke="var(--line)" stroke-width="{8 * k:.1f}" stroke-linecap="round"/>', .15 + li * .1, .45, 0))
        times = new_t if new else old_t
        badges, labs = [], []
        for i, ((px, py), s) in enumerate(zip(pts, steps)):
            badges.append(_sm_badge(names[i], px, py, R) + _sm_lit_badge(names[i], px, py, R, times[i], "var(--c4)" if new else "var(--c2)"))
            if P:
                labs.append(card(lx + 10 * k, py + R + 6 * k, lw_ - 20 * k, 34 * k, "var(--card)", "var(--line)", 8, 1)
                            + _sm_text(px, py + R + 23 * k, s, 17 * k, lw_ - 30 * k, anchor="middle", lines_max=1))
            else:
                cwid = (lw_ - 80) / n - 10
                labs.append(card(px - cwid / 2, py + R + 10, cwid, 34, "var(--card)", "var(--line)", 8, 1)
                            + _sm_text(px, py + R + 27, s, 17, cwid - 10, anchor="middle", lines_max=1))
            if i < n - 1:
                seg = f"M{px:.1f} {py:.1f} L{pts[i + 1][0]:.1f} {pts[i + 1][1]:.1f}"
                if new or i != 1:
                    a0 = times[i] + .01
                else:
                    a0 = .46
                art.append(f'<path d="{seg}" stroke="{"var(--c4)" if new else "var(--c2)"}" stroke-width="3.5" stroke-linecap="round" opacity="0">{_sm_on(times[i + 1])}</path>')
                art.append(_sm_ride(seg, a0, times[i + 1], 7 * k, "var(--c4)" if new else "var(--c2)"))
        art.append(seq(badges, .2 + li * .1, .45, 8))
        text.append(seq(labs, .2 + li * .1, .45, 8))
        if not new:
            # the detour: from the second station back to the first, then again forward
            (ax_, ay_), (bx_, by_) = pts[0], pts[1]
            if P:
                off = lw_ * .32
                back = f"M{bx_:.1f} {by_:.1f} C{bx_ + off:.1f} {by_:.1f} {ax_ + off:.1f} {ay_:.1f} {ax_:.1f} {ay_:.1f}"
                tx, ty, anc = ax_ + off * .8, (ay_ + by_) / 2, "middle"
            else:
                off = lh_ * .22
                back = f"M{bx_:.1f} {by_:.1f} C{bx_:.1f} {by_ - off - 30:.1f} {ax_:.1f} {ay_ - off - 30:.1f} {ax_:.1f} {ay_:.1f}"
                tx, ty, anc = (ax_ + bx_) / 2, ay_ - off - 20, "middle"
            art.append(land(f'<path d="{back}" fill="none" stroke="var(--c5)" stroke-width="2.4" stroke-dasharray="6 6" opacity=".85"/>', .3, .45, 0))
            art.append(_sm_ride(back, .23, .3, 7 * k, "var(--c5)"))
            fw = pts[1]
            art.append(_sm_ride(f"M{ax_:.1f} {ay_:.1f} L{fw[0]:.1f} {fw[1]:.1f}", .31, .45, 7 * k, "var(--c2)"))
            dl = sl.get("detour", "")
            dw = min(bold_width(_(str(dl)), 17 * k, current_factor()) + 30 * k, lw_ * .9 if not P else lw_ - 16 * k)
            if P:
                tx = lx + lw_ / 2
                ty = ay_ + R + 40 * k + (by_ - ay_ - 2 * R - 40 * k) / 2
            text.append(land(card(tx - dw / 2, ty - 17 * k, dw, 34 * k, "var(--card)", "var(--c5)", 17 * k, 1.4)
                             + _sm_text(tx, ty, dl, 17 * k, dw - 16 * k, "var(--white)", "middle", 1), .3, .45, 0))
        else:
            ex, ey = pts[-1]
            art.append(_sm_ok(ex + R * .8, ey - R * .8, 12 * k, finish_new, ok))
    ga, gl = _ix_goal(x + w / 2, y + h - 26 * k, sl.get("result", ""), finish_new + .04, k, w - 20)
    art.append(land(ga, .4, .45, 8))
    text.append(land(gl, .4, .45, 8))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 7 · matrix: a 2x2 of impact and effort
@register("scene", "ix07_matrix_quadrants")
@register("scene", "matrix-quadrants")
def sc_ix07_matrix_quadrants(sl, ctx):
    """A 2x2: effort across, impact up; the four quadrants named. Loop: the ideas drop in one by one to their place
    (relative positions, not measures) and land with their label; then the first quadrant lights with its pick.
    Frozen: every idea placed, the first quadrant lit."""
    x, y, w, h, P, k = _sm_zone(sl)
    xa = list(sl.get("x_axis") or ["Menor esfuerzo", "Mayor esfuerzo"]) + [""]
    ya = list(sl.get("y_axis") or ["Menor impacto", "Mayor impacto"]) + [""]
    qs = list(sl.get("quadrants") or ["", "", "", ""]) + ["", "", "", ""]
    items = [list(i) + [.5, .5] for i in (sl.get("ideas") or [])][:5]
    names = _sm_icons(sl, max(1, len(items)))
    side = min(w - 40 * k, h - 110 * k)
    gx, gy = x + (w - side) / 2 + 20 * k, y + 10 * k
    half = side / 2
    drops = [.08 + .1 * i for i in range(len(items))]
    pick_at = (drops[-1] if drops else .1) + .12
    art, text = [], []
    quads = [(gx, gy), (gx + half, gy), (gx, gy + half), (gx + half, gy + half)]
    qa = ""
    for q, (qx, qy) in enumerate(quads):
        qa += card(qx + 3, qy + 3, half - 6, half - 6, "var(--card)" if q else "color-mix(in srgb, var(--c4) 6%, var(--card))", "var(--line)", 12, 1.2)
    qa += (f'<rect x="{gx + 3:.1f}" y="{gy + 3:.1f}" width="{half - 6:.1f}" height="{half - 6:.1f}" rx="12" fill="color-mix(in srgb, var(--c4) 14%, transparent)" stroke="var(--c4)" stroke-width="2.6" opacity="0">{_sm_on(pick_at)}</rect>'
           + _sm_ping(gx + half / 2, gy + half / 2, half * .3, half * .7, pick_at))
    # the axes: arrows along the left and the bottom
    ax = (f'<path d="M{gx - 14 * k:.1f} {gy + side:.1f} V{gy - 4:.1f} M{gx - 20 * k:.1f} {gy + 6 * k:.1f} L{gx - 14 * k:.1f} {gy - 4:.1f} L{gx - 8 * k:.1f} {gy + 6 * k:.1f}" fill="none" stroke="var(--c2)" stroke-width="2"/>'
          f'<path d="M{gx:.1f} {gy + side + 14 * k:.1f} H{gx + side + 4:.1f} M{gx + side - 6 * k:.1f} {gy + side + 8 * k:.1f} L{gx + side + 4:.1f} {gy + side + 14 * k:.1f} L{gx + side - 6 * k:.1f} {gy + side + 20 * k:.1f}" fill="none" stroke="var(--c2)" stroke-width="2"/>')
    art.append(land(qa + ax, .1, .5, 10))
    ql = ""
    for q, (qx, qy) in enumerate(quads):
        ql += _sm_text(qx + 16 * k, qy + 26 * k, qs[q], 18 * k, half - 32 * k, "var(--c4)" if q == 0 else "var(--muted)", lines_max=1)
    axl = (_sm_text(gx, gy + side + 42 * k, xa[0], 16 * k, half - 10, "var(--muted)", lines_max=1, extra="")
           + _sm_text(gx + side, gy + side + 42 * k, xa[1], 16 * k, half - 10, "var(--muted)", "end", 1, extra="")
           + f'<g transform="rotate(-90 {gx - 30 * k:.1f} {gy + side / 2:.1f})">'
           + _sm_text(gx - 30 * k - side / 2, gy + side / 2, ya[0], 16 * k, half - 10, "var(--muted)", lines_max=1, extra="")
           + _sm_text(gx - 30 * k + side / 2, gy + side / 2, ya[1], 16 * k, half - 10, "var(--muted)", "end", 1, extra="") + '</g>')
    text.append(land(ql + axl, .1, .5, 10))
    # the ideas drop in
    R = 20 * k
    for i, (lab, fx, fy, *_r) in enumerate(items):
        px, py = gx + side * float(fx), gy + side * (1 - float(fy))
        px, py = max(gx + R + 6, min(gx + side - R - 6, px)), max(gy + 50 * k, min(gy + side - R - 40 * k, py))
        at = drops[i]
        ride = f"M{px:.1f} {gy - 30:.1f} L{px:.1f} {py:.1f}"
        art.append(_sm_ride(ride, at - .05, at, 6 * k))
        cw = min(half - 16 * k, bold_width(_(str(lab)), 17 * k, current_factor()) + 22 * k)
        lx = px - cw / 2
        lx = max(gx + 6, min(gx + side - cw - 6, lx))
        text.append(f'<g opacity="0">{_sm_on(at)}' + _sm_badge(names[i], px, py, R, "var(--c4)", "var(--c4)")
                    + card(lx, py + R + 6 * k, cw, 32 * k, "var(--card)", "var(--line)", 8, 1)
                    + _sm_text(lx + cw / 2, py + R + 22 * k, lab, 17 * k, cw - 12 * k, anchor="middle", lines_max=1)
                    + '</g>' + _sm_ping(px, py, R, R * 2.2, at))
    if sl.get("pick"):
        text.append(f'<g opacity="0">{_sm_on(pick_at)}' + pill(gx + half / 2, gy + half - 26 * k, sl["pick"], "var(--c4)", ctx, int(17 * k), half - 20, "matrix pick") + '</g>')
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE


# ---------------------------------------------------------------- 8 · matrix: options against criteria
@register("scene", "ix08_matrix_table")
@register("scene", "matrix-table")
def sc_ix08_matrix_table(sl, ctx):
    """A table: options in rows, criteria in columns, each cell a qualitative mark (full, half, empty; never a
    number). Loop: the marks fill column by column, then the chosen row lights with its label. Frozen: the table
    full, the chosen row lit."""
    x, y, w, h, P, k = _sm_zone(sl)
    rows = list(sl.get("rows") or [])[:4]
    cols = list(sl.get("criteria") or [])[:3]
    marks = list(sl.get("marks") or [])
    pick = int(sl.get("pick", 0))
    nr, nc = max(1, len(rows)), max(1, len(cols))
    names = _sm_icons(sl, nr)
    heads = ("generico/meta", "generico/reloj", "generico/alerta", "generico/dato")
    art, text = [], []
    lw = w * (.42 if not P else .4)
    hh = 96 * k
    bot = 110 * k
    rh = min((h - hh - bot) / nr, 120 * k)
    cw = (w - lw) / nc
    fills = [[.08 + .1 * c + .025 * r for c in range(nc)] for r in range(nr)]
    pick_at = .08 + .1 * nc + .06
    # headers
    hd, hl = [], []
    for c, col in enumerate(cols):
        cx = x + lw + cw * (c + .5)
        hd.append(card(x + lw + cw * c + 4, y, cw - 8, hh - 8, "var(--card)", "var(--line)", 12, 1.2) + icon(heads[c % 4], cx, y + 26 * k, 26 * k, "var(--c2)"))
        hl.append(_sm_text(cx, y + hh * .66, col, 17 * k, cw - 16, anchor="middle", lines_max=1))
    art.append(seq(hd, .1, .45, 10))
    text.append(seq(hl, .1, .45, 10))
    # rows
    for r, lab in enumerate(rows):
        ry = y + hh + r * rh
        row = card(x, ry + 4, w, rh - 8, "var(--card)", "var(--line)", 12, 1.2)
        if r == pick:
            row += f'<rect x="{x:.1f}" y="{ry + 4:.1f}" width="{w:.1f}" height="{rh - 8:.1f}" rx="12" fill="color-mix(in srgb, var(--c4) 12%, transparent)" stroke="var(--c4)" stroke-width="2.4" opacity="0">{_sm_on(pick_at)}</rect>'
        ir = min(20 * k, rh * .25)
        row += _sm_badge(names[r], x + 14 * k + ir, ry + rh / 2, ir)
        for c in range(nc):
            lvl = int((marks[r] if r < len(marks) else [])[c] if c < len((marks[r] if r < len(marks) else [])) else 0)
            cx, cy = x + lw + cw * (c + .5), ry + rh / 2
            mr = min(15 * k, rh * .2)
            at = fills[r][c]
            row += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{mr:.1f}" fill="none" stroke="var(--c2)" stroke-width="1.8"/>'
            if lvl >= 2:
                row += f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{mr:.1f}" fill="var(--c4)" opacity="0">{_sm_on(at)}</circle>'
            elif lvl == 1:
                row += (f'<path d="M{cx:.1f} {cy - mr:.1f} A{mr:.1f} {mr:.1f} 0 0 1 {cx:.1f} {cy + mr:.1f} Z" fill="var(--c4)" opacity="0">{_sm_on(at)}</path>')
            row += _sm_ping(cx, cy, mr, mr * 2, at)
        art.append(land(row, .18 + r * .08, .45, 10))
        text.append(land(_sm_text(x + 26 * k + 2 * ir, ry + rh / 2, lab, 18 * k, lw - 36 * k - 2 * ir, lines_max=2), .18 + r * .08, .45, 10))
    # legend and the pick
    ly = y + hh + nr * rh + 22 * k
    leg = list(sl.get("legend") or ["Alto", "Medio", "Bajo"])[:3]
    lg, ll = "", ""
    lx = x + 10 * k
    for j, t in enumerate(leg):
        mr = 10 * k
        cx = lx + mr
        lg += f'<circle cx="{cx:.1f}" cy="{ly:.1f}" r="{mr:.1f}" fill="none" stroke="var(--c2)" stroke-width="1.6"/>'
        if j == 0:
            lg += f'<circle cx="{cx:.1f}" cy="{ly:.1f}" r="{mr:.1f}" fill="var(--c4)"/>'
        elif j == 1:
            lg += f'<path d="M{cx:.1f} {ly - mr:.1f} A{mr:.1f} {mr:.1f} 0 0 1 {cx:.1f} {ly + mr:.1f} Z" fill="var(--c4)"/>'
        ll += _sm_text(cx + mr + 8 * k, ly, t, 16 * k, w / 3 - 40 * k, "var(--muted)", lines_max=1, extra="")
        lx += w / 3
    art.append(land(lg, .3, .45, 6))
    text.append(land(ll, .3, .45, 6))
    ga, gl = _ix_goal(x + w / 2, y + h - 26 * k, sl.get("pick_label", ""), pick_at, k, w - 20, "uso/estrella")
    art.append(land(ga, .4, .45, 8))
    text.append(land(gl, .4, .45, 8))
    return portrait_mark("".join(art) + "".join(text)), D, FREEZE
