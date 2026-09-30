"""Icon library of dynamic-commercial-decks (0.5.0): line icons on a 48-unit grid, one registry for every scene.

Loaded by assets/ext.py right after lib.py, in the same namespace. Contract:
  icon(name, x, y, size=48, color="var(--c2)", sw=1.8)  -> svg: the icon «vertical/key» centered at (x, y), size px wide
  icons(vertical)                                       -> [name, …] of that vertical, in catalog order
  ICONS                                                 -> {vertical: {key: (label_es, draw)}}
A draw function returns markup for a 48 x 48 box with its origin top-left: strokes only (fill="none" is set on the
group), except small accent dots, which use fill="currentColor". Colors come from the pack (var(--…)); an icon never
carries text. Every vertical has at least 4 icons (scripts/icons.py selftest; references/icons.md is the catalog).
Drawing rules: one stroke weight, 3-4 units of padding, round caps and joins, legible at 32 px.
"""
import math

ICON_VERTICALS = ("banca", "seguros", "salud", "energia", "mineria", "retail", "pagos", "telco", "industria",
                  "publico", "consumo", "logistica")
ICON_SETS = ICON_VERTICALS + ("arquitectura", "generico", "entrega", "uso", "ia")


# ---------------------------------------------------------------- drawing atoms (48 x 48 box); _i* names: shared namespace
def _iP(*ds):
    return "".join(f'<path d="{d}"/>' for d in ds)


def _iC(cx, cy, r):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}"/>'


def _iR(x, y, w, h, rx=3):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>'


def _iD(*pts, r=1.9):
    """Small filled accent dots."""
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="currentColor" stroke="none"/>' for x, y in pts)


def _i_star(cx, cy, R, r, n=5):
    pts = [(cx + (R, r)[k % 2] * math.sin(math.pi * k / n), cy - (R, r)[k % 2] * math.cos(math.pi * k / n)) for k in range(2 * n)]
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"


def _i_gear(cx=24, cy=24, R=18, r=13.5, teeth=8):
    pts = []
    for k in range(teeth):
        a = 2 * math.pi * k / teeth
        for da, rr in ((-.3, r), (-.17, R), (.17, R), (.3, r)):
            pts.append((cx + rr * math.cos(a + da), cy + rr * math.sin(a + da)))
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"


def _i_spark(cx, cy, R):
    """The four-point spark that marks an AI capability (concave sides, cusps at N/E/S/W)."""
    return (f"M{cx} {cy - R} Q{cx} {cy} {cx + R} {cy} Q{cx} {cy} {cx} {cy + R} Q{cx} {cy} {cx - R} {cy} "
            f"Q{cx} {cy} {cx} {cy - R} Z")


def _i_arc(cx, cy, r, a0, a1, head=0):
    """Arc from angle a0 to a1 in degrees (screen: 0 east, 90 south; clockwise when a1 > a0); head > 0 adds an arrowhead at a1."""
    pt = lambda a: (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
    (x0, y0), (x1, y1) = pt(a0), pt(a1)
    d = f"M{x0:.1f} {y0:.1f} A{r} {r} 0 {int(abs(a1 - a0) > 180)} {int(a1 > a0)} {x1:.1f} {y1:.1f}"
    if head:
        s, t = (1 if a1 > a0 else -1), math.radians(a1)
        tx, ty = -math.sin(t) * s, math.cos(t) * s
        (ax, ay), (bx, by) = [(x1 - head * (tx * math.cos(q) - ty * math.sin(q)), y1 - head * (tx * math.sin(q) + ty * math.cos(q)))
                              for q in (math.radians(35), math.radians(-35))]
        d += f" M{ax:.1f} {ay:.1f} L{x1:.1f} {y1:.1f} L{bx:.1f} {by:.1f}"
    return d


def _i_ticks(cx, cy, r0, r1, angles):
    return " ".join(f"M{cx + r0 * math.cos(math.radians(a)):.1f} {cy + r0 * math.sin(math.radians(a)):.1f} "
                    f"L{cx + r1 * math.cos(math.radians(a)):.1f} {cy + r1 * math.sin(math.radians(a)):.1f}" for a in angles)


_I_DOC = "M11 5 H29 L37 13 V41 C37 42 36 43 35 43 H13 C12 43 11 42 11 41 V7 C11 6 12 5 13 5 Z M29 5 V13 H37"
_I_CLIP = "M18 9 H14 C12 9 11 10 11 12 V40 C11 42 12 43 14 43 H34 C36 43 37 42 37 40 V12 C37 10 36 9 34 9 H30"


# {vertical: {key: (label_es, draw)}}; draw() -> markup in a 48 x 48 box
ICONS = {
    "banca": {
        "credito": ("Crédito", lambda: _iC(24, 24, 18) + _iP("M17 31 L31 17") + _iC(18.5, 18.5, 2.6) + _iC(29.5, 29.5, 2.6)),
        "ahorro": ("Ahorro", lambda: _iP("M9 24 C9 16 16 12 24 12 C31 12 36 15 38 19 L42 18 V26 L39 27 C38 30 36 32 34 33 V39 H29 V35 "
                                         "H19 V39 H14 V33 C11 31 9 28 9 24 Z", "M20 17 H28", "M9 22 C6 22 5 20 6 18")
                   + _iD((33, 20))),
        "tarjeta": ("Tarjeta", lambda: _iR(5, 11, 38, 26, 4) + _iP("M5 18 H43", "M11 30 H19", "M23 30 H27")),
        "sucursal": ("Sucursal", lambda: _iP("M6 17 L24 7 L42 17 Z", "M11 21 V35 M19 21 V35 M29 21 V35 M37 21 V35",
                                             "M8 36 H40 M5 41 H43")),
        "riesgo": ("Riesgo", lambda: _iP("M6 33 A18 18 0 0 1 42 33", "M24 33 L33 21", "M6 33 H11 M37 33 H42",
                                         "M12 21 L15 24 M24 16 V20 M36 21 L33 24") + _iD((24, 33), r=2.6)),
    },
    "seguros": {
        "poliza": ("Póliza", lambda: _iP(_I_DOC, "M16 19 H31 M16 25 H26",
                                         "M24 29 L31 31.5 V35.5 C31 39 28.5 41 24 42.5 C19.5 41 17 39 17 35.5 V31.5 Z")),
        "siniestro": ("Siniestro", lambda: _iP("M5 36 V30 C5 28 6 27 8 27 L13 19 H26 L33 27 H38 C40 27 41 28 41 30 V36",
                                               "M5 36 H9 M17 36 H27 M35 36 H41", "M16 27 H31")
                      + _iC(13, 36, 4) + _iC(31, 36, 4) + _iP("M38 7 L39 13 M44 11 L40 15 M34 9 L37 14")),
        "proteccion": ("Protección", lambda: _iP("M5 24 C5 14 13 7 24 7 C35 7 43 14 43 24 C40 21 36 21 33.5 24 C31 21 27 21 24 24 "
                                                 "C21 21 17 21 14.5 24 C12 21 8 21 5 24 Z", "M24 24 V37 C24 41 17 41 17 37")),
        "suscripcion": ("Suscripción", lambda: _iP(_I_CLIP, "M18 6 H30 V12 H18 Z", "M16 21 L18.5 23.5 L22.5 19.5 M26 22 H32",
                                                   "M16 32 L18.5 34.5 L22.5 30.5 M26 33 H32")),
        "hogar": ("Hogar", lambda: _iP("M6 23 L24 8 L42 23", "M11 19 V41 H37 V19", "M20 41 V30 H28 V41")),
    },
    "salud": {
        "consulta": ("Consulta", lambda: _iP("M13 6 H17 M29 6 H33", "M15 6 V16 A9 9 0 0 0 33 16 V6",
                                             "M24 25 V31 C24 37 29 40 33 40 C37 40 39 37 39 33") + _iC(39, 29.5, 3.5)),
        "pulso": ("Signos vitales", lambda: _iP("M24 41 C12 33 6 26 6 18 C6 12 10 7 15.5 7 C19.5 7 22.5 9.5 24 12.5 C25.5 9.5 28.5 7 "
                                                "32.5 7 C38 7 42 12 42 18 C42 26 36 33 24 41 Z", "M11 23 H18 L21 17 L25 29 L28 23 H37")),
        "medicamento": ("Medicamento", lambda: '<rect x="17" y="5" width="14" height="38" rx="7" transform="rotate(45 24 24)"/>'
                        + _iP("M19 19 L29 29")),
        "historia": ("Historia clínica", lambda: _iP("M5 13 C5 11 6 10 8 10 H18 L22 14 H40 C42 14 43 15 43 17 V38 C43 40 42 41 40 41 "
                                                     "H8 C6 41 5 40 5 38 Z", "M24 21 V35 M17 28 H31")),
        "hospital": ("Hospital", lambda: _iP("M9 42 V13 C9 12 10 11 11 11 H37 C38 11 39 12 39 13 V42", "M5 42 H43", "M24 16 V28 M18 22 H30",
                                             "M20 42 V34 H28 V42")),
    },
    "energia": {
        "torre": ("Transmisión", lambda: _iP("M24 5 L14 43 M24 5 L34 43", "M7 13 H41", "M7 13 V18 M41 13 V18 M17 13 V17 M31 13 V17",
                                             "M19.8 21 L30.6 31 M28.2 21 L17.4 31 M17.4 31 H30.6", "M11 43 H37")),
        "solar": ("Solar", lambda: _iP("M10 43 L16 25 H42 L36 43 Z", "M13 34 H39", "M24.7 25 L18.7 43 M33.3 25 L27.3 43")
                  + _iC(13, 12, 4.5) + _iP("M13 3.5 V5 M13 19 V20.5 M4.5 12 H6 M20 12 H21.5 M7 6 L8 7 M18 17 L19 18 M19 6 L18 7 M8 17 L7 18")),
        "ducto": ("Ducto", lambda: _iP("M5 24 H43 M5 34 H43", "M13 20 V38 M35 20 V38", "M24 24 V15", "M17 12 H31", "M24 12 V15")),
        "medidor": ("Medidor", lambda: _iR(10, 5, 28, 38, 5) + _iR(15, 10, 18, 9, 2) + _iP("M26 24 L19 33 H25 L22 39 L30 30 H24 Z")),
        "eolica": ("Eólica", lambda: _iP("M24 21 L23 43 H25 Z", "M18 43 H30", "M24 15.5 C22 11 23 6 24 3 C26 7 26.5 11 24 15.5 Z", "M21.8 19.3 C17 19.8 12.5 22.3 10 24 C14 24.5 18 23.5 21.8 19.3 Z", "M26.2 19.3 C31 19.8 35.5 22.3 38 24 C34 24.5 30 23.5 26.2 19.3 Z") + _iC(24, 18, 2.5)),
    },
    "mineria": {
        "casco": ("Seguridad", lambda: _iP("M9 32 C9 21 15 13 24 13 C33 13 39 21 39 32", "M5 32 H43 C44 32 44 37 43 37 H5 C4 37 4 32 5 32 Z",
                                           "M20 14 V24 M28 14 V24")),
        "mina": ("Mina", lambda: _iP("M4 41 L18 14 L26 24 L31 18 L44 41 Z", "M17 41 V33 C17 29 20 27 24 27 C28 27 31 29 31 33 V41",
                                     "M24 27 V41")),
        "volqueta": ("Acarreo", lambda: _iP("M4 14 H29 L27 29 H7 Z", "M29 20 H36 L42 27 V34 H39 M29 20 V34 H31",
                                            "M4 34 H8 M18 34 H23", "M32 23 H35 L38 27 H32 Z") + _iC(13, 35, 5) + _iC(35, 35, 4.5)),
        "mineral": ("Mineral", lambda: _iP("M15 9 H33 L42 20 L24 41 L6 20 Z", "M6 20 H42", "M19 9 L16 20 L24 41 L32 20 L29 9")),
        "pico": ("Extracción", lambda: _iP("M11 42 L29 17", "M13 11 Q31 2 42 20 Q31 12 13 11 Z")),
    },
    "retail": {
        "carrito": ("Compra", lambda: _iP("M4 8 H10 L15 32 H37 L41 15 H12", "M16 24 H38") + _iC(18, 39, 3) + _iC(34, 39, 3)),
        "tienda": ("Tienda", lambda: _iP("M6 17 L9 7 H39 L42 17", "M6 17 C6 21 12 21 12 17 C12 21 18 21 18 17 C18 21 24 21 24 17 "
                                         "C24 21 30 21 30 17 C30 21 36 21 36 17 C36 21 42 21 42 17", "M9 21 V41 H39 V21",
                                         "M13 41 V29 H21 V41", "M26 29 H34 V35 H26 Z")),
        "etiqueta": ("Precio", lambda: _iP("M7 9 C7 8 8 7 9 7 H23 L41 25 C42 26 42 27 41 28 L28 41 C27 42 26 42 25 41 L7 23 Z")
                     + _iC(15, 15, 3)),
        "lealtad": ("Lealtad", lambda: _iP(_i_star(24, 25, 19, 8))),
        "bolsa": ("Venta", lambda: _iP("M9 17 H39 L37 41 C37 42 36 43 35 43 H13 C12 43 11 42 11 41 Z",
                                       "M18 22 V13 C18 9 21 6 24 6 C27 6 30 9 30 13 V22")),
    },
    "pagos": {
        "pos": ("Datáfono", lambda: _iR(12, 5, 24, 38, 4) + _iR(16, 9, 16, 10, 1.5)
                + _iD((18.5, 26), (24, 26), (29.5, 26), (18.5, 31.5), (24, 31.5), (29.5, 31.5), (18.5, 37), (24, 37), (29.5, 37), r=1.6)),
        "billetera": ("Billetera", lambda: _iR(5, 13, 38, 28, 4) + _iP("M11 13 L31 6 L34 13", "M43 21 H33 C31 21 29 23 29 26 C29 29 31 31 33 31 H43")
                      + _iD((34, 26))),
        "transferencia": ("Transferencia", lambda: _iP("M8 16 H38 M31 9 L38 16 L31 23", "M40 32 H10 M17 25 L10 32 L17 39")),
        "qr": ("Pago QR", lambda: _iR(6, 6, 13, 13, 2) + _iR(29, 6, 13, 13, 2) + _iR(6, 29, 13, 13, 2)
               + _iD((12.5, 12.5), (35.5, 12.5), (12.5, 35.5), r=2.2) + _iP("M29 29 H34 V34", "M38 29 H42", "M42 34 V42 H37", "M29 38 V42 H32")
               + _iD((25, 25), (37.5, 37.5), r=1.6)),
        "movil": ("Pago móvil", lambda: _iR(8, 5, 20, 38, 4) + _iP("M15 10 H21", "M16 38 H20", "M32 18 Q35.5 24 32 30", "M37 13 Q44 24 37 35")),
    },
    "telco": {
        "antena": ("Antena", lambda: _iP("M24 20 L16 43 M24 20 L32 43", "M19.6 33 H28.4", "M16 43 H32", "M16 9 C13 13 13 19 16 23",
                                         "M11 5 C6 11 6 21 11 27", "M32 9 C35 13 35 19 32 23", "M37 5 C42 11 42 21 37 27") + _iC(24, 16, 3)),
        "fibra": ("Fibra", lambda: _iR(4, 31, 9, 10, 2) + _iP("M13 36 C24 36 24 13 38 13", "M13 36 C24 36 26 25 38 25", "M13 36 H38")
                  + _iD((41, 13), (41, 25), (41, 36), r=2.4)),
        "sim": ("Línea", lambda: _iP("M13 5 H29 L37 13 V40 C37 42 36 43 34 43 H14 C12 43 11 42 11 40 V7 C11 6 12 5 13 5 Z")
                + _iR(16, 20, 16, 16, 2) + _iP("M16 28 H32 M24 20 V36")),
        "cobertura": ("Cobertura", lambda: _iR(6, 32, 6, 10, 1.5) + _iR(15.5, 25, 6, 17, 1.5) + _iR(25, 17, 6, 25, 1.5) + _iR(34.5, 8, 6, 34, 1.5)),
        "satelite": ("Satélite", lambda: '<g transform="rotate(-45 24 24)">' + _iR(19, 18, 10, 12, 2) + _iR(3, 19, 12, 10, 1.5)
                     + _iR(33, 19, 12, 10, 1.5) + _iP("M15 24 H19 M29 24 H33 M9 19 V29 M39 19 V29") + '</g>'
                     + _iP("M33 34 C35 34 38 37 38 39", "M34 29 C39 29 43 34 43 38")),
    },
    "industria": {
        "fabrica": ("Planta", lambda: _iP("M5 42 V23 L14 17 V23 L23 17 V23 L32 17 V8 H40 V42 Z", "M3 42 H45") + _iR(10, 29, 5, 5, 1)
                    + _iR(19, 29, 5, 5, 1) + _iR(28, 29, 5, 5, 1)),
        "engranaje": ("Mantenimiento", lambda: _iP(_i_gear()) + _iC(24, 24, 5.5)),
        "robot": ("Automatización", lambda: _iP("M8 42 H32", "M12 42 C12 37 15.5 35 20 35 C24.5 35 28 37 28 42", "M18.5 32.5 L13.5 23.5 M22 32 L17 23",
                                                "M17.5 18.5 L28.5 12.5 M18.5 21.5 L29.5 15.5", "M34 11 L41 9 M35 16 L41 18")
                   + _iC(15, 21, 3.5) + _iC(32, 14, 3)),
        "silo": ("Producción", lambda: _iP("M10 16 C10 9 16 5 24 5 C32 5 38 9 38 16 V42 H10 Z", "M10 16 H38 M10 24 H38 M10 32 H38",
                                           "M6 42 H42")),
        "linea": ("Línea de producción", lambda: _iR(4, 31, 40, 10, 5) + _iC(10, 36, 2) + _iC(24, 36, 2) + _iC(38, 36, 2)
                  + _iR(9, 17, 11, 14, 1.5) + _iR(27, 21, 11, 10, 1.5)),
    },
    "publico": {
        "edificio": ("Entidad", lambda: _iP("M14 21 C14 14 18.5 10 24 10 C29.5 10 34 14 34 21", "M9 21 H39", "M24 10 V4 H30 L28 6 L30 8 H24",
                                            "M13 25 V36 M20 25 V36 M28 25 V36 M35 25 V36", "M8 37 H40 M5 42 H43")),
        "ciudadano": ("Ciudadano", lambda: _iR(5, 10, 38, 28, 4) + _iC(16, 21, 4) + _iP("M9 32 C9 28 12 26 16 26 C20 26 23 28 23 32",
                                                                                     "M28 19 H37 M28 25 H37 M28 31 H33")),
        "tramite": ("Trámite", lambda: _iP("M19 21 C19 16 15 14 15 10 C15 6.5 19 4 24 4 C29 4 33 6.5 33 10 C33 14 29 16 29 21 H37 "
                                           "C39 21 40 22 40 24 V31 H8 V24 C8 22 9 21 11 21 Z", "M8 36 H40", "M14 42 H34")),
        "normativa": ("Normativa", lambda: _iP("M24 7 V41", "M17 41 H31", "M9 12 H39", "M9 12 L4 26 M9 12 L14 26", "M39 12 L34 26 M39 12 L44 26",
                                               "M4 26 H14 C14 30 12 32 9 32 C6 32 4 30 4 26 Z",
                                               "M34 26 H44 C44 30 42 32 39 32 C36 32 34 30 34 26 Z") + _iC(24, 8, 2)),
        "ciudad": ("Ciudad", lambda: _iP("M4 42 H44", "M7 42 V22 H17 V42", "M17 42 V8 H30 V42", "M30 42 V17 H41 V42")
                   + _iD((21.5, 14), (25.5, 14), (21.5, 21), (25.5, 21), (21.5, 28), (25.5, 28), (12, 28), (35.5, 24), (35.5, 31), r=1.4)),
    },
    "consumo": {
        "empaque": ("Empaque", lambda: _iP("M14 16 L19 6 H29 L34 16 V42 H14 Z", "M14 16 H34", "M19 6 L24 16 L29 6", "M14 25 H34",
                                           "M20 33 H28")),
        "anaquel": ("Anaquel", lambda: _iP("M6 6 V43 M42 6 V43", "M6 20 H42 M6 34 H42 M6 43 H42") + _iR(10, 11, 6, 9, 1) + _iR(19, 13, 6, 7, 1)
                    + _iR(28, 10, 9, 10, 1) + _iR(10, 26, 8, 8, 1) + _iR(22, 27, 5, 7, 1) + _iR(31, 25, 7, 9, 1)),
        "marca": ("Marca", lambda: _iC(24, 18, 12) + _iC(24, 18, 6) + _iP("M17 28 L13 43 L19 40 L22 44", "M31 28 L35 43 L29 40 L26 44")),
        "demanda": ("Demanda", lambda: _iP("M6 6 V42 H42", "M12 34 L20 25 L27 30 L39 15", "M31 15 H39 V23")),
        "canasta": ("Canasta", lambda: _iP("M5 21 H43", "M8 21 L11 40 C11 41 12 42 13 42 H35 C36 42 37 41 37 40 L40 21",
                                           "M15 21 L21 8 M33 21 L27 8", "M18 27 V36 M24 27 V36 M30 27 V36")),
    },
    "logistica": {
        "camion": ("Transporte", lambda: _iP("M28 34 V12 H6 C5 12 4 13 4 14 V34 H8", "M16 34 H31", "M28 18 H36 L43 26 V34 H39",
                                             "M31 21 H35 L39 26 H31 Z") + _iC(12, 35, 4) + _iC(35, 35, 4)),
        "bodega": ("Bodega", lambda: _iP("M4 18 L24 7 L44 18", "M8 16 V42 H40 V16", "M16 42 V25 H32 V42", "M16 30 H32 M16 35 H32")),
        "ruta": ("Ruta", lambda: _iC(10, 38, 3.5) + '<path d="M14 38 C23 38 19 28 27 28 C31 28 33 27 34 25" stroke-dasharray="3 4"/>'
                 + _iP("M34 23 C30 18 27 15 27 11 A7 7 0 0 1 41 11 C41 15 38 18 34 23 Z") + _iD((34, 11), r=2)),
        "caja": ("Despacho", lambda: _iP("M24 6 L41 14 V34 L24 42 L7 34 V14 Z", "M7 14 L24 22 L41 14", "M24 22 V42", "M15.5 10 L32.5 18 V24")),
        "barco": ("Carga marítima", lambda: _iP("M5 29 H43 L38 39 H10 Z", "M11 29 V21 H22 V29", "M22 29 V16 H33 V29", "M28 16 V9 H33",
                                                "M6 44 C9 42 12 42 15 44 C18 46 21 46 24 44 C27 42 30 42 33 44 C36 46 39 46 42 44")),
    },
    "arquitectura": {
        "persona": ("Persona", lambda: _iC(24, 14, 7.5) + _iP("M9 42 V36 C9 29 15 25 24 25 C33 25 39 29 39 36 V42 Z")),
        "sistema": ("Sistema", lambda: _iR(5, 8, 38, 32, 4) + _iP("M5 16 H43", "M12 24 H30 M12 31 H24") + _iD((10, 12), (14.5, 12), (19, 12), r=1.5)),
        "externo": ("Sistema externo", lambda: '<rect x="5" y="13" width="29" height="29" rx="4" stroke-dasharray="4 4"/>'
                    + _iP("M21 27 L41 7", "M30 7 H41 V18")),
        "contenedor": ("Contenedor", lambda: _iR(5, 12, 38, 24, 2) + _iP("M12 16 V32 M18 16 V32 M24 16 V32 M30 16 V32 M36 16 V32")),
        "componente": ("Componente", lambda: _iP("M12 15 V10 C12 9 13 8 14 8 H38 C39 8 40 9 40 10 V38 C40 39 39 40 38 40 H14 C13 40 12 39 12 38 V33",
                                                 "M12 21 V27") + _iR(7, 15, 10, 6, 1.5) + _iR(7, 27, 10, 6, 1.5)),
        "base-datos": ("Base de datos", lambda: '<ellipse cx="24" cy="11" rx="15" ry="5"/>'
                       + _iP("M9 11 V37 C9 40 15.7 42 24 42 C32.3 42 39 40 39 37 V11", "M9 24 C9 27 15.7 29 24 29 C32.3 29 39 27 39 24")),
        "cola": ("Cola de mensajes", lambda: _iP("M5 15 H33 M5 33 H33") + _iR(8, 19, 6, 10, 1.5) + _iR(16, 19, 6, 10, 1.5) + _iR(24, 19, 6, 10, 1.5)
                 + _iP("M34 24 H43 M39 20 L43 24 L39 28")),
        "api": ("API", lambda: _iP("M16 8 C12 8 12 10 12 14 V19 C12 22 10 24 7 24 C10 24 12 26 12 29 V34 C12 38 12 40 16 40",
                                   "M32 8 C36 8 36 10 36 14 V19 C36 22 38 24 41 24 C38 24 36 26 36 29 V34 C36 38 36 40 32 40")
                + _iD((19, 24), (24, 24), (29, 24), r=2)),
        "nube": ("Nube", lambda: _iP("M14 37 H35 C40 37 43 33 43 28.5 C43 24 39.5 20.5 35 20.5 C34 14.5 29 10 23 10 C16.5 10 12 15 12 21 "
                                     "C8 21.5 5 25 5 29 C5 33.5 9 37 14 37 Z")),
        "servidor": ("Servidor", lambda: _iR(7, 6, 34, 10, 2.5) + _iR(7, 19, 34, 10, 2.5) + _iR(7, 32, 34, 10, 2.5)
                     + _iP("M12 11 H22 M12 24 H22 M12 37 H22") + _iD((35, 11), (35, 24), (35, 37), r=1.7)),
        "red": ("Red", lambda: _iC(24, 24, 4.5) + _iC(9, 10, 3.5) + _iC(39, 10, 3.5) + _iC(9, 38, 3.5) + _iC(39, 38, 3.5)
                + _iP("M11.6 12.5 L20.8 20.8 M36.4 12.5 L27.2 20.8 M11.6 35.5 L20.8 27.2 M36.4 35.5 L27.2 27.2", "M12.5 10 H35.5 M12.5 38 H35.5")),
        "almacenamiento": ("Almacenamiento", lambda: _iR(5, 8, 38, 9, 2) + _iP("M8 17 V39 C8 40 9 41 10 41 H38 C39 41 40 40 40 39 V17",
                                                                               "M19 24 H29")),
        "lago": ("Lago de datos", lambda: _iP("M5 31 C9 28 13 28 17 31 C21 34 25 34 29 31 C33 28 37 28 41 31",
                                              "M5 39 C9 36 13 36 17 39 C21 42 25 42 29 39 C33 36 37 36 41 39")
                 + _iR(11, 12, 6, 6, 1.5) + _iR(21, 6, 6, 6, 1.5) + _iR(31, 13, 6, 6, 1.5) + _iD((24, 20), (14, 23), (34, 24), r=1.5)),
        "pipeline": ("Pipeline", lambda: _iP("M4 14 H13 L19 24 L13 34 H4 L10 24 Z", "M17 14 H26 L32 24 L26 34 H17 L23 24 Z",
                                             "M30 14 H38 L44 24 L38 34 H30 L36 24 Z")),
        "seguridad": ("Seguridad", lambda: _iP("M24 5 L39 11 V22 C39 32 32 39 24 43 C16 39 9 32 9 22 V11 Z",
                                               "M20 22 V19 C20 16.5 22 15 24 15 C26 15 28 16.5 28 19 V22") + _iR(17, 22, 14, 11, 2)),
        "monitoreo": ("Monitoreo", lambda: _iR(5, 7, 38, 27, 3) + _iP("M17 41 H31 M24 34 V41", "M10 27 L17 20 L23 24 L31 14 L38 18")),
    },
    "generico": {
        "meta": ("Meta", lambda: _iC(22, 26, 17) + _iC(22, 26, 10) + _iD((22, 26), r=3) + _iP("M22 26 L38 10", "M34 6 V10 H38 L42 6 H38 V2")),
        "dato": ("Dato", lambda: _iP("M6 42 H42") + _iR(10, 27, 7, 15, 1.5) + _iR(20.5, 17, 7, 25, 1.5) + _iR(31, 8, 7, 34, 1.5)),
        "ia": ("IA", lambda: _iP("M21 8 C22 18 24 21 34 23 C24 25 22 28 21 38 C20 28 18 25 8 23 C18 21 20 18 21 8 Z",
                                 "M37 5 C37.4 9 38.5 10.1 42 10.5 C38.5 10.9 37.4 12 37 16 C36.6 12 35.5 10.9 32 10.5 C35.5 10.1 36.6 9 37 5 Z")
                + _iD((37, 38), r=2.2)),
        "equipo": ("Equipo", lambda: _iC(24, 15, 5.5) + _iP("M14 38 C14 29 18 25 24 25 C30 25 34 29 34 38") + _iC(11, 19, 4) + _iC(37, 19, 4)
                   + _iP("M4 35 C4 29 7 26.5 11 26.5 C13 26.5 14.5 27 16 28", "M44 35 C44 29 41 26.5 37 26.5 C35 26.5 33.5 27 32 28")),
        "reloj": ("Tiempo", lambda: _iC(24, 24, 18) + _iP("M24 13 V24 L31 29")),
        "alerta": ("Alerta", lambda: _iP("M21.4 8.5 C22.6 6.5 25.4 6.5 26.6 8.5 L42.5 36 C43.6 38 42.2 40.5 40 40.5 H8 C5.8 40.5 4.4 38 5.5 36 Z",
                                         "M24 18 V28") + _iD((24, 34), r=2)),
        "check": ("Validado", lambda: _iC(24, 24, 18) + _iP("M16 24.5 L21.5 30 L32 19")),
        "documento": ("Documento", lambda: _iP(_I_DOC, "M16 20 H32 M16 26 H32 M16 32 H27")),
    },
    # the software-delivery cycle (a set, not a vertical): the glyphs of the m07/n05 hypothesis scenes, drawn so that
    # icon(name, 0, 0, 30, "var(--c2)", 1.5) reproduces them exactly (48 grid = 24 + 1.6 x the old glyph coordinates)
    "entrega": {
        "requisito": ("Requisito", lambda: _iR(9.6, 6.4, 28.8, 35.2, 4.8) + _iP("M17.6 17.6 H30.4 M17.6 25.6 H30.4 M17.6 33.6 H25.6")),
        "codigo": ("Código", lambda: _iP("M14.4 11.2 L3.2 24 L14.4 36.8 M33.6 11.2 L44.8 24 L33.6 36.8 M28.8 8 L19.2 40")),
        "prueba": ("Prueba", lambda: _iP("M9.6 24 L19.2 33.6 L38.4 12.8")),
        "despliegue": ("Despliegue", lambda: _iP("M24 40 V9.6 M12.8 20.8 L24 9.6 L35.2 20.8")),
    },
}

_I_TRAY = "M7 31 V38 C7 40.5 8 42 10 42 H38 C40 42 41 40.5 41 38 V31"
_I_SHIELD = "M24 5 L39 11 V22 C39 32 32 39 24 43 C16 39 9 32 9 22 V11 Z"

# the everyday UI vocabulary (a set, not a vertical). Keys may repeat another set's (alerta, equipo, reloj, nube,
# codigo): a bare key still resolves to the older set, so write "uso/<key>". The file formats read by shape, never by
# letters: archivo = blank page, doc = lines, xls = grid, ppt = slide frame, pdf = seal.
ICONS["uso"] = {
    "info": ("Información", lambda: _iC(24, 24, 18) + _iP("M24 22 V33") + _iD((24, 15.5), r=2.2)),
    "alerta": ("Alerta", lambda: _iP("M12 34 V22 C12 14 17 9 24 9 C31 9 36 14 36 22 V34 L39 37 H9 Z", "M24 5 V9",
                                     "M20.5 40.5 A3.5 3.5 0 0 0 27.5 40.5")),
    "mensaje": ("Mensaje", lambda: _iP("M9 8 H39 C41 8 42 9 42 11 V31 C42 33 41 34 39 34 H20 L11 41 V34 H9 C7 34 6 33 6 31 V11 C6 9 7 8 9 8 Z",
                                       "M14 17 H34 M14 25 H28")),
    "mail": ("Correo", lambda: _iR(5, 10, 38, 28, 4) + _iP("M7 13 L24 26 L41 13")),
    "web": ("Web", lambda: _iC(24, 24, 18) + '<ellipse cx="24" cy="24" rx="8" ry="18"/>' + _iP("M6 24 H42", "M9 15 H39 M9 33 H39")),
    "codigo": ("Código", lambda: _iR(5, 8, 38, 32, 4) + _iP("M5 16 H43", "M18 23 L13 28 L18 33 M30 23 L35 28 L30 33 M26.5 21 L21.5 35")),
    "chat": ("Chat", lambda: _iP("M9 6 H27 C29 6 30 7 30 9 V21 C30 23 29 24 27 24 H15 L9 29 V24 C7 24 6 23 6 21 V9 C6 7 7 6 9 6 Z",
                                 "M30 16 H39 C41 16 42 17 42 19 V33 C42 35 41 36 39 36 V41 L33 36 H21 C19 36 18 35 18 33 V24")),
    "calendario": ("Calendario", lambda: _iR(6, 9, 36, 33, 4) + _iP("M6 18 H42", "M16 5 V12 M32 5 V12")
                   + _iD((15, 26), (24, 26), (33, 26), (15, 34), (24, 34), r=1.8)),
    "telefono": ("Teléfono", lambda: _iP("M17 6 L21 15 L17.5 18.5 C19.5 23.5 24.5 28.5 29.5 30.5 L33 27 L42 31 V37 C42 40 40 42 37 42 "
                                         "C20 41 7 28 6 11 C6 8 8 6 11 6 Z")),
    "busqueda": ("Búsqueda", lambda: _iC(21, 21, 13) + _iP("M30.5 30.5 L41 41")),
    "filtro": ("Filtro", lambda: _iP("M6 8 H42 L28 25 V37 L20 42 V25 Z")),
    "descarga": ("Descarga", lambda: _iP("M24 6 V29", "M15 20 L24 29 L33 20", _I_TRAY)),
    "subir": ("Subir", lambda: _iP("M24 29 V6", "M15 15 L24 6 L33 15", _I_TRAY)),
    "compartir": ("Compartir", lambda: _iC(35, 11, 5) + _iC(13, 24, 5) + _iC(35, 37, 5) + _iP("M17.3 21.5 L30.7 13.5 M17.3 26.5 L30.7 34.5")),
    "enlace": ("Enlace", lambda: '<g transform="rotate(-45 24 24)">' + _iR(5, 18, 22, 12, 6) + _iR(21, 18, 22, 12, 6) + '</g>'),
    "usuario": ("Usuario", lambda: _iC(24, 24, 18) + _iC(24, 19, 6) + _iP("M12.5 37 C14.5 31.5 18.5 29 24 29 C29.5 29 33.5 31.5 35.5 37")),
    "equipo": ("Equipo", lambda: _iC(18, 15, 6) + _iP("M6 40 C6 31 11 26 18 26 C25 26 30 31 30 40") + _iC(33, 17, 4.5)
               + _iP("M33 26 C38.5 26 42 30 42 37")),
    "candado": ("Candado", lambda: _iR(10, 21, 28, 21, 4) + _iP("M16 21 V15 C16 10 19.5 7 24 7 C28.5 7 32 10 32 15 V21", "M24 30 V35")
                + _iD((24, 30), r=2.2)),
    "llave": ("Llave", lambda: _iC(14, 24, 8) + _iP("M22 24 H42 V31 M35 24 V30")),
    "nube": ("Nube", lambda: _iP("M14 37 H35 C39.5 37 43 33.5 43 29 C43 24.5 39.5 21 35 21 C34 15 29 11 23 11 C16.5 11 12 16 12 22 "
                                 "C8 22.5 5 26 5 30 C5 34 9 37 14 37 Z", "M24 33 V22 M19.5 26.5 L24 22 L28.5 26.5")),
    "ok": ("Aprobado", lambda: _iR(7, 7, 34, 34, 6) + _iP("M15 24.5 L21 30.5 L33 18")),
    "error": ("Error", lambda: _iC(24, 24, 18) + _iP("M17.5 17.5 L30.5 30.5 M30.5 17.5 L17.5 30.5")),
    "pendiente": ("Pendiente", lambda: _iP("M12 6 H36 M12 42 H36", "M15 6 C15 16 21 19 21 24 C21 29 15 32 15 42",
                                           "M33 6 C33 16 27 19 27 24 C27 29 33 32 33 42", "M19 38 L24 34 L29 38 Z")),
    "flecha-der": ("Avanzar", lambda: _iP("M7 24 H41", "M30 13 L41 24 L30 35")),
    "flecha-arr": ("Subir nivel", lambda: _iP("M24 41 V7", "M13 18 L24 7 L35 18")),
    "sincronizar": ("Sincronizar", lambda: _iP(_i_arc(24, 24, 16, -20, -160, 6), _i_arc(24, 24, 16, 160, 20, 6))),
    "ajustes": ("Ajustes", lambda: _iP("M7 14 H12 M20 14 H41 M7 24 H27 M35 24 H41 M7 34 H16 M24 34 H41") + _iC(16, 14, 4) + _iC(31, 24, 4)
                + _iC(20, 34, 4)),
    "grafico": ("Gráfico", lambda: _iP("M22 10 A16 16 0 1 0 38 26 H22 Z", "M26 6 A16 16 0 0 1 42 22 H26 Z")),
    "tabla": ("Tabla", lambda: _iR(6, 8, 36, 32, 3) + _iP("M6 16 H42 M6 24 H42 M6 32 H42 M18 8 V40 M30 8 V40")),
    "carpeta": ("Carpeta", lambda: _iP("M5 13 C5 11 6 10 8 10 H18 L22 14 H40 C42 14 43 15 43 17 V38 C43 40 42 41 40 41 H8 C6 41 5 40 5 38 Z",
                                       "M5 20 H43")),
    "archivo": ("Archivo", lambda: _iP(_I_DOC)),
    "pdf": ("PDF", lambda: _iP(_I_DOC, "M16 17 H26", "M20.8 31.5 L19 40 L22 38.3 L24 40.5 L26 38.3 L29 40 L27.2 31.5")
                + _iC(24, 27, 5.5)),
    "xls": ("Hoja de cálculo", lambda: _iP(_I_DOC) + _iR(16, 18, 16, 18, 1.5) + _iP("M16 24 H32 M16 30 H32 M21.3 18 V36 M26.7 18 V36")),
    "doc": ("Documento de texto", lambda: _iP(_I_DOC, "M16 18 H26 M16 24 H32 M16 30 H32 M16 36 H28")),
    "ppt": ("Presentación", lambda: _iP(_I_DOC) + _iR(15, 18, 18, 13, 1.5) + _iP("M18 36 H30", "M21.5 21.5 L27 24.5 L21.5 27.5 Z")),
    "imprimir": ("Imprimir", lambda: _iP("M14 17 V6 H34 V17", "M14 33 H9 C7 33 6 32 6 30 V20 C6 18 7 17 9 17 H39 C41 17 42 18 42 20 V30 "
                                         "C42 32 41 33 39 33 H34", "M14 27 H34 V42 H14 Z", "M18 32 H30 M18 37 H26") + _iD((36.5, 22), r=1.7)),
    "reloj": ("Cronómetro", lambda: _iC(24, 27, 15) + _iP("M20 6 H28 M24 6 V12", "M24 27 V19", "M36 13 L39 10")),
    "ubicacion": ("Ubicación", lambda: _iP("M24 43 C18 36 10 28 10 19 A14 14 0 0 1 38 19 C38 28 30 36 24 43 Z") + _iC(24, 19, 5)),
    "estrella": ("Destacado", lambda: _iP(_i_star(24, 25, 18, 7.5))),
    "bandera": ("Hito", lambda: _iP("M11 43 V6", "M11 8 C17 4 22 12 28 8 C32 5.5 35 5.5 38 7.5 V25.5 C35 23.5 32 23.5 28 26 "
                                    "C22 30 17 22 11 26")),
}

# AI capabilities (a set, not a vertical). The spark (_i_spark) marks "AI does this" only where the base drawing would
# otherwise read as plain software; every icon keeps a different base shape so no two read the same at 32 px.
ICONS["ia"] = {
    "resumen": ("Resumen", lambda: _iP("M5 12 H21 M5 19 H21 M5 26 H21 M5 33 H21 M5 40 H15", "M25 20 L30 26 L25 32",
                                       "M34 20 H43 M34 26 H43 M34 32 H40")),
    "clasificacion": ("Clasificación", lambda: _iR(6, 6, 36, 36, 4) + _iP("M24 6 V42 M6 24 H42") + _iC(15, 15, 4.5)
                      + _iP("M33 10.5 L37.5 19 H28.5 Z", "M33 28 L38 33 L33 38 L28 33 Z") + _iR(10.5, 28.5, 9, 9, 1.5)),
    "extraccion": ("Extracción", lambda: _iR(5, 6, 22, 36, 3) + _iP("M10 13 H22 M10 33 H22 M10 38 H18", "M24 23 H41 M37 19 L41 23 L37 27")
                   + '<rect x="8" y="18" width="16" height="10" rx="2" stroke-dasharray="3 3"/>'),
    "agente": ("Agente", lambda: _iR(9, 14, 30, 24, 7) + _iP("M24 14 V9", "M5 23 V29 M43 23 V29", "M19 31 H29")
               + _iD((24, 7), (18.5, 23.5), (29.5, 23.5), r=2.2)),
    "copiloto": ("Copiloto", lambda: _iC(17, 16, 6) + _iP("M5 41 C5 32 10 27 17 27 C24 27 29 32 29 41", _i_spark(36, 18, 8))),
    "rag": ("RAG", lambda: '<ellipse cx="14" cy="10" rx="9" ry="3.5"/>'
            + _iP("M5 10 V26 C5 28 9 29.5 14 29.5 C19 29.5 23 28 23 26 V10", "M5 18 C5 20 9 21.5 14 21.5 C19 21.5 23 20 23 18",
                  "M14 33 V36 C14 38.5 15.5 40 18 40 H24 M21 37 L24 40 L21 43",
                  "M30 20 H40 C42 20 43 21 43 23 V32 C43 34 42 35 40 35 H38 V40 L33 35 H30 C28 35 27 34 27 32 V23 C27 21 28 20 30 20 Z",
                  _i_spark(35, 27.5, 4.5))),
    "ocr": ("OCR", lambda: _iP("M6 14 V9 C6 7.3 7.3 6 9 6 H14", "M34 6 H39 C40.7 6 42 7.3 42 9 V14", "M42 34 V39 C42 40.7 40.7 42 39 42 H34",
                               "M14 42 H9 C7.3 42 6 40.7 6 39 V34", "M15 16 H33 M15 32 H27", "M9 24 H39")),
    "prediccion": ("Predicción", lambda: _iC(24, 20, 14) + _iP("M17.7 32.5 L15 42 H33 L30.3 32.5", _i_spark(24, 20, 6))),
    "recomendacion": ("Recomendación", lambda: _iR(6, 21, 8, 20, 2) + _iP("M14 23 L21 8 C24 7 27 9 26.5 13 L25.5 19 H37 C40 19 42 22 41.3 25 "
                                                                         "L38.7 37.5 C38.3 39.5 36.6 41 34.6 41 H14")),
    "traduccion": ("Traducción", lambda: _iP("M8 6 H24 C26 6 27 7 27 9 V19 C27 21 26 22 24 22 H13 L8 26 V22 C6.5 22 5 21 5 19 V9 C5 7 6 6 8 6 Z",
                                             "M10 12 H22 M10 17 H18",
                                             "M24 24 H40 C42 24 43 25 43 27 V35 C43 37 42 38 40 38 V42 L35 38 H24 C22 38 21 37 21 35 V27 C21 25 22 24 24 24 Z",
                                             "M26 31 C28 28 30 34 32 31 C34 28 36 34 38 31",
                                             "M32 8 C37 8 40 11 40 17 M37 14 L40 17 L43 14", "M17 41 C11 41 8 38 8 31 M5 34 L8 31 L11 34")),
    "transcripcion": ("Transcripción", lambda: _iP("M7 21 V27 M11.5 15 V33 M16 19 V29 M20.5 22 V26", "M24 24 H30 M27 21 L30 24 L27 27",
                                                   "M34 17 H43 M34 24 H43 M34 31 H40")),
    "busqueda-semantica": ("Búsqueda semántica", lambda: _iC(21, 21, 14) + _iP("M31 31 L41 41", _i_spark(21, 21, 7.5))),
    "deteccion-anomalias": ("Detección de anomalías", lambda: '<path d="M5 25 H43 M5 38 H43" stroke-dasharray="2 4"/>'
                            + _iD((9, 33), (15, 30), (21, 34), (27, 31), (39, 32), r=1.9) + _iC(32, 12, 5.5) + _iD((32, 12), r=2)),
    "generacion-texto": ("Generación de texto", lambda: _iP("M6 11 H27 M6 19 H23 M6 27 H16", "M20 41 L21.5 34 L35 20.5 L40.5 26 L27 39.5 Z",
                                                          "M31.5 24 L37 29.5", _i_spark(38, 10, 5))),
    "generacion-imagen": ("Generación de imagen", lambda: _iR(5, 14, 30, 26, 3) + _iP("M5 35 L14 26 L20 32 L25 27 L35 37", _i_spark(38, 10, 6))
                          + _iC(14, 21, 2.8)),
    "chatbot": ("Chatbot", lambda: _iP("M12 10 H36 C39.3 10 42 12.7 42 16 V28 C42 31.3 39.3 34 36 34 H21 L13 41 V34 H12 C8.7 34 6 31.3 6 28 "
                                       "V16 C6 12.7 8.7 10 12 10 Z", "M24 10 V7") + _iD((24, 5.5), (18, 22), (30, 22), r=2)),
    "sentimiento": ("Sentimiento", lambda: _iC(24, 24, 18) + _iP("M16 28 C18 33 30 33 32 28") + _iD((18, 19), (30, 19), r=2.2)),
    "pronostico": ("Pronóstico", lambda: _iP("M6 6 V42 H42", "M10 35 L16 29 L22 31", "M22 31 L38 11 M22 31 L38 27")
                   + '<path d="M22 31 L38 19" stroke-dasharray="2.5 3.5"/>'),
    "vision": ("Visión artificial", lambda: _iP("M4 24 C9 14 16 10 24 10 C32 10 39 14 44 24 C39 34 32 38 24 38 C16 38 9 34 4 24 Z")
               + _iC(24, 24, 6.5) + _iD((24, 24), r=2.4)),
    "voz": ("Voz", lambda: _iR(18, 5, 12, 22, 6) + _iP("M11 20 C11 28 17 33 24 33 C31 33 37 28 37 20", "M24 33 V41 M17 41 H31")),
    "embeddings": ("Embeddings", lambda: _iP("M8 6 V40 H43", "M8 40 L22 15 M8 40 L38 29")
                   + f'<path d="{_i_arc(8, 40, 13, -58, -23)}" stroke-dasharray="2 3"/>'
                   + _iD((22, 15), (38, 29), r=2.6) + _iD((33, 17), (41, 11), (16, 9), r=1.5)),
    "orquestacion": ("Orquestación", lambda: _iR(17, 5, 14, 10, 2.5) + _iP("M24 15 V22 M10 22 H38 M10 22 V29 M24 22 V29 M38 22 V29")
                     + _iC(10, 34, 5) + _iC(24, 34, 5) + _iC(38, 34, 5)),
    "evaluacion": ("Evaluación", lambda: _iP("M6 11 L9 14 L14 8", "M6 23 L9 26 L14 20", "M7 33 L13 39 M13 33 L7 39",
                                             "M20 11 H42 M20 23 H42 M20 36 H36")),
    "guardrail": ("Guardrail", lambda: _iR(5, 15, 38, 11, 3) + _iP("M5 20.5 H43", "M11 26 V41 M24 26 V41 M37 26 V41")),
    "humano-en-el-bucle": ("Humano en el bucle", lambda: _iP(_i_arc(24, 24, 18, -60, 240, 6)) + _iC(24, 20, 4.5)
                           + _iP("M16 33 C16 28.5 19.5 26.5 24 26.5 C28.5 26.5 32 28.5 32 33")),
    "prompt": ("Prompt", lambda: _iR(5, 9, 38, 30, 4) + _iP("M12 19 L17 24 L12 29", "M21 29 H31")),
    "fine-tuning": ("Ajuste fino", lambda: _iC(24, 26, 10) + _iP(_i_arc(24, 26, 17, 135, 405), _i_ticks(24, 26, 17, 13.5, (135, 270, 405)),
                                                                "M24 26 L29 21") + _iD((24, 26), r=2)),
    "conocimiento": ("Base de conocimiento", lambda: _iP("M24 13 C19 9 12 8.5 5 10 V38 C12 36.5 19 37 24 41 C29 37 36 36.5 43 38 V10 "
                                                         "C36 8.5 29 9 24 13 Z", "M24 13 V41")),
    "automatizacion": ("Automatización", lambda: _iP(_i_gear(18, 30, 13, 9.8, 8), "M36 4 L29 16 H35 L32 26 L41 13 H35 L38 4 Z")
                       + _iC(18, 30, 4)),
    "documento-inteligente": ("Documento inteligente", lambda: _iP(_I_DOC, "M16 19 H27 M16 25 H24", _i_spark(27, 34, 6.5))),
    "analitica": ("Analítica", lambda: _iR(10, 31, 5, 11, 1) + _iR(18, 25, 5, 17, 1) + _iR(26, 28, 5, 14, 1) + _iR(34, 21, 5, 21, 1)
                  + _iP("M10 22 L20 14 L28 18 L39 8") + _iD((39, 8), r=2)),
    "gobierno-ia": ("Gobierno de IA", lambda: _iP(_I_SHIELD, _i_spark(24, 23, 8))),
}


def icon(name, x, y, size=48, color="var(--c2)", sw=1.8):
    """The icon «vertical/key» (or a bare key, searched in catalog order) centered at (x, y), size px wide."""
    vert, _sep, key = name.rpartition("/")
    sets = [vert] if vert else list(ICON_SETS)
    for v in sets:
        if key in ICONS.get(v, {}):
            k = size / 48
            return (f'<g transform="translate({x - size / 2:.1f} {y - size / 2:.1f}) scale({k:.4f})" fill="none" '
                    f'stroke="{color}" stroke-width="{sw / k:.2f}" stroke-linecap="round" stroke-linejoin="round" '
                    f'color="{color}">{ICONS[v][key][1]()}</g>')
    raise KeyError(f"icon {name!r} is not in the catalog (references/icons.md)")


def icons(vertical):
    """The icon names of a vertical, «vertical/key», in catalog order."""
    return [f"{vertical}/{k}" for k in ICONS[vertical]]
