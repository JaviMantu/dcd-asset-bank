"""Group D, slides 10-12 of the pagos deck: federated autonomy, how we decide, how to start. Each scene lands once
inside 2 s and then tells a 12-second story in loop with beat() (explicit keyTimes). Runs in the shared namespace
(the pagos deck's module/ext.py), so it reuses the energía v4 helpers of slide 10 (_n10_face, _n10_on, _n10_ping, _N10_CLEAR):
the resolved state holds from its beat to the end of the loop, the next cycle clears it in its first half second, and
the reduced-motion frame (0.9 of the loop, 10.8 s) shows the story told."""


# ---------------------------------------------------------------- 10 · federated autonomy, inside IT governance
def _q10_head(x, y, col):
    """A member of a space, as a tiny faceless head and shoulders centered at (x, y)."""
    return (f'<circle cx="{x:.1f}" cy="{y - 5:.1f}" r="4.5" fill="{col}"/>'
            f'<path d="M{x - 7.5:.1f} {y + 7:.1f} C{x - 7.5:.1f} {y - 1:.1f} {x + 7.5:.1f} {y - 1:.1f} {x + 7.5:.1f} {y + 7:.1f} Z" fill="{col}"/>')


def _q10_doc(x, y, col="var(--c2)"):
    """A source document glyph whose text baseline is y (the label goes at x + 22)."""
    return (f'<path d="M{x} {y - 13} h8 l5 5 v12 h-13 Z M{x + 3} {y - 3} h7 M{x + 3} {y + 1} h7" fill="none" stroke="{col}" '
            f'stroke-width="1.3" stroke-linejoin="round"/>')


def _q10_tile(x, y, col, w=72, h=58, ph=0.0):
    """An agent: a rounded tile with its spark, in the color of its space; the spark breathes (the agent is live)."""
    return card(x, y, w, h, "var(--dim)", col, 14, 1.4) + f'<g>{loop("opacity", ".55;1;.55", 3, ph)}{spark(x + w / 2, y + h / 2, .7, col)}</g>'


def _q10_ring(x, y, w, h, r, spans, col="var(--c4)", sw=3):
    """A frame around (x, y, w, h) shown during each (a, b) of spans: an agent answering, a row being adjusted."""
    pts = [(0, 0)]
    for a, b in spans:
        pts += [(a, 0), (a + .01, 1), (b, 1), (b + .01, 0)]
    pts.append((1, 0))
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" fill="none" stroke="{col}" stroke-width="{sw}" opacity="0">'
            f'{beat("opacity", pts)}</rect>')


def _q10_ride(path, a, b, col="var(--c4)", r=5):
    """A token that rides path between a and b and is hidden otherwise (static pose: hidden)."""
    return (f'<g opacity="0">{beat("opacity", [(0, 0), (a, 0), (a + .004, 1), (b, 1), (b + .004, 0), (1, 0)])}'
            f'{move(path, [(0, 0), (a, 0), (b, 1), (1, 1)], D)}{token(col, r)}</g>')


def _q10_swap(a, shown, hidden):
    """`shown` holds from a to the end of the loop (the resolved state) and `hidden` before it: both cleared together."""
    return (f'<g opacity="0">{beat("opacity", [(0, 0), (_N10_CLEAR, 0), (_N10_CLEAR + .004, 1), (a, 1), (a + .008, 0), (1, 0)])}{hidden}</g>'
            f'<g>{beat("opacity", _n10_on(a))}{shown}</g>')


@register("scene", "n10_federado")
def n10_federado(sl, ctx):
    """Federated autonomy under IT governance, told as one 12-second loop. At the top, IT's live console: the activity
    log, the permissions per space and the usage per team. Below, three team spaces, each with its person, its sources
    and its agents (two restricted, with a lock; one open). A person in the first space taps «Crear agente» and the agent
    appears; the log records it. The agent answers from its own space's sources, and when it reaches for the restricted
    space next door the lock holds: the log records it. The other teams' agents answer too and usage climbs per team.
    Then IT adjusts access: one more member for the restricted space, sent down to it and recorded. The frozen frame:
    three autonomous spaces, every agent live, and the console with usage, permissions and log under a single status,
    local autonomy with central control."""
    P = ORIENT() == "portrait"  # portrait: 20 units narrower (680), then scaled x1.206 to the art zone; labels 16 where they fit
    f15 = 16 if P else 15
    ok = ctx.brand.c("dark.ok")
    c0 = _N10_CLEAR
    spaces = sl["spaces"][:3]            # [name, short name, kind, restricted, [two sources], agents]
    log, (p_log, p_perm, p_use) = sl["log"][:3], sl["panes"]
    # the beats (fractions of the 12-second loop)
    t_tap, t_new, t_log1 = .12, .18, .235
    t_use, t_probe, t_log2 = (.27, .37), (.37, .41), .45
    t_team = ((.48, .52), (.54, .58))   # the other two spaces answer: source to agent, then the agent answers
    t_adj, t_down, t_log3, t_ok = .65, (.68, .73), .77, .81
    X, Y, W, H = 846, 96, (680 if P else 700), 256      # IT's console
    y0, sw_, sh_ = 432, (218 if P else 224), 368        # the spaces
    xs = [846 + k * (sw_ + (13 if P else 14)) for k in range(3)]
    mids = [x + sw_ / 2 for x in xs]
    cols = ["var(--accent)" if s[3] else "var(--c2)" for s in spaces]
    g = ['<defs><clipPath id="q10-badge"><circle r="46"/></clipPath></defs>', "" if P else glow(1196, 360, 480, "var(--brand)", .5)]
    ping = (lambda *a, **k: "") if P else _n10_ping  # portrait (35 KB budget): only the pings of the three key beats stay

    # ---- IT's console: header (IT's person, the title, the resolved status) and three panes
    hoff, sep1, sep2 = (2, 1076, 1296) if P else (8, 1082, 1310)
    hud = "".join(f'<path d="M{x0} {y0_ + dy * 22} V{y0_} H{x0 + dx * 22}" fill="none" stroke="var(--c4)" stroke-width="1.5" opacity=".8" transform="translate({dx * -hoff} {dy * -hoff})"/>'
                  for x0, y0_, dx, dy in ((X, Y, 1, 1), (X + W, Y, -1, 1), (X, Y + H, 1, -1), (X + W, Y + H, -1, -1)))
    hud += (f'<rect x="{X + 2}" y="{Y + 46}" width="{W - 4}" height="2" fill="var(--c2)" opacity=".16">'
            f'<animateTransform attributeName="transform" type="translate" values="0 0;0 {H - 52}" dur="5s" repeatCount="indefinite"/></rect>')
    hud = "" if P else hud  # portrait: no HUD corners nor scan line
    it_face = (_q10_head(X + 26, Y + 24, "var(--c1)") if P else
               f'<g transform="translate({X + 26} {Y + 22})">{_n10_face("q10-badge", SKIN_LIGHT, "var(--c1)", HAIR, "short", 16)}</g>')
    con = (card(X, Y, W, H, "var(--card)", "var(--c2)", 22, 1.2) + hud + f'<path d="M{X} {Y + 44} H{X + W}" stroke="var(--line)" stroke-width="1.5"/>'
           + it_face
           + T(X + 52, Y + 28, sl["console"], fit(sl["console"], 16, 300, "federated console", floor=15), "var(--white)", W6)
           + f'<g>{loop("opacity", ".4;1;.4", 3)}{spark(X + W - 26, Y + 22, .6, "var(--c4)")}</g>')
    sep = "".join(f'<path d="M{x} {Y + 60} V{Y + H - 16}" stroke="var(--line)" stroke-width="1.2"/>' for x in (sep1, sep2))
    rows = [Y + 120, Y + 160, Y + 200]
    lx, px, ux = 862, (1092 if P else 1098), (1312 if P else 1326)
    con += sep + "".join(T(x, Y + 82, t, fit(t, f15, 200, "federated pane", floor=15), "var(--c4)", W6) for x, t in ((lx, p_log), (px, p_perm), (ux, p_use)))
    live = ""                            # what the story changes on the console: it lands after the first clear (0.48 s)
    # the log: an empty line waits until its event arrives
    for j, (row, a) in enumerate(zip(log, (t_log1, t_log2, t_log3))):
        y = rows[j]
        dot = ok if j != 1 else "var(--accent)"
        live += _q10_swap(a, f'<circle cx="{lx + 6}" cy="{y - 5}" r="5" fill="{dot}"/>' + T(lx + 20, y, row, fit(row, f15, 190, "federated log", floor=15), "var(--white)", W6),
                          f'<rect x="{lx}" y="{y - 9}" width="{150 - j * 30}" height="8" rx="4" fill="var(--line)" opacity=".7"/>')
        live += ping(lx + 6, y - 5, 5, 22, a, dot)
    # permissions per space: a restricted space shows its lock and its members; an open one says so
    for k, ((name, short, kind, closed, docs, n_ag), y) in enumerate(zip(spaces, rows)):
        con += T(px, y, short, fit(short, f15, 100, "federated perm", floor=15), "var(--white)", W6)
        if closed:
            con += _lock(px + 112, y - 6) + _q10_head(px + 140, y - 3, "var(--c2)") + _q10_head(px + 162, y - 3, "var(--c2)")
            if k == 1:  # IT adds one member here
                live += (f'<g>{beat("opacity", _n10_on(t_adj + .02))}' + _q10_head(px + 184, y - 3, "var(--c4)") + '</g>'
                        + ping(px + 184, y - 5, 6, 24, t_adj + .02))
        else:
            con += T(px + 190, y, sl["open"], fit(sl["open"], f15, 90, "federated open", floor=15), "var(--c2)", 'text-anchor="end" font-weight="600"')
    live += _q10_ring(px - 10, rows[1] - 24, 216, 36, 10, [(t_adj, t_log3 + .02)])
    # usage per team: bars (never a number) that climb when a team's agents answer
    use_steps = ((.3, [(t_log1, .5), (t_probe[0] + .01, .75)]), (.4, [(t_team[0][1] + .06, .7)]), (.45, [(t_team[1][1] + .06, .8)]))
    tw = 112
    for k, ((name, short, *_r), y, (base, steps)) in enumerate(zip(spaces, rows, use_steps)):
        pts, cur = [(0, steps[-1][1]), (c0, steps[-1][1]), (c0 + .004, base)], base
        for a, v in steps:
            pts += [(a, cur), (a + .02, v)]
            cur = v
        pts.append((1, cur))
        con += (T(ux, y, short, fit(short, f15, 80, "federated use", floor=15), "var(--white)", W6)
                + f'<rect x="{ux + 90}" y="{y - 10}" width="{tw}" height="8" rx="4" fill="var(--line)"/>')
        live += (f'<rect x="{ux + 90}" y="{y - 10}" width="{tw * cur:.0f}" height="8" rx="4" fill="var(--c2)">{beat("width", [(t, round(tw * v)) for t, v in pts])}</rect>')
    # the resolved status: local autonomy, central control
    s = fit(sl["status"], f15, 300, "federated status", floor=15)
    pw = bold_width(_(str(sl["status"])), s, current_factor()) + 28
    status = f'<g>{beat("opacity", _n10_on(t_ok))}' + pill(X + W - 50 - pw / 2, Y + 22, sl["status"], ok, ctx, s, pw, "federated status", 14) + '</g>'
    status += _n10_ping(X + W - 50 - pw / 2, Y + 22, 10, 40, t_ok, ok)
    g.append(land(con, .1, .5, 14) + land(live, .6, .3, 0))

    # ---- the links: each space reports up to the console; the console's decisions travel down
    rails = "".join(f'<path d="M{m} {y0} V{Y + H}" stroke="var(--line)" stroke-width="2" stroke-dasharray="3 6"/>'
                    + ("" if P else f'<circle cx="{m}" cy="{Y + H}" r="4" fill="var(--c4)" opacity=".8"/>') for m in mids)
    g.append(land(rails, .5, .4, 0))

    # ---- the spaces
    parts = []
    ns = min(fit(sp[0], 17, sw_ - 36 - (20 if sp[3] else 0), "federated space", floor=15) for sp in spaces)  # one size for the three names
    for k, ((name, short, kind, closed, docs, n_ag), x, col) in enumerate(zip(spaces, xs, cols)):
        c = card(x, y0, sw_, sh_, "var(--card)", col, 16, 1.6)
        c += T(x + 18, y0 + 34, name, ns, "var(--white)", W6)
        c += T(x + 18, y0 + 58, kind, fit(kind, f15, sw_ - 36, "federated kind", floor=15), "var(--muted)", W6)
        c += _lock(x + sw_ - 20, y0 + 28) if closed else ""
        for j, d in enumerate(docs[:2]):
            yy = y0 + 96 + j * 28
            c += _q10_doc(x + 18, yy) + T(x + (36 if P else 40), yy, d, fit(d, f15, sw_ - (50 if P else 58), "federated source", floor=15), "var(--muted)", W6)
        c += f'<path d="M{x + 18} {y0 + 142} H{x + sw_ - 18}" stroke="var(--line)" stroke-width="1"/>'
        c += "".join(_q10_tile(x + 18 + j * 82, y0 + 158, col, ph=k * .9 + j * 1.4) for j in range(1 if k == 0 else n_ag))
        skin, jacket, hair, kind_ = _N10_PEOPLE[(0, 3, 2)[k]]
        c += f'<g transform="translate({x + 56} {y0 + 290})">{_n10_face("q10-badge", skin, jacket, hair, kind_, 36)}</g>'
        parts.append(c)
    g.append(seq(parts, .35, .5, 16))

    # ---- beat 1: a person in the first space creates an agent
    x, col = xs[0], cols[0]
    nx, ny = x + 100, y0 + 158                      # the new agent's slot
    bx, by = x + (150 if P else 156), y0 + 290      # «Crear agente», next to the person
    slot = (f'<rect x="{nx}" y="{ny}" width="72" height="58" rx="14" fill="none" stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="5 6"/>'
            + f'<path d="M{nx + 36} {ny + 20} V{ny + 38} M{nx + 27} {ny + 29} H{nx + 45}" stroke="var(--c2)" stroke-width="2" stroke-linecap="round"/>')
    new = _q10_tile(nx, ny, col, ph=2.1)
    beat1 = _q10_swap(t_new, new, slot) + _n10_ping(nx + 36, ny + 29, 30, 58, t_new)
    btn = pill(bx, by, sl["create"], "var(--c4)", ctx, f15, 124, "federated create", 14)
    done = (card(bx - 62, by - 18, 124, 36, "none", ok, 18, 1.5)
            + f'<circle cx="{bx - 38}" cy="{by}" r="10" fill="{ok}"/>{check(bx - 38, by + 1, .5, "var(--ink)")}'
            + T(bx - 22, by + 5.5, sl["created"], fit(sl["created"], f15, 80, "federated created", floor=15), ok, W6))
    beat1 += _q10_swap(t_new, done, btn)
    beat1 += (f'<circle cx="{bx}" cy="{by}" r="6" fill="none" stroke="var(--white)" stroke-width="1.5" opacity="0">'
              f'{beat("r", [(0, 6), (t_tap, 6), (t_tap + .06, 34), (1, 34)])}{beat("opacity", [(0, 0), (t_tap - .002, 0), (t_tap, 1), (t_tap + .06, 0), (1, 0)])}</circle>')
    beat1 += _q10_ride(f"M{bx} {by - 18} C{bx} {by - 50} {nx + 36} {ny + 90} {nx + 36} {ny + 30}", t_tap + .01, t_new)
    beat1 += _q10_ride(f"M{mids[0]} {y0} V{Y + H}", t_new + .01, t_log1)
    g.append(land(beat1, .9, .4, 0))

    # ---- beat 2: the agent answers from its own space; the restricted space next door stays out of reach
    b2 = _q10_ring(x - 6, y0 - 6, sw_ + 12, sh_ + 12, 20, [(t_use[0], t_log2)], "var(--c4)", 2)
    for j in range(2):
        yy = y0 + 92 + j * 28
        b2 += _q10_ride(f"M{x + 26} {yy} C{x + 70} {yy} {nx + 36} {ny - 30} {nx + 36} {ny + 29}", t_use[0] + j * .02, t_use[0] + .05 + j * .02)
        b2 += _q10_ring(x + 12, yy - 20, 170, 28, 8, [(t_use[0] + j * .02, t_use[0] + .07 + j * .02)], "var(--c4)", 1.5)
    b2 += _q10_ring(nx - 6, ny - 6, 84, 70, 18, [(t_use[0] + .07, t_use[1])])
    wx, wy = xs[1], ny + 29
    b2 += _q10_ride(f"M{nx + 72} {wy} H{wx - 8}", t_probe[0], t_probe[1])
    b2 += (f'<g opacity="0">{beat("opacity", [(0, 0), (t_probe[1], 0), (t_probe[1] + .006, 1), (t_probe[1] + .07, 1), (t_probe[1] + .09, 0), (1, 0)])}'
           f'<circle cx="{wx - 3}" cy="{wy}" r="20" fill="var(--accent)"/>{_lock(wx - 3, wy - 2, "var(--ink)")}</g>'
           + _n10_ping(wx - 3, wy, 20, 48, t_probe[1], "var(--accent)")
           + _q10_ring(xs[1], y0, sw_, sh_, 16, [(t_probe[1], t_probe[1] + .07)], "var(--accent)", 3)
           + ping(xs[1] + sw_ - 20, y0 + 30, 12, 34, t_probe[1] + .01, "var(--accent)"))
    b2 += _q10_ride(f"M{mids[0]} {y0} V{Y + H}", t_use[1] - .03, t_probe[0] + .01)
    g.append(land(b2, .9, .4, 0))

    # ---- beat 3: the other teams' agents answer too; each reports up and its usage climbs
    b3 = ""
    for k, (a, b) in zip((1, 2), t_team):
        x = xs[k]
        yy = y0 + 92
        b3 += _q10_ride(f"M{x + 26} {yy} C{x + 70} {yy} {x + 54} {ny - 30} {x + 54} {ny + 29}", a, b, cols[k])
        b3 += _q10_ring(x + 12, ny - 6, 84, 70, 18, [(b, b + .05)])
        b3 += _q10_ride(f"M{mids[k]} {y0} V{Y + H}", b + .02, b + .06)
    g.append(land(b3, .9, .4, 0))

    # ---- beat 4: IT adjusts access (one more member for the restricted space); the change travels down and is recorded
    b4 = ping(X + 26, Y + 22, 17, 40, t_adj - .03)
    b4 += "" if P else _q10_ride(f"M{X + 26} {Y + 44} H{sep1} V{rows[1] - 6} H{px - 8}", t_adj - .04, t_adj)  # portrait: the row's ring says it
    b4 += _q10_ride(f"M{mids[1]} {Y + H} V{y0}", t_down[0], t_down[1])
    skin, jacket, hair, kind_ = _N10_PEOPLE[4]
    mx_, my_ = xs[1] + 140, y0 + 290
    b4 += (f'<g>{beat("opacity", _n10_on(t_down[1]))}<g transform="translate({mx_} {my_})">{_n10_face("q10-badge", skin, jacket, hair, kind_, 30)}'
           f'<circle cx="22" cy="-22" r="11" fill="var(--c4)"/><path d="M22 -28 V-16 M16 -22 H28" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round"/></g>'
           + TC(mx_, my_ + 56, sl["member"], fit(sl["member"], f15, 130, "federated member", floor=15), "var(--c4)", W6) + '</g>'
           + ping(mx_, my_, 30, 56, t_down[1]))
    g.append(land(b4 + status, .9, .4, 0))
    if P:  # IT's console over the three spaces: already a stack, 680 units wide -> the art zone's 820
        return _pz_fit("".join(g), (846, 88, 680, 720), "pz-n10"), D, FREEZE
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 11 · how we decide (energía's m11_criterio, with ideas on two lines)
def _q11_idea(lines, x, y, verdict, t, lane, w=300, h=72):
    """One idea card at (x, y), its text in one or two lines. verdict «ok»: a check and a stripe in the color of its reason;
    «aside»: a pause mark, set aside politely. t: the fraction of the loop at which the verdict shows."""
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
    lines = lines if isinstance(lines, list) else [lines]
    s = min(fit(ln, 17, w - 74, "idea card", floor=15) for ln in lines)
    y1 = y + h / 2 + s * .36 - (len(lines) - 1) * s * .62
    c += "".join(T(x + 58, f"{y1 + j * s * 1.24:.1f}", ln, s, "var(--white)", W6) for j, ln in enumerate(lines))
    return c


@register("scene", "n11_criterio")
def n11_criterio(sl, ctx):
    """How we decide, as a sorting loop (energía's m11_criterio, fitted to the pagos ideas). Ideas arrive one by one under
    the two criteria. The first («Responder a comercios sin esperar») lights «Retorno claro» and goes to «Construimos»;
    the second («Una demo vistosa») lights neither and is set aside, politely, under «Por ahora, no»; the third
    («Conocimiento gobernado por equipo», slide 10's federated knowledge) lights «Habilitador clave» and is built too.
    Between ideas the empty spot asks «¿Retorno o habilitador?». The frozen frame: two ideas built, each checked in the
    color of its reason, one set aside, an empty slot and the question waiting for the next idea: theirs."""
    ok = ctx.brand.c("dark.ok")
    cols = (ok, "var(--c2)")
    cw, ch, cy0, cxs = 334, 200, 96, (846, 1208)
    mid = 1194
    ex, ey, ew, eh = 1044, 346, 300, 72           # the evaluation spot, under the «o»
    zy, zh = 468, 344                             # «Construimos»; the tray for the rest is shorter (it starts at ay)
    ay = 640
    slot = lambda k: 683 - k * 84                 # slots stack upwards from the zone's base
    P = ORIENT() == "portrait"
    g = [] if P else [glow(1194, 440, 440, "var(--brand)", .45)]  # portrait: no glow under the ask
    ideas = sl["ideas"]                           # [[text or [line, line], verdict («retorno» | «habilitador» | «no»)], ...]
    starts = (.10, .36, .62)
    lock = {"retorno": 0, "habilitador": 1}
    # criteria: the matching card glows while its idea is judged, and keeps its check once one has passed through it
    cards = []
    for k, ((name, text, *_r), col) in enumerate(zip(sl["criteria"], cols)):
        x = cxs[k]
        c = card(x, cy0, cw, ch, "var(--card)", col, 18, 2)
        if k == 0:
            c += "".join(f'<rect x="{x + 28 + j * 26}" y="{cy0 + 80 - hh}" width="17" height="{hh}" rx="4" fill="{col}"/>' for j, hh in enumerate((20, 34, 50)))
        else:
            c += (f'<rect x="{x + 28}" y="{cy0 + 68}" width="84" height="12" rx="4" fill="{col}"/>'
                  + "".join(f'<rect x="{x + 33 + j * 42}" y="{cy0 + 30}" width="32" height="32" rx="4" fill="none" stroke="{col}" stroke-width="2.5"/>' for j in range(2)))
        c += T(x + 28, cy0 + 118, name, fit(name, 26, cw - 56, "criterion name", floor=15), "var(--white)", W6)
        c += TCW(x + 28, cy0 + 152, text, 30, 18, "var(--muted)", W6, 1.3, "start")
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
    beam = [f"M{ex + 76} {ey} C{ex + 76} {ey - 26} {cxs[0] + cw / 2} {cy0 + ch + 24} {cxs[0] + cw / 2} {cy0 + ch + 2}",
            f"M{ex + ew - 76} {ey} C{ex + ew - 76} {ey - 26} {cxs[1] + cw / 2} {cy0 + ch + 24} {cxs[1] + cw / 2} {cy0 + ch + 2}"]
    lane = [f"M{ex + 56} {ey + eh} C{ex + 56} {ey + eh + 40} {cxs[0] + cw / 2} {zy - 36} {cxs[0] + cw / 2} {zy}",
            f"M{ex + ew - 56} {ey + eh} C{ex + ew - 56} {ey + eh + 44} {cxs[1] + cw / 2} {ay - 70} {cxs[1] + cw / 2} {ay}"]
    rails = "".join(f'<path d="{d}" fill="none" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 7"/>' for d in beam + lane)
    spot = (f'<rect x="{ex}" y="{ey}" width="{ew}" height="{eh}" rx="14" fill="none" stroke="var(--c4)" stroke-width="1.5" stroke-dasharray="6 7" opacity=".7">'
            f'{loop("stroke-opacity", ".35;1;.35", 3)}</rect>')
    away = [(0, 1)] + [p for s in starts for p in ((s + .02, 1), (s + .04, 0), (s + .19, 0), (s + .22, 1))] + [(1, 1)]
    spot += f'<g>{beat("opacity", away)}' + TC(ex + ew / 2, ey + eh / 2 + 6, sl["ask"], fit(sl["ask"], 17, ew - 40, "criterion ask", floor=15), "var(--muted)", W6) + '</g>'
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
                    + _q11_idea(text, ex, ey, "ok" if verdict in lock else "aside", vt, cols[lock.get(verdict, 0)], ew, eh) + '</g>')
    g.append(land("".join(flow), .5, .3, 0))
    if P:  # already a stack (criteria, verdict, trays): scaled to the art zone, ask 17 -> 20 units
        return _pz_fit("".join(g), (844, 92, 700, 724), "pz-n11"), D, FREEZE
    return "".join(g), D, FREEZE


# ---------------------------------------------------------------- 12 · how to start (energía's m12_formas, handing off to the discovery)
@register("scene", "n12_formas")
def n12_formas(sl, ctx):
    """Four ways to start, and a need that picks its way (energía's m12_formas). Under the columns a chip asks «¿Qué
    necesitan hoy?»; it becomes one need at a time (probar, velocidad, control, continuidad) and a spark climbs its
    branch to the way that answers it: the column lights and its promise is underlined. When the question comes back,
    a spark leaves the root to the right and lights the hand-off to slide 13: which way, we decide it together in the
    discovery. The frozen frame: all four branches lit, every promise underlined, the question at the root and the
    hand-off lit: any of them is a way in, they combine, and the discovery decides."""
    if ORIENT() == "portrait":  # the 2x2 of energía's m12 (energia_s10_12.py), with the hand-off under the grid
        return _pz_formas(sl, ctx, .16, .78, .775, "q12-badge", sl["next"], .80), D, FREEZE
    cols = ("var(--c1)", "var(--accent)", "var(--c3)", "var(--c2)")
    n, gap, y0, h = len(sl["models"]), 24, 404, 282
    w = (1408 - gap * (n - 1)) / n
    xs = [96 + k * (w + gap) for k in range(n)]
    rx, ry, rw, rh = 800, 788, 400, 50             # the root chip, centered at (rx, ry)
    starts = [.14 + k * .16 for k in range(n)]
    arrive = [s + .08 for s in starts]
    t_back, t_next = .78, .80                      # the question comes back; the hand-off lights
    g = ['<defs><clipPath id="q12-badge"><circle r="46"/></clipPath></defs>', glow(800, 600, 560, "var(--brand)", .4)]
    parts, lines = [], []
    for k, (x, (name, promise, items), col) in enumerate(zip(xs, sl["models"], cols)):
        c = card(x, y0, w, h, "var(--card)", col, 18, 2)
        c += pill(x + 24 + min(w / 2 - 24, bold_width(_(str(name)), 17, current_factor()) / 2 + 18), y0 + 36, name, col, ctx, 17, w - 48, "model name")
        ps = fit(promise, 20, w - 48, "model promise", floor=15)
        c += T(x + 24, y0 + 88, promise, ps, "var(--c4)", W6)
        for j, it in enumerate(items[:4]):
            c += f'<circle cx="{x + 30:.1f}" cy="{y0 + 130 + j * 40}" r="5" fill="{col}"/>' + T(x + 46, y0 + 136 + j * 40, it, fit(it, 17, w - 70, "model item", floor=15), "var(--white)")
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
        e = arrive[k + 1] - .02 if k + 1 < n else t_back - .005
        live.append(f'<rect x="{xs[k] - 6:.1f}" y="{y0 - 6}" width="{w + 12:.1f}" height="{h + 12}" rx="22" fill="none" stroke="var(--c4)" stroke-width="3" opacity="0">'
                    f'{beat("opacity", [(0, 0), (a, 0), (a + .01, 1), (e, 1), (e + .015, 0), (1, 0)])}</rect>')
    g.append(land("".join(live), .5, .3, 0))
    # the root: one of their people (the operator of slide 14, headset on) and the question, which becomes one need at a time
    root = (card(rx - rw / 2, ry - rh / 2, rw, rh, "var(--dim)", "var(--c4)", rh / 2, 1.5)
            + f'<g transform="translate({rx - rw / 2 + 27} {ry})">{_n10_face("q12-badge", SKIN_LIGHT, "var(--c1)", HAIR, "short", 20)}</g>')
    tx = rx + 16
    q = sl["ask"]
    root += f'<g>{beat("opacity", [(0, 1), (starts[0], 1), (starts[0] + .01, 0), (t_back, 0), (t_back + .01, 1), (1, 1)])}' + TC(tx, ry + 6.5, q, fit(q, 18, rw - 76, "need ask", floor=15), "var(--c4)", W6) + '</g>'
    for k, need in enumerate(sl["needs"][:n]):
        s = starts[k]
        e = starts[k + 1] if k + 1 < n else t_back
        root += (f'<g opacity="0">{beat("opacity", [(0, 0), (s + .005, 0), (s + .015, 1), (e - .01, 1), (e, 0), (1, 0)])}'
                 + TC(tx, ry + 6.5, need, fit(need, 18, rw - 76, "need"), "var(--white)", W6) + '</g>')
    g.append(land(root, 1.0, .45, 12))
    # the hand-off: which way to start, we decide it in the discovery (slide 13)
    nx0 = rx + rw / 2 + 28
    s = fit(sl["next"], 17, 1504 - nx0 - 90, "formas next", floor=15)
    nw = bold_width(_(str(sl["next"])), s, current_factor()) + 76
    hand = (f'<path d="M{rx + rw / 2} {ry} H{nx0}" stroke="var(--line)" stroke-width="2" stroke-dasharray="4 7"/>'
            + f'<g>{beat("opacity", _n10_on(t_next))}' + card(nx0, ry - rh / 2, nw, rh, "var(--card)", "var(--c4)", rh / 2, 1.5)
            + spark(nx0 + 28, ry, .55, "var(--c4)") + T(nx0 + 48, ry + s * .36, sl["next"], s, "var(--white)", W6)
            + f'<path d="M{nx0 + nw - 26} {ry - 7} L{nx0 + nw - 18} {ry} L{nx0 + nw - 26} {ry + 7}" fill="none" stroke="var(--c4)" stroke-width="2" stroke-linecap="round"/></g>'
            + _q10_ride(f"M{rx + rw / 2} {ry} H{nx0 + 10}", t_back, t_next)
            + _n10_ping(nx0 + 28, ry, 10, 36, t_next))
    g.append(land(hand, 1.1, .45, 12))
    return "".join(g), D, FREEZE
