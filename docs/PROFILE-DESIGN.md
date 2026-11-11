# Diseño visual del perfil

## Dirección: «Fuera de registro», paleta Miles

Perfil de Daniel Santiago Mayorga / Dvanielx03, rediseñado el 11 de noviembre de 2026. El lenguaje visual reinterpreta la animación de Spider-Verse sin usar personajes, máscaras ni logotipos oficiales: impresión de cómic con la tinta roja y la azul fuera de registro, trama de puntos (Ben-Day), contorno de tinta y movimiento «a dos» (12 fotogramas por segundo, siempre a saltos).

La primera versión usaba cian y magenta; se cambió porque ese desfase sobre negro recuerda al logotipo de TikTok. La paleta actual parte del traje negro y rojo, con azul eléctrico solo para destellos y amarillo para los cuadros de narración.

## Sistema visual

| Token | Noche (tema oscuro) | Papel (tema claro) | Uso |
| --- | --- | --- | --- |
| Fondo | #120C18 | #FBF4E2 | Paneles |
| Tinta | #F5EFE6 | #140E19 | Texto principal y contornos |
| Suave | #C9C0D3 | #4D4556 | Texto secundario |
| Rojo | #F0313C | #D3121C | Tinta principal, telarañas, sombras |
| Azul | #3D7BFF | #1F5FE0 | Tinta desplazada y destellos |
| Amarillo | #FFD23F | #FFD23F | Cuadros de narración y rol |
| Línea | #3A2E46 | #DCCFB3 | Divisores |

Tipografía: Fraunces/Playfair/Georgia itálica para el nombre; Arial Black para titulares de viñeta; Arial para el texto; Consolas/Liberation Mono para etiquetas. No se descargan fuentes.

## Tarjeta y personaje

La tarjeta adapta Aurora Veil: la aurora se recolorea a rojo y púrpura, las montañas se sustituyen por azoteas con tanques de agua y ventanas encendidas, y a la derecha aparece «Daniel en el Spider-Verse», una ilustración original: sudadera abierta sobre un traje negro con líneas rojas, audífonos al cuello, zapatillas altas rojas y la máscara en la mano. No reproduce el emblema ni los rasgos de ningún personaje existente, y no usa imágenes oficiales.

Animaciones de la tarjeta (SMIL, con variantes estáticas para movimiento reducido):

- El nombre llega fuera de registro y encaja en siete pasos a 12 fps.
- Cada 6 s, tres franjas del nombre se desplazan y vuelven a su sitio (glitch de dimensión).
- Líneas de sentido arácnido vibran alrededor de la cabeza cada 4 s.
- Daniel respira a saltos y los ojos de la máscara destellan en azul cada 3 s.
- El rol parpadea en azul eléctrico cada 5 s.

## Componentes animados

Todas usan CSS con `steps()` dentro del SVG; la regla `prefers-reduced-motion` las detiene y deja el estado final visible.

| Pieza | Animación |
| --- | --- |
| Divisor | Una telaraña se dispara de izquierda a derecha y se pega con una salpicadura de puntos, cada 6 s |
| Tríptico | Las viñetas entran con fotograma de impacto; el globo de XEON escribe «…» y pasa a `{ }`, la etiqueta de Tool Rental se balancea y la tira de Motion Studio avanza fotograma a fotograma |
| Pegatinas | Se pegan una a una con un golpe, quedan algo giradas y cada 6 s vuelven a asentarse por turnos |
| Cierre | La telaraña se teje anillo a anillo, «CONTINUARÁ…» parpadea y una araña genérica baja por su hilo |

Cada pieza tiene versión noche y papel (`prefers-color-scheme`) y versión móvil a 640 px cuando contiene texto.

## Fuentes y licencias

La tarjeta adapta [Aurora Veil](https://github.com/beydemirfurkan/awesome-github-profile/tree/main/templates/09-avant-garde/aurora-veil) (MIT). La fuente original está en `assets/profile/vendor/aurora-veil.svg` y su licencia en `assets/profile/vendor/LICENSE`, copiada también en los SVG derivados. El personaje, el resto de los dibujos y el generador son propios. Ningún SVG contiene scripts ni recursos remotos.

Referencias de técnica consultadas: simulación de Ben-Day y errores de impresión offset, Kirby dots, separación de color fuera de foco y frame rate de animación 2D en Spider-Verse.

## Mantenimiento

Desde la raíz del repositorio:

    python assets/profile/generate.py

Los textos de las viñetas están en `VINETAS`, las tecnologías en `TECNOLOGIAS` y el personaje en `personaje()`, dentro del generador. Los textos profesionales se editan en README.md. Revisar el perfil al publicar un proyecto importante, cambiar de rol o iniciar una búsqueda laboral.
