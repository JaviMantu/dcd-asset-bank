"""Architecture scenes (0.5.0) for the «arquitectura» deck type and any technical deck: C4 levels C1-C4, solution
layers, a generic component diagram, data architecture, infrastructure and environments, decisions (ADR), risks and
trade-offs, plus the cover, the quality drivers and the roadmap of an architecture deck. Every scene is args-driven
(references/architecture.md has one JSON example per scene), lays its nodes out by itself so they never overlap, and is
portrait-aware: it draws on CANVAS() inside ART_ZONE(layout) and returns portrait_mark(svg), top-to-bottom when the zone
is not wide, with labels 1.3x larger in portrait (the phone stage is read smaller). Runs in the shared namespace of
module/ext.py (lib.py and icons.py before it).

The 12-second story is the same idea everywhere: a request travels along the edges in the order they are given and
each node lights when it is reached; everything is lit and still at 10.8 s (the reduced-motion frame). Labels are
painted last, over plates, never over a glow.

- arq_hero / arq-hero                the system at the centre, its people on one side and its systems on the other
- arq_drivers / quality-drivers      the quality attributes that drive the design, each with its target
- arq_c4_context / c4-context        C1: people, the system, external systems and labelled relations
- arq_c4_container / c4-container    C2: containers with their technology inside the system boundary
- arq_c4_component / c4-component    C3: components inside one container, with its neighbours outside
- arq_c4_code / c4-code              C4: classes or modules (view "code"), or a deployment view (view "deployment")
- arq_layers / solution-layers       channels -> experience -> services -> data -> platform, cross-cutting pillars
- arq_components / component-diagram generic boxes with ports and labelled edges
- arq_data / data-architecture       sources -> ingest -> store -> serve -> consume beside a governance band
- arq_infra / infra-topology         entry, region, security zones with nodes, and the dev -> qa -> prod promotion
- arq_adr / adr-decisions            decision cards: context, decision, consequence, status
- arq_risks / risks-tradeoffs        a probability x impact matrix; each risk moves to its residual cell
- arq_roadmap / arq-roadmap          the phases, the next step highlighted, the signature of the close
"""
from aula.i18n import overflow as _arq_overflow
from aula.svg import TEXT_TOKENS as _ARQ_TT, is_themed as _arq_themed

_ARQ_LIT = "var(--c4)"
_ARQ_MIX = {"person": 72, "system": 50, "container": 30, "component": 14}      # % of c1 in the fill: C4 dark -> light
_ARQ_FAMILY = {"person": "person", "system": "system", "component": "component", "class": "component",
               "module": "component", "external": "external", "db": "db", "queue": "queue"}   # else: a container
_ARQ_ICON = {"person": "persona", "system": "sistema", "external": "externo", "container": "contenedor",
             "web": "contenedor", "app": "contenedor", "api": "api", "component": "componente", "class": "componente",
             "module": "componente", "db": "base-datos", "queue": "cola", "storage": "almacenamiento", "lake": "lago",
             "pipeline": "pipeline", "server": "servidor", "network": "red", "cloud": "nube", "security": "seguridad",
             "monitor": "monitoreo"}
_ARQ_TYPE = {"person": "Persona", "system": "Sistema", "container": "Contenedor", "component": "Componente",
             "external": "Sistema externo", "db": "Base de datos", "queue": "Cola de mensajes", "boundary": "Límite"}


def _arq_k():
    """The label scale: 1.3 on the portrait stage, 1 on the desktop one."""
    return 1.3 if ORIENT() == "portrait" else 1.0


def _k(size):
    return round(size * _arq_k())


def _arq_fam(kind):
    return _ARQ_FAMILY.get(kind, "container")


# ---------------------------------------------------------------- text: wrapped to a width, never under 15 px (20 portrait)
def _arq_wrap(s, room, size, bold=True):
    out, cur, f = [], "", current_factor()
    for w in _(str(s)).split():
        t = f"{cur} {w}".strip()
        if cur and bold_width(t, size, f, bold) > room:
            out.append(cur)
            cur = w
        else:
            cur = t
    return out + [cur]


def _arq_fit(s, room, size, maxl, where, bold=True, clip=False):
    """(lines, size): s in at most maxl lines of room units, at size (x the label scale) or smaller, down to the floor.
    A label that does not fit is recorded for the build's gate (named, with its box), unless clip: then its last line
    ends in «…»."""
    size, floor = _k(size), _k(15)
    for z in range(size, floor - 1, -1):
        L = _arq_wrap(s, room, z, bold)
        if len(L) <= maxl and all(bold_width(x, z, current_factor(), bold) <= room for x in L):
            if len(L) == 2:                                             # two lines: the split that balances them
                ws = (L[0] + " " + L[1]).split()
                L = min(([" ".join(ws[:i]), " ".join(ws[i:])] for i in range(1, len(ws))),
                        key=lambda t: max(bold_width(x, z, current_factor(), bold) for x in t))
            return L, z
    L = _arq_wrap(s, room, floor, bold)
    if clip:
        L = L[:maxl]
        while L[-1] and bold_width(L[-1] + "…", floor, current_factor(), bold) > room:
            L[-1] = L[-1].rsplit(" ", 1)[0] if " " in L[-1] else L[-1][:-1]
        return L[:-1] + [L[-1].rstrip(",;:·") + "…"], floor
    _arq_overflow(f"label «{_(str(s))}» overflows its {where} ({room:.0f} units, {maxl} lines) even at size {floor}")
    return L, floor


def _arq_tl(x, y, lines, size, fill="var(--white)", bold=True, anchor="start", lh=1.22, extra=""):
    """Lines already in the current language (and size already scaled), as one <text> with tspans."""
    fill = _ARQ_TT.get(fill, fill) if _arq_themed() else fill
    sp = E(lines[0]) if len(lines) == 1 else "".join(
        f'<tspan x="{x:.1f}" dy="{0 if i == 0 else round(size * lh, 1)}">{E(t)}</tspan>' for i, t in enumerate(lines))
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"'
            f'{" " + W6 if bold else ""} {extra}>{sp}</text>')


def _arq_text(x, y, s, room, size, fill="var(--white)", where="label", maxl=2, bold=True, anchor="start", clip=False, mid=None):
    """(markup, height) of s wrapped in room: the top of the first line at y, or the block centred on mid."""
    L, z = _arq_fit(s, room, size, maxl, where, bold, clip)
    h = len(L) * z * 1.22
    top = mid - h / 2 + z * .1 if mid is not None else y
    return _arq_tl(x, top + z * .92, L, z, fill, bold, anchor), h


def _arq_line(x, y, s, size, fill="var(--muted)", bold=False, anchor="start"):
    """One short label (a legend entry, a tick, a number): scaled, never wrapped."""
    return _arq_tl(x, y, [_(str(s))], _k(size), fill, bold, anchor)


def _arq_w(s, size, bold=True):
    return bold_width(_(str(s)), _k(size), current_factor(), bold)


def _arq_plate(cx, cy, s, size=15, fill="var(--muted)", bold=False):
    """(plate, text): one line on a card-coloured plate centred at (cx, cy), so any line behind it stays behind."""
    w = _arq_w(s, size, bold) + 18 * _arq_k()
    h = _k(size) * 1.3 + 8
    return (f'<rect x="{cx - w / 2:.1f}" y="{cy - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="7" fill="var(--card)" '
            f'stroke="var(--line)" stroke-width="1"/>',
            _arq_tl(cx, cy + _k(size) * .36, [_(str(s))], _k(size), fill, bold, "middle"))


# ---------------------------------------------------------------- timing
def _arq_on(t, off=.97):
    """Opacity: 0 until t, 1 until the loop resets (so the 10.8 s frame shows it)."""
    return beat("opacity", [(0, 0), (t, 0), (t + .012, 1), (off, 1), (off + .015, 0), (1, 0)])


def _arq_win(a, b):
    """Opacity: 1 only between a and b (a traveller)."""
    return beat("opacity", [(0, 0), (a, 0), (a + .006, 1), (b, 1), (b + .006, 0), (1, 0)])


def _arq_dot(path, a, b, color=_ARQ_LIT, r=7, ref=""):
    """A request travelling along path (or along the path whose id is ref) between a and b, hidden otherwise."""
    mv = (move(path, [(0, 0), (a, 0), (b, 1), (1, 1)], D) if not ref else
          f'<animateMotion dur="{D}s" repeatCount="indefinite" keyTimes="0;{a:.3f};{b:.3f};1" keyPoints="0;0;1;1" '
          f'calcMode="linear"><mpath href="#{ref}"/></animateMotion>')
    return (f'<g opacity="0">{_arq_win(a, b)}{mv}'
            f'<circle r="{r * 2.2:.1f}" fill="{color}" opacity=".22"/><circle r="{r:.1f}" fill="{color}"/></g>')


_ARQ_IDS = [0]


def _arq_id():
    """A page-unique id for a path the travellers ride (every scene of a build runs in one process)."""
    _ARQ_IDS[0] += 1
    return f"arq{_ARQ_IDS[0]}"


def _arq_draw(path, t0, t1, color=_ARQ_LIT, width=2.2):
    """A lit copy of path that draws between t0 and t1 and stays drawn until the loop resets."""
    return (f'<path d="{path}" pathLength="1" stroke-dasharray="1" fill="none" stroke="{color}" stroke-width="{width}" '
            f'stroke-linecap="round" opacity=".9">'
            f'{beat("stroke-dashoffset", [(0, 1), (t0, 1), (t1, 0), (.97, 0), (.985, 1), (1, 1)])}</path>')


def _arq_ring(x, y, w, h, t, r=14, color=_ARQ_LIT):
    """The lit outline of a box (lights at t)."""
    return (f'<rect x="{x - 4:.1f}" y="{y - 4:.1f}" width="{w + 8:.1f}" height="{h + 8:.1f}" rx="{r}" fill="none" '
            f'stroke="{color}" stroke-width="1.8" opacity="0">'
            f'{beat("opacity", [(0, 0), (t, 0), (t + .012, .85), (.97, .85), (.985, 0), (1, 0)])}</rect>')


def _arq_ok(x, y, t, s=.5):
    ok = "var(--okc)" if _arq_themed() else "#19C29B"
    return f'<g opacity="0">{_arq_on(t)}{check(x, y, s * _arq_k(), ok)}</g>'


# ---------------------------------------------------------------- args: lists (documented order) or dicts
def _arq_items(items, fields, kind="container", **extra):
    out = []
    for it in items or []:
        d = dict(it) if isinstance(it, dict) else dict(zip(fields, it if isinstance(it, (list, tuple)) else [it]))
        d["id"] = str(d.get("id") or d.get("name"))
        d["name"] = d.get("name") or d["id"]
        d["kind"] = d.get("kind") or kind
        d.update({k: v for k, v in extra.items() if d.get(k) is None})
        out.append(d)
    return out


def _arq_rels(rels, nodes):
    """[(from id, to id, label)] from [from, to, label, tech?]: a node is named by its id or its name."""
    key = {**{n["name"]: n["id"] for n in nodes}, **{n["id"]: n["id"] for n in nodes}}
    out = []
    for r in rels or []:
        r = [r.get(k, "") for k in ("from", "to", "label", "tech")] if isinstance(r, dict) else list(r) + ["", ""]
        a, b = key.get(str(r[0])), key.get(str(r[1]))
        if a is None or b is None:
            raise SystemExit(f"architecture scene: relation {r[0]!r} -> {r[1]!r} names a node that is not drawn "
                             f"(ids: {', '.join(n['id'] for n in nodes)})")
        out.append((a, b, str(r[2] or "") + (f" [{r[3]}]" if r[3] else "")))
    return out


def _arq_depth(nodes, rels, cap=3):
    """Longest-path rank of each node among nodes (relations inside the set), capped: {id: 0..cap-1}; a node's tier
    (an int) fixes its own."""
    ids = {n["id"] for n in nodes}
    rk = {i: 0 for i in ids}
    for _k2 in range(len(ids)):
        for a, b, _l in rels:
            if a in ids and b in ids and a != b and rk[b] <= rk[a]:
                rk[b] = min(rk[a] + 1, cap - 1)
    return {n["id"]: int(n["tier"]) if str(n.get("tier", "")).lstrip("-").isdigit() else rk[n["id"]] for n in nodes}


def _arq_zone(sl):
    """(x, y, w, h, wide): the art zone of the slide's layout, kept clear of the footer (and of the source line on the
    phone stage); wide lays out left-to-right, else top-to-bottom."""
    x, y, w, h = ART_ZONE(sl.get("layout", "left"))
    h = min(h, (1490 if ORIENT() == "portrait" else 830) - y)
    return x, y, w, h, w >= 1.3 * h


def _arq_type(kind, legend):
    fam = _arq_fam(kind)
    return (legend or {}).get(fam, _ARQ_TYPE.get(fam, _ARQ_TYPE["container"]))


# ---------------------------------------------------------------- C4 shapes
def _arq_paint(kind):
    fam = _arq_fam(kind)
    if fam == "external":
        return "var(--card)", "var(--muted)", ' stroke-dasharray="7 5"'
    return f"color-mix(in srgb, var(--c1) {_ARQ_MIX.get(fam, 30)}%, var(--card))", "var(--c2)", ""


def _arq_head(kind):
    """Room a shape takes above its text: the person's head, the cylinder's lid."""
    return {"person": 30, "db": 16}.get(kind, 0) * _arq_k()


def _arq_shape(kind, x, y, w, h):
    """(markup, top of the text area) of a C4 element: person, cylinder (db), pipe (queue), box."""
    fill, stroke, dash = _arq_paint(kind)
    a = f'fill="{fill}" stroke="{stroke}" stroke-width="1.6"{dash}'
    if kind == "person":
        r = min(16 * _arq_k(), h * .16)
        return (f'<rect x="{x:.1f}" y="{y + r * 1.3:.1f}" width="{w:.1f}" height="{h - r * 1.3:.1f}" rx="20" {a}/>'
                f'<circle cx="{x + w / 2:.1f}" cy="{y + r:.1f}" r="{r:.1f}" {a}/>', y + r * 1.9)
    if kind == "db":
        e = 8 * _arq_k()
        return (f'<path d="M{x:.1f} {y + e:.1f} V{y + h - e:.1f} A{w / 2:.1f} {e:.1f} 0 0 0 {x + w:.1f} {y + h - e:.1f} '
                f'V{y + e:.1f}" {a}/><ellipse cx="{x + w / 2:.1f}" cy="{y + e:.1f}" rx="{w / 2:.1f}" ry="{e:.1f}" {a}/>', y + 2 * e)
    if kind == "queue":
        e = min(12, w * .07)
        return (f'<path d="M{x + e:.1f} {y:.1f} H{x + w - e:.1f} A{e:.1f} {h / 2:.1f} 0 0 1 {x + w - e:.1f} {y + h:.1f} '
                f'H{x + e:.1f} A{e:.1f} {h / 2:.1f} 0 0 1 {x + e:.1f} {y:.1f} Z" {a}/>'
                f'<ellipse cx="{x + w - e:.1f}" cy="{y + h / 2:.1f}" rx="{e:.1f}" ry="{h / 2:.1f}" {a}/>', y)
    if kind == "class":
        return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="8" {a}/>', y
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="12" {a}/>', y


def _arq_tech(n, legend, notation, room):
    """The C4 notation line: «[Type: tech]», else «[tech]» when that does not fit, else «[Type]»."""
    kind_label = _arq_type(n["kind"], legend) if notation else ""
    tech = n.get("tech") or ""
    opts = ([f"[{kind_label}: {tech}]", f"[{tech}]"] if kind_label and tech else
            [f"[{kind_label}]"] if kind_label else [tech] if tech else [])
    for o in opts:
        if _arq_w(o, 15, False) <= room:
            return o
    return opts[-1] if opts else ""


def _arq_need(n, w, legend, notation):
    """The height a node needs to show all its texts at width w."""
    k, pad, lh = _arq_k(), 12, _k(15) * 1.22
    if n["kind"] == "class":
        st = lh if n.get("stereotype") else 0
        return 9 + st + _k(18) * 1.22 + 12 + len(n.get("members") or []) * lh + 12
    right = w - 2 * pad - (14 if n["kind"] == "queue" else 0)
    L, z = _arq_fit(n["name"], right - 30 * k, 18, 2, "node name")
    h = _arq_head(n["kind"]) + 9 + max(len(L) * z * 1.22, 24 * k) + 2
    if _arq_tech(n, legend, notation, right):
        h += lh + 2
    if n.get("desc"):
        h += min(3, len(_arq_wrap(n["desc"], right, _k(15), False))) * lh
    return h + 12


def _arq_label(n, x, y, w, h, top, legend=None, notation=True):
    """The texts of a node, left-aligned: icon + name, «[Type: tech]», then its description while there is room."""
    k, kind, pad = _arq_k(), n["kind"], 12
    right = w - 2 * pad - (14 if kind == "queue" else 0)
    fam = _arq_fam(kind)
    muted, lh = "var(--muted)", _k(15) * 1.22
    g, yy, bottom = [], top + 9, y + h - 8
    if kind == "class":
        if n.get("stereotype"):
            m, dh = _arq_text(x + w / 2, yy, f"«{n['stereotype']}»", w - 2 * pad, 15, muted, "class stereotype", 1, False, "middle")
            g.append(m)
            yy += dh
        m, dh = _arq_text(x + w / 2, yy, n["name"], w - 2 * pad, 18, "var(--white)", "class name", 1, True, "middle")
        g.append(m)
        yy += dh + 6
        g.append(f'<path d="M{x:.1f} {yy:.1f} H{x + w:.1f}" stroke="var(--c2)" stroke-width="1.2" opacity=".7"/>')
        yy += 6
        for mem in n.get("members") or []:
            if yy + lh > bottom + 2:
                break
            m, dh = _arq_text(x + pad, yy, mem, w - 2 * pad, 15, muted, "class member", 1, False, clip=True)
            g.append(m)
            yy += dh
        return "".join(g)
    g.append(icon(f"arquitectura/{_ARQ_ICON.get(kind, 'contenedor')}", x + pad + 11 * k, yy + 11 * k, 24 * k,
                  "var(--c2)" if fam != "external" else muted))
    m, dh = _arq_text(x + pad + 30 * k, yy, n["name"], right - 30 * k, 18, "var(--white)", "node name", 2)
    g.append(m)
    yy += max(dh, 24 * k) + 2
    line = _arq_tech(n, legend, notation, right)
    if line and yy + lh <= bottom + 2:
        g.append(_arq_text(x + pad, yy, line, right, 15, muted, "node technology", 1, False, clip=True)[0])
        yy += lh + 2
    room = int((bottom + 2 - yy) // lh)
    if n.get("desc") and room >= 1:
        g.append(_arq_text(x + pad, yy, n["desc"], right, 15, muted, "node description", min(room, 3), False, clip=True)[0])
    return "".join(g)


def _arq_legend(kinds, x, y, w, legend=None, boundary=False):
    """(shapes, labels, height) of the C4 legend: one row, two when it does not fit, top at y."""
    k = _arq_k()
    fams = {_arq_fam(kd) for kd in kinds}
    items = [f for f in ("person", "system", "container", "component", "db", "queue", "external") if f in fams]
    items += ["boundary"] if boundary else []
    labs = [(legend or {}).get(f, _ARQ_TYPE[f]) for f in items]
    ws = [(30 + 22) * k + _arq_w(t, 15, False) for t in labs]
    rows = [[]]
    for j, ww in enumerate(ws):
        if rows[-1] and sum(ws[i] for i in rows[-1]) + ww > w:
            rows.append([])
        rows[-1].append(j)
    rh = 26 * k
    sh, tx = [], []
    for r, row in enumerate(rows):
        cx = x + (w - sum(ws[j] for j in row)) / 2
        yy = y + r * rh
        s = 20 * k
        for j in row:
            f = items[j]
            if f == "boundary":
                sh.append(f'<rect x="{cx:.1f}" y="{yy + 2:.1f}" width="{s:.1f}" height="{s * .8:.1f}" rx="4" fill="none" '
                          f'stroke="var(--c2)" stroke-width="1.4" stroke-dasharray="4 3"/>')
            elif f in ("db", "queue", "person"):
                sh.append(_arq_shape(f, cx, yy - (2 if f == "person" else 0), s, s * (1.1 if f == "person" else .9))[0])
            else:
                fill, stroke, dash = _arq_paint(f)
                sh.append(f'<rect x="{cx:.1f}" y="{yy + 2:.1f}" width="{s:.1f}" height="{s * .8:.1f}" rx="4" fill="{fill}" '
                          f'stroke="{stroke}" stroke-width="1.4"{dash}/>')
            tx.append(_arq_line(cx + 28 * k, yy + 15 * k, labs[j], 15))
            cx += ws[j]
    return "".join(sh), "".join(tx), len(rows) * rh


# ---------------------------------------------------------------- the layered auto-layout (C4, components, code)
def _arq_graph(nodes, rels, zone, wide, boundary=None, legend=None, notation=True, ports=False, legend_on=True):
    """Lay nodes out by rank (n["rank"]; rows top-to-bottom, or columns left-to-right when wide), order each rank by
    barycentre, size the boxes to their texts, route every relation (adjacent ranks: a curve; same rank: a dip into the
    free space beside the rank; skipping ranks: a side channel), spread the relation labels inside their gap so plates
    never overlap, and animate a request along the relations in order. Returns (svg, {id: (x, y, w, h)})."""
    k = _arq_k()
    zx, zy, zw, zh = zone
    tb = not wide
    kinds = {n["kind"] for n in nodes}
    idx = {n["id"]: n for n in nodes}
    inside = [n for n in nodes if n.get("inside")]
    hb = bool(boundary and inside)
    leg_h = _arq_legend(kinds, zx, 0, zw, legend, hb)[2] + 14 if legend_on else 0
    rs = sorted({n["rank"] for n in nodes})
    for n in nodes:
        n["r"] = rs.index(n["rank"])
    R = len(rs)
    by = [[n for n in nodes if n["r"] == r] for r in range(R)]
    nb = {n["id"]: [] for n in nodes}
    for a, b, _l in rels:
        nb[a].append(b)
        nb[b].append(a)
    for sweep, ref_of in ((range(1, R), -1), (range(R - 2, -1, -1), 1)):   # barycentre ordering, down then up
        for r in sweep:
            pos = {n["id"]: (j + .5) / len(by[r + ref_of]) for j, n in enumerate(by[r + ref_of])}
            cur = {n["id"]: (j + .5) / len(by[r]) for j, n in enumerate(by[r])}

            def bary(n, pos=pos, cur=cur):
                v = [pos[m] for m in nb[n["id"]] if m in pos]
                return sum(v) / len(v) if v else cur[n["id"]]
            by[r].sort(key=bary)
    ir = [n["r"] for n in inside] if hb else []
    ir0, ir1 = (min(ir), max(ir)) if hb else (-1, -1)
    U = (zh - leg_h) if tb else zw
    V = zw if tb else zh - leg_h
    u0, v0 = (zy, zx) if tb else (zx, zy)
    skip = any(abs(idx[a]["r"] - idx[b]["r"]) > 1 for a, b, _l in rels)
    chan = 26 if skip else 0
    pa, pb = ((34 * k, 14) if tb else (16, 16)) if hb else (0, 0)
    vtop = 34 * k if hb and not tb else 0
    gmin, gmax = ((62 * k, 150) if tb else (150, 250))
    Va = V - 2 * chan - vtop
    gv = 22 if tb else 18
    b = min(250 * k if tb else 118 * k, min((Va - (len(rr) - 1) * gv) / len(rr) for rr in by))
    room_d = max(56, (U - pa - pb - (R - 1) * gmin) / R)
    if tb:                                                              # boxes as tall as their texts need
        d = min(room_d, max(max((_arq_need(n, b, legend, notation) for n in nodes), default=80), 72 * k))
    else:
        d = min(room_d, 210)
    g = min(gmax, (U - pa - pb - R * d) / (R - 1)) if R > 1 else 0
    u = u0 + (U - (R * d + (R - 1) * g + pa + pb)) / 2
    up = []
    for r in range(R):
        u += pa if r == ir0 else 0
        up.append(u)
        u += d + (pb if r == ir1 else 0) + g
    for r, rr in enumerate(by):
        slot = Va / len(rr)
        for j, n in enumerate(rr):
            n["u"], n["v"] = up[r], v0 + chan + vtop + slot * (j + .5) - b / 2
    below = (u0 + U) - (up[-1] + d)                                     # free space after the last rank

    def P(uu, vv):
        return f"{vv:.1f} {uu:.1f}" if tb else f"{uu:.1f} {vv:.1f}"

    def box(n):
        return (n["v"], n["u"], b, d) if tb else (n["u"], n["v"], d, b)

    def dips_down(r):
        return r < R - 1 or below >= 50

    # ports: each side of a node spreads its relations by the other end's position
    side = {}
    for e, (a, bb, _l) in enumerate(rels):
        s, t = idx[a], idx[bb]
        dr = t["r"] - s["r"]
        ss, ts = (("far", "near") if dr > 0 else ("near", "far") if dr < 0 else
                  ("far", "far") if dips_down(s["r"]) else ("near", "near"))
        side.setdefault((a, ss), []).append((e, t["v"], "s"))
        side.setdefault((bb, ts), []).append((e, s["v"], "t"))
    port, pside = {}, {}
    for (nid, sd), lst in side.items():
        lst.sort(key=lambda q: q[1])
        for i, (e, _v, role) in enumerate(lst):
            port[(e, role)] = idx[nid]["v"] + b * (i + 1) / (len(lst) + 1)
            pside[(e, role)] = sd
    # routes and label anchors (u, v, gap)
    routes = []
    for e, (a, bb, lab) in enumerate(rels):
        s, t = idx[a], idx[bb]
        dr, sv, tv = t["r"] - s["r"], port[(e, "s")], port[(e, "t")]
        if abs(dr) == 1:
            su, tu = (s["u"] + d, t["u"]) if dr > 0 else (s["u"], t["u"] + d)
            mu = (su + tu) / 2
            routes.append((f"M{P(su, sv)} C{P(mu, sv)} {P(mu, tv)} {P(tu, tv)}", mu, (sv + tv) / 2, min(s["r"], t["r"])))
        elif dr == 0:
            down = dips_down(s["r"])
            su = s["u"] + d if down else s["u"]
            depth = ((g if s["r"] < R - 1 else min(below, 120)) * .5) if down else -g * .5
            routes.append((f"M{P(su, sv)} C{P(su + depth, sv)} {P(su + depth, tv)} {P(su, tv)}", su + depth * .75,
                           (sv + tv) / 2, s["r"] if down else s["r"] - 1))
        else:
            fw = dr > 0
            su, tu = (s["u"] + d, t["u"]) if fw else (s["u"], t["u"] + d)
            u1, u2 = (su + g / 2, tu - g / 2) if fw else (su - g / 2, tu + g / 2)
            vc = v0 + chan / 2 if (sv + tv) / 2 < v0 + V / 2 else v0 + V - chan / 2
            routes.append((f"M{P(su, sv)} L{P(u1, sv)} L{P(u1, vc)} L{P(u2, vc)} L{P(u2, tv)} L{P(tu, tv)}", u1,
                           (sv + vc) / 2, s["r"] if fw else s["r"] - 1))
    # plates: sized, then spread along v inside their gap (staggered across it when still crowded)
    plates = []
    for e, (p, mu, mv, gap) in enumerate(routes):
        lab = rels[e][2]
        if not lab:
            plates.append(None)
            continue
        room = 200 * k if tb else max(110, min(200, g - 20))
        L, z = _arq_fit(lab, room, 15, 2 if tb else 3, "relation label", False)
        plates.append({"L": L, "z": z, "w": max(bold_width(x, z, current_factor(), False) for x in L) + 16,
                       "h": len(L) * z * 1.22 + 9, "u": mu, "v": mv, "gap": gap})
    half = (lambda p: p["w"] / 2) if tb else (lambda p: p["h"] / 2)
    for gap in {p["gap"] for p in plates if p}:
        row = sorted((p for p in plates if p and p["gap"] == gap), key=lambda p: p["v"])
        for i in range(1, len(row)):
            row[i]["v"] = max(row[i]["v"], row[i - 1]["v"] + half(row[i - 1]) + half(row[i]) + 6)
        hi = v0 + V - 4
        if row and row[-1]["v"] + half(row[-1]) > hi:
            row[-1]["v"] = hi - half(row[-1])
            for i in range(len(row) - 2, -1, -1):
                row[i]["v"] = min(row[i]["v"], row[i + 1]["v"] - half(row[i + 1]) - half(row[i]) - 6)
        for i in range(1, len(row)):
            if row[i]["v"] - half(row[i]) < row[i - 1]["v"] + half(row[i - 1]):
                dep = (row[i]["h"] if tb else row[i]["w"]) / 2 + 3
                row[i - 1]["u"] -= dep
                row[i]["u"] += dep
    # the story: a request along the relations in order; a node lights when reached
    step = .7 / max(1, len(rels))
    lit = {}
    for e, (a, bb, _l) in enumerate(rels):
        t0 = .07 + e * step
        lit.setdefault(a, t0)
        lit.setdefault(bb, t0 + step * .8)
    base, over, dots, labels, pl, pt = [], [], [], [], [], []
    for e, (p, *_r) in enumerate(routes):
        t0 = .07 + e * step
        pid = _arq_id()
        base.append(trace(p, "var(--c2)", 1.6, .3, .8, f'id="{pid}" opacity=".75" marker-end="url(#arrow)"'))
        over.append(_arq_draw(p, t0, t0 + step * .8))
        dots.append(_arq_dot(p, t0, t0 + step * .8, r=7 * k, ref=pid))
        pp = plates[e]
        if pp:
            cx, cy = (pp["v"], pp["u"]) if tb else (pp["u"], pp["v"])
            pl.append(f'<rect x="{cx - pp["w"] / 2:.1f}" y="{cy - pp["h"] / 2:.1f}" width="{pp["w"]:.1f}" height="{pp["h"]:.1f}" '
                      f'rx="7" fill="var(--card)" stroke="var(--line)" stroke-width="1"/>')
            pt.append(_arq_tl(cx, cy - pp["h"] / 2 + 4.5 + pp["z"] * .92, pp["L"], pp["z"], "var(--muted)", False, "middle"))
    rects, shapes = {}, [""] * R                                        # one entrance per rank keeps the scene light
    for n in nodes:
        x, y, w, h = box(n)
        rects[n["id"]] = (x, y, w, h)
        m, top = _arq_shape(n["kind"], x, y, w, h)
        if ports:
            for (e, role), pv in port.items():
                if rels[e][0 if role == "s" else 1] != n["id"]:
                    continue
                pu = n["u"] + (d if pside[(e, role)] == "far" else 0)
                px, py = (pv, pu) if tb else (pu, pv)
                m += (f'<rect x="{px - 6:.1f}" y="{py - 6:.1f}" width="12" height="12" rx="2" fill="var(--card)" '
                      f'stroke="var(--c2)" stroke-width="1.6"/>')
        shapes[n["r"]] += m
        over.append(_arq_ring(x, y, w, h, lit.get(n["id"], .8)))
        labels.append(_arq_label(n, x, y, w, h, top, legend, notation))
    bnd, btxt = "", ""
    if hb:
        ins = [rects[n["id"]] for n in inside]
        bx0 = min(r[0] for r in ins) - 16
        by0 = min(r[1] for r in ins) - (pa - 4 if tb else vtop)
        bx1, by1 = max(r[0] + r[2] for r in ins) + 16, max(r[1] + r[3] for r in ins) + 12
        bnd = (f'<rect x="{bx0:.1f}" y="{by0:.1f}" width="{bx1 - bx0:.1f}" height="{by1 - by0:.1f}" rx="16" '
               f'fill="color-mix(in srgb, var(--c2) 5%, transparent)" stroke="var(--c2)" stroke-width="1.5" stroke-dasharray="8 6"/>')
        L, z = _arq_fit(boundary, bx1 - bx0 - 40, 16, 1, "boundary name")
        pl.append(f'<rect x="{bx0 + 8:.1f}" y="{by0 + 4:.1f}" width="{bold_width(L[0], z, current_factor()) + 18:.1f}" '
                  f'height="{z * 1.3 + 4:.1f}" rx="6" fill="var(--card)"/>')
        btxt = _arq_tl(bx0 + 17, by0 + 6 + z * .98, L, z, "var(--c2)", True)
    lsh, ltx = "", ""
    if legend_on:
        lsh, ltx, _lh = _arq_legend(kinds, zx, zy + zh - leg_h + 14, zw, legend, hb)
    svg = (land(bnd, .1, .5, 8) + "".join(base) + seq(shapes, .15, .5, 12, 1.4) + land(lsh, .9, .5, 6)
           + "".join(over) + "".join(dots)
           + land("".join(pl) + "".join(pt), 1.15, .5, 6) + land("".join(labels) + btxt + ltx, 1.1, .5, 6))
    return svg, rects


def _arq_c4(sl, level):
    zx, zy, zw, zh, wide = _arq_zone(sl)
    legend = sl.get("legend") if isinstance(sl.get("legend"), dict) else None
    f5 = ("id", "name", "tech", "desc", "kind", "tier")
    if level == 1:
        f3 = ("id", "name", "desc")
        top = _arq_items(sl.get("people"), f3, "person", rank=0)
        mid = _arq_items([sl["system"]] if sl.get("system") else [], f3, "system", rank=1)
        low = _arq_items(sl.get("externals"), f3, "external", rank=2)
        nodes, boundary = top + mid + low, None
    else:
        inner_key, above_key, below_key = (("containers", "people", "externals") if level == 2
                                           else ("components", "inputs", "outputs"))
        top = _arq_items(sl.get(above_key), f5, "person" if level == 2 else "container", rank=0)
        inner = _arq_items(sl.get(inner_key), f5, "container" if level == 2 else "component", inside=True)
        low = _arq_items(sl.get(below_key), f5, "external")
        dep = _arq_depth(inner, _arq_rels(sl.get("rels"), top + inner + low), 3)
        for n in inner:
            n["rank"] = 1 + dep[n["id"]]
        for n in low:
            n["rank"] = 2 + max(dep.values(), default=0)
        nodes, boundary = top + inner + low, sl.get("boundary") or None
    svg, _r = _arq_graph(nodes, _arq_rels(sl.get("rels"), nodes), (zx, zy, zw, zh), wide, boundary, legend)
    return portrait_mark(svg), D, FREEZE


@register("scene", "c4-context")
@register("scene", "arq_c4_context")
def sc_arq_c4_context(sl, ctx):
    """C1 · System context. args people [[id, name, desc]], system [id, name, desc], externals [[id, name, desc]],
    rels [[from, to, label, tech?]], legend {kind: label} (optional). People on top, the system in the middle, the
    external systems below; the request follows rels in order and lights each element it reaches."""
    return _arq_c4(sl, 1)


@register("scene", "c4-container")
@register("scene", "arq_c4_container")
def sc_arq_c4_container(sl, ctx):
    """C2 · Containers. args boundary (the system's name), people [[id, name, tech?, desc?, kind?]], containers [[id,
    name, tech, desc, kind, tier?]] (kind web|app|api|container|db|queue|storage|lake), externals [[id, name, tech?,
    desc?, kind?]], rels. Containers inside the dashed boundary, ranked by their relations (at most three levels; tier
    fixes one), datastores as cylinders, queues as pipes."""
    return _arq_c4(sl, 2)


@register("scene", "c4-component")
@register("scene", "arq_c4_component")
def sc_arq_c4_component(sl, ctx):
    """C3 · Components of one container. args boundary (the container's name), inputs [[id, name, tech, desc, kind]]
    (who calls it: drawn above), components [[id, name, tech, desc, kind?, tier?]], outputs [[id, name, tech, desc,
    kind]] (datastores and external systems: drawn below; kind db|queue|external|container), rels."""
    return _arq_c4(sl, 3)


# ---------------------------------------------------------------- C4 · code (or deployment)
@register("scene", "c4-code")
@register("scene", "arq_c4_code")
def sc_arq_c4_code(sl, ctx):
    """C4 · Code. args classes [[id, name, stereotype, [members], tier?]], rels [[from, to, label]] (usa, implementa,
    crea…). UML-like boxes laid out by their relations. view "deployment" draws the deployment view instead, with the
    args of infra-topology (entry, region, zones, links, envs, promote)."""
    if sl.get("view") == "deployment":
        return sc_arq_infra(sl, ctx)
    zx, zy, zw, zh, wide = _arq_zone(sl)
    nodes = _arq_items(sl.get("classes"), ("id", "name", "stereotype", "members", "tier"), "class")
    rels = _arq_rels(sl.get("rels"), nodes)
    dep = _arq_depth(nodes, rels, 3)
    for n in nodes:
        n["rank"] = dep[n["id"]]
    svg, _r = _arq_graph(nodes, rels, (zx, zy, zw, zh), wide, None, None, False, False, legend_on=False)
    return portrait_mark(svg), D, FREEZE


@register("scene", "component-diagram")
@register("scene", "arq_components")
def sc_arq_components(sl, ctx):
    """Generic component diagram. args nodes [[id, name, tech, kind?, tier?]] (kind as in c4-container; default
    component), edges [[from, to, label, tech?]], boundary (optional: a dashed frame around every node). Boxes with a
    port where each edge attaches, ranked by the edges (four levels at most)."""
    zx, zy, zw, zh, wide = _arq_zone(sl)
    nodes = _arq_items(sl.get("nodes"), ("id", "name", "tech", "kind", "tier"), "component",
                       inside=bool(sl.get("boundary")))
    rels = _arq_rels(sl.get("edges"), nodes)
    dep = _arq_depth(nodes, rels, 4)
    for n in nodes:
        n["rank"] = dep[n["id"]]
    svg, _r = _arq_graph(nodes, rels, (zx, zy, zw, zh), wide, sl.get("boundary") or None, None, False, True,
                         legend_on=False)
    return portrait_mark(svg), D, FREEZE


# ---------------------------------------------------------------- cover: the system and its promise
@register("scene", "arq-hero")
@register("scene", "arq_hero")
def sc_arq_hero(sl, ctx):
    """Cover. args system (its name), promise (one line inside it), actors [..] (people), systems [..] (external
    systems), 1-4 each. The system at the centre, its people above it and its systems below (left and right when the
    zone is wide), in faint orbits. Loop: a request leaves each person, crosses the system and reaches a system; each
    one lights as it is reached. Frozen: every spoke lit."""
    k = _arq_k()
    zx, zy, zw, zh, wide = _arq_zone(sl)
    actors, systems = list(sl.get("actors") or [])[:4], list(sl.get("systems") or [])[:4]
    cx, cy = zx + zw / 2, zy + zh / 2
    hw, hh = (min(420 * k, zw * .62), 190 * k) if not wide else (min(400, zw * .34), 200)
    hx, hy = cx - hw / 2, cy - hh / 2
    g, over, dots, labels, shapes = [], [], [], [], []
    for r in (1.0, 1.35):
        g.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{hw * .5 * r + 40:.1f}" ry="{hh * .5 * r + 40:.1f}" fill="none" '
                 f'stroke="var(--c2)" stroke-width="1" stroke-dasharray="2 7" opacity=".45"/>')
    shapes.append(_arq_shape("system", hx, hy, hw, hh)[0])
    labels.append(icon("arquitectura/sistema", cx, hy + 36 * k, 40 * k, "var(--c2)"))
    m, h1 = _arq_text(cx, hy + 64 * k, sl.get("system", ""), hw - 40, 26, "var(--white)", "hero system", 2, True, "middle")
    labels.append(m)
    if sl.get("promise"):
        labels.append(_arq_text(cx, hy + 72 * k + h1, sl["promise"], hw - 40, 19, "var(--c4)", "hero promise", 1, True,
                                "middle")[0])

    def spots(n, first):
        """(x, y, w, h) of n satellites: a row above/below the hub, or a column left/right of it when wide."""
        if not wide:
            w = min(230 * k, (zw - (n - 1) * 16) / max(1, n))
            h = 78 * k
            y = zy + 4 if first else zy + zh - h - 4
            return [(zx + (zw - n * w - (n - 1) * 16) / 2 + j * (w + 16), y, w, h) for j in range(n)]
        w, h = min(220, zw * .24), 72
        x = zx if first else zx + zw - w
        return [(x, cy + (j - (n - 1) / 2) * (h + 26) - h / 2, w, h) for j in range(n)]

    A, S = spots(len(actors), True), spots(len(systems), False)
    n = max(len(A), len(S), 1)
    step = .72 / n
    for j in range(n):
        t0 = .07 + j * step
        for side, lst, names, kind in (("a", A, actors, "person"), ("s", S, systems, "external")):
            if j >= len(lst):
                continue
            x, y, w, h = lst[j]
            m, top = _arq_shape(kind, x, y, w, h)
            shapes.append(m)
            labels.append(_arq_text(x + w / 2, 0, names[j], w - 20, 18, "var(--white)", "hero spoke", 2, True, "middle",
                                    mid=(top + y + h) / 2)[0])
            px = hx + hw * (j + 1) / (len(lst) + 1)
            if not wide:
                my = (y + h + hy) / 2 if side == "a" else (hy + hh + y) / 2
                p = (f"M{x + w / 2:.1f} {y + h:.1f} C{x + w / 2:.1f} {my:.1f} {px:.1f} {my:.1f} {px:.1f} {hy:.1f}" if side == "a"
                     else f"M{px:.1f} {hy + hh:.1f} C{px:.1f} {my:.1f} {x + w / 2:.1f} {my:.1f} {x + w / 2:.1f} {y:.1f}")
            else:
                py = hy + hh * (j + 1) / (len(lst) + 1)
                mx = (x + w + hx) / 2 if side == "a" else (hx + hw + x) / 2
                p = (f"M{x + w:.1f} {y + h / 2:.1f} C{mx:.1f} {y + h / 2:.1f} {mx:.1f} {py:.1f} {hx:.1f} {py:.1f}" if side == "a"
                     else f"M{hx + hw:.1f} {py:.1f} C{mx:.1f} {py:.1f} {mx:.1f} {y + h / 2:.1f} {x:.1f} {y + h / 2:.1f}")
            a, b = (t0, t0 + step * .4) if side == "a" else (t0 + step * .45, t0 + step * .85)
            g.append(trace(p, "var(--c2)", 1.6, .35, .8, 'opacity=".75" marker-end="url(#arrow)"'))
            over.append(_arq_draw(p, a, b))
            dots.append(_arq_dot(p, a, b, r=7 * k))
            over.append(_arq_ring(x, y, w, h, a if side == "a" else b))
    over.append(_arq_ring(hx, hy, hw, hh, .1, 18))
    over.append(f'<rect x="{hx - 12:.1f}" y="{hy - 12:.1f}" width="{hw + 24:.1f}" height="{hh + 24:.1f}" rx="24" fill="none" '
                f'stroke="var(--c4)" stroke-width="1.2" opacity=".35">{loop("opacity", ".15;.5;.15", 3)}</rect>')
    svg = "".join(g) + seq(shapes, .1, .5, 12, 1.4) + "".join(over) + "".join(dots) + land("".join(labels), 1.0, .5, 8)
    return portrait_mark(svg), D, FREEZE


# ---------------------------------------------------------------- the quality attributes that drive the design
@register("scene", "quality-drivers")
@register("scene", "arq_drivers")
def sc_arq_drivers(sl, ctx):
    """Problem and drivers. args drivers [[attribute, target, scenario]] (2-6: «Disponibilidad», «Meta: 99,9 %», «si
    cae una zona, el portal sigue»), icons [..] (optional, «vertical/key» per driver). Cards in a grid; loop: each
    driver lights in turn, its bar fills and it gets a check. The target text is static (it never counts up)."""
    k = _arq_k()
    zx, zy, zw, zh, wide = _arq_zone(sl)
    ds = [(list(d) + ["", "", ""])[:3] for d in list(sl.get("drivers") or [])[:6]]
    ics = list(sl.get("icons") or [])
    defaults = ["arquitectura/monitoreo", "arquitectura/seguridad", "arquitectura/nube", "generico/reloj",
                "arquitectura/api", "generico/check"]
    cols = (3 if len(ds) > 4 else max(1, len(ds))) if wide else (2 if len(ds) > 1 else 1)
    rows = -(-len(ds) // cols)
    gx, gy = 22, 22
    cw = (zw - (cols - 1) * gx) / cols
    lh = _k(15) * 1.22
    head = 20 + 30 * k
    need = head + 12 + _k(26) * 1.22 + 12 + 6 + 14 + 3 * lh + 16
    ch = min(need, (zh - (rows - 1) * gy) / rows)
    oy = zy + (zh - (rows * ch + (rows - 1) * gy)) / 2
    step = .7 / max(1, len(ds))
    shapes, over, labels = [], [], []
    for j, (name, target, scen) in enumerate(ds):
        x, y = zx + (j % cols) * (cw + gx), oy + (j // cols) * (ch + gy)
        t0 = .08 + j * step
        shapes.append(card(x, y, cw, ch, "var(--card)", "var(--line)", 14, 1.4))
        labels.append(icon(ics[j] if j < len(ics) and ics[j] else defaults[j % len(defaults)], x + 32 * k, y + 20 + 15 * k,
                           30 * k, "var(--c2)"))
        labels.append(_arq_text(x + 58 * k, 0, name, cw - 70 * k - 30, 19, "var(--white)", "driver attribute", 1,
                                mid=y + 20 + 15 * k)[0])
        yy = y + head + 12
        m, h2 = _arq_text(x + 18, yy, target, cw - 36, 26, "var(--c4)", "driver target", 1)
        labels.append(m)
        by_ = yy + h2 + 12
        shapes.append(f'<rect x="{x + 18:.1f}" y="{by_:.1f}" width="{cw - 36:.1f}" height="6" rx="3" fill="var(--line)"/>')
        over.append(f'<rect x="{x + 18:.1f}" y="{by_:.1f}" width="{cw - 36:.1f}" height="6" rx="3" fill="var(--c4)" '
                    f'transform-origin="{x + 18:.1f} {by_ + 3:.1f}">'
                    f'<animateTransform attributeName="transform" type="scale" values="0 1;0 1;1 1;1 1;0 1;0 1" '
                    f'keyTimes="0;{t0:.3f};{t0 + step * .7:.3f};.97;.985;1" dur="{D}s" repeatCount="indefinite"/></rect>')
        room = int((y + ch - 12 - (by_ + 20)) // lh)
        if scen and room >= 1:
            labels.append(_arq_text(x + 18, by_ + 20, scen, cw - 36, 15, "var(--muted)", "driver scenario", min(room, 3),
                                    False, clip=True)[0])
        over.append(_arq_ring(x, y, cw, ch, t0, 18))
        over.append(_arq_ok(x + cw - 26, y + 20 + 15 * k, t0 + step * .7))
    svg = seq(shapes, .1, .5, 12, 1.3) + "".join(over) + land("".join(labels), 1.0, .5, 8)
    return portrait_mark(svg), D, FREEZE


# ---------------------------------------------------------------- solution layers
@register("scene", "solution-layers")
@register("scene", "arq_layers")
def sc_arq_layers(sl, ctx):
    """Solution layers. args layers [[name, [items]]] from the top (channels) to the bottom (platform), 3-6 layers of
    1-5 items; cross [..] (0-3 cross-cutting concerns: seguridad, observabilidad…, drawn as pillars on the right);
    path [index per layer] (the item the request uses in each layer; default the first). Loop: the request goes down
    through the layers, lighting one item per layer and each pillar it crosses, and the answer comes back up."""
    k = _arq_k()
    zx, zy, zw, zh, wide = _arq_zone(sl)
    layers = [(list(l) + ["", []])[:2] for l in list(sl.get("layers") or [])[:6]]
    cross = list(sl.get("cross") or [])[:3]
    path = list(sl.get("path") or [])
    pw, pg = 58 * k, 10
    bw = zw - len(cross) * (pw + pg)
    n = max(1, len(layers))
    gy = 14
    bh = min(124 * k + (30 if k > 1 else 0), (zh - (n - 1) * gy) / n)
    oy = zy + (zh - (n * bh + (n - 1) * gy)) / 2
    stack = k > 1                                                       # phone: the name heads its band
    name_w = 0 if stack else (170 if bw > 600 else 140)
    step = .5 / n
    shapes, over, labels, pts = [], [], [], []
    for j, (name, items) in enumerate(layers):
        y = oy + j * (bh + gy)
        t0 = .08 + j * step
        mix = 8 + 6 * (n - 1 - j) / max(1, n - 1)
        shapes.append(card(zx, y, bw, bh, f"color-mix(in srgb, var(--c1) {mix:.0f}%, var(--card))", "var(--line)", 12, 1.2))
        nh = _k(18) * 1.3 + 8 if stack else 0
        labels.append(_arq_text(zx + 16, y + 8, name, bw - 32, 18, "var(--white)", "layer name", 1)[0] if stack else
                      _arq_text(zx + 16, 0, name, name_w - 24, 18, "var(--white)", "layer name", 2, mid=y + bh / 2)[0])
        items = list(items)[:5] or [""]
        cx0, cwid = zx + (12 if stack else name_w), bw - (24 if stack else name_w + 12)
        iw = (cwid - (len(items) - 1) * 10) / len(items)
        ih = min(60 * k, bh - 26 - nh)
        pick = path[j] if j < len(path) and isinstance(path[j], int) and 0 <= path[j] < len(items) else 0
        for i, it in enumerate(items):
            ix, iy = cx0 + i * (iw + 10), y + nh + (bh - nh - ih) / 2
            shapes.append(card(ix, iy, iw, ih, "var(--card)", "var(--c2)", 10, 1.2))
            labels.append(_arq_text(ix + iw / 2, 0, it, iw - 14, 16, "var(--white)", "layer item",
                                    1 if ih < 50 * k else 2, True, "middle", mid=iy + ih / 2)[0])
            if i == pick:
                over.append(f'<rect x="{ix:.1f}" y="{iy:.1f}" width="{iw:.1f}" height="{ih:.1f}" rx="10" '
                            f'fill="color-mix(in srgb, var(--c4) 12%, var(--card))" stroke="var(--c4)" stroke-width="2" '
                            f'opacity="0">{_arq_on(t0 + step * .6)}</rect>')
                pts.append((ix + iw / 2, iy, iy + ih, t0, iw))
        over.append(_arq_ring(zx, y, bw, bh, t0 + step * .6, 16))
    ph = n * bh + (n - 1) * gy
    for c, name in enumerate(cross):
        px = zx + bw + pg + c * (pw + pg)
        shapes.append(card(px, oy, pw, ph, "color-mix(in srgb, var(--c2) 7%, var(--card))", "var(--c2)", 12, 1.2))
        L, z = _arq_fit(name, ph - 40, 17, 1, "cross-cutting concern")
        labels.append(f'<g transform="translate({px + pw / 2 + z * .35:.1f} {oy + ph / 2:.1f}) rotate(-90)">'
                      + _arq_tl(0, 0, L, z, "var(--c2)", True, "middle") + "</g>")
        over.append(_arq_ring(px, oy, pw, ph, .08 + .5 * (c + 1) / (len(cross) + 1), 16))
    back = []
    for (x0, _t0, b0, a0, _w0), (x1, t1, _b1, a1, _w1) in zip(pts, pts[1:]):   # the request only in the gaps
        my = (b0 + t1) / 2
        seg = f"M{x0:.1f} {b0:.1f} C{x0:.1f} {my:.1f} {x1:.1f} {my:.1f} {x1:.1f} {t1:.1f}"
        shapes.append(f'<path d="{seg}" fill="none" stroke="var(--c2)" stroke-width="1.4" opacity=".6" marker-end="url(#arrow)"/>')
        over.append(_arq_draw(seg, a0 + step * .3, a1 + step * .6, "var(--c4)", 2))
        over.append(_arq_dot(seg, a0 + step * .3, a1 + step * .6, r=6 * k))
        back.append(f"M{x1:.1f} {t1:.1f} C{x1:.1f} {my:.1f} {x0:.1f} {my:.1f} {x0:.1f} {b0:.1f}")
    for i, p in enumerate(reversed(back)):                              # the answer comes back up
        a = .62 + i * .18 / len(back)
        over.append(_arq_dot(p, a, a + .18 / len(back), "var(--c2)", 5 * k))
    if pts:
        x0, t0_, _b, _a, w0 = pts[0]
        over.append(_arq_ok(x0 + w0 / 2 - 16 * k, t0_ - 12 * k, .82, .42))
    svg = seq(shapes, .1, .45, 10, 1.4) + "".join(over) + land("".join(labels), 1.0, .5, 8)
    return portrait_mark(svg), D, FREEZE


# ---------------------------------------------------------------- data architecture
@register("scene", "data-architecture")
@register("scene", "arq_data")
def sc_arq_data(sl, ctx):
    """Data architecture. args flow [[name, [items], icon?]] (3-6 steps: sources, ingest, store, serve, consume),
    governance [name, [items]] (the band that spans every step: catálogo, linaje, calidad, acceso). Rows top-to-bottom
    with the governance pillar on the right, or columns left-to-right over a governance band when the zone is wide.
    Loop: three data tokens flow through the steps; each step lights as the first one passes and each governance item
    gets its check."""
    k = _arq_k()
    zx, zy, zw, zh, wide = _arq_zone(sl)
    flow = [(list(f) + [[], ""])[:3] for f in list(sl.get("flow") or [])[:6]]
    gov = (list(sl.get("governance") or []) + ["", []])[:2]
    defaults = ["arquitectura/sistema", "arquitectura/pipeline", "arquitectura/lago", "arquitectura/api",
                "arquitectura/persona", "generico/dato"]
    n = max(1, len(flow))
    gi = list(gov[1])[:5]
    shapes, over, labels = [], [], []
    step = .6 / n
    band = wide or k > 1                                                # governance as a band at the bottom
    gbh = (_k(17) * 1.3 + 52 * k + 44 if k > 1 else 96) if gov[0] and band else 0
    if not wide:
        gw = 150 if gov[0] and not band else 0
        fw = zw - (gw + 16 if gw else 0)
        gy = 26
        fh = zh - (gbh + 16 if gbh else 0)
        rh = min(118 * k, (fh - (n - 1) * gy) / n)
        oy = zy + (fh - (n * rh + (n - 1) * gy)) / 2
        boxes = [(zx, oy + j * (rh + gy), fw, rh) for j in range(n)]
        head_w = min(215, fw * .38) if k == 1 else fw * .42
        spine = [(zx + 30 * k, b[1] + b[3] / 2) for b in boxes]
    else:
        fh = zh - (gbh + 16 if gbh else 0)
        gx = 36
        cw = (zw - (n - 1) * gx) / n
        boxes = [(zx + j * (cw + gx), zy, cw, fh) for j in range(n)]
        spine = [(b[0] + b[2] / 2, zy + 46) for b in boxes]
    for j, (name, items, ic) in enumerate(flow):
        x, y, w, h = boxes[j]
        t0 = .08 + j * step
        shapes.append(card(x, y, w, h, "color-mix(in srgb, var(--c1) 12%, var(--card))", "var(--line)", 14, 1.3))
        if not wide:
            labels.append(icon(ic or defaults[j % 6], x + 30 * k, y + h / 2, 30 * k, "var(--c2)"))
            labels.append(_arq_text(x + 56 * k, 0, name, head_w - 62 * k, 18, "var(--white)", "data step", 2, mid=y + h / 2)[0])
            its = list(items)[:4]
            if its:
                ax, aw = x + head_w, w - head_w - 12
                iw = (aw - (len(its) - 1) * 8) / len(its)
                ih = min(52 * k, h - 24)
                for i, it in enumerate(its):
                    ix, iy = ax + i * (iw + 8), y + (h - ih) / 2
                    shapes.append(card(ix, iy, iw, ih, "var(--card)", "var(--c2)", 9, 1.1))
                    labels.append(_arq_text(ix + iw / 2, 0, it, iw - 12, 15, "var(--white)", "data item", 2, False,
                                            "middle", mid=iy + ih / 2)[0])
            if j:
                x0, y0 = boxes[j - 1][0] + 30 * k, boxes[j - 1][1] + boxes[j - 1][3]
                shapes.append(f'<path d="M{x0:.1f} {y0 + 2:.1f} V{y - 4:.1f}" stroke="var(--c2)" stroke-width="1.6" '
                              f'marker-end="url(#arrow)" opacity=".8"/>')
        else:
            labels.append(icon(ic or defaults[j % 6], x + 30, y + 32, 30, "var(--c2)"))
            labels.append(_arq_text(x + 52, 0, name, w - 64, 17, "var(--white)", "data step", 1, mid=y + 32)[0])
            ih = 40
            for i, it in enumerate(list(items)[:5]):
                ix, iy = x + 12, y + 64 + i * (ih + 8)
                if iy + ih > y + h - 8:
                    break
                shapes.append(card(ix, iy, w - 24, ih, "var(--card)", "var(--c2)", 9, 1.1))
                labels.append(_arq_text(ix + (w - 24) / 2, 0, it, w - 40, 15, "var(--white)", "data item", 1, False,
                                        "middle", mid=iy + ih / 2)[0])
            if j:
                x0 = boxes[j - 1][0] + boxes[j - 1][2]
                shapes.append(f'<path d="M{x0 + 2:.1f} {zy + 32:.1f} H{x - 4:.1f}" stroke="var(--c2)" stroke-width="1.6" '
                              f'marker-end="url(#arrow)" opacity=".8"/>')
        over.append(_arq_ring(x, y, w, h, t0 + step * .4, 18))
    if len(spine) > 1:
        sp = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in spine)
        for i in range(3):
            a = .08 + i * .06
            over.append(_arq_dot(sp, a, a + .6, "var(--c4)", 6 * k))
    if gov[0]:
        if not band:
            gx0 = zx + zw - gw
            gy0, gh_ = boxes[0][1], boxes[-1][1] + boxes[-1][3] - boxes[0][1]
            shapes.append(card(gx0, gy0, gw, gh_, "color-mix(in srgb, var(--c2) 8%, var(--card))", "var(--c2)", 14, 1.3))
            labels.append(icon("arquitectura/seguridad", gx0 + gw / 2, gy0 + 30 * k, 28 * k, "var(--c2)"))
            m, hh_ = _arq_text(gx0 + gw / 2, gy0 + 52 * k, gov[0], gw - 16, 17, "var(--c2)", "governance name", 2, True, "middle")
            labels.append(m)
            ih = 44 * k
            top = gy0 + 52 * k + hh_ + 18
            gap = max(8, min(60, (gy0 + gh_ - 14 - top - len(gi) * ih) / max(1, len(gi) - 1))) if len(gi) > 1 else 0
            for i, it in enumerate(gi):
                iy = top + i * (ih + gap)
                shapes.append(card(gx0 + 10, iy, gw - 20, ih, "var(--card)", "var(--line)", 9, 1.1))
                labels.append(_arq_text(gx0 + 20, 0, it, gw - 64 * k, 15, "var(--white)", "governance item", 1, False,
                                        mid=iy + ih / 2)[0])
                over.append(_arq_ok(gx0 + gw - 26 * k, iy + ih / 2 + 1, .12 + (i + 1) * .6 / (len(gi) + 1), .4))
        else:
            gh, gy0 = gbh, zy + zh - gbh
            shapes.append(card(zx, gy0, zw, gh, "color-mix(in srgb, var(--c2) 8%, var(--card))", "var(--c2)", 14, 1.3))
            if k > 1:                                                   # phone: the name above, the items below
                labels.append(icon("arquitectura/seguridad", zx + 28 * k, gy0 + 14 + _k(17) * .65, 26 * k, "var(--c2)"))
                labels.append(_arq_text(zx + 50 * k, gy0 + 14, gov[0], zw - 70 * k, 17, "var(--c2)", "governance name", 1)[0])
                ax, iy, ih = zx + 12, gy0 + 22 + _k(17) * 1.3, 52 * k
                room = zw - 24
            else:
                labels.append(icon("arquitectura/seguridad", zx + 30, gy0 + gh / 2, 28, "var(--c2)"))
                labels.append(_arq_text(zx + 54, 0, gov[0], 200, 17, "var(--c2)", "governance name", 2, mid=gy0 + gh / 2)[0])
                ax, iy, ih = zx + 270, gy0 + 24, gh - 48
                room = zw - 280
            iw = (room - (len(gi) - 1) * 10) / max(1, len(gi))
            for i, it in enumerate(gi):
                ix = ax + i * (iw + 10)
                shapes.append(card(ix, iy, iw, ih, "var(--card)", "var(--line)", 9, 1.1))
                labels.append(_arq_text(ix + 12, 0, it, iw - 24 - 26 * k, 15, "var(--white)", "governance item", 1, False,
                                        mid=iy + ih / 2)[0])
                over.append(_arq_ok(ix + iw - 18 * k, iy + ih / 2 + 1, .12 + (i + 1) * .6 / (len(gi) + 1), .4))
    svg = seq(shapes, .1, .45, 10, 1.4) + "".join(over) + land("".join(labels), 1.0, .5, 8)
    return portrait_mark(svg), D, FREEZE


# ---------------------------------------------------------------- infrastructure and environments
_ARQ_ZONE = {"publica": "var(--c3)", "privada": "var(--c2)", "datos": "var(--c4)", "gestion": "var(--muted)"}


@register("scene", "infra-topology")
@register("scene", "arq_infra")
def sc_arq_infra(sl, ctx):
    """Infrastructure. args entry (who comes in: «Usuarios · Internet»), region (the frame: «Nube · región
    principal»), zones [[name, kind, [[id, name, tech, icon?]]]] (kind publica|privada|datos|gestion: the colour of the
    security zone; 1-4 nodes each), links [[from, to, label?]] (optional; default: the first node of each zone to the
    next), envs [[name, note]] (optional: dev, qa, prod), promote (the label of the promotion). Loop: the request enters
    and crosses every zone through its links, each zone border lighting as it passes; then a release is promoted
    dev -> qa -> prod."""
    k = _arq_k()
    zx, zy, zw, zh, wide = _arq_zone(sl)
    zones = [(list(z) + ["", "privada", []])[:3] for z in list(sl.get("zones") or [])[:4]]
    envs = [(list(e) + [""])[:2] for e in list(sl.get("envs") or [])[:4]]
    env_h = 84 * k if envs else 0
    env_gap = (26 + _k(15)) if envs and sl.get("promote") else (16 if envs else 0)
    entry_h = 46 * k if sl.get("entry") else 0
    shapes, over, labels, dots, plates = [], [], [], [], []
    nodes, rects = [], {}
    rx, ry, rw = zx, zy + entry_h + (24 if entry_h else 0), zw
    rh = zh - (ry - zy) - env_h - env_gap
    shapes.append(f'<rect x="{rx:.1f}" y="{ry:.1f}" width="{rw:.1f}" height="{rh:.1f}" rx="16" fill="none" stroke="var(--c2)" '
                  f'stroke-width="1.4" stroke-dasharray="8 6"/>')
    head = 40 * k
    if sl.get("region"):
        L, z = _arq_fit(sl["region"], rw - 80 * k, 16, 1, "region name")
        tw = bold_width(L[0], z, current_factor(), True) + 50 * k
        plates.append(f'<rect x="{rx + 10:.1f}" y="{ry + 6:.1f}" width="{tw:.1f}" height="{z * 1.3 + 8:.1f}" rx="7" fill="var(--card)"/>')
        labels.append(icon("arquitectura/nube", rx + 26 * k, ry + 10 + z * .65, 24 * k, "var(--c2)"))
        labels.append(_arq_tl(rx + 46 * k, ry + 10 + z * .98, L, z, "var(--c2)", True))
    n = max(1, len(zones))
    iz = 12
    if not wide:
        zh_ = (rh - head - 14 - (n - 1) * iz) / n
        zb = [(rx + 14, ry + head + j * (zh_ + iz), rw - 28, zh_) for j in range(n)]
    else:
        zw_ = (rw - 28 - (n - 1) * iz) / n
        zb = [(rx + 14 + j * (zw_ + iz), ry + head, zw_, rh - head - 14) for j in range(n)]
    step = .5 / n
    zhead = _k(15) * 1.22 + 16
    for j, (name, kind, members) in enumerate(zones):
        x, y, w, h = zb[j]
        colr = _ARQ_ZONE.get(kind, "var(--c2)")
        shapes.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="12" '
                      f'fill="color-mix(in srgb, {colr} 7%, var(--card))" stroke="{colr}" stroke-width="1.4"/>')
        labels.append(_arq_text(x + 12, y + 8, name, w - 24, 15, colr if kind != "gestion" else "var(--muted)", "zone name", 1)[0])
        ms = _arq_items(members, ("id", "name", "tech", "icon"), "server")[:4]
        m = max(1, len(ms))
        if not wide:
            nw, nh = min(250 * k, (w - 24 - (m - 1) * 16) / m), min(66 * k, h - zhead - 8)
            gapx = (w - 24 - m * nw) / (m - 1) if m > 1 else 0
            pos = [(x + 12 + j2 * (nw + gapx) + (0 if m > 1 else (w - 24 - nw) / 2), y + zhead + (h - zhead - 8 - nh) / 2)
                   for j2 in range(m)]
        else:
            nw, nh = w - 24, min(66 * k, (h - zhead - 8 - (m - 1) * 10) / m)
            pos = [(x + 12, y + zhead + j2 * (nh + 10)) for j2 in range(m)]
        for (px, py), nd in zip(pos, ms):
            rects[nd["id"]] = (px, py, nw, nh)
            nodes.append(nd)
            nd["zone"] = j
            shapes.append(card(px, py, nw, nh, "var(--card)", "var(--line)", 10, 1.2))
            labels.append(icon(nd.get("icon") or "arquitectura/servidor", px + 22 * k, py + nh / 2, 24 * k, "var(--c2)"))
            if nd.get("tech") and nh >= 2 * _k(15) * 1.22 + 10:
                labels.append(_arq_text(px + 42 * k, py + nh / 2 - _k(16) * 1.2, nd["name"], nw - 52 * k, 16, "var(--white)",
                                        "infra node", 1)[0])
                labels.append(_arq_text(px + 42 * k, py + nh / 2 + 1, nd["tech"], nw - 52 * k, 15, "var(--muted)",
                                        "infra tech", 1, False, clip=True)[0])
            else:
                labels.append(_arq_text(px + 42 * k, 0, nd["name"], nw - 52 * k, 16, "var(--white)", "infra node", 1,
                                        mid=py + nh / 2)[0])
        over.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="12" fill="none" stroke="var(--c4)" '
                    f'stroke-width="1.8" opacity="0">{_arq_on(.08 + (j + .6) * step)}</rect>')
    firsts = [next((nd["id"] for nd in nodes if nd["zone"] == j), None) for j in range(n)]
    links = _arq_rels(sl.get("links"), nodes) if sl.get("links") else [
        (a, b, "") for a, b in zip(firsts, firsts[1:]) if a and b]
    zone_of = {nd["id"]: nd["zone"] for nd in nodes}
    chain = []
    if sl.get("entry"):
        ew = min(zw * .8, _arq_w(sl["entry"], 17) + 70 * k)
        ex, ey = zx + zw / 2 - ew / 2, zy
        shapes.append(card(ex, ey, ew, entry_h, "color-mix(in srgb, var(--c1) 60%, var(--card))", "var(--c2)", entry_h / 2, 1.4))
        labels.append(icon("arquitectura/persona", ex + 26 * k, ey + entry_h / 2, 24 * k, "var(--white)"))
        labels.append(_arq_text(ex + 46 * k, 0, sl["entry"], ew - 60 * k, 17, "var(--white)", "entry", 1, mid=ey + entry_h / 2)[0])
        if nodes:
            f = rects[links[0][0]] if links else rects[nodes[0]["id"]]
            chain.append((f"M{zx + zw / 2:.1f} {ey + entry_h:.1f} C{zx + zw / 2:.1f} {ey + entry_h + 60:.1f} "
                          f"{f[0] + f[2] / 2:.1f} {f[1] - 60:.1f} {f[0] + f[2] / 2:.1f} {f[1]:.1f}", ""))
    for a, b, lab in links:
        (x0, y0, w0, h0), (x1, y1, w1, h1) = rects[a], rects[b]
        if zone_of[a] == zone_of[b]:                                    # same zone: a straight connector
            if not wide:
                xa, xb = (x0 + w0, x1) if x1 > x0 else (x0, x1 + w1)
                p = f"M{xa:.1f} {y0 + h0 / 2:.1f} H{xb:.1f}"
            else:
                ya, yb = (y0 + h0, y1) if y1 > y0 else (y0, y1 + h1)
                p = f"M{x0 + w0 / 2:.1f} {ya:.1f} V{yb:.1f}"
        elif not wide:
            p = (f"M{x0 + w0 / 2:.1f} {y0 + h0:.1f} C{x0 + w0 / 2:.1f} {y0 + h0 + 40:.1f} {x1 + w1 / 2:.1f} {y1 - 40:.1f} "
                 f"{x1 + w1 / 2:.1f} {y1:.1f}")
        else:
            p = (f"M{x0 + w0:.1f} {y0 + h0 / 2:.1f} C{x0 + w0 + 40:.1f} {y0 + h0 / 2:.1f} {x1 - 40:.1f} {y1 + h1 / 2:.1f} "
                 f"{x1:.1f} {y1 + h1 / 2:.1f}")
        chain.append((p, lab))
    cs = .5 / max(1, len(chain))
    for j, (p, lab) in enumerate(chain):
        t0 = .08 + j * cs
        shapes.append(f'<path d="{p}" fill="none" stroke="var(--c2)" stroke-width="1.6" opacity=".75" marker-end="url(#arrow)"/>')
        over.append(_arq_draw(p, t0, t0 + cs * .85))
        dots.append(_arq_dot(p, t0, t0 + cs * .85, r=7 * k))
    off = 1 if sl.get("entry") else 0
    for nd in nodes:
        x, y, w, h = rects[nd["id"]]
        hit = ([j for j, (a, b, _l) in enumerate(links) if b == nd["id"]]
               or [j for j, (a, b, _l) in enumerate(links) if a == nd["id"]])
        t = .08 + (min(hit) + off + .85) * cs if hit else .6
        over.append(_arq_ring(x, y, w, h, t, 13))
    if envs:
        ey0 = zy + zh - env_h
        m = len(envs)
        ag = 44
        ew = (zw - (m - 1) * ag) / m
        for j, (name, note) in enumerate(envs):
            ex = zx + j * (ew + ag)
            t = .6 + j * .07
            shapes.append(card(ex, ey0, ew, env_h, "var(--card)", "var(--c2)" if j < m - 1 else "var(--c4)", 12, 1.4))
            labels.append(_arq_text(ex + 14, ey0 + 10, name, ew - 50 * k, 18, "var(--white)", "environment", 1)[0])
            if note:
                labels.append(_arq_text(ex + 14, ey0 + 14 + _k(18) * 1.22, note, ew - 28, 15, "var(--muted)",
                                        "environment note", 2, False, clip=True)[0])
            over.append(_arq_ring(ex, ey0, ew, env_h, t + .03, 16))
            over.append(_arq_ok(ex + ew - 22 * k, ey0 + 22 * k, t + .03, .42))
            if j:
                shapes.append(f'<path d="M{ex - ag + 4:.1f} {ey0 + env_h / 2:.1f} H{ex - 6:.1f}" stroke="var(--c2)" '
                              f'stroke-width="1.6" marker-end="url(#arrow)"/>')
        rel = f"M{zx + ew / 2:.1f} {ey0 + env_h / 2:.1f} H{zx + (m - 1) * (ew + ag) + ew / 2:.1f}"
        dots.append(_arq_dot(rel, .6, .6 + .07 * (m - 1) + .03, "var(--c4)", 7 * k))
        if sl.get("promote"):
            p1, p2 = _arq_plate(zx + zw / 2, ey0 - env_gap / 2, sl["promote"])
            plates.append(p1)
            labels.append(p2)
    svg = (seq(shapes, .1, .45, 10, 1.4) + "".join(over) + "".join(dots)
           + land("".join(plates) + "".join(labels), 1.0, .5, 8))
    return portrait_mark(svg), D, FREEZE


# ---------------------------------------------------------------- decisions (ADR)
@register("scene", "adr-decisions")
@register("scene", "arq_adr")
def sc_arq_adr(sl, ctx):
    """Key decisions. args decisions [[id, title, context, decision, consequence, status]] (2-4 cards: «ADR-01»,
    «Aceptada»), labels [context, decision, consequence] (default «Contexto», «Decisión», «Consecuencia»). Loop: each
    card in turn lights its context, then its decision, then its consequence, and its status stamps in."""
    zx, zy, zw, zh, wide = _arq_zone(sl)
    ds = [(list(d) + [""] * 6)[:6] for d in list(sl.get("decisions") or [])[:4]]
    labs = (list(sl.get("labels") or []) + ["Contexto", "Decisión", "Consecuencia"])[:3]
    n = max(1, len(ds))
    cols = n if wide else (2 if n == 4 else 1)
    rows = -(-n // cols)
    g_ = 18
    cw, ch = (zw - (cols - 1) * g_) / cols, (zh - (rows - 1) * g_) / rows
    step = .7 / n
    lh = _k(15) * 1.22
    shapes, over, labels = [], [], []
    for j, (aid, title, c1, c2, c3, status) in enumerate(ds):
        x, y = zx + (j % cols) * (cw + g_), zy + (j // cols) * (ch + g_)
        t0 = .07 + j * step
        shapes.append(card(x, y, cw, ch, "var(--card)", "var(--line)", 14, 1.4))
        shapes.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="6" height="{ch:.1f}" rx="3" fill="var(--c2)"/>')
        if aid:
            labels.append(_arq_line(x + 20, y + 12 + _k(15), aid, 15, "var(--c2)", True))
        if status:
            sw, sh_ = _arq_w(status, 15) + 22, _k(15) + 11
            over.append(f'<g opacity="0">{_arq_on(t0 + step * .8)}<rect x="{x + cw - sw - 14:.1f}" y="{y + 10:.1f}" width="{sw:.1f}" '
                        f'height="{sh_:.1f}" rx="{sh_ / 2:.1f}" fill="none" stroke="var(--c4)" stroke-width="1.6"/>'
                        + _arq_line(x + cw - sw / 2 - 14, y + 10 + sh_ / 2 + _k(15) * .36, status, 15, "var(--c4)", True, "middle")
                        + "</g>")
        yy = y + 20 + _k(15) * 1.3
        m, h = _arq_text(x + 20, yy, title, cw - 40, 19, "var(--white)", "decision title", 2)
        labels.append(m)
        yy += h + 8
        per = (y + ch - 12 - yy) / 3
        lines = max(1, int((per - lh - 6) // lh))
        for i, (lab, txt) in enumerate(zip(labs, (c1, c2, c3))):
            ly = yy + i * per
            labels.append(_arq_line(x + 20, ly + _k(15), _(str(lab)).upper(), 15, "var(--c4)" if i == 1 else "var(--c2)", True))
            if txt:
                labels.append(_arq_text(x + 20, ly + lh + 4, txt, cw - 40, 15, "var(--white)" if i == 1 else "var(--muted)",
                                        "decision text", min(lines, 4), False, clip=True)[0])
            over.append(f'<rect x="{x + 8:.1f}" y="{ly - 2:.1f}" width="4" height="{per - 6:.1f}" rx="2" fill="var(--c4)" '
                        f'opacity="0">{_arq_on(t0 + i * step * .25)}</rect>')
        over.append(_arq_ring(x, y, cw, ch, t0, 18))
    svg = seq(shapes, .1, .45, 10, 1.3) + "".join(over) + land("".join(labels), 1.0, .5, 8)
    return portrait_mark(svg), D, FREEZE


# ---------------------------------------------------------------- risks and trade-offs
@register("scene", "risks-tradeoffs")
@register("scene", "arq_risks")
def sc_arq_risks(sl, ctx):
    """Risks and trade-offs. args risks [[risk, likelihood 1-3, impact 1-3, mitigation, [residual likelihood,
    residual impact]?]] (2-5), axes [x label, y label] (default «Probabilidad», «Impacto»), levels [low, mid, high].
    A 3 x 3 matrix and the list beside it (below it when the zone is not wide). Loop: each risk pulses on its cell, its
    row lights with the mitigation and the risk moves to its residual cell (default one step lower on each axis)."""
    k = _arq_k()
    zx, zy, zw, zh, wide = _arq_zone(sl)
    rs = [(list(r) + ["", 2, 2, "", None])[:5] for r in list(sl.get("risks") or [])[:5]]
    ax = (list(sl.get("axes") or []) + ["Probabilidad", "Impacto"])[:2]
    lv = (list(sl.get("levels") or []) + ["Baja", "Media", "Alta"])[:3]
    tick_w = max(_arq_w(l, 15, False) for l in lv) + 12
    lab_w = _k(16) * 1.6
    ms = min(zw * .46, zh * .6) if wide else min(zw * .62 - tick_w, zh * .42)
    left = zx if wide else zx + (zw - (lab_w + tick_w + ms)) / 2
    mx, my = left + lab_w + tick_w, zy + 6
    cs = ms / 3
    shapes, over, labels = [], [], []
    for i in range(3):
        for j in range(3):
            sev = i + j                                                  # 0 low .. 4 high
            colr = "var(--c5)" if sev >= 3 else ("var(--c3)" if sev == 2 else "var(--c2)")
            shapes.append(f'<rect x="{mx + i * cs + 2:.1f}" y="{my + (2 - j) * cs + 2:.1f}" width="{cs - 4:.1f}" '
                          f'height="{cs - 4:.1f}" rx="8" fill="color-mix(in srgb, {colr} {(6, 10, 16, 24, 32)[sev]}%, var(--card))" '
                          f'stroke="var(--line)"/>')
    for i, l in enumerate(lv):
        labels.append(_arq_line(mx + (i + .5) * cs, my + ms + _k(15) + 8, l, 15, "var(--muted)", False, "middle"))
        labels.append(_arq_line(mx - 10, my + (2 - i + .5) * cs + _k(15) * .36, l, 15, "var(--muted)", False, "end"))
    labels.append(_arq_line(mx + ms / 2, my + ms + _k(15) + _k(16) + 16, ax[0], 16, "var(--c2)", True, "middle"))
    labels.append(f'<g transform="translate({left + lab_w / 2 + _k(16) * .36:.1f} {my + ms / 2:.1f}) rotate(-90)">'
                  + _arq_line(0, 0, ax[1], 16, "var(--c2)", True, "middle") + "</g>")
    n = max(1, len(rs))
    step = .7 / n
    if wide:
        lx, ly = mx + ms + 50, zy
        lw, lh = zx + zw - lx, zh
    else:
        lx, ly, lw = zx, my + ms + _k(15) + _k(16) + 34, zw
        lh = zy + zh - ly
    rh = min(96 * k, (lh - (n - 1) * 10) / n)
    seen = {}
    r0 = 16 * k
    o = max(r0 + 3, cs * .24)

    def spot(li, im):
        c = seen.get((li, im), 0)
        seen[(li, im)] = c + 1
        ox, oy = ((0, 0), (-o, -o), (o, o), (o, -o), (-o, o))[c % 5]
        return mx + (li - .5) * cs + ox, my + (3 - im + .5) * cs + oy

    for j, (risk, li, im, mit, res) in enumerate(rs):
        li, im = max(1, min(3, int(li or 2))), max(1, min(3, int(im or 2)))
        rl, ri = res if isinstance(res, (list, tuple)) and len(res) == 2 else (max(1, li - 1), max(1, im - 1))
        rl, ri = max(1, min(3, int(rl))), max(1, min(3, int(ri)))
        t0 = .07 + j * step
        x0, y0 = spot(li, im)
        x1, y1 = spot(rl, ri)
        num = str(j + 1)
        shapes.append(f'<circle cx="{x0:.1f}" cy="{y0:.1f}" r="{r0 - 1:.1f}" fill="var(--card)" stroke="var(--c5)" '
                      f'stroke-width="1.6" stroke-dasharray="3 3"/>')
        over.append(_arq_draw(f"M{x0:.1f} {y0:.1f} L{x1:.1f} {y1:.1f}", t0 + step * .3, t0 + step * .7, "var(--c4)", 2))
        labels.append(f'<g><animateTransform attributeName="transform" type="translate" values="0 0;0 0;{x1 - x0:.1f} {y1 - y0:.1f};'
                      f'{x1 - x0:.1f} {y1 - y0:.1f};0 0;0 0" keyTimes="0;{t0 + step * .3:.3f};{t0 + step * .7:.3f};.97;.985;1" '
                      f'dur="{D}s" repeatCount="indefinite"/>'
                      f'<circle cx="{x0:.1f}" cy="{y0:.1f}" r="{r0:.1f}" fill="var(--c1)" stroke="var(--c4)" stroke-width="1.8"/>'
                      + _arq_line(x0, y0 + _k(16) * .36, num, 16, "var(--white)", True, "middle") + "</g>")
        over.append(f'<circle cx="{x0:.1f}" cy="{y0:.1f}" r="{r0:.1f}" fill="none" stroke="var(--c4)" stroke-width="2" opacity="0">'
                    f'{_arq_win(t0, t0 + step * .3)}{pulse_r(r0, r0 + 10, t0 + .01, D)}</circle>')
        yy = ly + j * (rh + 10)
        shapes.append(card(lx, yy, lw, rh, "var(--card)", "var(--line)", 12, 1.2))
        labels.append(f'<circle cx="{lx + 24 * k:.1f}" cy="{yy + rh / 2:.1f}" r="{14 * k:.1f}" fill="var(--c1)"/>'
                      + _arq_line(lx + 24 * k, yy + rh / 2 + _k(16) * .36, num, 16, "var(--white)", True, "middle"))
        L, z = _arq_fit(risk, lw - 60 * k, 17, 1 if rh < 80 * k else 2, "risk")
        body = len(L) * z * 1.22
        room = int((rh - 16 - body) // (_k(15) * 1.22))
        mh = min(room, 2) * _k(15) * 1.22 if mit and room >= 1 else 0
        top = yy + (rh - body - mh - 4) / 2
        labels.append(_arq_tl(lx + 48 * k, top + z * .92, L, z, "var(--white)", True))
        if mh:
            labels.append(_arq_text(lx + 48 * k, top + body + 4, mit, lw - 60 * k, 15, "var(--muted)", "mitigation",
                                    min(room, 2), False, clip=True)[0])
        over.append(_arq_ring(lx, yy, lw, rh, t0 + step * .3, 15))
    svg = seq(shapes, .1, .45, 10, 1.3) + "".join(over) + land("".join(labels), 1.0, .5, 8)
    return portrait_mark(svg), D, FREEZE


# ---------------------------------------------------------------- roadmap and next step
@register("scene", "arq-roadmap")
@register("scene", "arq_roadmap")
def sc_arq_roadmap(sl, ctx):
    """Roadmap and the next step. args phases [[name, when, [items]]] (3-5), now (index of the next step; default 0),
    next (its label: «Próximo paso»), sign (optional: the close's line in the art, «Audacious Ideas, Delivered
    Beyond.»). A timeline (vertical when the zone is not wide) of cards sized to their text; loop: a marker travels the
    phases, each lights, and the next step keeps its ring."""
    k = _arq_k()
    zx, zy, zw, zh, wide = _arq_zone(sl)
    ph = [(list(p) + ["", "", []])[:3] for p in list(sl.get("phases") or [])[:5]]
    now = sl.get("now", 0) if isinstance(sl.get("now", 0), int) else 0
    n = max(1, len(ph))
    sign_h = _k(22) * 1.8 if sl.get("sign") else 0
    lh = _k(15) * 1.22
    shapes, over, labels = [], [], []
    step = .6 / n
    avail = zh - sign_h
    if not wide:
        gy = 18
        need = 12 + lh + 2 + _k(19) * 1.22 + 6 + lh + 14
        rh = min(need, (avail - (n - 1) * gy) / n)
        top = zy + (avail - (n * rh + (n - 1) * gy)) / 2
        spine_x = zx + 26
        boxes = [(zx + 60, top + j * (rh + gy), zw - 60, rh) for j in range(n)]
        pts = [(spine_x, b[1] + b[3] / 2) for b in boxes]
        line = f"M{spine_x} {pts[0][1]:.1f} V{pts[-1][1]:.1f}"
    else:
        gx = 18
        cw = (zw - (n - 1) * gx) / n
        ly = zy + 24
        pts = [(zx + j * (cw + gx) + cw / 2, ly) for j in range(n)]
        boxes = [(zx + j * (cw + gx), ly + 34, cw, min(avail - 60, 12 + lh + _k(19) * 2.44 + 3 * lh + 30)) for j in range(n)]
        line = f"M{pts[0][0]:.1f} {ly} H{pts[-1][0]:.1f}"
    shapes.append(f'<path d="{line}" stroke="var(--line)" stroke-width="3" stroke-linecap="round"/>')
    over.append(_arq_draw(line, .08, .08 + .6, "var(--c4)", 3))
    for j, ((name, when, items), (px, py), (x, y, w, h)) in enumerate(zip(ph, pts, boxes)):
        t0 = .08 + j * step
        is_now = j == now
        shapes.append(card(x, y, w, h, "color-mix(in srgb, var(--c1) 22%, var(--card))" if is_now else "var(--card)",
                           "var(--c4)" if is_now else "var(--line)", 12, 1.6 if is_now else 1.2))
        shapes.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{11 * k:.1f}" fill="var(--card)" stroke="var(--c2)" stroke-width="2"/>')
        over.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{11 * k:.1f}" fill="var(--c4)" opacity="0">{_arq_on(t0 + step * .5)}</circle>')
        yy = y + 12
        pill_w = _arq_w(sl.get("next", ""), 15) + 24 if is_now and sl.get("next") else 0
        if when:
            m, dh = _arq_text(x + 16, yy, when, w - 40 - pill_w, 15, "var(--c4)" if is_now else "var(--c2)", "phase when", 1)
            labels.append(m)
            yy += dh + 2
        m, dh = _arq_text(x + 16, yy, name, w - 32, 19, "var(--white)", "phase name", 1 if not wide else 2)
        labels.append(m)
        yy += dh + 6
        its = [str(i) for i in list(items)[:3]]
        if not wide and its:
            labels.append(_arq_text(x + 16, yy, " · ".join(its), w - 32, 15, "var(--muted)", "phase items", 1, False,
                                    clip=True)[0])
        else:
            for it in its:
                if yy + lh > y + h - 6:
                    break
                labels.append(f'<circle cx="{x + 22:.1f}" cy="{yy + lh * .45:.1f}" r="3" fill="var(--c2)"/>')
                m, dh = _arq_text(x + 32, yy, it, w - 48, 15, "var(--muted)", "phase item", 1, False, clip=True)
                labels.append(m)
                yy += dh + 1
        over.append(_arq_ring(x, y, w, h, t0 + step * .5, 16))
        if is_now:
            over.append(f'<rect x="{x - 9:.1f}" y="{y - 9:.1f}" width="{w + 18:.1f}" height="{h + 18:.1f}" rx="20" fill="none" '
                        f'stroke="var(--c4)" stroke-width="1.4">{loop("opacity", ".25;.8;.25", 2.4)}</rect>')
            if pill_w:
                ph_ = _k(15) + 13
                bx = x + w - pill_w - 12
                labels.append(f'<rect x="{bx:.1f}" y="{y + 10:.1f}" width="{pill_w:.1f}" height="{ph_:.1f}" rx="{ph_ / 2:.1f}" fill="var(--c4)"/>'
                              + _arq_line(bx + pill_w / 2, y + 10 + ph_ / 2 + _k(15) * .36, sl["next"], 15, "var(--ink)", True, "middle"))
    trav = f"M{pts[0][0]:.1f} {pts[0][1]:.1f} " + " ".join(f"L{x:.1f} {y:.1f}" for x, y in pts[1:])
    over.append(_arq_dot(trav, .08, .08 + .6, "var(--c4)", 8 * k))
    if sl.get("sign"):
        labels.append(_arq_text(zx + zw / 2, zy + zh - sign_h + 8, sl["sign"], zw - 20, 22, "var(--c2)", "sign", 1, True, "middle")[0])
    svg = seq(shapes, .1, .45, 10, 1.3) + "".join(over) + land("".join(labels), 1.0, .5, 8)
    return portrait_mark(svg), D, FREEZE
