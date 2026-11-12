"""Sección Tecnologías: «cajones del multiverso», pegatinas y fichas de expediente.

Se ejecuta desde generate.py (python assets/profile/generate.py). Genera:

- assets/profile/stack/cajon-<categoria>-<tema>.svg   cabecera de cada cajón
- assets/profile/stack/<tecnologia>-<tema>.svg         pegatina pulsable
- assets/profile/stack/ficha-<tecnologia>.svg          cabecera de la ficha
- assets/profile/stack/sello.svg                       sello «VERIFICADO»
- docs/stack/<tecnologia>.md                          ficha de expediente
- el bloque de README.md entre <!-- tecnologias:inicio --> y <!-- tecnologias:fin -->

Cada uso declarado apunta al archivo del repositorio que lo prueba. Para añadir
una tecnología: agrégala a CATEGORIAS con sus usos y vuelve a ejecutar el generador.
"""
import json
from pathlib import Path
from xml.sax.saxutils import escape

from generate import ROOT, TEMAS, MONO, SANS, TEXTO, t, desfase, trama, guardar

REPO = ROOT.parent.parent
PERFIL = "https://github.com/Dvanielx03"
ICONOS = json.loads((ROOT / "vendor" / "simple-icons.json").read_text(encoding="utf-8"))["icons"]

# Proyectos: (nombre, repositorio, rama)
X = ("XEON", "Dvanielx03/Xeon-agente-cotizaciones", "develop")
TR = ("Tool Rental Platform", "Dvanielx03/Tool-rental-platform", "develop")
JPA = ("Backend clínico con JPA y DDD", "Dvanielx03/SpringBootDataJPA-DDD", "main")
FW = ("Backend clínico con Flyway", "Dvanielx03/BackendMigraci-n_SpringBoot", "main")
CC = ("Campus Control", "Dvanielx03/soluciones-rocket", "main")
WL = ("WildLens AI", "Dvanielx03/fiftyone_pruebas", "main")
MS = ("Motion Studio", "Dvanielx03/motion-studio-design", "main")
SST = ("Plataforma SST/PESV", "Dvanielx03/Plataforma_multi-tenant_de_gesti-n_SST-PESV", "main")
SP = ("Sistema de préstamo de herramientas", "Dvanielx03/Sistema-Prestamo-Herramientas", "main")
GF = ("GoogleFlow Studio", "Dvanielx03/googleflow-studio", "main")
F1 = ("Formula1Simulator (aporte)", "CondezJuan8/Formula1Simulator", "develop")

PRIVADO = "La uso en un proyecto privado (deportivo-langchain); su código no es público."
SIN_PUBLICO = "La uso, pero todavía no tengo un proyecto público con ella."
TODOS = "Todos mis proyectos se versionan con Git y se publican en GitHub."

# (clave, nombre, icono, [(proyecto, archivo que lo prueba)], nota)
CATEGORIAS = [
    ("backend", "TIERRA-01", "Backend", [
        ("java", "Java", "openjdk", [(TR, "pom.xml"), (JPA, "pom.xml"), (FW, "pom.xml"), (F1, "pom.xml")], ""),
        ("spring-boot", "Spring Boot", "springboot", [(TR, "pom.xml"), (JPA, "pom.xml"), (FW, "pom.xml")], ""),
        ("hibernate", "Hibernate / JPA", "hibernate", [(TR, "infrastructure/pom.xml"), (JPA, "infrastructure/pom.xml")], ""),
        ("maven", "Maven", "apachemaven", [(TR, "pom.xml"), (JPA, "pom.xml"), (FW, "pom.xml"), (F1, "pom.xml")], ""),
        ("python", "Python", "python", [(X, "pyproject.toml"), (CC, "backend/requirements.txt"), (WL, "backend/requirements.txt"),
                                        (MS, "motion-studio/scripts/nuevo.py"), (SP, "main.py")], ""),
        ("fastapi", "FastAPI", "fastapi", [(X, "pyproject.toml"), (CC, "backend/requirements.txt"), (WL, "backend/requirements.txt")], ""),
    ]),
    ("frontend", "TIERRA-02", "Frontend", [
        ("html", "HTML", "html5", [(TR, "frontend/index.html"), (CC, "frontend/index.html"), (WL, "frontend/index.html"),
                                   (MS, "motion-studio/assets/plantilla/index.html")], ""),
        ("css", "CSS", "css", [(TR, "frontend/src/styles.css"), (CC, "frontend/src/styles.css"), (WL, "frontend/src/index.css")], ""),
        ("javascript", "JavaScript", "javascript", [(TR, "frontend/src/main.jsx"), (CC, "frontend/src/main.jsx"), (WL, "frontend/src/main.jsx"),
                                                    (MS, "motion-studio/assets/plantilla/kit/camara.js")], ""),
        ("typescript", "TypeScript", "typescript", [], PRIVADO),
        ("react", "React", "react", [(TR, "frontend/package.json"), (CC, "frontend/package.json"), (WL, "frontend/package.json")], ""),
        ("tailwind", "Tailwind CSS", "tailwindcss", [(CC, "frontend/package.json")], PRIVADO),
        ("vite", "Vite", "vite", [(TR, "frontend/vite.config.js"), (CC, "frontend/vite.config.js"), (WL, "frontend/vite.config.js")], ""),
    ]),
    ("datos", "TIERRA-03", "Datos", [
        ("postgresql", "PostgreSQL", "postgresql", [(TR, "infrastructure/pom.xml"), (JPA, "infrastructure/pom.xml"),
                                                    (SST, "sql/01_schema.sql"), (X, "pyproject.toml")], ""),
        ("flyway", "Flyway", "flyway", [(TR, "infrastructure/pom.xml"), (JPA, "infrastructure/pom.xml"), (FW, "infrastructure/pom.xml")], ""),
        ("sqlalchemy", "SQLAlchemy", "sqlalchemy", [(X, "pyproject.toml"), (CC, "backend/requirements.txt")], ""),
        ("sqlite", "SQLite", "sqlite", [(CC, "backend/app/core/config.py")], ""),
        ("supabase", "Supabase", "supabase", [], SIN_PUBLICO),
    ]),
    ("herramientas", "TIERRA-04", "Herramientas e IA", [
        ("git", "Git", "git", [], TODOS),
        ("github", "GitHub", "github", [], TODOS),
        ("vscode", "VS Code", None, [(X, ".vscode/settings.json"), (TR, ".vscode/settings.json"), (JPA, ".vscode/settings.json"),
                                     (MS, ".vscode/settings.json")], ""),
        ("docker", "Docker", "docker", [(X, "compose.yaml"), (TR, "compose.yml"), (CC, "compose.yaml"), (WL, "docker-compose.yml"),
                                        (SST, "docker-compose.yml")], ""),
        ("github-actions", "GitHub Actions", "githubactions", [(X, ".github/workflows/ci.yml"), (CC, ".github/workflows/commit-convention.yml")], ""),
        ("pytest", "Pytest", "pytest", [(X, "pyproject.toml"), (CC, "backend/requirements.txt"), (WL, "backend/requirements.txt")], ""),
        ("google-flow", "Google Flow", "google", [(GF, "SKILL.md")], ""),
        ("langchain", "LangChain", "langchain", [], PRIVADO),
        ("streamlit", "Streamlit", "streamlit", [], PRIVADO),
    ]),
]

# VS Code no está en Simple Icons: se dibuja una ventana de editor genérica.
EDITOR = '<path d="M3 4.5h18v15H3z M3 8h18 M9.5 11l-3 3 3 3 M14.5 11l3 3-3 3" fill="none" stroke-width="1.6" stroke-linejoin="round"/>'


def blob(proyecto, archivo):
    _, repo, rama = proyecto
    return f"https://github.com/{repo}/blob/{rama}/{archivo}"


def logo(icono, x, y, tam, color, extra=""):
    """Logo de 24 unidades escalado a `tam` píxeles con esquina en (x, y)."""
    e = tam / 24
    if icono is None:
        return f'<g transform="translate({x:g} {y:g}) scale({e:.3f})" stroke="{color}" {extra}>{EDITOR}</g>'
    return f'<g transform="translate({x:g} {y:g}) scale({e:.3f})" fill="{color}" {extra}><path d="{ICONOS[icono]["path"]}"/></g>'


def logo_desfasado(icono, x, y, tam, k, d=2.5):
    """El logo se define una vez y se reutiliza para las tres tintas (archivos más ligeros)."""
    e = tam / 24
    if icono is None:
        forma, pintura = EDITOR, "stroke"
    else:
        forma, pintura = f'<path d="{ICONOS[icono]["path"]}"/>', "fill"
    defs = f'<defs><g id="L">{forma}</g></defs>'

    def copia(dx, dy, color):
        return (f'<use href="#L" transform="translate({x + dx:g} {y + dy:g}) scale({e:.3f})" '
                f'{pintura}="{color}"/>')
    return (defs + f'<g opacity="0.85">{copia(-d, -d * 0.4, k["azul"])}{copia(d, d * 0.4, k["rojo"])}</g>'
            + copia(0, 0, k["tinta"]))


def cuenta(usos):
    return len({p[1] for p, _ in usos})


# ---------------------------------------------------------------- Pegatina

CSS_PEGATINA = (
    ".p{transform-origin:center;animation:pega .5s steps(1) var(--r) forwards}"
    "@keyframes pega{0%{opacity:1;transform:scale(1) rotate(0deg)}"
    "33%{opacity:1;transform:scale(.92) rotate(0deg)}66%,100%{opacity:1;transform:scale(1) rotate(var(--g))}}"
    ".brillo{animation:brillo 7s steps(1) var(--b) infinite}"
    "@keyframes brillo{0%,90%{transform:translateX(0)}92%{transform:translateX(90px)}"
    "94%{transform:translateX(150px)}96%{transform:translateX(210px)}98%,100%{transform:translateX(320px)}}"
    ".placa{animation:placa 3s steps(1) var(--b) infinite}"
    "@keyframes placa{0%,88%{transform:scale(1)}90%{transform:scale(1.25)}94%,100%{transform:scale(1)}}"
)


def pegatina(clave, nombre, icono, usos, nota, tema, indice):
    k = TEMAS[tema]
    w, h = 128, 148
    giro = [-3, 2, -1, 3, -2, 1, 2, -3][indice % 8]
    sombra = k["rojo"] if indice % 2 == 0 else k["azul"]
    n = cuenta(usos)
    tam_texto = min(15, 104 / (len(nombre) * 0.6))
    cuerpo = (f'<clipPath id="c"><rect x="8" y="10" width="106" height="124" rx="14"/></clipPath>'
              f'<rect x="14" y="16" width="106" height="124" rx="14" fill="{sombra}"/>'
              f'<rect x="9.5" y="11.5" width="103" height="121" rx="13" fill="{k["fondo"]}" stroke="{k["contorno"]}" stroke-width="3"/>'
              f'<g clip-path="url(#c)">{trama(60, 10, 54, 50, sombra, 8, 2.6, (1, 0), 1.0, 0.35)}'
              f'<path class="brillo" d="M-40 10L-18 10L-50 134L-72 134Z" fill="#FFFFFF" opacity="0.28"/></g>'
              + logo_desfasado(icono, 33, 30, 56, k)
              + t(61, 118, nombre, f"{tam_texto:.1f}", k["tinta"], 700, TEXTO, 'text-anchor="middle"'))
    if n:
        cuerpo += (f'<g class="placa"><circle cx="106" cy="18" r="15" fill="{k["amarillo"]}" stroke="{k["contorno"]}" stroke-width="2.5"/>'
                   + t(106, 23, f"×{n}", 13, k["sobre_amarillo"], 700, SANS, 'text-anchor="middle"') + "</g>")
    css = CSS_PEGATINA + f".p{{--g:{giro}deg;--r:{indice * 0.09:.2f}s}}.brillo,.placa{{--b:{indice * 0.6:.1f}s}}"
    detalle = (f"usada en {n} proyecto{'s' if n != 1 else ''} público{'s' if n != 1 else ''}"
               if n else "sin proyecto público enlazado")
    guardar(f"stack/{clave}-{tema}", w, h, f'<g class="p">{cuerpo}</g>', f"{nombre}: {detalle}", css)


# ---------------------------------------------------------------- Cajón

def cajon(cid, tierra, titulo, techs, tema, orden):
    k = TEMAS[tema]
    w, h = 960, 128
    s = (f'<rect x="1.5" y="1.5" width="{w - 3}" height="{h - 3}" rx="8" fill="{k["fondo"]}" stroke="{k["contorno"]}" stroke-width="3"/>'
         f'<clipPath id="m"><rect x="0" y="0" width="{w}" height="{h}" rx="8"/></clipPath>'
         f'<g clip-path="url(#m)">{trama(w - 420, 0, 420, h, k["rojo"] if orden % 2 == 0 else k["azul"], 10, 3.4, (1, 1), 1.0, 0.3)}</g>')
    s += (f'<rect x="20" y="18" width="128" height="30" fill="{k["amarillo"]}" stroke="{k["contorno"]}" stroke-width="2"/>'
          + t(32, 39, tierra, 17, k["sobre_amarillo"], 700, MONO, 'letter-spacing="1"')
          + t(162, 39, f"{len(techs)} TECNOLOGÍAS", 15, k["suave"], 400, MONO, 'letter-spacing="1"'))
    s += f'<g class="titulo">{desfase(22, 100, titulo, 44, k)}</g>'
    # Vista previa de los logos del cajón, de derecha a izquierda.
    paso = min(46, 360 / len(techs))
    tam = min(30, paso - 12)
    x = w - 34 - tam
    for _, _, icono, _, _ in reversed(techs):
        s += logo(icono, x, 70, tam, k["tinta"])
        x -= paso
    css = (f".titulo{{animation:glitch 5s steps(1) {orden * 1.25:.2f}s infinite}}"
           "@keyframes glitch{0%,90%{transform:translate(0,0)}91%{transform:translate(-14px,0)}"
           "92%{transform:translate(10px,-2px)}93%{transform:translate(-4px,1px)}94%,100%{transform:translate(0,0)}}")
    guardar(f"stack/cajon-{cid}-{tema}", w, h, s, f"{tierra}: {titulo}, {len(techs)} tecnologías", css)


# ---------------------------------------------------------------- Ficha

def marcas(w, h, color):
    """Marcas de registro de imprenta en las cuatro esquinas."""
    s = ""
    for x, y, sx, sy in ((14, 14, 1, 1), (w - 14, 14, -1, 1), (14, h - 14, 1, -1), (w - 14, h - 14, -1, -1)):
        s += f'<path d="M{x} {y + sy * 14}V{y}H{x + sx * 14}" fill="none" stroke="{color}" stroke-width="1.5"/>'
    return s


def cabecera_ficha(clave, nombre, icono, usos, nota, numero, tierra, categoria):
    k = TEMAS["noche"]
    w, h = 960, 250
    n = cuenta(usos)
    s = (f'<rect width="{w}" height="{h}" rx="10" fill="{k["fondo"]}"/>'
         f'{trama(w - 380, 0, 380, 190, k["rojo"], 12, 4.4, (1, 0), 1.0, 0.35)}'
         f'{marcas(w, h, k["suave"])}')
    s += (f'<rect x="40" y="34" width="{len(f"EXPEDIENTE N.º {numero:02d} · {tierra} {categoria.upper()}") * 10 + 24}" height="30" '
          f'fill="{k["amarillo"]}" stroke="{k["contorno"]}" stroke-width="2"/>'
          + t(52, 55, f"EXPEDIENTE N.º {numero:02d} · {tierra} {categoria.upper()}", 16, k["sobre_amarillo"], 700, MONO))
    s += f'<g class="logo">{logo_desfasado(icono, 44, 88, 112, k, 4)}</g>'
    s += desfase(186, 164, nombre, 60 if len(nombre) < 14 else 48, k, d=2)
    if n:
        linea = f"Usada en {n} proyecto{'s' if n != 1 else ''} público{'s' if n != 1 else ''}, con la prueba en el código."
    else:
        linea = "Uso personal o en proyectos privados."
    s += t(188, 204, linea, 18, k["suave"], 400, TEXTO)
    if n:
        s += (f'<g class="sello" transform="rotate(-9 820 120)"><rect x="730" y="94" width="180" height="52" rx="6" fill="none" '
              f'stroke="{k["rojo"]}" stroke-width="4"/>' + t(820, 131, "VERIFICADO", 26, k["rojo"], 700, SANS,
                                                           'text-anchor="middle" letter-spacing="2"') + "</g>")
    css = (".logo{animation:salto 4s steps(1) infinite}"
           "@keyframes salto{0%,86%{transform:translate(0,0)}88%{transform:translate(-8px,0)}"
           "90%{transform:translate(6px,-2px)}92%,100%{transform:translate(0,0)}}"
           ".sello{transform-origin:center;transform-box:fill-box;animation:sella 6s steps(1) infinite}"
           "@keyframes sella{0%{opacity:0;transform:rotate(-9deg) scale(1.7)}4%{opacity:1;transform:rotate(-9deg) scale(.9)}"
           "8%,100%{opacity:1;transform:rotate(-9deg) scale(1)}}")
    guardar(f"stack/ficha-{clave}", w, h, s, f"Expediente de {nombre}", css)


def sello():
    k = TEMAS["noche"]
    s = (f'<g class="s" transform="rotate(-5 64 18)"><rect x="4" y="4" width="120" height="28" rx="4" fill="none" '
         f'stroke="{k["rojo"]}" stroke-width="2.5"/>' + t(64, 24, "VERIFICADO", 14, k["rojo"], 700, SANS,
                                                         'text-anchor="middle" letter-spacing="2"') + "</g>")
    css = (".s{transform-origin:center;transform-box:fill-box;animation:golpe 4s steps(1) infinite}"
           "@keyframes golpe{0%,92%{transform:rotate(-5deg) scale(1)}94%{transform:rotate(-5deg) scale(1.15)}"
           "96%,100%{transform:rotate(-5deg) scale(1)}}")
    guardar("stack/sello", 128, 36, s, "Verificado", css)


def ficha_md(clave, nombre, icono, usos, nota, tierra, categoria):
    filas = ""
    for proyecto, archivo in usos:
        titulo, repo, _ = proyecto
        filas += (f"| [{titulo}](https://github.com/{repo}) | "
                  f'<a href="{blob(proyecto, archivo)}"><img src="../../assets/profile/stack/sello.svg" height="26" alt="Verificado"></a> '
                  f"[`{archivo}`]({blob(proyecto, archivo)}) |\n")
    cuerpo = ""
    if filas:
        cuerpo += ("## Dónde la uso\n\nCada sello abre el archivo del proyecto donde se declara o se usa.\n\n"
                   "| Proyecto | Prueba |\n| :-- | :-- |\n" + filas + "\n")
    if nota == PRIVADO and filas:
        cuerpo += "> **Nota:** también la uso en un proyecto privado (deportivo-langchain), cuyo código no es público.\n\n"
    elif nota:
        cuerpo += f"{nota}\n\n"
    if clave in ("git", "github"):
        cuerpo += f"[Ver todos mis repositorios]({PERFIL}?tab=repositories)\n\n"
    return (f'<img src="../../assets/profile/stack/ficha-{clave}.svg" width="100%" alt="Expediente de {nombre}">\n\n'
            f"**{tierra} · {categoria}**\n\n{cuerpo}"
            f"[Volver al perfil]({PERFIL})\n\n"
            f"<!-- Generado por assets/profile/stack.py. Edita los datos allí, no este archivo. -->\n")


# ---------------------------------------------------------------- README

def bloque_readme():
    total = sum(len(techs) for *_, techs in CATEGORIAS)
    s = ("<!-- tecnologias:inicio (generado por assets/profile/stack.py) -->\n"
         f"Abre cada Tierra y toca una pegatina: verás los proyectos donde uso esa tecnología, "
         f"con la prueba en el código. El número indica en cuántos proyectos públicos aparece.\n\n")
    for orden, (cid, tierra, titulo, techs) in enumerate(CATEGORIAS):
        # La pestaña es texto: GitHub convierte en enlace toda imagen sin enlace propio, y una
        # imagen dentro de <summary> abriría el SVG en lugar de desplegar el cajón.
        # Todos los cajones empiezan cerrados.
        s += ("<details>\n"
              f"<summary><kbd>{tierra}</kbd> <b>{titulo}</b> · {len(techs)} tecnologías</summary>\n<br>\n\n"
              f'<a href="#tecnologias"><picture>'
              f'<source media="(prefers-color-scheme: dark)" srcset="./assets/profile/stack/cajon-{cid}-noche.svg">'
              f'<img src="./assets/profile/stack/cajon-{cid}-papel.svg" width="100%" alt="{tierra}: {titulo}, {len(techs)} tecnologías">'
              f"</picture></a>\n\n")
        for clave, nombre, _, usos, _ in techs:
            n = cuenta(usos)
            alt = f"{nombre}: {n} proyectos" if n else nombre
            s += (f'<a href="./docs/stack/{clave}.md"><picture>'
                  f'<source media="(prefers-color-scheme: dark)" srcset="./assets/profile/stack/{clave}-noche.svg">'
                  f'<img src="./assets/profile/stack/{clave}-papel.svg" width="96" alt="{escape(alt)}"></picture></a> ')
        # Todas en una línea: así ningún modo de Markdown inserta saltos entre pegatinas.
        s = s.rstrip() + "\n\n</details>\n\n"
    s += "<!-- tecnologias:fin -->"
    return s, total


def generar():
    (ROOT / "stack").mkdir(exist_ok=True)
    docs = REPO / "docs" / "stack"
    docs.mkdir(parents=True, exist_ok=True)
    sello()
    numero = 0
    for orden, (cid, tierra, titulo, techs) in enumerate(CATEGORIAS):
        for tema in TEMAS:
            cajon(cid, tierra, titulo, techs, tema, orden)
        for indice, (clave, nombre, icono, usos, nota) in enumerate(techs):
            numero += 1
            for tema in TEMAS:
                pegatina(clave, nombre, icono, usos, nota, tema, indice)
            cabecera_ficha(clave, nombre, icono, usos, nota, numero, tierra, titulo)
            (docs / f"{clave}.md").write_text(ficha_md(clave, nombre, icono, usos, nota, tierra, titulo), encoding="utf-8")
    readme = REPO / "README.md"
    texto = readme.read_text(encoding="utf-8")
    inicio, fin = texto.find("<!-- tecnologias:inicio"), texto.find("<!-- tecnologias:fin -->")
    if inicio != -1 and fin != -1:
        bloque, _ = bloque_readme()
        readme.write_text(texto[:inicio] + bloque + texto[fin + len("<!-- tecnologias:fin -->"):], encoding="utf-8")


def evidencias():
    """Lista (url) de todas las pruebas, para comprobarlas."""
    return sorted({blob(p, a) for *_, techs in CATEGORIAS for *_, usos, _ in techs for p, a in usos})


if __name__ == "__main__":
    generar()
