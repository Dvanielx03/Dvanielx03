"""Genera los SVG locales del perfil (dirección «Fuera de registro»).

Uso desde la raíz: python assets/profile/generate.py
Solo usa la biblioteca estándar. Decisiones de diseño en docs/PROFILE-DESIGN.md.

Lenguaje visual: impresión de cómic con las tintas cian y magenta desfasadas,
trama de puntos (halftone) y contorno de tinta. Única animación: el nombre de
la tarjeta encaja su registro a 12 fotogramas por segundo («animación a dos»).
"""
from math import cos, hypot, pi, sin
from pathlib import Path
from xml.sax.saxutils import escape
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent

# Tintas por tema. «noche» sale de la tarjeta Aurora; «papel» es su impresión clara.
TEMAS = {
    "noche": {"fondo": "#070B22", "panel": "#0E1B3A", "tinta": "#FEF3C7",
              "suave": "#CBD5E1", "linea": "#3B335F", "cian": "#3FFFE6",
              "magenta": "#FF3D8A", "violeta": "#A78BFA", "contorno": "#FEF3C7"},
    "papel": {"fondo": "#FBF4E2", "panel": "#F3E9CF", "tinta": "#070B22",
              "suave": "#4A4F6A", "linea": "#D9CDB0", "cian": "#00A3B4",
              "magenta": "#D61F69", "violeta": "#6D4FD8", "contorno": "#070B22"},
}
SANS = "'Arial Black', 'Helvetica Neue', Arial, Helvetica, sans-serif"
TEXTO = "Arial, Helvetica, sans-serif"
MONO = "Consolas, 'Liberation Mono', Menlo, monospace"
SERIF = "Fraunces, 'Playfair Display', Georgia, serif"


def t(x, y, valor, tam, color, peso=400, fuente=TEXTO, extra=""):
    return (f'<text x="{x:g}" y="{y:g}" fill="{color}" font-family="{fuente}" '
            f'font-size="{tam}" font-weight="{peso}" {extra}>{escape(valor)}</text>')


def desfase(x, y, valor, tam, k, peso=700, fuente=SANS, d=2, extra=""):
    """Texto impreso con las tintas cian y magenta fuera de registro."""
    return (f'<g opacity="0.8">'
            + t(x + d, y + d * 0.5, valor, tam, k["magenta"], peso, fuente, extra)
            + t(x - d, y - d * 0.5, valor, tam, k["cian"], peso, fuente, extra)
            + "</g>" + t(x, y, valor, tam, k["tinta"], peso, fuente, extra))


def trama(x0, y0, w, h, color, paso=11, rmax=4.2, origen=(0, 0), alcance=1.0, opacidad=1.0):
    """Trama de puntos que se agranda hacia `origen` (coordenadas relativas 0..1)."""
    ox, oy = x0 + origen[0] * w, y0 + origen[1] * h
    diag = hypot(w, h) * alcance
    puntos = []
    fila = 0
    y = y0 + paso / 2
    while y < y0 + h:
        x = x0 + paso / 2 + (paso / 2 if fila % 2 else 0)
        while x < x0 + w:
            r = rmax * (1 - hypot(x - ox, y - oy) / diag)
            if r > 0.5:
                puntos.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}"/>')
            x += paso
        y += paso
        fila += 1
    return f'<g fill="{color}" opacity="{opacidad}">{"".join(puntos)}</g>'


def guardar(nombre, w, h, cuerpo, titulo):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" role="img" aria-label="{escape(titulo)}">'
           f'<title>{escape(titulo)}</title>{cuerpo}</svg>\n')
    (ROOT / f"{nombre}.svg").write_text(svg, encoding="utf-8")


# ---------------------------------------------------------------- Tarjeta

# Recorrido del cian hasta encajar, un valor por fotograma a 12 fps.
PASOS = ["-30 -8", "-21 -6", "-14 -4", "-9 -3", "-5 -2", "-3 -1", "-2 -1"]


def registro(signo):
    """Animación discreta a 12 fps que lleva una tinta a su sitio."""
    valores = ";".join(" ".join(str(float(v) * signo) for v in p.split()) for p in PASOS)
    return (f'<animateTransform attributeName="transform" type="translate" '
            f'values="{valores}" dur="{len(PASOS) / 12:.3f}s" calcMode="discrete" '
            f'begin="0.35s" fill="freeze"/>')


def tarjeta(movil=False, quieta=False):
    """Aurora Veil (vendor/, MIT) con el nombre impreso fuera de registro."""
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
        "Junior Backend Developer. Java, Python y SQL. Nombre impreso con tintas "
        "cian y magenta fuera de registro sobre una aurora nocturna.")
    hijos = list(original)
    svg.append(hijos[0])
    escena = ET.SubElement(svg, f"{{{ns}}}g", {"transform": "translate(-280 0)"} if movil else {})
    for hijo in hijos[1:]:
        if "Fraunces" in hijo.get("font-family", ""):
            break
        escena.append(hijo)

    # Esquina de trama magenta, como una página impresa.
    capa = trama(w - 300, 0, 300, 170, k["magenta"], 12, 4.6, (1, 0), 1.0, 0.45)

    def nombre(x, y, valor, tam):
        estilo = 'font-style="italic" letter-spacing="-1.2"'
        cian = t(x, y, valor, tam, k["cian"], 500, SERIF, estilo)
        magenta = t(x, y, valor, tam, k["magenta"], 500, SERIF, estilo)
        crema = t(x, y, valor, tam, k["tinta"], 500, SERIF, estilo)
        anim_m = "" if quieta else registro(-1)
        anim_c = "" if quieta else registro(1)
        return (f'<g transform="translate(2 1)" opacity="0.9">{magenta}{anim_m}</g>'
                f'<g transform="translate(-2 -1)" opacity="0.9">{cian}{anim_c}</g>{crema}')

    if movil:
        capa += t(32, 42, "JAVA / PYTHON / SQL", 18, k["suave"], 400, MONO, 'letter-spacing="2"')
        capa += nombre(32, 316, "Daniel Santiago", 54)
        capa += nombre(32, 374, "Mayorga", 58)
        capa += t(36, 410, "JUNIOR BACKEND DEVELOPER", 22, k["cian"], 400, MONO, 'letter-spacing="2"')
    else:
        capa += t(80, 42, "JAVA / PYTHON / SQL", 14, k["suave"], 400, MONO, 'letter-spacing="3"')
        capa += nombre(80, 368, "Daniel Santiago Mayorga", 68)
        capa += t(82, 400, "JUNIOR BACKEND DEVELOPER", 18, k["cian"], 400, MONO, 'letter-spacing="3"')
        capa += t(1120, 400, "github.com/Dvanielx03", 16, k["suave"], 400, MONO, 'text-anchor="end"')
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


# ---------------------------------------------------------------- Piezas


def divisor(tema):
    k = TEMAS[tema]
    w, h = 960, 24
    s = ""
    for capa, color, dx in (("m", k["magenta"], 2), ("c", k["cian"], -2)):
        puntos = []
        for i in range(48):
            x = 10 + i * 20
            # Puntos que crecen y se apagan, como una tira de trama.
            r = 4.5 * max(0.0, 1 - abs(i - 9) / 22) if i < 31 else 0
            if r > 0.6:
                puntos.append(f'<circle cx="{x + dx}" cy="{12 + dx / 2:g}" r="{r:.1f}"/>')
        s += f'<g fill="{color}" opacity="0.85">{"".join(puntos)}</g>'
    s += f'<path d="M640 12H960" stroke="{k["linea"]}" stroke-width="1"/>'
    guardar(f"divider-{tema}", w, h, s, "Separador decorativo")


VINETAS = [
    ("XEON", ["La IA interpreta.", "El backend decide."], "conversación → reglas → borrador"),
    ("TOOL RENTAL", ["Del catálogo", "a la devolución."], "catálogo → reserva → devolución"),
    ("MOTION STUDIO", ["Cada fotograma,", "una función."], "window.seek(t) → MP4"),
]


def glifo(i, cx, cy, k):
    """Dibujo de línea de cada viñeta, con contorno de tinta y sombra cian."""
    c, m, ink = k["cian"], k["magenta"], k["contorno"]
    if i == 0:  # globo de diálogo que se convierte en llaves
        forma = (f'<path d="M{cx-46} {cy-30}h60a10 10 0 0 1 10 10v26a10 10 0 0 1-10 10h-36l-14 14v-14h-10'
                 f'a10 10 0 0 1-10-10v-26a10 10 0 0 1 10-10z"/>')
        extra = t(cx - 16, cy + 6, "{ }", 22, ink, 700, MONO, 'text-anchor="middle"')
    elif i == 1:  # etiqueta de alquiler con su ojal
        forma = (f'<path d="M{cx-44} {cy-28}h56l26 28-26 28h-56z"/>'
                 f'<circle cx="{cx+16}" cy="{cy}" r="6"/>')
        extra = ""
    else:  # fotograma de película
        forma = (f'<rect x="{cx-46}" y="{cy-30}" width="84" height="60" rx="4"/>'
                 f'<path d="M{cx-46} {cy-18}h84M{cx-46} {cy+18}h84"/>')
        extra = "".join(f'<rect x="{cx-40+j*16}" y="{cy-27}" width="7" height="6" fill="{ink}"/>' for j in range(5))
    return (f'<g transform="translate(5 4)" fill="none" stroke="{c}" stroke-width="4" stroke-linejoin="round">{forma}</g>'
            f'<g fill="none" stroke="{m}" stroke-width="4" stroke-linejoin="round" opacity="0.6" transform="translate(2 2)">{forma}</g>'
            f'<g fill="none" stroke="{ink}" stroke-width="3" stroke-linejoin="round">{forma}</g>{extra}')


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
        clip = f"v{i}"
        s += f'<clipPath id="{clip}"><rect x="{x:g}" y="{y:g}" width="{pw:g}" height="{ph:g}" rx="6"/></clipPath>'
        s += f'<rect x="{x:g}" y="{y:g}" width="{pw:g}" height="{ph:g}" rx="6" fill="{k["fondo"]}"/>'
        # La trama vive en la esquina superior derecha, lejos del texto.
        alto_trama = ph * (0.5 if movil else 0.55)
        s += f'<g clip-path="url(#{clip})">{trama(x + pw * 0.4, y, pw * 0.6, alto_trama, k["magenta"] if i != 1 else k["cian"], 11, 4, (1, 0), 1.0, 0.35)}</g>'
        s += f'<rect x="{x + 1.5:g}" y="{y + 1.5:g}" width="{pw - 3:g}" height="{ph - 3:g}" rx="6" fill="none" stroke="{k["contorno"]}" stroke-width="3"/>'
        # Cuadro de narración con el nombre del proyecto.
        etiqueta_w = len(nombre) * 11.5 + 24
        s += f'<rect x="{x + 16:g}" y="{y + 16:g}" width="{etiqueta_w:g}" height="30" fill="{k["tinta"]}"/>'
        s += t(x + 28, y + 37, nombre, 16, k["fondo"], 700, MONO, 'letter-spacing="1"')
        if movil:
            s += glifo(i, x + pw - 100, y + 78, k)
            s += desfase(x + 22, y + 140, lineas[0], 34, k, d=1.5)
            s += desfase(x + 22, y + 180, lineas[1], 34, k, d=1.5)
            s += t(x + 24, y + 212, flujo, 20, k["suave"], 400, MONO)
        else:
            s += glifo(i, x + pw / 2, y + 112, k)
            s += desfase(x + 20, y + 212, lineas[0], 25, k, d=1.5)
            s += desfase(x + 20, y + 244, lineas[1], 25, k, d=1.5)
            s += t(x + 21, y + 276, flujo, 13, k["suave"], 400, MONO)
    nombre_archivo = f"projects-{tema}" + ("-mobile" if movil else "")
    guardar(nombre_archivo, w, h, s,
            "Tres viñetas: XEON, la IA interpreta y el backend decide; Tool Rental, del catálogo "
            "a la devolución; Motion Studio, cada fotograma es una función del tiempo.")


TECNOLOGIAS = ["Java", "Spring Boot", "Python", "FastAPI", "PostgreSQL", "Docker"]


def pegatinas(tema, movil=False):
    k = TEMAS[tema]
    cols = 3 if movil else 6
    w = 640 if movil else 960
    gap = 16
    cw = (w - (cols - 1) * gap - 8) / cols
    ch = 76 if movil else 64
    filas = (len(TECNOLOGIAS) + cols - 1) // cols
    h = filas * ch + (filas - 1) * gap + 8
    tam = 25 if movil else 19
    s = ""
    for i, nombre in enumerate(TECNOLOGIAS):
        x = (i % cols) * (cw + gap)
        y = (i // cols) * (ch + gap)
        sombra = k["cian"] if i % 2 == 0 else k["magenta"]
        s += f'<rect x="{x + 6:g}" y="{y + 6:g}" width="{cw:g}" height="{ch:g}" rx="10" fill="{sombra}"/>'
        s += (f'<rect x="{x + 1.5:g}" y="{y + 1.5:g}" width="{cw - 3:g}" height="{ch - 3:g}" rx="10" '
              f'fill="{k["fondo"]}" stroke="{k["contorno"]}" stroke-width="3"/>')
        s += t(x + cw / 2, y + ch / 2 + tam * 0.36, nombre, tam, k["tinta"], 700, TEXTO, 'text-anchor="middle"')
    guardar(f"technologies-{tema}" + ("-mobile" if movil else ""), w, h, s,
            "Tecnologías principales: " + ", ".join(TECNOLOGIAS))


def telarana(cx, cy, radio, k):
    """Esquina de telaraña dibujada con puntos que se desvanecen hacia fuera."""
    s = ""
    angulos = [pi + j * (pi / 2) / 5 for j in range(6)]  # cuarto de círculo hacia arriba-izquierda
    for a in angulos:
        x, y = cx + radio * cos(a), cy + radio * sin(a)
        s += f'<path d="M{cx} {cy}L{x:.1f} {y:.1f}"/>'
    for n, r in enumerate((0.25, 0.45, 0.65, 0.85)):
        pts = []
        for j, a in enumerate(angulos):
            pts.append(f"{cx + radio * r * cos(a):.1f} {cy + radio * r * sin(a):.1f}")
        s += f'<path d="M{"L".join(pts)}" opacity="{1 - n * 0.2:.1f}"/>'
    return (f'<g fill="none" stroke="{k["magenta"]}" stroke-width="3.2" stroke-linecap="round" '
            f'stroke-dasharray="0 9">{s}</g>')


def cierre(tema, movil=False):
    k = TEMAS[tema]
    w, h = (640, 260) if movil else (960, 210)
    s = f'<rect x="1.5" y="1.5" width="{w - 3}" height="{h - 3}" rx="8" fill="{k["fondo"]}" stroke="{k["contorno"]}" stroke-width="3"/>'
    s += telarana(w - 4, h - 4, 200 if movil else 190, k)
    s += f'<rect x="24" y="24" width="{"236" if movil else "196"}" height="30" fill="{k["tinta"]}"/>'
    s += t(36, 45, "CONTINUARÁ…", 20 if movil else 16, k["fondo"], 700, MONO, 'letter-spacing="1"')
    if movil:
        s += desfase(28, 128, "¿Construimos", 46, k)
        s += desfase(28, 182, "algo juntos?", 46, k)
        s += t(30, 228, "Escríbeme con tu idea o tu reto.", 24, k["suave"])
    else:
        s += desfase(28, 124, "¿Construimos algo juntos?", 48, k)
        s += t(30, 170, "Escríbeme con tu idea, tu reto o una oportunidad.", 21, k["suave"])
    guardar(f"contact-{tema}" + ("-mobile" if movil else ""), w, h, s,
            "¿Construimos algo juntos? Escríbeme con tu idea, tu reto o una oportunidad.")


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
