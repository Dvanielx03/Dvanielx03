"""Genera el encabezado del perfil en versión clara y oscura.

Uso (desde la raíz del repositorio):

    python assets/generar_encabezado.py

Para añadir un proyecto, agrega una fila al final de MIGRACIONES con la
fecha de creación del repositorio y vuelve a ejecutar el script. Recuerda
añadir la misma fila a la tabla «Historial completo» del README.
"""

from pathlib import Path
from xml.sax.saxutils import escape

NOMBRE = "Daniel Santiago Mayorga"
ROL = "Desarrollador backend junior: Java, Python y PostgreSQL"
CONSULTA = "SELECT version, descripcion, creado, estado FROM flyway_schema_history;"

# (versión, descripción en estilo de script Flyway, fecha de creación del repo)
MIGRACIONES = [
    ("V1", "sistema_prestamo_herramientas", "2026-01-22"),
    ("V2", "wildlens_ai_vision", "2026-06-19"),
    ("V3", "sst_pesv_multi_tenant", "2026-09-21"),
    ("V4", "clinica_flyway_52_tablas", "2026-10-01"),
    ("V5", "clinica_jpa_ddd", "2026-10-04"),
    ("V6", "xeon_agente_cotizaciones", "2026-10-08"),
    ("V7", "tool_rental_platform", "2026-10-09"),
    ("V8", "campus_gestion_operativa", "2026-10-16"),
    ("V9", "motion_studio_skill", "2026-10-28"),
]

TEMAS = {
    "claro": {
        "fondo": "#F2F5F8",
        "borde": "#C9D3DD",
        "texto": "#16212C",
        "suave": "#566574",
        "linea": "#D6DEE6",
        "version": "#9A4A00",
        "exito": "#1C6B44",
        "franja": "#E8EDF2",
    },
    "oscuro": {
        "fondo": "#131B23",
        "borde": "#2B3743",
        "texto": "#E4EAF0",
        "suave": "#97A4B1",
        "linea": "#26313C",
        "version": "#F0A35C",
        "exito": "#63C792",
        "franja": "#18222C",
    },
}

ANCHO = 880
FILA = 27
SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace"
COLUMNAS = {"version": 44, "descripcion": 112, "creado": 520, "estado": 694}


def svg(tema: dict) -> str:
    y_cabecera = 196
    y_primera = y_cabecera + 34
    alto = y_primera + FILA * (len(MIGRACIONES) - 1) + 40

    filas = []
    for i, (version, descripcion, creado) in enumerate(MIGRACIONES):
        y = y_primera + i * FILA
        franja = (
            f'<rect x="28" y="{y - 19}" width="{ANCHO - 56}" height="{FILA}" fill="{tema["franja"]}"/>'
            if i % 2 == 0
            else ""
        )
        filas.append(
            f"<g>{franja}"
            f'<text x="{COLUMNAS["version"]}" y="{y}" class="m v">{version}</text>'
            f'<text x="{COLUMNAS["descripcion"]}" y="{y}" class="m">{escape(descripcion)}</text>'
            f'<text x="{COLUMNAS["creado"]}" y="{y}" class="m s">{creado}</text>'
            f'<text x="{COLUMNAS["estado"]}" y="{y}" class="m e">Success</text></g>'
        )

    cabecera = "".join(
        f'<text x="{x}" y="{y_cabecera}" class="m s b">{nombre}</text>'
        for nombre, x in COLUMNAS.items()
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO}" height="{alto}" viewBox="0 0 {ANCHO} {alto}" role="img" aria-labelledby="t d">
<title id="t">{escape(NOMBRE)}</title>
<desc id="d">{escape(ROL)}. Historial de proyectos presentado como migraciones de Flyway, de V1 a V{len(MIGRACIONES)}.</desc>
<style>
.n{{font:700 40px {SANS};fill:{tema["texto"]};letter-spacing:-0.5px}}
.r{{font:400 20px {SANS};fill:{tema["suave"]}}}
.m{{font:400 16px {MONO};fill:{tema["texto"]}}}
.q{{font:400 14px {MONO};fill:{tema["suave"]}}}
.s{{fill:{tema["suave"]}}}
.b{{font-weight:700;font-size:14px}}
.v{{fill:{tema["version"]};font-weight:700}}
.e{{fill:{tema["exito"]}}}
.cursor{{animation:aplicar {0.16 * len(MIGRACIONES):.2f}s steps({len(MIGRACIONES) - 1}, jump-none) .4s both}}
@keyframes aplicar{{from{{transform:translateY(0)}}to{{transform:translateY({FILA * (len(MIGRACIONES) - 1)}px)}}}}
@media (prefers-reduced-motion:reduce){{.cursor{{animation:none;transform:translateY({FILA * (len(MIGRACIONES) - 1)}px)}}}}
</style>
<rect x="0.5" y="0.5" width="{ANCHO - 1}" height="{alto - 1}" rx="10" fill="{tema["fondo"]}" stroke="{tema["borde"]}"/>
<text x="44" y="78" class="n">{escape(NOMBRE)}</text>
<text x="44" y="112" class="r">{escape(ROL)}</text>
<line x1="28" y1="140" x2="{ANCHO - 28}" y2="140" stroke="{tema["linea"]}"/>
<text x="44" y="168" class="q">{escape(CONSULTA)}</text>
{cabecera}
<line x1="28" y1="{y_cabecera + 10}" x2="{ANCHO - 28}" y2="{y_cabecera + 10}" stroke="{tema["linea"]}"/>
{"".join(filas)}
<rect class="cursor" x="28" y="{y_primera - 19}" width="4" height="{FILA}" fill="{tema["version"]}"/>
</svg>
"""


def main() -> None:
    carpeta = Path(__file__).parent
    for nombre, tema in TEMAS.items():
        destino = carpeta / f"encabezado-{nombre}.svg"
        destino.write_text(svg(tema), encoding="utf-8")
        print(f"{destino.name}: {destino.stat().st_size} bytes")


if __name__ == "__main__":
    main()
