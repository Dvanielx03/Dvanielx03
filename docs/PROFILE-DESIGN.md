# Diseño visual del perfil

## Encargo y dirección

Perfil de Daniel Santiago Mayorga / Dvanielx03. Objetivo: facilitar que un posible cliente entienda qué problemas aborda su trabajo y cómo iniciar una conversación. Rol verificado: desarrollador backend junior. Se conservan titulación, idiomas y contactos autorizados. No se incluye experiencia laboral ni sección de recorrido de proyectos. No se usan emojis.

Dirección elegida: una mesa de conexiones de backend, con tipografía de gran formato, diagramas del flujo de cada proyecto y líneas de enlace entre secciones. La firma es una línea azul que une entradas, reglas y salidas. Los diagramas son explicaciones esquemáticas, no capturas de interfaces ni sistemas anunciados como producción.

## Sistema visual

| Token | Valor | Uso |
| --- | --- | --- |
| Midnight | #152640 | Hero, paneles de proyectos y CTA |
| Cobalt | #4D7CFE | Conexiones y foco |
| Action | #315DD9 | Fondos de contacto con texto blanco |
| Apricot | #F2B181 | Acentos secundarios |
| Ice | #F5F8FD | Tipografía sobre paneles |
| Steel | #B7C9E2 | Etiquetas sobre paneles |
| Border | #334B6C | Separadores y estructura |

Tipografía: Arial/Helvetica para titulares y texto; Consolas/Liberation Mono para etiquetas técnicas. Son familias de reserva: no se descargan fuentes.

Composición: una sola columna; proyectos consecutivos; capacidades agrupadas; colaboración con PR enlazados; formación, idiomas y forma de trabajo; cierre de contacto. Las tablas amplias se sustituyen por grupos breves de texto para mejorar el uso móvil.

Los SVG tienen variante compacta cuando contienen texto. La cabecera usa imagen alternativa para pantallas pequeñas con <picture>. Los nombres, capacidades, aportes y contactos continúan en Markdown. Los SVG no contienen scripts, recursos remotos ni animaciones; por ello no hay que esperar a una secuencia para entender el perfil.

## Investigación

Revisión realizada el 11 de noviembre de 2026:

- [Blueprint Schematic](https://github.com/beydemirfurkan/awesome-github-profile/tree/main/templates/10-print-analog/blueprint-schematic): referencia para las conexiones y la lectura por capas.
- [Type Specimen](https://github.com/beydemirfurkan/awesome-github-profile/tree/main/templates/11-swiss-brutalist/type-specimen): referencia para una jerarquía tipográfica con personalidad.
- [Open to Work](https://github.com/beydemirfurkan/awesome-github-profile/tree/main/templates/13-purpose-built/open-to-work): útil por su ruta de contacto; no se adoptan disponibilidad, modalidad contractual ni plazos no confirmados.
- [Light / Dark Switcher](https://github.com/beydemirfurkan/awesome-github-profile/tree/main/templates/08-markdown-tricks/light-dark-switcher): referencia para <picture>. La composición elegida mantiene paneles oscuros autocontenidos que funcionan en los dos temas; <picture> se usa para adaptar la composición al tamaño.
- [Capsule Render](https://github.com/kyechan99/capsule-render): se evaluaron sus cabeceras. El propio proyecto advierte de límites de disponibilidad del servicio público; no se añadió una dependencia en ese endpoint.
- [Readme Typing SVG](https://github.com/DenverCoder1/readme-typing-svg): se evaluó el efecto de escritura. Se descartó porque retrasaría el mensaje principal y repetiría la dirección visual anterior.
- [Awesome GitHub Profile README](https://github.com/abhisheknaiidu/awesome-github-profile-readme): catálogo de estilos y ejemplos; no se copian datos ni identidades.

La implementación SVG es propia; no se copiaron gráficos ni código de las plantillas. Se mantiene intacto el recurso terminal anterior con su atribución existente.

## Mantenimiento

Ejecutar desde la raíz del repositorio:

    python assets/profile/generate.py

El generador usa solo la biblioteca estándar de Python. Los archivos SVG generados se publican junto al README y son las fuentes servidas por GitHub. Los textos profesionales se editan en README.md. No se activan workflows de actualización ni se añaden tokens.

Actualizar la evidencia al publicar versiones relevantes. El resultado del diseño se evalúa con la rúbrica de 100 puntos adjunta al informe de revisión; una valoración estética no demuestra conversión comercial.
