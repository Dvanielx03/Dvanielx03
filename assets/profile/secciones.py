"""Rótulos de capítulo, tarjetas-portada de proyectos, crossovers y panel de método.

Se ejecuta desde generate.py (python assets/profile/generate.py). Cada pieza tiene
versión noche y papel, y versión móvil a 640 px. Una imagen solo admite un enlace:
cada tarjeta lleva a un único destino (su repositorio o su PR).
"""
from generate import TEMAS, MONO, SANS, TEXTO, t, desfase, trama, guardar, glifo, CSS_TRIPTICO
from stack import logo, marcas

TEMAS_LISTA = list(TEMAS)

# ---------------------------------------------------------------- Rótulos

CAPITULOS = [("01", "proyectos", "Proyectos"), ("02", "tecnologias", "Tecnologías"),
             ("03", "colaboracion", "Colaboración y método")]


def rotulo(numero, clave, titulo, tema, movil=False):
    k = TEMAS[tema]
    w, h = (640, 112) if movil else (960, 92)
    s = marcas(w, h, k["suave"])
    s += (f'<rect x="20" y="{16 if movil else 22}" width="98" height="30" fill="{k["amarillo"]}" '
          f'stroke="{k["contorno"]}" stroke-width="2"/>'
          + t(32, 37 if movil else 43, f"CAP. {numero}", 17, k["sobre_amarillo"], 700, MONO, 'letter-spacing="1"'))
    if movil:
        x_hilo, y_hilo, x_titulo, y_titulo, tam = 132, 31, 22, 92, 42
    else:
        tam = 40
        x_titulo, y_titulo = 136, 62
        x_hilo, y_hilo = x_titulo + len(titulo) * tam * 0.62 + 24, 46
    s += f'<g class="titulo">{desfase(x_titulo, y_titulo, titulo, tam, k, d=2)}</g>'
    fin = w - 34
    s += (f'<path d="M{x_hilo:.0f} {y_hilo}Q{(x_hilo + fin) / 2:.0f} {y_hilo - 8} {fin} {y_hilo}" fill="none" '
          f'stroke="{k["rojo"]}" stroke-width="2.5" stroke-linecap="round"/>'
          f'<g class="nudo" fill="{k["rojo"]}"><circle cx="{fin}" cy="{y_hilo}" r="5"/>'
          f'<circle cx="{fin + 9}" cy="{y_hilo - 6}" r="2"/><circle cx="{fin + 10}" cy="{y_hilo + 5}" r="2"/>'
          f'<circle cx="{fin - 3}" cy="{y_hilo + 9}" r="1.6"/></g>')
    retraso = (int(numero) - 1) * 1.7
    css = (f".titulo{{animation:glitch 6s steps(1) {retraso:.1f}s infinite}}"
           "@keyframes glitch{0%,92%{transform:translate(0,0)}93%{transform:translate(-12px,0)}"
           "94%{transform:translate(9px,-2px)}95%{transform:translate(-3px,1px)}96%,100%{transform:translate(0,0)}}"
           f".nudo{{transform-origin:center;animation:late 3s steps(1) {retraso:.1f}s infinite}}"
           "@keyframes late{0%,80%{transform:scale(1)}84%{transform:scale(1.5)}88%,100%{transform:scale(1)}}")
    guardar(f"chapter-{clave}-{tema}" + ("-mobile" if movil else ""), w, h, s, titulo, css)


# ---------------------------------------------------------------- Proyectos

PROYECTOS = [
    ("xeon", "XEON", "https://github.com/Dvanielx03/Xeon-agente-cotizaciones",
     ["La IA interpreta.", "El backend decide."],
     "Cotiza por WhatsApp o terminal con FastAPI y arquitectura hexagonal.",
     ["Cotiza por WhatsApp o terminal con", "FastAPI y arquitectura hexagonal."],
     "PROTOTIPO", ["python", "fastapi", "docker", "githubactions", "pytest"]),
    ("tool-rental", "TOOL RENTAL", "https://github.com/Dvanielx03/Tool-rental-platform",
     ["Del catálogo", "a la devolución."],
     "Alquileres en equipo con Java 21, Spring Boot y PostgreSQL.",
     ["Alquileres en equipo con Java 21,", "Spring Boot y PostgreSQL."],
     "MVP LOCAL", ["openjdk", "springboot", "postgresql", "react", "docker"]),
    ("motion-studio", "MOTION STUDIO", "https://github.com/Dvanielx03/motion-studio-design",
     ["Cada fotograma,", "una función."],
     "Skill abierta que crea video con HTML y JavaScript, del guion al MP4.",
     ["Skill abierta que crea video con HTML", "y JavaScript, del guion al MP4."],
     "LICENCIA MIT", ["html5", "javascript", "python"]),
]

CSS_PORTADA = CSS_TRIPTICO + (
    ".flecha{animation:empuja .67s steps(1) infinite}"
    "@keyframes empuja{0%{transform:translateX(0)}50%{transform:translateX(5px)}}")


def caja_nombre(x, y, nombre, k, tam=16):
    ancho = len(nombre) * tam * 0.62 + 24
    return (f'<rect x="{x}" y="{y}" width="{ancho:.0f}" height="30" fill="{k["amarillo"]}" stroke="{k["contorno"]}" stroke-width="2"/>'
            + t(x + 12, y + 21, nombre, tam, k["sobre_amarillo"], 700, MONO, 'letter-spacing="1"'))


def sello_estado(cx, cy, texto, k, tam=17):
    ancho = len(texto) * tam * 0.72 + 28
    return (f'<g transform="rotate(-7 {cx} {cy})"><rect x="{cx - ancho / 2:.0f}" y="{cy - 18}" width="{ancho:.0f}" height="36" rx="5" '
            f'fill="none" stroke="{k["rojo"]}" stroke-width="3"/>'
            + t(cx, cy + 6, texto, tam, k["rojo"], 700, SANS, 'text-anchor="middle" letter-spacing="1.5"') + "</g>")


def boton(x, y, w, texto, k, sombra):
    return (f'<rect x="{x + 5}" y="{y + 5}" width="{w}" height="40" rx="6" fill="{sombra}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="6" fill="{k["tinta"]}" stroke="{k["contorno"]}" stroke-width="2"/>'
            + t(x + 16, y + 26, texto, 15, k["fondo"], 700, MONO, 'letter-spacing="1"')
            + f'<g class="flecha"><path d="M{x + w - 34} {y + 20}h16m-6-6 6 6-6 6" fill="none" stroke="{k["fondo"]}" '
              f'stroke-width="2.5" stroke-linecap="round"/></g>')


def marco(w, h, k, color_trama, origen=(1, 0), alto_trama=0.6):
    return (f'<rect x="1.5" y="1.5" width="{w - 3}" height="{h - 3}" rx="8" fill="{k["fondo"]}"/>'
            f'<clipPath id="m"><rect width="{w}" height="{h}" rx="8"/></clipPath>'
            + (f'<g clip-path="url(#m)">{trama(w * 0.55, 0, w * 0.45, h * alto_trama, color_trama, 11, 4, origen, 1.0, 0.3)}</g>' if alto_trama else '')
            + f'<rect x="1.5" y="1.5" width="{w - 3}" height="{h - 3}" rx="8" fill="none" stroke="{k["contorno"]}" stroke-width="3"/>')


def portada(i, tema, movil=False):
    clave, nombre, _, lineas, desc, desc_movil, estado, iconos = PROYECTOS[i]
    k = TEMAS[tema]
    color = k["azul"] if i == 1 else k["rojo"]
    if movil:
        w, h = 640, 430
        s = marco(w, h, k, color)
        s += caja_nombre(22, 22, nombre, k, 17)
        s += sello_estado(w - 120, 44, estado, k, 16)
        s += glifo(i, w - 110, 160, k)
        s += desfase(24, 156, lineas[0], 36, k, d=2) + desfase(24, 200, lineas[1], 36, k, d=2)
        s += t(26, 250, desc_movil[0], 22, k["suave"]) + t(26, 280, desc_movil[1], 22, k["suave"])
        s += "".join(logo(ic, 26 + j * 42, 302, 28, k["tinta"]) for j, ic in enumerate(iconos))
        s += boton(24, 360, w - 58, "ABRIR REPOSITORIO", k, color)
    else:
        w, h = 960, 250
        s = marco(w, h, k, color)
        s += caja_nombre(22, 22, nombre, k)
        s += sello_estado(w - 130, 52, estado, k)
        s += glifo(i, 118, 142, k)
        s += desfase(230, 104, lineas[0], 30, k, d=1.5) + desfase(230, 140, lineas[1], 30, k, d=1.5)
        s += t(232, 178, desc, 18, k["suave"])
        s += "".join(logo(ic, 232 + j * 36, 196, 24, k["tinta"]) for j, ic in enumerate(iconos))
        s += boton(w - 290, 186, 250, "ABRIR REPOSITORIO", k, color)
    guardar(f"project-{clave}-{tema}" + ("-mobile" if movil else ""), w, h, s,
            f"{nombre}: {' '.join(lineas)} {desc} Estado: {estado.lower()}. Abrir repositorio.", CSS_PORTADA)


# ---------------------------------------------------------------- Crossovers y método

APORTES = [
    ("campus-control", "CROSSOVER · HACKATÓN DE 5", "Campus Control",
     "Persistencia, datos iniciales, inventario, importación y Docker Compose.",
     ["Persistencia, datos iniciales, inventario,", "importación y Docker Compose."],
     "VER PR #3", "https://github.com/Dvanielx03/soluciones-rocket/pull/3"),
    ("formula1", "CROSSOVER · APORTE", "Formula1Simulator",
     "Refactoricé a arquitectura hexagonal y corregí el menú JavaFX.",
     ["Refactoricé a arquitectura hexagonal", "y corregí el menú JavaFX."],
     "VER PR #4", "https://github.com/CondezJuan8/Formula1Simulator/pull/4"),
]


def crossover(i, tema, movil=False):
    clave, etiqueta, titulo, desc, desc_movil, cta, _ = APORTES[i]
    k = TEMAS[tema]
    color = k["rojo"] if i == 0 else k["azul"]
    if movil:
        w, h = 640, 250
        s = marco(w, h, k, color)
        s += caja_nombre(22, 22, etiqueta, k, 15)
        s += desfase(24, 100, titulo, 36, k, d=2)
        s += t(26, 140, desc_movil[0], 21, k["suave"]) + t(26, 168, desc_movil[1], 21, k["suave"])
        s += boton(24, 190, w - 58, cta, k, color)
    else:
        w, h = 960, 150
        s = marco(w, h, k, color)
        s += caja_nombre(22, 22, etiqueta, k)
        s += desfase(24, 94, titulo, 30, k, d=1.5)
        s += t(26, 126, desc, 17, k["suave"])
        s += boton(w - 220, 54, 180, cta, k, color)
    guardar(f"crossover-{clave}-{tema}" + ("-mobile" if movil else ""), w, h, s,
            f"{titulo}: {desc} {cta}.", CSS_PORTADA)


REGLAS = [
    ("Separo las reglas del negocio", "de frameworks y servicios.",
     '<path d="M20 4l14 8v16l-14 8-14-8V12z"/><path d="M20 12l7 4v8l-7 4-7-4v-8z"/>'),
    ("Versiono la base de datos", "con migraciones.",
     '<ellipse cx="20" cy="9" rx="13" ry="5"/><path d="M7 9v22c0 3 6 5 13 5s13-2 13-5V9M7 20c0 3 6 5 13 5s13-2 13-5"/>'),
    ("Documento alcance, pruebas", "y lo que queda pendiente.",
     '<path d="M9 3h16l7 7v27H9z"/><path d="M25 3v7h7"/><path d="M14 24l4 4 8-9"/>'),
    ("Trabajo con agentes de IA", "con reglas escritas y revisión.",
     '<rect x="4" y="7" width="32" height="26" rx="3"/><path d="M4 13h32M11 20l5 4-5 4M19 28h9"/>'),
]


def metodo(tema, movil=False):
    k = TEMAS[tema]
    if movil:
        w, h, cols, cw, ch, y0 = 640, 520, 1, 600, 104, 70
    else:
        w, h, cols, cw, ch, y0 = 960, 270, 2, 450, 96, 72
    s = marco(w, h, k, k["rojo"], (1, 1), alto_trama=0)
    s += caja_nombre(22, 22, "CÓMO TRABAJO", k)
    tam_texto = 22 if movil else 18
    for j, (l1, l2, forma) in enumerate(REGLAS):
        x = 24 + (j % cols) * (cw + 20)
        y = y0 + (j // cols) * ch
        base = f'transform="translate({x} {y + 10}) scale(1.2)" fill="none" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"'
        s += (f'<g {base} stroke="{k["azul"]}" opacity="0.7"><g transform="translate(-1.5 0)">{forma}</g></g>'
              f'<g {base} stroke="{k["rojo"]}" opacity="0.7"><g transform="translate(1.5 0.6)">{forma}</g></g>'
              f'<g {base}><g class="g g{j}" stroke="{k["tinta"]}">{forma}</g></g>')
        s += t(x + 70, y + 32, l1, tam_texto, k["tinta"], 700) + t(x + 70, y + 32 + tam_texto + 6, l2, tam_texto, k["suave"])
    css = (f".g{{animation:enciende 8s steps(1) infinite}}"
           f"@keyframes enciende{{0%,22%{{stroke:{k['rojo']}}}25%,100%{{stroke:{k['tinta']}}}}}"
           + "".join(f".g{j}{{animation-delay:{j * 2}s}}" for j in range(4)))
    guardar(f"method-{tema}" + ("-mobile" if movil else ""), w, h, s,
            "Cómo trabajo: " + " ".join(f"{a} {b}" for a, b, _ in REGLAS), css)


def generar():
    for movil in (False, True):
        for tema in TEMAS_LISTA:
            for numero, clave, titulo in CAPITULOS:
                rotulo(numero, clave, titulo, tema, movil)
            for i in range(len(PROYECTOS)):
                portada(i, tema, movil)
            for i in range(len(APORTES)):
                crossover(i, tema, movil)
            metodo(tema, movil)


if __name__ == "__main__":
    generar()
