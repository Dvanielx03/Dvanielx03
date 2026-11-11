# Diseño visual del perfil

## Dirección: «Fuera de registro»

Perfil de Daniel Santiago Mayorga / Dvanielx03, rediseñado el 11 de noviembre de 2026. El lenguaje visual reinterpreta la animación de Spider-Verse sin usar personajes, máscaras ni logotipos: una impresión de cómic con las tintas cian y magenta desplazadas, trama de puntos (halftone) y contorno de tinta. La tarjeta Aurora Veil del nombre sigue siendo la referencia central; su turquesa y su magenta pasan a funcionar como las dos tintas de impresión.

Principios:

- Una sola idea visual repetida con mesura: desfase de tintas + trama de puntos.
- Una sola animación: al cargar, el nombre aparece desfasado y encaja su registro en siete pasos a 12 fotogramas por segundo, la «animación a dos» de las películas. Después queda quieto. La aurora original sigue moviéndose.
- El texto importante vive en Markdown; las imágenes solo refuerzan.

## Sistema visual

| Token | Noche (tema oscuro) | Papel (tema claro) | Uso |
| --- | --- | --- | --- |
| Fondo | #070B22 | #FBF4E2 | Paneles |
| Tinta | #FEF3C7 | #070B22 | Texto principal y contornos |
| Suave | #CBD5E1 | #4A4F6A | Texto secundario |
| Cian | #3FFFE6 | #00A3B4 | Tinta desplazada, sombras de pegatinas |
| Magenta | #FF3D8A | #D61F69 | Tinta desplazada, trama y telaraña |
| Línea | #3B335F | #D9CDB0 | Divisores |

Tipografía: Fraunces/Playfair/Georgia itálica para el nombre (de la tarjeta original); Arial Black para los titulares de viñeta; Arial para el texto; Consolas/Liberation Mono para etiquetas. No se descargan fuentes.

## Estructura

1. Tarjeta del nombre (H1) con cuatro variantes en `<picture>`: escritorio, móvil y sus versiones estáticas para movimiento reducido.
2. Presentación en primera persona, titulación, idiomas y enlaces de contacto.
3. Proyectos: un tríptico de viñetas (XEON, Tool Rental, Motion Studio) y debajo cada proyecto con «Compruébalo» y «Estado».
4. Tecnologías: tira de pegatinas y cuatro líneas de dónde se usan.
5. Colaboración y método.
6. Cierre «Continuará…» con una esquina de telaraña hecha de puntos, enlazado al correo.

Cada pieza tiene versión noche y papel, elegida con `prefers-color-scheme`, y versión móvil a 640 px cuando contiene texto. Solo hay 2 divisores.

Se retiraron respecto a la versión anterior: el eslogan «Ideas nuevas», los diez iconos de título, el menú de navegación, los diagramas repetidos de los proyectos, las secciones vacías de Portafolio y Hoja de vida (se añadirán como enlaces junto al contacto cuando existan) y el triple bloque de contacto.

## Fuentes y licencias

La tarjeta adapta [Aurora Veil](https://github.com/beydemirfurkan/awesome-github-profile/tree/main/templates/09-avant-garde/aurora-veil) (MIT). La fuente original está en `assets/profile/vendor/aurora-veil.svg` y su licencia en `assets/profile/vendor/LICENSE`, copiada también en los SVG derivados. El resto de los dibujos y el generador son propios. Ningún SVG contiene scripts ni recursos remotos.

## Mantenimiento

Desde la raíz del repositorio:

    python assets/profile/generate.py

Los textos de las viñetas están en `VINETAS` y las tecnologías en `TECNOLOGIAS`, dentro del generador. Los textos profesionales se editan en README.md. Revisar el perfil al publicar un proyecto importante, cambiar de rol o iniciar una búsqueda laboral.
