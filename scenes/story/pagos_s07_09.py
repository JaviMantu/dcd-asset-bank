"""Group C · pagos slides 7, 8 and 9: the evidence, who we are and our own case.

Slides 7 and 8 reuse the energía v4 scenes with pagos args, because their content is homologous: m09_evidencia (the 70 %
stays still; one more tool waits, the new way of working arrives) and m10_quienes with `roles` (six colleagues, one
discipline each). Slide 9 is this deck's own, n09_casa, keyed on seconds of the loop with the energía group C timing helpers
(_n07_*): every resolved state holds until _N07_RESET, so the frozen frame (10.8 s) shows the story told."""

_Q09_ROWS = (198, 350, 502, 654)     # people and knowledge rows
_Q09_SLOTS = (250, 426, 602)         # agent rows
_Q09_PX, _Q09_PR = 900, 36           # people: badge center x and radius
_Q09_AX, _Q09_AW, _Q09_AH = 1173, 136, 84
_Q09_KX, _Q09_KW, _Q09_KH = 1462, 112, 72
_Q09_WHO = _N10_PEOPLE[:4]           # the colleagues of slide 8, now at work
_Q09_JACKET = [p[1] for p in _Q09_WHO]


def _q09_pa(k, j):
    """The link from person k to agent j."""
    x0, x1, y0, y1 = _Q09_PX + _Q09_PR + 4, _Q09_AX - _Q09_AW / 2, _Q09_ROWS[k], _Q09_SLOTS[j]
    return f"M{x0} {y0} C{x0 + 84} {y0} {x1 - 84} {y1} {x1} {y1}"


def _q09_ak(j, i):
    """The link from agent j to knowledge source i."""
    x0, x1, y0, y1 = _Q09_AX + _Q09_AW / 2, _Q09_KX - _Q09_KW / 2, _Q09_SLOTS[j], _Q09_ROWS[i]
    return f"M{x0} {y0} C{x0 + 74} {y0} {x1 - 74} {y1} {x1} {y1}"


def _q09_link(d, at=None, dur=.4, col="var(--c4)"):
    """A link at rest (at None) or one that draws itself at `at` in `col` and settles as a link at rest until the reset."""
    base = 'fill="none" stroke="var(--c2)" stroke-width="1.5" opacity=".6"'
    if at is None:
        return f'<path d="{d}" {base}/>'
    r0, r1 = _N07_RESET
    draw = _n07_key("stroke-dashoffset", [(at, 1), (at + dur, 0), (r0, 0), (r1, 1)])
    return (f'<path d="{d}" {base} pathLength="1" stroke-dasharray="1" stroke-dashoffset="1">{draw}</path>'
            f'<path d="{d}" fill="none" stroke="{col}" stroke-width="2" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" opacity="0">'
            f'{draw}{_n07_win(at, at + dur + .5, .1)}</path>')


def _q09_run(d, a, b, back=False, inner=None):
    """A token along path d between a and b seconds (back: from its end to its start)."""
    inner = inner or token("var(--c4)", 5)
    return (f'<g opacity="0">{_n07_key("opacity", [(a - .01, 0), (a, 1), (b, 1), (b + .01, 0)])}'
            f'{_n07_move(d, [(a, 1 if back else 0), (b, 0 if back else 1)])}{inner}</g>')


def _q09_doc():
    """The answer, carrying its source."""
    return ('<rect x="-8" y="-10" width="16" height="20" rx="2.5" fill="var(--ink)" stroke="var(--c4)" stroke-width="1.6"/>'
            '<path d="M-4 -4 H4 M-4 0 H4 M-4 4 H1" stroke="var(--c4)" stroke-width="1.3" stroke-linecap="round"/>')


def _q09_glyph(i):
    """The four kinds of knowledge, in thin strokes around 0,0: a document, a table, a conversation, a restricted folder."""
    st = 'fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"'
    return ('<path d="M-9 -13 H4 L10 -7 V13 H-9 Z M4 -13 V-7 H10 M-5 -2 H6 M-5 3 H6 M-5 8 H2" {0}/>',
            '<rect x="-12" y="-10" width="24" height="20" rx="2.5" {0}/><path d="M-12 -3 H12 M-12 4 H12 M-4 -10 V10" {0}/>',
            '<path d="M-13 -10 H5 V2 H-6 L-11 6 V2 H-13 Z M8 -4 H13 V8 H11 V12 L7 8 H-2 V5" {0}/>',
            '<path d="M-13 -8 H-4 L-1 -5 H12 V10 H-13 Z" {0}/>')[i].format(st)


_PN09_ROWS = (846, 1014, 1182, 1350)   # portrait: people and knowledge rows
_PN09_SLOTS = (900, 1098, 1296)        # portrait: agent rows
_PN09_PX, _PN09_PR = 130, 44
_PN09_AX, _PN09_AW, _PN09_AH = 452, 190, 100
_PN09_KX, _PN09_KW, _PN09_KH = 752, 150, 86


def _pn09_pa(k, j):
    """Portrait: the link from person k to agent j."""
    x0, x1, y0, y1 = _PN09_PX + _PN09_PR + 4, _PN09_AX - _PN09_AW // 2, _PN09_ROWS[k], _PN09_SLOTS[j]
    return f"M{x0} {y0} C{x0 + 70} {y0} {x1 - 70} {y1} {x1} {y1}"


def _pn09_ak(j, i):
    """Portrait: the link from agent j to knowledge source i."""
    x0, x1, y0, y1 = _PN09_AX + _PN09_AW // 2, _PN09_KX - _PN09_KW // 2, _PN09_SLOTS[j], _PN09_ROWS[i]
    return f"M{x0} {y0} C{x0 + 50} {y0} {x1 - 50} {y1} {x1} {y1}"


def _pn09_link(d, at=None, dur=.4):
    """Portrait: a link at rest, or one that draws itself at `at` and holds until the reset (one path, one animation)."""
    base = f'<path d="{d}" fill="none" stroke="var(--c2)" stroke-width="2" opacity=".7"'
    if at is None:
        return base + '/>'
    r0, r1 = _N07_RESET
    return base + f' pathLength="1" stroke-dasharray="1" stroke-dashoffset="1">{_n07_key("stroke-dashoffset", [(at, 1), (at + dur, 0), (r0, 0), (r1, 1)])}</path>'


def _pn09_op(pts):
    """Portrait: a compact looping opacity keyed on seconds, pts = [(s, value)] strictly increasing inside (0, D)."""
    kt = "0;" + ";".join(f"{t / D:.3f}" for t, _v in pts) + ";1"
    vals = ";".join(str(v) for v in [pts[0][1]] + [v for _t, v in pts] + [pts[-1][1]])
    return f'<animate attributeName="opacity" values="{vals}" keyTimes="{kt}" dur="{D}s" repeatCount="indefinite"/>'


def _pn09_win(a, b, f=.12):
    return _pn09_op([(a, 0), (a + f, 1), (b - f, 1), (b, 0)])


def _pn09_hold(on, f=.15):
    return _pn09_op([(on, 0), (on + f, 1), (_N07_RESET[0], 1), (_N07_RESET[1], 0)])


def _pn09_run(d, a, b, back=False, inner='<use href="#pn09-t"/>'):
    """Portrait: a token along path d between a and b seconds (back: from its end to its start), in two compact animations."""
    k0, k1 = (1, 0) if back else (0, 1)
    ka, kb = f"{a / D:.3f}", f"{b / D:.3f}"
    return (f'<g opacity="0"><animate attributeName="opacity" values="0;1;0" keyTimes="0;{ka};{kb}" calcMode="discrete" dur="{D}s" repeatCount="indefinite"/>'
            f'<animateMotion path="{d}" keyPoints="{k0};{k0};{k1};{k1}" keyTimes="0;{ka};{kb};1" calcMode="linear" dur="{D}s" repeatCount="indefinite"/>{inner}</g>')


def _pn09_twin(sl, ctx):
    """internal-case in portrait: the same three columns (people with their disciplines, the agents they create and share,
    our governed knowledge) redrawn on the 900x1600 stage with rows 168 units apart and labels at 20 or more, and the seal
    at the foot. Same beats in seconds of the loop as the desktop story; the highlight overlays of the links and a few
    pings are folded into the rings to keep the budget; the frozen frame shows the same resolved state."""
    zx, zy, zw, zh = ART_ZONE(sl.get("layout") or "left")
    ok = ctx.brand.c("dark.ok")
    R = _N07_RESET
    PX, PR, AX, AW, AH, KX, KW, KH = _PN09_PX, _PN09_PR, _PN09_AX, _PN09_AW, _PN09_AH, _PN09_KX, _PN09_KW, _PN09_KH
    ys, sy = _PN09_ROWS, _PN09_SLOTS
    pa, ak, link, run = _pn09_pa, _pn09_ak, _pn09_link, _pn09_run
    g = [f'<defs><clipPath id="pn09-badge"><circle r="46"/></clipPath><g id="pn09-t">{token("var(--c4)", 6)}</g></defs>']

    # the three column heads, wrapped at 20 units
    hy = zy + 34
    heads = "".join(TCW(x, hy, sl[k], _n07_chars(sl[k], 20, room), 20, "var(--white)", W6, 1.2)
                    for x, k, room in ((PX, "people", 2 * (PX - zx)), (AX, "agents", 250), (KX, "knowledge", 2 * (zx + zw - KX))))
    heads += '<path d="' + " ".join(f"M{x - 30} {hy + 94} H{x + 30}" for x in (PX, AX, KX)) + '" stroke="var(--c4)" stroke-width="2" opacity=".7"/>'

    P3_ON, A2_BORN = 2.2, 3.0
    CONNECT = 3.4
    SHARE = ((0, 4.5), (1, 4.8), (3, 5.1))
    ASK, ANSWER = 5.9, 7.05
    P4_ON, A3_BORN, LOCKED, SHARE3 = 7.8, 8.55, 9.55, 9.7
    SEAL = 10.1

    links = [link(pa(k, 0)) for k in (0, 1)] + [link(ak(0, i)) for i in (0, 1)]
    links.append(link(pa(2, 1), P3_ON + .15, .45))
    links += [link(ak(1, i), CONNECT) for i in (1, 2)]
    links += [link(pa(k, 1), t) for k, t in SHARE]
    links.append(link(pa(3, 2), P4_ON + .1))
    links.append(link(ak(2, 3), A3_BORN + .35, .35))
    links.append(link(pa(2, 2), SHARE3, .35))

    # people: the colleagues of slide 8, each augmented (its spark badge), with their discipline under the badge
    people = []
    for k, (skin, jacket, hair, kind) in enumerate(_Q09_WHO):
        b = PR * .74
        c = (_n10_face("pn09-badge", skin, jacket, hair, kind, PR)
             + f'<circle cx="{b:.0f}" cy="{-b:.0f}" r="11" fill="var(--c4)"/>{spark(round(b), round(-b), .42, "var(--ink)")}')
        people.append(pop(c, PX, ys[k], .3 + k * .1, .45))
        if sl.get("roles"):
            people.append(land(pill(PX, ys[k] + 68, sl["roles"][k], "var(--dim)", ctx, 20, 2 * (PX - zx), "case role"), .75 + k * .08, .4, 8))
    people = "".join(people)

    ring_p = lambda k, a, b, col="var(--c4)": f'<circle cx="{PX}" cy="{ys[k]}" r="{PR + 4}" fill="none" stroke="{col}" stroke-width="3" opacity="0">{_pn09_win(a, b)}</circle>'

    def face(j, n, k, at=None):
        x, y = AX - AW // 2 + 26 + 24 * n, sy[j] + 28
        dot = f'<circle cx="{x}" cy="{y}" r="10" fill="{_Q09_JACKET[k]}"/>'
        return dot if at is None else f'<g opacity="0">{_pn09_hold(at, .12)}{dot}</g>'

    def tile(j, faces=""):
        x = AX - AW // 2
        return (card(x, sy[j] - AH // 2, AW, AH, "var(--dim)", "var(--accent)", 14, 1.5)
                + f'<path d="M{x + 76} {sy[j] - 18} h64 M{x + 76} {sy[j] - 4} h40" stroke="var(--c2)" stroke-width="7" stroke-linecap="round" opacity=".6"/>' + faces)

    def spark_a(j, born=None):
        s = spark(0, 0, .9, "var(--accent)")
        if born is not None:
            s = f'<g>{_n07_tr([(born - .05, "0"), (born + .15, "1.35"), (born + .35, "1"), (R[0], "1"), (R[1], "0")], "scale")}{s}</g>'
        return f'<g transform="translate({AX - AW // 2 + 38} {sy[j] - 12})">{s}</g>'

    def slot(j, born):
        x, y = AX - AW // 2, sy[j] - AH // 2
        return (f'<g>{_n07_key("opacity", [(born - .25, 1), (born - .1, 0), (R[1], 0), (R[1] + .1, 1)])}'
                f'<rect x="{x}" y="{y}" width="{AW}" height="{AH}" rx="14" fill="none" stroke="var(--c2)" stroke-width="1.8" stroke-dasharray="6 8" opacity=".7"/>'
                f'<path d="M{AX - 11} {sy[j]} H{AX + 11} M{AX} {sy[j] - 11} V{sy[j] + 11}" stroke="var(--c2)" stroke-width="2" stroke-linecap="round"/></g>')

    ring_a = lambda j, a, b, col="var(--c4)": (f'<rect x="{AX - AW // 2 - 5}" y="{sy[j] - AH // 2 - 5}" width="{AW + 10}" height="{AH + 10}" rx="18" fill="none" '
                                                f'stroke="{col}" stroke-width="3" opacity="0">{_pn09_win(a, b)}</rect>')

    a1 = tile(0, face(0, 0, 0) + face(0, 1, 1)) + spark_a(0)
    a2 = (slot(1, A2_BORN) + f'<g opacity="0">{_pn09_hold(A2_BORN - .1)}{tile(1, face(1, 0, 2, A2_BORN + .15) + "".join(face(1, n + 1, k, t + .4) for n, (k, t) in enumerate(SHARE)))}</g>'
          + spark_a(1, A2_BORN))
    lock_at = (AX + AW // 2 - 20, sy[2] - AH // 2 + 24)
    a3 = (slot(2, A3_BORN) + f'<g opacity="0">{_pn09_hold(A3_BORN - .1)}{tile(2, face(2, 0, 3, A3_BORN + .15) + face(2, 1, 2, SHARE3 + .35))}</g>'
          + spark_a(2, A3_BORN) + f'<g opacity="0">{_pn09_hold(LOCKED, .1)}{_lock(*lock_at)}</g>' + _n07_ping(lock_at[0], lock_at[1] + 4, 10, 28, LOCKED, "var(--accent)"))

    # knowledge: four sources that stay where they are; the fourth is restricted (its lock)
    srcs = []
    for i, y in enumerate(ys):
        restricted = i == 3
        x0 = KX - KW // 2
        srcs.append(card(x0, y - KH // 2, KW, KH, "var(--card)", "var(--accent)" if restricted else "var(--c1)", 12, 1.5)
                    + f'<g transform="translate({x0 + 36} {y}) scale(1.3)">{_q09_glyph(i)}</g>'
                    + f'<path d="M{x0 + 71} {y - 7} h{24 if restricted else 48} M{x0 + 71} {y + 7} h{16 if restricted else 32}" stroke="var(--c2)" stroke-width="6" stroke-linecap="round" opacity=".5"/>'
                    + (_lock(x0 + KW - 20, y - KH // 2 + 24) if restricted else ""))
    ring_k = lambda i, a, b, col="var(--c4)": (f'<rect x="{KX - KW // 2 - 5}" y="{ys[i] - KH // 2 - 5}" width="{KW + 10}" height="{KH + 10}" rx="16" fill="none" '
                                                f'stroke="{col}" stroke-width="3" opacity="0">{_pn09_win(a, b)}</rect>')
    tok = '<use href="#pn09-t"/>'

    fx = []
    # 1 · a colleague creates an agent
    fx += [ring_p(2, P3_ON, A2_BORN + .5), run(pa(2, 1), P3_ON + .15, P3_ON + .6, inner=tok)]
    # 2 · it connects to two sources: the knowledge stays in place, only its signal travels
    fx += [ring_k(i, CONNECT, CONNECT + 1.1) for i in (1, 2)]
    fx += [run(ak(1, i), CONNECT + .45, CONNECT + .9, True, tok) for i in (1, 2)]
    # 3 · she shares it: each colleague joins its row of faces
    for k, t in SHARE:
        fx.append(run(pa(k, 1), t, t + .4, True, tok))
    # 4 · one of them asks; the agent reads its sources and answers with the source
    fx += [ring_p(0, ASK - .1, ANSWER + .7), run(pa(0, 1), ASK, ASK + .4, inner=tok), ring_a(1, ASK + .4, ANSWER + .2)]
    fx += [run(ak(1, i), ASK + .5, ANSWER - .05, True, tok) for i in (1, 2)]  # the sources' signal comes back to the agent
    fx += [run(pa(0, 1), ANSWER, ANSWER + .45, True, f'<g transform="scale(1.3)">{_q09_doc()}</g>'),
           _n07_badge(round(PX + PR * .74), round(ys[0] + PR * .74), ANSWER + .45, ok, 13)]
    # 5 · another colleague creates his own over the restricted source: it inherits the lock; only who has access joins it
    fx += [ring_p(3, P4_ON, A3_BORN + .5), run(pa(3, 2), P4_ON + .1, P4_ON + .5, inner=tok)]
    fx += [ring_k(3, A3_BORN + .35, LOCKED + .3, "var(--accent)"), run(ak(2, 3), A3_BORN + .7, LOCKED - .05, True, tok)]
    fx.append(run(pa(2, 2), SHARE3, SHARE3 + .35, True, tok))

    # the seal: our partnership, said as ours
    seal_y = zy + zh - 60
    ss = fit(sl["badge"], 22, zw - 76, "case badge", floor=20)
    seal = pill(zx + zw / 2, seal_y, sl["badge"], "var(--c4)", ctx, ss, zw - 40, "case badge")
    sw = min(zw - 40, bold_width(_(str(sl["badge"])), ss, current_factor()) + 36)
    hh = ss + 20
    shine = (f'<rect x="{zx + zw / 2 - sw / 2 - 5:.0f}" y="{seal_y - hh / 2 - 5:.0f}" width="{sw + 10:.0f}" height="{hh + 10}" rx="{hh / 2 + 5:.0f}" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">'
             f'{_pn09_win(SEAL, SEAL + .6, .15)}</rect>')

    g += [land(heads, .1, .45, 8), land("".join(links), 1.0, .5, 0), people, seq([a1, a2, a3], .55, .45, 12, 1.4),
          seq(srcs, .7, .45, 12, 1.6), "".join(fx), land(seal, 1.35, .45, 12), shine]
    return portrait_mark("".join(g)), D, FREEZE


@register("scene", "n09_casa")
def sc_n09_casa(sl, ctx):
    """Our own case, as one working day in 12 seconds. Three columns: people of every team (four colleagues of slide 8,
    with the same faces and disciplines, `roles`), the agents they create and share, and our knowledge, connected and
    governed (one source restricted, with its lock). One agent is already in use. Software creates a second one: it
    connects to two sources, where the knowledge stays (only its signal travels), and she shares it with the other three,
    who join its row of faces. Datos asks it and gets the answer with its source. Then Cloud creates his own agent over the
    restricted source: it inherits the lock, and only Software, who has access to that space, joins it. The seal lights
    last: what we use at home, we implement for our clients. The frozen frame: three agents in use, shared across teams,
    over governed knowledge; no figure anywhere."""
    if ORIENT() == "portrait":
        return _pn09_twin(sl, ctx)
    ok = ctx.brand.c("dark.ok")
    R = _N07_RESET
    PX, PR, AX, AW, AH, KX, KW, KH = _Q09_PX, _Q09_PR, _Q09_AX, _Q09_AW, _Q09_AH, _Q09_KX, _Q09_KW, _Q09_KH
    ys, sy = _Q09_ROWS, _Q09_SLOTS
    g = ['<defs><clipPath id="q09-badge"><circle r="46"/></clipPath></defs>', glow(AX, 440, 420, "var(--brand)", .45)]

    # the three column heads
    heads = "".join(TCW(x, 108, sl[k], _n07_chars(sl[k], 16, room), 16, "var(--white)", W6, 1.3)
                    for x, k, room in ((PX, "people", 2 * (PX - 824)), (AX, "agents", 212), (KX, "knowledge", 2 * (1558 - KX))))
    heads += "".join(f'<path d="M{x - 26} 146 H{x + 26}" stroke="var(--c4)" stroke-width="1.5" opacity=".7"/>' for x in (PX, AX, KX))

    # --- the story, in seconds of the loop
    P3_ON, A2_BORN = 2.2, 3.0                           # a colleague creates an agent
    CONNECT = 3.4                                       # it connects to two sources
    SHARE = ((0, 4.5), (1, 4.8), (3, 5.1))              # she shares it with three colleagues
    ASK, ANSWER = 5.9, 7.05                             # one of them asks and gets the answer with its source
    P4_ON, A3_BORN, LOCKED, SHARE3 = 7.8, 8.55, 9.55, 9.7  # another creates his own over the restricted source
    SEAL = 10.1                                         # and what we use at home, we implement for our clients

    # links at rest (the agent already in use) and the ones the story draws
    links = [_q09_link(_q09_pa(k, 0)) for k in (0, 1)] + [_q09_link(_q09_ak(0, i)) for i in (0, 1)]
    links.append(_q09_link(_q09_pa(2, 1), P3_ON + .15, .45))
    links += [_q09_link(_q09_ak(1, i), CONNECT) for i in (1, 2)]
    links += [_q09_link(_q09_pa(k, 1), t) for k, t in SHARE]
    links.append(_q09_link(_q09_pa(3, 2), P4_ON + .1))
    links.append(_q09_link(_q09_ak(2, 3), A3_BORN + .35, .35, "var(--accent)"))
    links.append(_q09_link(_q09_pa(2, 2), SHARE3, .35))

    # people: the faceless colleagues of slide 8, each augmented (its spark badge)
    people = []
    for k, (skin, jacket, hair, kind) in enumerate(_Q09_WHO):
        c = (f'<circle r="{PR + 7}" fill="none" stroke="var(--c2)" stroke-width="1" stroke-dasharray="2 6" opacity=".5"/>'
             + _n10_face("q09-badge", skin, jacket, hair, kind, PR)
             + f'<circle cx="{PR * .74:.1f}" cy="{-PR * .74:.1f}" r="10" fill="var(--c4)"/>{spark(PR * .74, -PR * .74, .38, "var(--ink)")}')
        people.append(pop(c, PX, ys[k], .3 + k * .1, .45))
        if sl.get("roles"):  # the discipline each one had on slide 8
            people.append(land(pill(PX, ys[k] + 58, sl["roles"][k], "var(--dim)", ctx, 15, 150, "case role"), .75 + k * .08, .4, 8))
    people = "".join(people)

    def ring_p(k, a, b, col="var(--c4)"):
        return f'<circle cx="{PX}" cy="{ys[k]}" r="{PR + 3}" fill="none" stroke="{col}" stroke-width="2.5" opacity="0">{_n07_win(a, b, .12)}</circle>'

    def ping_p(k, at, col="var(--c4)"):
        return _n07_ping(PX, ys[k], PR + 3, PR + 26, at, col, 2)

    # agents: a tile with its spark, its name, its row of faces (who uses it) and, when restricted, the lock
    def face(j, n, k, at=None):
        x, y = AX - AW / 2 + 22 + 13 * n, sy[j] + 23
        dot = f'<circle cx="{x}" cy="{y}" r="8" fill="{_Q09_JACKET[k]}" stroke="var(--dim)" stroke-width="2"/>'
        return dot if at is None else f'<g opacity="0">{_n07_hold(at, .12)}{dot}</g>' + _n07_ping(x, y, 8, 20, at, "var(--c4)", 1.5, .45)

    def tile(j, faces=""):
        x, y = AX - AW / 2, sy[j] - AH / 2
        return (card(x, y, AW, AH, "var(--dim)", "var(--accent)", 14, 1.4)
                + f'<rect x="{x + 54}" y="{sy[j] - 17}" width="50" height="6" rx="3" fill="var(--c2)" opacity=".7"/>'
                + f'<rect x="{x + 54}" y="{sy[j] - 5}" width="34" height="6" rx="3" fill="var(--c2)" opacity=".45"/>' + faces)

    def spark_a(j, born=None):
        x, y = AX - AW / 2 + 30, sy[j] - 9
        s = spark(0, 0, .72, "var(--accent)")
        if born is not None:
            s = f'<g>{_n07_tr([(born - .05, "0"), (born + .15, "1.35"), (born + .35, "1"), (R[0], "1"), (R[1], "0")], "scale")}{s}</g>'
        return f'<g transform="translate({x} {y})">{s}</g>'

    def slot(j, born):
        """The empty slot where an agent is about to be created; it traces into a tile at `born`."""
        x, y = AX - AW / 2, sy[j] - AH / 2
        empty = (f'<g>{_n07_key("opacity", [(born - .25, 1), (born - .1, 0), (R[1], 0), (R[1] + .1, 1)])}'
                 f'<rect x="{x}" y="{y}" width="{AW}" height="{AH}" rx="14" fill="none" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="5 7" opacity=".7"/>'
                 f'<path d="M{AX - 9} {sy[j]} H{AX + 9} M{AX} {sy[j] - 9} V{sy[j] + 9}" stroke="var(--c2)" stroke-width="1.8" stroke-linecap="round"/></g>')
        outline = (f'<rect x="{x}" y="{y}" width="{AW}" height="{AH}" rx="14" fill="none" stroke="var(--c4)" stroke-width="2" pathLength="1" '
                   f'stroke-dasharray="1" stroke-dashoffset="1" opacity="0">{_n07_key("stroke-dashoffset", [(born - .3, 1), (born, 0)])}{_n07_win(born - .3, born + .6, .1)}</rect>')
        return empty + outline

    ring_a = lambda j, a, b, col="var(--c4)": (f'<rect x="{AX - AW / 2 - 4}" y="{sy[j] - AH / 2 - 4}" width="{AW + 8}" height="{AH + 8}" rx="17" fill="none" '
                                                f'stroke="{col}" stroke-width="2.5" opacity="0">{_n07_win(a, b, .12)}</rect>')

    a1 = tile(0, face(0, 0, 0) + face(0, 1, 1)) + spark_a(0)
    a2 = (slot(1, A2_BORN)
          + f'<g opacity="0">{_n07_hold(A2_BORN - .1, .15)}{tile(1, face(1, 0, 2, A2_BORN + .15) + "".join(face(1, n + 1, k, t + .4) for n, (k, t) in enumerate(SHARE)))}</g>'
          + spark_a(1, A2_BORN) + _n07_ping(AX - AW / 2 + 30, sy[1] - 9, 12, 34, CONNECT + .9, "var(--c4)"))
    lock_at = (AX + AW / 2 - 17, sy[2] - AH / 2 + 22)
    a3 = (slot(2, A3_BORN)
          + f'<g opacity="0">{_n07_hold(A3_BORN - .1, .15)}{tile(2, face(2, 0, 3, A3_BORN + .15) + face(2, 1, 2, SHARE3 + .35))}</g>'
          + spark_a(2, A3_BORN)
          + f'<g opacity="0">{_n07_hold(LOCKED, .1)}{_lock(*lock_at)}</g>' + _n07_ping(lock_at[0], lock_at[1] + 4, 10, 26, LOCKED, "var(--accent)"))

    # knowledge: four sources that stay where they are; the fourth is restricted (its lock)
    srcs = []
    for i, y in enumerate(ys):
        restricted = i == 3
        x0 = KX - KW / 2
        s = (card(x0, y - KH / 2, KW, KH, "var(--card)", "var(--accent)" if restricted else "var(--c1)", 12, 1.3)
             + f'<g transform="translate({x0 + 30} {y})">{_q09_glyph(i)}</g>'
             + f'<rect x="{x0 + 54}" y="{y - 8}" width="{26 if restricted else 42}" height="5" rx="2.5" fill="var(--c2)" opacity=".6"/>'
             + f'<rect x="{x0 + 54}" y="{y + 3}" width="{18 if restricted else 30}" height="5" rx="2.5" fill="var(--c2)" opacity=".4"/>'
             + (_lock(x0 + KW - 17, y - KH / 2 + 22) if restricted else ""))
        srcs.append(s)
    ring_k = lambda i, a, b, col="var(--c4)": (f'<rect x="{KX - KW / 2 - 4}" y="{ys[i] - KH / 2 - 4}" width="{KW + 8}" height="{KH + 8}" rx="15" fill="none" '
                                                f'stroke="{col}" stroke-width="2.5" opacity="0">{_n07_win(a, b, .12)}</rect>')

    # the beats: rings, pings and tokens
    fx = []
    # 1 · a colleague creates an agent
    fx += [ring_p(2, P3_ON, A2_BORN + .5), ping_p(2, P3_ON), _q09_run(_q09_pa(2, 1), P3_ON + .15, P3_ON + .6)]
    # 2 · it connects to two sources: the knowledge stays in place, only its signal travels
    fx += [ring_k(i, CONNECT, CONNECT + 1.1) for i in (1, 2)]
    fx += [_q09_run(_q09_ak(1, i), CONNECT + .45, CONNECT + .9, True) for i in (1, 2)]
    # 3 · she shares it: each colleague joins its row of faces
    for k, t in SHARE:
        fx += [_q09_run(_q09_pa(k, 1), t, t + .4, True), ping_p(k, t + .4)]
    # 4 · one of them asks; the agent reads its sources and answers with the source
    fx += [ring_p(0, ASK - .1, ANSWER + .7), _q09_run(_q09_pa(0, 1), ASK, ASK + .4), ring_a(1, ASK + .4, ANSWER + .2)]
    fx += [_q09_run(_q09_ak(1, i), ASK + .45, ASK + .75) for i in (1, 2)] + [_q09_run(_q09_ak(1, i), ASK + .8, ANSWER - .05, True) for i in (1, 2)]
    fx += [_n07_ping(KX - KW / 2, ys[i], 5, 22, ASK + .75) for i in (1, 2)]
    fx += [_q09_run(_q09_pa(0, 1), ANSWER, ANSWER + .45, True, _q09_doc()), _n07_badge(PX + PR * .74, ys[0] + PR * .74, ANSWER + .45, ok, 11),
           ping_p(0, ANSWER + .45, ok)]
    # 5 · another colleague creates his own over the restricted source: it inherits the lock; only who has access joins it
    fx += [ring_p(3, P4_ON, A3_BORN + .5), ping_p(3, P4_ON), _q09_run(_q09_pa(3, 2), P4_ON + .1, P4_ON + .5)]
    fx += [ring_k(3, A3_BORN + .35, LOCKED + .3, "var(--accent)"), _q09_run(_q09_ak(2, 3), A3_BORN + .7, LOCKED - .05, True)]
    fx += [_q09_run(_q09_pa(2, 2), SHARE3, SHARE3 + .35, True), ping_p(2, SHARE3 + .35)]

    # the seal: our partnership, said as ours
    seal = pill(AX, 784, sl["badge"], "var(--c4)", ctx, 17, 560, "case badge")
    sw = min(560, bold_width(_(str(sl["badge"])), fit(sl["badge"], 17, 524, "case badge"), current_factor()) + 36)
    shine = (f'<rect x="{AX - sw / 2 - 5}" y="{784 - 23.5}" width="{sw + 10}" height="47" rx="23.5" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">'
             f'{_n07_win(SEAL, SEAL + .6, .15)}</rect>')

    g += [land(heads, .1, .45, 8), land("".join(links), 1.0, .5, 0), people, seq([a1, a2, a3], .55, .45, 12, 1.4),
          seq(srcs, .7, .45, 12, 1.6), "".join(fx), land(seal, 1.35, .45, 12), shine]
    return "".join(g), D, FREEZE
