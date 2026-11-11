"""Genera assets/terminal.svg, el encabezado del perfil.

Basado en la plantilla «Typewriter Intro» de
https://github.com/beydemirfurkan/awesome-github-profile (MIT).

Uso, desde la raíz del repositorio:

    python assets/generar_terminal.py

Para cambiar el texto, edita las listas de abajo y vuelve a ejecutarlo.
"""

from pathlib import Path
from xml.sax.saxutils import escape

USUARIO = "daniel@backend"
TITULO = "~/daniel — bash"

# Cada bloque: (comando, [(color, texto), ...])
BLOQUES = [
    (
        "whoami",
        [
            ("texto", "↳ Daniel Santiago Mayorga — desarrollador backend junior"),
            ("suave", "  APIs y bases de datos con Java, Python y PostgreSQL"),
        ],
    ),
    (
        "cat habilidades.txt",
        [
            ("titulo", "## lenguajes     Java  Python  SQL  JavaScript"),
            ("titulo", "## frameworks    Spring Boot  FastAPI  React  Node.js"),
            ("titulo", "## herramientas  PostgreSQL  MySQL  Docker  Git  n8n"),
        ],
    ),
    (
        "contact --all",
        [("enlace", "→ github.com/TuMinipeka   linkedin   discord")],
    ),
]

COLORES = {
    "usuario": "#a78bfa",
    "prompt": "#7ee787",
    "separador": "#7a7f99",
    "texto": "#c9d1d9",
    "suave": "#8b90a8",
    "titulo": "#fcd34d",
    "enlace": "#58a6ff",
}

ANCHO, ALTO = 1000, 470
X = 72
TAM = 17
CARACTER = TAM * 0.62  # ancho aproximado de un carácter monoespaciado
LINEA = 25
FUENTE = "ui-monospace, SFMono-Regular, 'JetBrains Mono', Consolas, 'Liberation Mono', Menlo, monospace"

# Ritmo de la animación (segundos)
PAUSA_INICIAL = 0.4
POR_CARACTER = 0.06
ESPERA_SALIDA = 0.25
ENTRE_BLOQUES = 0.45
DURACION = 7.0


def prompt(y: int) -> str:
    return (
        f'<tspan fill="{COLORES["usuario"]}">{USUARIO}</tspan>'
        f'<tspan fill="{COLORES["separador"]}">:</tspan>'
        f'<tspan fill="{COLORES["prompt"]}">~</tspan>'
        f'<tspan fill="{COLORES["separador"]}">$ </tspan>'
    )


def clave(t: float) -> str:
    return f"{min(max(t / DURACION, 0), 1):.4f}"


def svg() -> str:
    partes = []
    recortes = []
    y = 112
    t = PAUSA_INICIAL
    ancho_prompt = (len(USUARIO) + 4) * CARACTER

    for n, (comando, salidas) in enumerate(BLOQUES):
        # Línea del comando: aparece el prompt y después se escribe el comando.
        fin_escritura = t + len(comando) * POR_CARACTER
        ancho_total = ancho_prompt + len(comando) * CARACTER + 8
        recortes.append(
            f'<clipPath id="c{n}"><rect x="{X - 4}" y="{y - TAM - 2}" height="{TAM + 10}" width="{ancho_total:.0f}">'
            f'<animate attributeName="width" dur="{DURACION}s" fill="freeze" '
            f'values="0;0;{ancho_prompt:.0f};{ancho_total:.0f};{ancho_total:.0f}" '
            f'keyTimes="0;{clave(t)};{clave(t)};{clave(fin_escritura)};1"/></rect></clipPath>'
        )
        partes.append(
            f'<text x="{X}" y="{y}" clip-path="url(#c{n})">{prompt(y)}'
            f'<tspan fill="{COLORES["texto"]}">{escape(comando)}</tspan></text>'
        )
        t = fin_escritura + ESPERA_SALIDA
        y += LINEA + 3

        # Salidas: aparecen de golpe, como en una terminal real.
        for color, texto in salidas:
            partes.append(
                f'<text x="{X}" y="{y}" fill="{COLORES[color]}" xml:space="preserve">{escape(texto)}'
                f'<animate attributeName="opacity" dur="{DURACION}s" fill="freeze" values="0;0;1;1" '
                f'keyTimes="0;{clave(t)};{clave(t)};1"/></text>'
            )
            y += LINEA
        t += ENTRE_BLOQUES
        y += 14

    # Prompt final con el cursor parpadeando.
    partes.append(
        f'<text x="{X}" y="{y}">{prompt(y)}'
        f'<animate attributeName="opacity" dur="{DURACION}s" fill="freeze" values="0;0;1;1" '
        f'keyTimes="0;{clave(t)};{clave(t)};1"/></text>'
    )
    partes.append(
        f'<rect x="{X + ancho_prompt:.0f}" y="{y - TAM + 3}" width="10" height="{TAM}" fill="{COLORES["texto"]}">'
        f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.1s" repeatCount="indefinite"/></rect>'
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {ALTO}" width="{ANCHO}" height="{ALTO}" role="img" aria-label="Terminal: Daniel Santiago Mayorga, desarrollador backend junior. Lenguajes: Java, Python, SQL y JavaScript. Frameworks: Spring Boot, FastAPI, React y Node.js. Herramientas: PostgreSQL, MySQL, Docker, Git y n8n.">
  <defs>
    <linearGradient id="fondo" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1a1238"/>
      <stop offset="1" stop-color="#0d0820"/>
    </linearGradient>
    <filter id="sombra" x="-10%" y="-10%" width="120%" height="130%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="20"/>
      <feOffset dy="12"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.5"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    {"".join(recortes)}
  </defs>

  <rect width="{ANCHO}" height="{ALTO}" rx="16" fill="url(#fondo)"/>

  <g filter="url(#sombra)">
    <rect x="40" y="30" width="{ANCHO - 80}" height="{ALTO - 60}" rx="14" fill="#11131c"/>
    <rect x="40" y="30" width="{ANCHO - 80}" height="40" rx="14" fill="#1c1f2e"/>
    <rect x="40" y="52" width="{ANCHO - 80}" height="18" fill="#1c1f2e"/>
    <line x1="40" y1="70" x2="{ANCHO - 40}" y2="70" stroke="#0a0c14" stroke-width="0.6"/>
  </g>

  <circle cx="68" cy="50" r="7" fill="#ff5f56"/>
  <circle cx="92" cy="50" r="7" fill="#ffbd2e"/>
  <circle cx="116" cy="50" r="7" fill="#27c93f"/>
  <text x="{ANCHO / 2:.0f}" y="55" text-anchor="middle" font-family="{FUENTE}" font-size="13" fill="#7a7f99" letter-spacing="1">{escape(TITULO)}</text>

  <g font-family="{FUENTE}" font-size="{TAM}">
    {chr(10).join("    " + p for p in partes).strip()}
  </g>

  <rect x="40" y="{ALTO - 54}" width="{ANCHO - 80}" height="24" rx="14" fill="#171a26"/>
  <rect x="40" y="{ALTO - 54}" width="{ANCHO - 80}" height="12" fill="#171a26"/>
  <line x1="40" y1="{ALTO - 54}" x2="{ANCHO - 40}" y2="{ALTO - 54}" stroke="#0a0c14" stroke-width="0.6"/>
  <g font-family="{FUENTE}" font-size="11" fill="#5a5f7a">
    <text x="70" y="{ALTO - 38}">UTF-8</text>
    <text x="130" y="{ALTO - 38}">bash</text>
    <text x="{ANCHO - 70}" y="{ALTO - 38}" text-anchor="end" fill="#7ee787">● conectado</text>
  </g>
</svg>
"""


def main() -> None:
    destino = Path(__file__).parent / "terminal.svg"
    destino.write_text(svg(), encoding="utf-8")
    print(f"{destino.name}: {destino.stat().st_size} bytes")


if __name__ == "__main__":
    main()
