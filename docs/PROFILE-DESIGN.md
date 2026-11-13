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
| Cajones | El título de cada Tierra hace un glitch a saltos cada 5 s, desfasado entre cajones |
| Pegatinas | Se pegan con un golpe y quedan algo giradas; un brillo las recorre por turnos y su contador «×N» late |
| Fichas | El logo salta en glitch cada 4 s y el sello «VERIFICADO» cae con un golpe cada 6 s |
| Cierre | La telaraña se teje anillo a anillo, «CONTINUARÁ…» parpadea y una araña genérica baja por su hilo |

Cada pieza tiene versión noche y papel (`prefers-color-scheme`) y versión móvil a 640 px cuando contiene texto. Ninguna animación empieza con la pieza oculta: si un visor no reproduce la animación, el contenido sigue visible.

## Composición por capítulos

El README se lee como un cómic por capítulos. Cada sección abre con un rótulo SVG («CAP. 01 Proyectos», «CAP. 02 Tecnologías», «CAP. 03 Colaboración y método»): cuadro amarillo, título con tinta roja y azul fuera de registro, un hilo de telaraña con su nudo y marcas de registro de imprenta en las esquinas. Los rótulos sustituyen a los antiguos divisores. Su título hace un glitch a saltos cada 6 s, desfasado entre capítulos.

- **Proyectos:** cada proyecto es una tarjeta-portada completa (nombre, dibujo animado, titular, una frase, logos del stack, sello de estado y banda «ABRIR REPOSITORIO») enlazada a su repositorio. No hay texto suelto debajo; las pruebas viven en cada repositorio.
- **Colaboración y método:** los aportes son tarjetas «crossover» enlazadas a su PR, y «Cómo trabajo» es un panel 2×2 donde cada glifo se enciende en rojo por turnos.
- **Cierre:** la tarjeta «Continuará…», enlazada al correo, y debajo dos botones de cómic: WhatsApp (`wa.me/573247571239`) y Gmail. Los botones activos llevan sombra roja o azul, flecha que empuja y un brillo ocasional.
- **Contraportada:** franja «FIN DEL N.º 01» con código de barras decorativo y los botones activos Portafolio y Hoja de vida. Enlazan al [portafolio DanielVerse](https://dvanielx03.github.io/DanielVerse/#E0-P1) y a la descarga del [CV en PDF](./CV-Daniel-Santiago-Mayorga.pdf), copiado sin modificaciones del archivo facilitado por Daniel. Sus destinos se mantienen en `EXTRAS` (`assets/profile/secciones.py`); al cambiarlos se debe regenerar. Los bloques del README entre `<!-- contacto:… -->` y `<!-- final:… -->` los escribe el generador.

Regla técnica: GitHub convierte en enlace a sí misma toda imagen que no esté dentro de un enlace propio, y eso separa la imagen de su `<picture>` (se pierden las variantes de móvil y tema). Por eso cada `<picture>` va dentro de un `<a>` útil y en una sola línea, y las pestañas de los cajones son texto.

## Sección Tecnologías: cajones del multiverso

GitHub no ejecuta JavaScript en un README y lo que hay dentro de un SVG no se puede pulsar. Por eso la sección usa lo único interactivo nativo, `<details>`: cuatro cajones plegables (Tierra-01 Backend, Tierra-02 Frontend, Tierra-03 Datos y Tierra-04 Herramientas e IA). La pestaña es texto con estilo de tecla (`<kbd>TIERRA-01</kbd> Backend`); al abrirla aparecen la cabecera ilustrada y las pegatinas. Todos empiezan cerrados.

Cada tecnología es una pegatina independiente dentro de un enlace. El número amarillo indica en cuántos proyectos públicos aparece. Al pulsarla se abre su ficha de expediente en `docs/stack/`, con una tabla de proyectos y un sello «VERIFICADO» que enlaza al archivo exacto donde se declara o se usa (`pom.xml`, `package.json`, `pyproject.toml`, `compose.yaml`…). Las tecnologías sin proyecto público (Supabase, y LangChain, Streamlit y TypeScript, que solo están en un repositorio privado) lo dicen en su ficha y no muestran contador.

Los datos viven en `CATEGORIAS`, dentro de `assets/profile/stack.py`. El generador escribe las pegatinas, las cabeceras, las fichas y el bloque del README entre `<!-- tecnologias:inicio -->` y `<!-- tecnologias:fin -->`. Los logotipos proceden de [Simple Icons](https://github.com/simple-icons/simple-icons) (CC0), guardados en `assets/profile/vendor/simple-icons.json`; son marcas de sus titulares y solo nombran cada tecnología. VS Code no está en Simple Icons y se dibuja como una ventana de editor genérica.

Antes de publicar, comprobar que todas las pruebas siguen existiendo:

    python -c "import sys; sys.path.insert(0, 'assets/profile'); import stack, urllib.request; print([u for u in stack.evidencias() if urllib.request.urlopen(urllib.request.Request(u, method='HEAD')).status != 200])"

## Fuentes y licencias

La tarjeta adapta [Aurora Veil](https://github.com/beydemirfurkan/awesome-github-profile/tree/main/templates/09-avant-garde/aurora-veil) (MIT). La fuente original está en `assets/profile/vendor/aurora-veil.svg` y su licencia en `assets/profile/vendor/LICENSE`, copiada también en los SVG derivados. El personaje, el resto de los dibujos y el generador son propios. Ningún SVG contiene scripts ni recursos remotos.

Referencias de técnica consultadas: simulación de Ben-Day y errores de impresión offset, Kirby dots, separación de color fuera de foco y frame rate de animación 2D en Spider-Verse.

## Mantenimiento

Desde la raíz del repositorio:

    python assets/profile/generate.py

Los textos de las viñetas están en `VINETAS`, las tecnologías en `TECNOLOGIAS` y el personaje en `personaje()`, dentro del generador. Los textos profesionales se editan en README.md. Revisar el perfil al publicar un proyecto importante, cambiar de rol o iniciar una búsqueda laboral.

Caché de imágenes: GitHub y los navegadores guardan cada SVG por su ruta. Cuando un cambio visual importante no aparece en el perfil, renombrar el archivo (en el generador y en README.md) obliga a todos a descargar la versión nueva. Por eso la tarjeta pasó de `aurora-name*.svg` a `miles-card*.svg` al añadir el personaje, y a `daniel-card*.svg` al añadir los roles («JUNIOR BACKEND · AI ENGINEERING · CREADOR DE CONTENIDO»; en móvil, «BACKEND · IA · CREADOR DE CONTENIDO»; constantes `ROL` y `ROL_MOVIL` en el generador).
