"""Genera los SVG locales del perfil (dirección «Fuera de registro», paleta Miles).

Uso desde la raíz: python assets/profile/generate.py
Solo usa la biblioteca estándar. Decisiones de diseño en docs/PROFILE-DESIGN.md.

Lenguaje visual: impresión de cómic con la tinta roja y la azul fuera de registro,
trama de puntos, contorno de tinta y movimiento «a dos» (12 fotogramas por
segundo, siempre a saltos). Cada pieza tiene una animación mínima en bucle y
una versión quieta cuando el visitante pide menos movimiento.
"""
from math import cos, hypot, pi, sin
from pathlib import Path
from xml.sax.saxutils import escape
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
FPS = 12

TEMAS = {
    "noche": {"fondo": "#120C18", "panel": "#1C1424", "tinta": "#F5EFE6",
              "suave": "#C9C0D3", "linea": "#3A2E46", "rojo": "#F0313C",
              "azul": "#3D7BFF", "amarillo": "#FFD23F", "contorno": "#F5EFE6",
              "sobre_amarillo": "#120C18"},
    "papel": {"fondo": "#FBF4E2", "panel": "#F3E9CF", "tinta": "#140E19",
              "suave": "#4D4556", "linea": "#DCCFB3", "rojo": "#D3121C",
              "azul": "#1F5FE0", "amarillo": "#FFD23F", "contorno": "#140E19",
              "sobre_amarillo": "#140E19"},
}
SANS = "'Arial Black', 'Helvetica Neue', Arial, Helvetica, sans-serif"
TEXTO = "Arial, Helvetica, sans-serif"
MONO = "Consolas, 'Liberation Mono', Menlo, monospace"
SERIF = "Fraunces, 'Playfair Display', Georgia, serif"

# CSS común: todo se mueve a saltos y se detiene si se pide menos movimiento.
CSS_BASE = ("*{transform-box:fill-box}"
            "@media (prefers-reduced-motion:reduce){*{animation:none!important}}")


def t(x, y, valor, tam, color, peso=400, fuente=TEXTO, extra=""):
    return (f'<text x="{x:g}" y="{y:g}" fill="{color}" font-family="{fuente}" '
            f'font-size="{tam}" font-weight="{peso}" {extra}>{escape(valor)}</text>')


def desfase(x, y, valor, tam, k, peso=700, fuente=SANS, d=1.5, extra=""):
    """Texto impreso con la tinta roja y la azul fuera de registro."""
    return ('<g opacity="0.85">'
            + t(x + d, y + d * 0.5, valor, tam, k["rojo"], peso, fuente, extra)
            + t(x - d, y - d * 0.5, valor, tam, k["azul"], peso, fuente, extra)
            + "</g>" + t(x, y, valor, tam, k["tinta"], peso, fuente, extra))


def trama(x0, y0, w, h, color, paso=11, rmax=4.2, origen=(0, 0), alcance=1.0, opacidad=1.0, clase=""):
    """Trama de puntos que se agranda hacia `origen` (coordenadas relativas 0..1)."""
    ox, oy = x0 + origen[0] * w, y0 + origen[1] * h
    diag = hypot(w, h) * alcance
    puntos, fila, y = [], 0, y0 + paso / 2
    while y < y0 + h:
        x = x0 + paso / 2 + (paso / 2 if fila % 2 else 0)
        while x < x0 + w:
            r = rmax * (1 - hypot(x - ox, y - oy) / diag)
            if r > 0.5:
                puntos.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}"/>')
            x += paso
        y += paso
        fila += 1
    c = f' class="{clase}"' if clase else ""
    return f'<g{c} fill="{color}" opacity="{opacidad}">{"".join(puntos)}</g>'


def guardar(nombre, w, h, cuerpo, titulo, css=""):
    estilo = f"<style>{CSS_BASE}{css}</style>" if css else ""
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" role="img" aria-label="{escape(titulo)}">'
           f'<title>{escape(titulo)}</title>{estilo}{cuerpo}</svg>\n')
    (ROOT / f"{nombre}.svg").write_text(svg, encoding="utf-8")


def anim(valores, dur, atributo="transform", tipo="translate", inicio="0s", repetir=True, tiempos=None):
    """Animación SMIL discreta (a saltos) para la tarjeta."""
    rep = 'repeatCount="indefinite"' if repetir else 'fill="freeze"'
    kt = f' keyTimes="{tiempos}"' if tiempos else ""
    if atributo == "transform":
        return (f'<animateTransform attributeName="transform" type="{tipo}" values="{valores}" '
                f'dur="{dur}s" calcMode="discrete" begin="{inicio}"{kt} {rep}/>')
    return (f'<animate attributeName="{atributo}" values="{valores}" dur="{dur}s" '
            f'calcMode="discrete" begin="{inicio}"{kt} {rep}/>')


# ---------------------------------------------------------------- Personaje
# «Daniel en el Spider-Verse»: ilustración original. Traje negro con líneas
# rojas, sudadera abierta, audífonos al cuello y la máscara en la mano.
# Sin logotipos ni rasgos de ningún personaje existente.

TINTA = "#0B070F"
PIEL, PIEL_SOMBRA = "#C99172", "#A06E55"
PELO = "#1B1216"
TRAJE, TRAJE_SOMBRA = "#17111D", "#0E0A12"
SUDADERA, SUDADERA_SOMBRA = "#3A2D45", "#2A2033"
ROJO_TRAJE = "#F0313C"

SILUETA = (  # contorno completo, usado para el halo rojo/azul desfasado
    '<path d="M90 18Q120 2 150 20L156 62Q156 98 136 104L136 112L172 118L196 190L206 226'
    'L224 238Q232 276 204 284Q178 280 180 248L176 222L178 262L168 264L160 352L168 374H128'
    'L124 352L120 268L114 352L112 374H70L80 352L72 262L64 262L60 252L48 204L62 124L104 112'
    'L104 104Q84 98 84 62Z"/>')


def personaje(animado=True):
    """Figura en coordenadas locales 0..240 x 0..380."""
    respira = anim("0 0;0 -1.5", 1.333) if animado else ""
    destello = (anim(f"#FFFFFF;#FFFFFF;{'#3D7BFF'};#FFFFFF", 3.0, "fill",
                     tiempos="0;0.82;0.86;0.94") if animado else "")
    web = ROJO_TRAJE

    # Telaraña del pecho: radios desde un punto, sin emblema.
    pecho = "".join(f'<path d="M120 150L{120 + 60 * cos(a):.0f} {150 + 70 * sin(a):.0f}"/>'
                    for a in [pi * (0.15 + 0.14 * j) for j in range(6)] + [-pi * 0.5])
    pecho += '<path d="M104 132Q120 140 136 132M98 172Q120 182 142 172M96 214Q120 226 144 214"/>'

    piernas = (
        f'<path d="M92 250L84 352H108L118 262Z" fill="{TRAJE}"/>'
        f'<path d="M122 262L134 352H158L150 250Z" fill="{TRAJE_SOMBRA}"/>'
        f'<g stroke="{web}" stroke-width="1.6" fill="none" opacity="0.9">'
        '<path d="M98 270L94 340M112 270L104 340M130 270L140 340M144 270L152 340"/>'
        '<path d="M90 300H114M128 300H154M88 330H110M132 330H156"/></g>'
        # zapatillas altas rojas y blancas
        f'<path d="M80 346H110L112 368H70Q70 356 80 346Z" fill="{ROJO_TRAJE}"/>'
        '<path d="M70 362H112V370H70Z" fill="#F5EFE6"/>'
        f'<path d="M132 346H162Q172 356 172 368H130Z" fill="{ROJO_TRAJE}"/>'
        '<path d="M130 362H172V370H130Z" fill="#F5EFE6"/>'
    )
    torso = (
        # capucha caída detrás de los hombros
        f'<ellipse cx="120" cy="114" rx="58" ry="16" fill="{SUDADERA_SOMBRA}"/>'
        # traje
        f'<path d="M78 120H162L152 252H88Z" fill="{TRAJE}"/>'
        f'<g stroke="{web}" stroke-width="1.8" fill="none">{pecho}</g>'
        # sudadera abierta
        f'<path d="M64 118H102L98 262H68Z" fill="{SUDADERA}"/>'
        f'<path d="M138 118H176L174 262H142Z" fill="{SUDADERA_SOMBRA}"/>'
        f'<path d="M100 120V258M140 120V258" stroke="{TINTA}" stroke-width="2"/>'
        # brazo izquierdo, relajado
        f'<path d="M64 122L48 204L54 250H72L78 200L84 140Z" fill="{SUDADERA}"/>'
        f'<path d="M52 246H74L72 268Q62 274 52 266Z" fill="{TRAJE}"/>'
        # brazo derecho, doblado hacia la cadera
        f'<path d="M176 122L198 192L190 228L172 222L178 192L160 140Z" fill="{SUDADERA_SOMBRA}"/>'
        f'<path d="M172 218L192 224L190 240L174 238Z" fill="{TRAJE}"/>'
        # cuello y audífonos
        f'<path d="M108 92H132V114H108Z" fill="{PIEL_SOMBRA}"/>'
        f'<path d="M92 114Q120 136 148 114" stroke="#26202C" stroke-width="7" fill="none"/>'
        f'<circle cx="92" cy="114" r="10" fill="{ROJO_TRAJE}"/><circle cx="148" cy="114" r="10" fill="{ROJO_TRAJE}"/>'
        # cabeza
        f'<ellipse cx="120" cy="62" rx="31" ry="37" fill="{PIEL}"/>'
        f'<path d="M120 25Q151 30 151 62Q151 96 120 99Z" fill="{PIEL_SOMBRA}" opacity="0.55"/>'
        f'<path d="M86 58Q84 18 120 16Q158 16 154 58Q148 40 132 36Q138 46 128 44Q114 30 96 44Q92 50 86 58Z" fill="{PELO}"/>'
        f'<path d="M104 58H114M126 58H136" stroke="{TINTA}" stroke-width="3" stroke-linecap="round"/>'
        f'<path d="M102 50L115 48M125 48L138 50" stroke="{PELO}" stroke-width="3" stroke-linecap="round"/>'
        f'<path d="M120 62L117 74H122" stroke="{PIEL_SOMBRA}" stroke-width="2" fill="none"/>'
        f'<path d="M110 84Q120 89 130 84" stroke="{TINTA}" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
    )
    mascara = (
        f'<path d="M206 234Q230 238 228 268Q224 294 206 296Q186 294 184 268Q182 238 206 234Z" fill="{TRAJE}"/>'
        f'<g stroke="{web}" stroke-width="1.4" fill="none">'
        '<path d="M206 236V294M186 256Q206 262 226 256M185 278Q206 284 227 278"/>'
        '<path d="M206 266L188 244M206 266L224 244M206 266L190 290M206 266L222 290"/></g>'
        f'<path d="M190 258L203 264L200 274Q192 272 190 258Z" fill="#FFFFFF" stroke="{TINTA}" stroke-width="1.5">{destello}</path>'
        f'<path d="M222 258L209 264L212 274Q220 272 222 258Z" fill="#FFFFFF" stroke="{TINTA}" stroke-width="1.5">{destello}</path>'
        f'<path d="M184 226Q192 222 196 232" stroke="{TINTA}" stroke-width="3" fill="none"/>'
    )
    halo = (f'<g fill="#3D7BFF" transform="translate(-5 0)" opacity="0.9">{SILUETA}</g>'
            f'<g fill="{ROJO_TRAJE}" transform="translate(5 1)" opacity="0.9">{SILUETA}</g>'
            f'<g fill="{TINTA}">{SILUETA}</g>')
    return (halo + f'<g stroke-linejoin="round">{piernas}<g>{torso}{mascara}{respira}</g></g>')


def sentido_aracnido(cx, cy, escala, animado=True):
    """Líneas onduladas alrededor de la cabeza que vibran a saltos."""
    def zig(x, y, lado, fase):
        pts = [f"{x + lado * i * 7:.0f} {y + (5 if (i + fase) % 2 else -5)}" for i in range(5)]
        return "M" + "L".join(pts)
    lineas = ""
    for lado in (-1, 1):
        for j, dy in enumerate((-22, 0, 22)):
            x = cx + lado * (44 + abs(dy) * 0.3) * escala
            a, b = zig(x, cy + dy * escala, lado, 0), zig(x, cy + dy * escala, lado, 1)
            vibra = anim(f"{a};{b}", 2 / FPS * 2, "d") if animado else ""
            lineas += f'<path d="{a}">{vibra}</path>'
    aparece = anim("0;1;1;0", 4.0, "opacity", tiempos="0;0.55;0.8;1") if animado else ""
    return (f'<g fill="none" stroke="{ROJO_TRAJE}" stroke-width="{3 * escala:.1f}" stroke-linecap="round" '
            f'opacity="{1 if not animado else 0}">{lineas}{aparece}</g>')


# ---------------------------------------------------------------- Tarjeta

PASOS = ["-30 -8", "-21 -6", "-14 -4", "-9 -3", "-5 -2", "-3 -1", "-2 -1"]
COLORES_AURORA = {  # aurora turquesa/magenta -> cielo rojo y púrpura de Brooklyn
    "#0e1b3a": "#2A1030", "#070b22": "#14091C", "#03050f": "#08040B",
    "#3fffe6": "#FF3B47", "#7df9ff": "#FF8A6E", "#ff3d8a": "#7B2CFF",
    "#a78bfa": "#B16CFF", "#94a3b8": "#C9C0D3",
}


def horizonte(w):
    """Azoteas de Brooklyn con tanques de agua, en tinta casi negra."""
    edificios = [(0, 300, 70), (70, 278, 60), (130, 312, 80), (210, 262, 56), (266, 292, 90),
                 (356, 270, 64), (420, 300, 70), (490, 254, 50), (540, 286, 96), (636, 268, 60),
                 (696, 296, 84), (780, 276, 70), (850, 300, 90), (940, 262, 70), (1010, 288, 90),
                 (1100, 272, 100)]
    s = ""
    for x, y, ancho in edificios:
        if x > w:
            break
        s += f'<rect x="{x}" y="{y}" width="{ancho + 1}" height="{420 - y}" fill="#07040B"/>'
        s += f'<path d="M{x} {y}H{x + ancho}" stroke="#FF3B47" stroke-width="0.8" opacity="0.5"/>'
    for x, y in ((92, 278), (300, 292), (560, 286), (962, 262)):
        if x < w:
            s += (f'<path d="M{x} {y}V{y - 10}M{x + 22} {y}V{y - 10}" stroke="#07040B" stroke-width="3"/>'
                  f'<path d="M{x - 2} {y - 10}H{x + 24}V{y - 30}Q{x + 11} {y - 38} {x - 2} {y - 30}Z" fill="#07040B"/>')
    # ventanas encendidas, pocas
    for x, y in ((24, 330), (150, 340), (290, 318), (380, 300), (602, 320), (722, 330), (880, 336), (1040, 318)):
        if x < w:
            s += f'<rect x="{x}" y="{y}" width="8" height="10" fill="#FFD23F" opacity="0.7"/>'
    return s


def tarjeta(movil=False, quieta=False):
    """Aurora Veil (vendor/, MIT) recoloreada, con azoteas, Daniel y su nombre."""
    ns = "http://www.w3.org/2000/svg"
    ET.register_namespace("", ns)
    original = ET.parse(ROOT / "vendor" / "aurora-veil.svg").getroot()
    w = 640 if movil else 1200
    k = TEMAS["noche"]
    svg = ET.Element(f"{{{ns}}}svg", {
        "viewBox": f"0 0 {w} 420", "width": str(w), "height": "420",
        "role": "img", "aria-label": "Daniel Santiago Mayorga, Junior Backend Developer"})
    svg.append(ET.Comment("Adapted from Aurora Veil, beydemirfurkan/awesome-github-profile.\n"
                          + (ROOT / "vendor" / "LICENSE").read_text(encoding="utf-8").strip()))
    ET.SubElement(svg, f"{{{ns}}}title").text = "Daniel Santiago Mayorga"
    ET.SubElement(svg, f"{{{ns}}}desc").text = (
        "Junior Backend Developer. Java, Python y SQL. Ilustración de Daniel con traje negro "
        "de líneas rojas y la máscara en la mano, sobre las azoteas de una ciudad de noche.")
    hijos = list(original)
    svg.append(hijos[0])
    escena = ET.SubElement(svg, f"{{{ns}}}g", {"transform": "translate(-280 0)"} if movil else {})
    for hijo in hijos[1:]:
        if "Fraunces" in hijo.get("font-family", ""):
            break
        # Se sustituyen las montañas por azoteas.
        if hijo.tag.endswith("path") and hijo.get("d", "").startswith(("M0,420", "M0,300")):
            continue
        escena.append(hijo)
    for nodo in svg.iter():
        for atributo in ("stop-color", "fill", "stroke"):
            valor = nodo.get(atributo, "").lower()
            if valor in COLORES_AURORA:
                nodo.set(atributo, COLORES_AURORA[valor])

    animado = not quieta
    capa = horizonte(w)
    capa += trama(w - 320, 0, 320, 180, k["rojo"], 12, 4.6, (1, 0), 1.0, 0.35)

    def nombre(x, y, valor, tam, alto):
        estilo = 'font-style="italic" letter-spacing="-1.2"'
        rojo = t(x, y, valor, tam, k["rojo"], 500, SERIF, estilo)
        azul = t(x, y, valor, tam, k["azul"], 500, SERIF, estilo)
        crema = t(x, y, valor, tam, k["tinta"], 500, SERIF, estilo)
        reg_r = reg_a = ""
        if animado:
            for signo in (-1, 1):
                v = ";".join(" ".join(str(float(n) * signo) for n in p.split()) for p in PASOS)
                a = (f'<animateTransform attributeName="transform" type="translate" values="{v}" '
                     f'dur="{len(PASOS) / FPS:.3f}s" calcMode="discrete" begin="0.35s" fill="freeze"/>')
                if signo == -1:
                    reg_r = a
                else:
                    reg_a = a
        tinta = (f'<g transform="translate(2 1)" opacity="0.9">{rojo}{reg_r}</g>'
                 f'<g transform="translate(-2 -1)" opacity="0.9">{azul}{reg_a}</g>')
        # Glitch de dimensión: tres franjas del nombre se desplazan cada 6 s.
        franjas = ""
        bandas = [(y - alto, alto * 0.38), (y - alto * 0.62, alto * 0.34), (y - alto * 0.28, alto * 0.5)]
        saltos = ["26 0;-14 0;8 0;0 0", "-34 0;18 0;-6 0;0 0", "18 0;-24 0;10 0;0 0"]
        for j, ((by, bh), salto) in enumerate(zip(bandas, saltos)):
            cid = f"f{len(valor)}{j}{int(y)}"
            mov = ""
            if animado:
                valores = salto + ";0 0"
                mov = anim(valores, 6.0, tiempos="0;0.014;0.028;0.042;1", inicio="1.4s")
            franjas += (f'<clipPath id="{cid}"><rect x="0" y="{by:.0f}" width="{w}" height="{bh + 2:.0f}"/></clipPath>'
                        f'<g clip-path="url(#{cid})"><g>{tinta}{crema}{mov}</g></g>')
        return franjas

    if movil:
        capa += t(32, 42, "JAVA / PYTHON / SQL", 18, k["suave"], 400, MONO, 'letter-spacing="2"')
        x0, y0, esc = 448, 34, 0.62
        capa += f'<g transform="translate({x0} {y0}) scale({esc})">{personaje(animado)}</g>'
        capa += sentido_aracnido(x0 + 120 * esc, y0 + 62 * esc, esc, animado)
        capa += nombre(32, 316, "Daniel Santiago", 54, 46)
        capa += nombre(32, 374, "Mayorga", 58, 50)
        rol_y = 410
    else:
        capa += t(80, 42, "JAVA / PYTHON / SQL", 14, k["suave"], 400, MONO, 'letter-spacing="3"')
        x0, y0, esc = 900, 46, 0.96
        capa += f'<g transform="translate({x0} {y0}) scale({esc})">{personaje(animado)}</g>'
        capa += sentido_aracnido(x0 + 120 * esc, y0 + 62 * esc, esc, animado)
        capa += nombre(80, 368, "Daniel Santiago Mayorga", 68, 58)
        rol_y = 400
    rol_x, rol_tam = (36, 22) if movil else (82, 18)
    destello = ""
    if animado:
        rol_azul = t(rol_x - 3, rol_y, "JUNIOR BACKEND DEVELOPER", rol_tam, k["azul"], 700, MONO, 'letter-spacing="3"')
        destello = (f'<g opacity="0">{rol_azul}'
                    + anim("0;1;0;1;0", 5.0, "opacity", tiempos="0;0.6;0.617;0.633;0.65") + "</g>")
    capa += t(rol_x, rol_y, "JUNIOR BACKEND DEVELOPER", rol_tam, k["amarillo"], 700, MONO, 'letter-spacing="3"')
    capa += destello
    svg.append(ET.fromstring(f'<g xmlns="{ns}">{capa}</g>'))

    if quieta:
        for padre in svg.iter():
            for hijo in list(padre):
                if hijo.tag in (f"{{{ns}}}animate", f"{{{ns}}}animateTransform"):
                    padre.remove(hijo)
    nombre_archivo = "aurora-name" + ("-mobile" if movil else "") + ("-static" if quieta else "")
    texto = ET.tostring(svg, encoding="unicode")
    (ROOT / f"{nombre_archivo}.svg").write_text(
        "\n".join(fila.rstrip() for fila in texto.splitlines()) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- Divisor


def divisor(tema):
    """Telaraña que se dispara (thwip) y se pega con una salpicadura de puntos."""
    k = TEMAS[tema]
    w, h = 960, 28
    hilo = "M8 14Q300 4 600 14"
    s = (f'<path class="hilo" d="{hilo}" fill="none" stroke="{k["azul"]}" stroke-width="2" '
         f'transform="translate(-2 1)" pathLength="100" stroke-dasharray="100" opacity="0.8"/>'
         f'<path class="hilo" d="{hilo}" fill="none" stroke="{k["rojo"]}" stroke-width="2.5" '
         f'pathLength="100" stroke-dasharray="100"/>')
    salpicadura = "".join(
        f'<circle cx="{600 + 14 * cos(a):.1f}" cy="{14 + 10 * sin(a):.1f}" r="{2.6 - j * 0.3:.1f}"/>'
        for j, a in enumerate([pi * (0.25 * i) for i in range(8)]))
    s += f'<g class="splat" fill="{k["rojo"]}">{salpicadura}<circle cx="600" cy="14" r="5"/></g>'
    s += f'<path d="M640 14H960" stroke="{k["linea"]}" stroke-width="1"/>'
    css = (".hilo{animation:thwip 6s steps(1) infinite}"
           "@keyframes thwip{0%{stroke-dashoffset:100}2%{stroke-dashoffset:70}4%{stroke-dashoffset:38}"
           "6%{stroke-dashoffset:12}8%,100%{stroke-dashoffset:0}}"
           ".splat{transform-origin:center;animation:splat 6s steps(1) infinite}"
           "@keyframes splat{0%,7%{opacity:0;transform:scale(.3)}8%{opacity:1;transform:scale(1.4)}"
           "10%,100%{opacity:1;transform:scale(1)}}")
    guardar(f"divider-{tema}", w, h, s, "Separador decorativo", css)


# ---------------------------------------------------------------- Tríptico

VINETAS = [
    ("XEON", ["La IA interpreta.", "El backend decide."], "conversación → reglas → borrador"),
    ("TOOL RENTAL", ["Del catálogo", "a la devolución."], "catálogo → reserva → devolución"),
    ("MOTION STUDIO", ["Cada fotograma,", "una función."], "window.seek(t) → MP4"),
]


def glifo(i, cx, cy, k):
    """Dibujo de cada viñeta con su acción en bucle."""
    ink, r, a = k["contorno"], k["rojo"], k["azul"]

    def capas(forma):
        return (f'<g transform="translate(-3 0)" fill="none" stroke="{a}" stroke-width="4" stroke-linejoin="round" opacity="0.8">{forma}</g>'
                f'<g transform="translate(3 1)" fill="none" stroke="{r}" stroke-width="4" stroke-linejoin="round" opacity="0.8">{forma}</g>'
                f'<g fill="none" stroke="{ink}" stroke-width="3" stroke-linejoin="round">{forma}</g>')
    if i == 0:  # globo que escribe «…» y se convierte en { }
        forma = (f'<path d="M{cx-46} {cy-30}h76a10 10 0 0 1 10 10v26a10 10 0 0 1-10 10h-46l-14 14v-14h-16'
                 f'a10 10 0 0 1-10-10v-26a10 10 0 0 1 10-10z"/>')
        puntos = "".join(f'<circle class="p{j}" cx="{cx - 22 + j * 14}" cy="{cy - 4}" r="4" fill="{ink}"/>' for j in range(3))
        llaves = t(cx - 8, cy + 4, "{ }", 24, ink, 700, MONO, 'text-anchor="middle" class="llaves"')
        return capas(forma) + puntos + llaves
    if i == 1:  # etiqueta que se balancea en su ojal
        forma = (f'<path d="M{cx-44} {cy-28}h56l26 28-26 28h-56z"/><circle cx="{cx+16}" cy="{cy}" r="6"/>')
        return (f'<path d="M{cx+16} {cy-56}V{cy-6}" stroke="{ink}" stroke-width="2" stroke-dasharray="3 4"/>'
                f'<g class="etiqueta">{capas(forma)}</g>')
    # tira de película que avanza fotograma a fotograma
    forma = (f'<rect x="{cx-46}" y="{cy-30}" width="84" height="60" rx="4"/>'
             f'<path d="M{cx-46} {cy-18}h84M{cx-46} {cy+18}h84"/>')
    agujeros = "".join(f'<rect x="{cx-58+j*16}" y="{cy-27}" width="7" height="6" fill="{ink}"/>' for j in range(8))
    clip = f'<clipPath id="tira"><rect x="{cx-44}" y="{cy-30}" width="80" height="60"/></clipPath>'
    cuadro = f'<rect class="cuadro" x="{cx-30}" y="{cy-8}" width="14" height="14" fill="{r}"/>'
    return (capas(forma) + clip + f'<g clip-path="url(#tira)"><g class="agujeros">{agujeros}</g>{cuadro}</g>')


CSS_TRIPTICO = (
    ".v{animation:impacto .5s steps(1) both}"
    ".v1{animation-delay:.33s}.v2{animation-delay:.66s}"
    "@keyframes impacto{0%{opacity:0;transform:scale(1.12)}33%{opacity:1;transform:scale(1.05)}"
    "66%,100%{opacity:1;transform:scale(1)}}"
    ".v{transform-origin:center}"
    # XEON: los puntos se escriben y luego aparecen las llaves
    ".p0,.p1,.p2{opacity:0}.p0,.p1,.p2,.llaves{animation:escribe 4s steps(1) infinite}"
    "@keyframes escribe{0%{opacity:0}100%{opacity:0}}"
    ".p0{animation-name:p0}.p1{animation-name:p1}.p2{animation-name:p2}.llaves{animation-name:ll}"
    "@keyframes p0{0%,8%{opacity:0}9%,50%{opacity:1}51%,100%{opacity:0}}"
    "@keyframes p1{0%,17%{opacity:0}18%,50%{opacity:1}51%,100%{opacity:0}}"
    "@keyframes p2{0%,26%{opacity:0}27%,50%{opacity:1}51%,100%{opacity:0}}"
    "@keyframes ll{0%,50%{opacity:0}51%,100%{opacity:1}}"
    # Tool Rental: balanceo a saltos alrededor del ojal
    ".etiqueta{transform-origin:72% 50%;animation:balanceo 1.33s steps(1) infinite}"
    "@keyframes balanceo{0%{transform:rotate(-7deg)}25%{transform:rotate(-2deg)}"
    "50%{transform:rotate(6deg)}75%{transform:rotate(2deg)}}"
    # Motion Studio: la tira avanza un agujero por fotograma
    ".agujeros{animation:avanza .667s steps(1) infinite}"
    "@keyframes avanza{0%{transform:translateX(0)}50%{transform:translateX(8px)}}"
    ".cuadro{animation:cuadro 2s steps(1) infinite}"
    "@keyframes cuadro{0%{transform:translate(0,0)}25%{transform:translate(14px,-6px)}"
    "50%{transform:translate(28px,0)}75%{transform:translate(42px,-6px)}}"
)


def triptico(tema, movil=False):
    k = TEMAS[tema]
    if movil:
        w, ph, gap = 640, 230, 18
        h = 3 * ph + 2 * gap
        cajas = [(0, i * (ph + gap), w, ph) for i in range(3)]
    else:
        w, h, gap = 960, 300, 16
        pw = (w - 2 * gap) / 3
        cajas = [(i * (pw + gap), 0, pw, h) for i in range(3)]
    s = ""
    for i, ((x, y, pw, ph), (nombre, lineas, flujo)) in enumerate(zip(cajas, VINETAS)):
        clip = f"v{i}c"
        p = f'<clipPath id="{clip}"><rect x="{x:g}" y="{y:g}" width="{pw:g}" height="{ph:g}" rx="6"/></clipPath>'
        p += f'<rect x="{x:g}" y="{y:g}" width="{pw:g}" height="{ph:g}" rx="6" fill="{k["fondo"]}"/>'
        alto_trama = ph * (0.5 if movil else 0.55)
        color_trama = k["rojo"] if i != 1 else k["azul"]
        p += f'<g clip-path="url(#{clip})">{trama(x + pw * 0.4, y, pw * 0.6, alto_trama, color_trama, 11, 4, (1, 0), 1.0, 0.35)}</g>'
        p += f'<rect x="{x + 1.5:g}" y="{y + 1.5:g}" width="{pw - 3:g}" height="{ph - 3:g}" rx="6" fill="none" stroke="{k["contorno"]}" stroke-width="3"/>'
        etiqueta_w = len(nombre) * 11.5 + 24
        p += f'<rect x="{x + 16:g}" y="{y + 16:g}" width="{etiqueta_w:g}" height="30" fill="{k["amarillo"]}" stroke="{k["contorno"]}" stroke-width="2"/>'
        p += t(x + 28, y + 37, nombre, 16, k["sobre_amarillo"], 700, MONO, 'letter-spacing="1"')
        if movil:
            p += glifo(i, x + pw - 100, y + 82, k)
            p += desfase(x + 22, y + 140, lineas[0], 34, k)
            p += desfase(x + 22, y + 180, lineas[1], 34, k)
            p += t(x + 24, y + 212, flujo, 20, k["suave"], 400, MONO)
        else:
            p += glifo(i, x + pw / 2, y + 112, k)
            p += desfase(x + 20, y + 212, lineas[0], 25, k)
            p += desfase(x + 20, y + 244, lineas[1], 25, k)
            p += t(x + 21, y + 276, flujo, 13, k["suave"], 400, MONO)
        s += f'<g class="v v{i}">{p}</g>'
    guardar(f"projects-{tema}" + ("-mobile" if movil else ""), w, h, s,
            "Tres viñetas: XEON, la IA interpreta y el backend decide; Tool Rental, del catálogo "
            "a la devolución; Motion Studio, cada fotograma es una función del tiempo.", CSS_TRIPTICO)


# ---------------------------------------------------------------- Pegatinas

TECNOLOGIAS = ["Java", "Spring Boot", "Python", "FastAPI", "PostgreSQL", "Docker"]
GIROS = [-3, 2, -2, 3, -1, 2]


def pegatinas(tema, movil=False):
    k = TEMAS[tema]
    cols = 3 if movil else 6
    w = 640 if movil else 960
    gap = 18
    cw = (w - (cols - 1) * gap - 14) / cols
    ch = 76 if movil else 64
    filas = (len(TECNOLOGIAS) + cols - 1) // cols
    h = filas * ch + (filas - 1) * gap + 16
    tam = 25 if movil else 19
    s, css = "", ""
    for i, nombre in enumerate(TECNOLOGIAS):
        x = (i % cols) * (cw + gap) + 4
        y = (i // cols) * (ch + gap) + 4
        sombra = k["rojo"] if i % 2 == 0 else k["azul"]
        cuerpo = (f'<rect x="{x + 6:g}" y="{y + 6:g}" width="{cw:g}" height="{ch:g}" rx="10" fill="{sombra}"/>'
                  f'<rect x="{x + 1.5:g}" y="{y + 1.5:g}" width="{cw - 3:g}" height="{ch - 3:g}" rx="10" '
                  f'fill="{k["fondo"]}" stroke="{k["contorno"]}" stroke-width="3"/>'
                  + t(x + cw / 2, y + ch / 2 + tam * 0.36, nombre, tam, k["tinta"], 700, TEXTO, 'text-anchor="middle"'))
        s += f'<g class="s s{i}">{cuerpo}</g>'
        retraso = 0.25 * i
        # Cada pegatina se pega con un golpe y, en su turno, vuelve a «asentarse».
        css += (f".s{i}{{transform:rotate({GIROS[i]}deg);animation:pega .42s steps(1) {retraso:.2f}s both,"
                f"asienta 6s steps(1) {retraso + 1.5:.2f}s infinite}}"
                f"")
    css += (".s{transform-origin:center}"
            "@keyframes pega{0%{opacity:0;transform:scale(1.4) rotate(0deg)}"
            "40%{opacity:1;transform:scale(.92) rotate(0deg)}"
            "80%,100%{opacity:1;transform:scale(1) rotate(var(--g,0deg))}}"
            "@keyframes asienta{0%{transform:scale(1.07) rotate(0deg)}4%,100%{transform:scale(1) rotate(var(--g,0deg))}}")
    # var(--g) para que cada pegatina conserve su giro al terminar la animación.
    for i in range(len(TECNOLOGIAS)):
        css += f".s{i}{{--g:{GIROS[i]}deg}}"
    guardar(f"technologies-{tema}" + ("-mobile" if movil else ""), w, h, s,
            "Tecnologías principales: " + ", ".join(TECNOLOGIAS), css)


# ---------------------------------------------------------------- Cierre


def telarana(cx, cy, radio, k):
    """Esquina de telaraña de puntos que se teje anillo a anillo."""
    angulos = [pi + j * (pi / 2) / 5 for j in range(6)]
    radios = "".join(f'<path d="M{cx} {cy}L{cx + radio * cos(a):.1f} {cy + radio * sin(a):.1f}"/>' for a in angulos)
    anillos = ""
    for n, r in enumerate((0.25, 0.45, 0.65, 0.85)):
        pts = [f"{cx + radio * r * cos(a):.1f} {cy + radio * r * sin(a):.1f}" for a in angulos]
        anillos += f'<path class="anillo a{n}" d="M{"L".join(pts)}" opacity="{1 - n * 0.2:.1f}"/>'
    return (f'<g fill="none" stroke="{k["rojo"]}" stroke-width="3.2" stroke-linecap="round" '
            f'stroke-dasharray="0 9">{radios}{anillos}</g>')


def arana(x, k):
    """Araña genérica (no es un logotipo) colgando de su hilo."""
    patas = ""
    for lado in (-1, 1):
        for j, dy in enumerate((-6, -2, 2, 6)):
            patas += (f'<path d="M{x} {dy}l{lado * 10} {-4 + j * 2}l{lado * 5} {6 + j}"/>')
    return (f'<g class="arana"><path d="M{x} -400V-8" stroke="{k["contorno"]}" stroke-width="1.2"/>'
            f'<g stroke="{k["contorno"]}" stroke-width="2" fill="none" stroke-linecap="round">{patas}</g>'
            f'<ellipse cx="{x}" cy="2" rx="6" ry="8" fill="{k["rojo"]}" stroke="{k["contorno"]}" stroke-width="1.5"/>'
            f'<circle cx="{x}" cy="-8" r="4" fill="{k["contorno"]}"/></g>')


def cierre(tema, movil=False):
    k = TEMAS[tema]
    w, h = (640, 260) if movil else (960, 210)
    s = (f'<clipPath id="marco"><rect x="0" y="0" width="{w}" height="{h}" rx="8"/></clipPath>'
         f'<rect x="1.5" y="1.5" width="{w - 3}" height="{h - 3}" rx="8" fill="{k["fondo"]}"/>'
         f'<g clip-path="url(#marco)">{telarana(w - 4, h - 4, 200 if movil else 190, k)}'
         f'<g transform="translate(0 {80 if movil else 70})">{arana(w - (80 if movil else 110), k)}</g></g>'
         f'<rect x="1.5" y="1.5" width="{w - 3}" height="{h - 3}" rx="8" fill="none" stroke="{k["contorno"]}" stroke-width="3"/>')
    s += (f'<g class="cartel"><rect x="24" y="24" width="{236 if movil else 196}" height="30" '
          f'fill="{k["amarillo"]}" stroke="{k["contorno"]}" stroke-width="2"/>'
          + t(36, 45, "CONTINUARÁ…", 20 if movil else 16, k["sobre_amarillo"], 700, MONO, 'letter-spacing="1"') + "</g>")
    if movil:
        s += desfase(28, 128, "¿Construimos", 46, k)
        s += desfase(28, 182, "algo juntos?", 46, k)
        s += t(30, 228, "Escríbeme con tu idea o tu reto.", 24, k["suave"])
    else:
        s += desfase(28, 124, "¿Construimos algo juntos?", 48, k)
        s += t(30, 170, "Escríbeme con tu idea, tu reto o una oportunidad.", 21, k["suave"])
    css = (".anillo{animation:teje 8s steps(1) infinite}"
           ".a1{animation-name:teje1}.a2{animation-name:teje2}.a3{animation-name:teje3}"
           "@keyframes teje{0%,3%{opacity:0}4%,100%{opacity:1}}"
           "@keyframes teje1{0%,7%{opacity:0}8%,100%{opacity:.8}}"
           "@keyframes teje2{0%,11%{opacity:0}12%,100%{opacity:.6}}"
           "@keyframes teje3{0%,15%{opacity:0}16%,100%{opacity:.4}}"
           ".cartel{animation:cartel 2.5s steps(1) infinite}"
           "@keyframes cartel{0%,84%{opacity:1}85%,90%{opacity:.25}91%,100%{opacity:1}}"
           ".arana{animation:baja 8s steps(1) infinite}"
           "@keyframes baja{0%{transform:translateY(-120px)}3%{transform:translateY(-80px)}"
           "6%{transform:translateY(-36px)}9%{transform:translateY(6px)}12%{transform:translateY(-2px)}"
           "15%,40%{transform:translateY(0)}45%{transform:translateY(3px)}50%,75%{transform:translateY(0)}"
           "80%{transform:translateY(3px)}85%,100%{transform:translateY(0)}}")
    guardar(f"contact-{tema}" + ("-mobile" if movil else ""), w, h, s,
            "¿Construimos algo juntos? Escríbeme con tu idea, tu reto o una oportunidad.", css)


if __name__ == "__main__":
    for movil in (False, True):
        tarjeta(movil)
        tarjeta(movil, quieta=True)
        for tema in TEMAS:
            triptico(tema, movil)
            pegatinas(tema, movil)
            cierre(tema, movil)
    for tema in TEMAS:
        divisor(tema)
    print("Generados", len(list(ROOT.glob("*.svg"))), "SVG locales.")
