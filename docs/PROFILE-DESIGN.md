# Diseño visual del perfil

## Encargo y dirección

Perfil de Daniel Santiago Mayorga / Dvanielx03. Objetivo: facilitar que un posible cliente entienda qué problemas aborda su trabajo y cómo iniciar una conversación. Rol verificado: desarrollador backend junior. Se conservan titulación, idiomas y contactos autorizados. No se incluye experiencia laboral ni sección de recorrido de proyectos. No se usan emojis.

Dirección elegida: Aurora Veil presenta el nombre sobre auroras animadas y un paisaje nocturno. La decoración restante mantiene los diagramas de backend y las líneas de conexión, adaptados a turquesa, violeta y magenta. Los diagramas son explicaciones esquemáticas, no capturas de interfaces ni sistemas anunciados como producción.

## Sistema visual

| Token | Valor | Uso |
| --- | --- | --- |
| Night | #070B22 | Fondo de los paneles, tomado del cielo de Aurora Veil |
| Deep sky | #0E1B3A | Contacto y fondo de iconos |
| Teal | #3FFFE6 | Conexiones, iconos y botón principal |
| Violet | #A78BFA | Acentos y contornos |
| Magenta | #FF3D8A | Puntos de unión y aurora |
| Warm light | #FEF3C7 | Nombres y texto sobre paneles |
| Cloud | #CBD5E1 | Etiquetas secundarias |
| Border | #3B335F | Separadores y estructura |

Tipografía: la tarjeta del nombre usa la pila Fraunces/Playfair Display/Georgia de la plantilla, con Georgia como alternativa local; Arial/Helvetica para las demás tarjetas y Consolas/Liberation Mono para etiquetas técnicas. No se descargan fuentes.

Composición: una sola columna; proyectos consecutivos; capacidades agrupadas; colaboración con PR enlazados; formación, idiomas y forma de trabajo; cierre de contacto. Las tablas amplias se sustituyen por grupos breves de texto para mejorar el uso móvil.

Los SVG tienen variante compacta cuando contienen texto. La tarjeta del nombre utiliza <picture> para seleccionar una composición móvil o una versión estática cuando se solicita reducir movimiento. El nombre y el rol siempre están visibles: la animación afecta al cielo y las estrellas. La tarjeta conserva una cabecera H1 accesible mediante su texto alternativo. Capacidades, aportes y contactos siguen en texto. Ningún SVG contiene scripts ni recursos remotos. Solo la tarjeta del nombre usa animaciones SMIL y filtros de turbulencia; las demás decoraciones son estáticas.

## Investigación

Revisión realizada el 11 de noviembre de 2026:

- [Blueprint Schematic](https://github.com/beydemirfurkan/awesome-github-profile/tree/main/templates/10-print-analog/blueprint-schematic): referencia para las conexiones y la lectura por capas.
- [Type Specimen](https://github.com/beydemirfurkan/awesome-github-profile/tree/main/templates/11-swiss-brutalist/type-specimen): referencia para una jerarquía tipográfica con personalidad.
- [Open to Work](https://github.com/beydemirfurkan/awesome-github-profile/tree/main/templates/13-purpose-built/open-to-work): útil por su ruta de contacto; no se adoptan disponibilidad, modalidad contractual ni plazos no confirmados.
- [Light / Dark Switcher](https://github.com/beydemirfurkan/awesome-github-profile/tree/main/templates/08-markdown-tricks/light-dark-switcher): referencia para <picture>. La composición elegida mantiene paneles oscuros autocontenidos que funcionan en los dos temas; <picture> se usa para adaptar la composición al tamaño.
- [Capsule Render](https://github.com/kyechan99/capsule-render): se evaluaron sus cabeceras. El propio proyecto advierte de límites de disponibilidad del servicio público; no se añadió una dependencia en ese endpoint.
- [Readme Typing SVG](https://github.com/DenverCoder1/readme-typing-svg): se evaluó el efecto de escritura. Se descartó porque retrasaría el mensaje principal y repetiría la dirección visual anterior.
- [Awesome GitHub Profile README](https://github.com/abhisheknaiidu/awesome-github-profile-readme): catálogo de estilos y ejemplos; no se copian datos ni identidades.

La tarjeta del nombre adapta directamente [Aurora Veil](https://github.com/beydemirfurkan/awesome-github-profile/tree/main/templates/09-avant-garde/aurora-veil), por petición del titular. La fuente original se conserva en assets/profile/vendor/aurora-veil.svg (blob c91a64b56210fd023e8932dad4c607342a64f0ee). Su licencia MIT está en assets/profile/vendor/LICENSE y se incluye también en los SVG derivados. Se sustituyeron el nombre, el rol y las etiquetas; se retiraron las coordenadas y datos de ejemplo. El resto de los dibujos y su generador son propios. El recurso terminal anterior conserva su atribución.

La escena animada se mantiene en las variantes de escritorio y móvil. Las dos variantes estáticas eliminan todos los elementos animate, conservando los colores, el paisaje y el texto. Solo una de las cuatro fuentes se muestra en cada viewport. La preferencia de movimiento reducido la evalúa el navegador mediante la etiqueta picture.

## Verificación de Aurora Veil

- Los SVG animados conservan 20 elementos SMIL; las dos alternativas estáticas no contienen ninguno.
- La cabecera H1 conserva nombre y rol como nombre accesible de la imagen.
- La vista de preparación cargó las 23 imágenes del README sin errores. A 390 px seleccionó la composición móvil y no presentó desbordamiento horizontal del cuerpo.
- Se observó variación de la aurora en capturas separadas del SVG abierto directamente y de la tarjeta incrustada en el README.
- Los contrastes de la decoración son 17,46:1 para texto sobre el panel, 13,10:1 para etiquetas, 7,14:1 para acentos violetas y 15,42:1 para el texto oscuro del botón turquesa. Los iconos tienen fondo propio para conservar el contraste en superficies claras y oscuras.
- La generación usa únicamente la biblioteca estándar y conserva una copia de la fuente y su licencia. No se añade ningún proveedor externo de imágenes.

## Mantenimiento

Las secciones Portafolio web y Hoja de vida están reservadas con su icono y separador, en la misma paleta de Aurora Veil. Muestran «Próximamente» hasta que el titular proporcione la URL del sitio y el PDF o enlace público de la hoja de vida. No contienen enlaces de ejemplo ni una descarga ficticia. Sus accesos en el menú solo llevan a esas secciones del README.

Ejecutar desde la raíz del repositorio:

    python assets/profile/generate.py

El generador usa solo la biblioteca estándar de Python. Los archivos SVG generados se publican junto al README y son las fuentes servidas por GitHub. Los textos profesionales se editan en README.md. No se activan workflows de actualización ni se añaden tokens.

Actualizar la evidencia al publicar versiones relevantes. El resultado del diseño se evalúa con la rúbrica de 100 puntos adjunta al informe de revisión; una valoración estética no demuestra conversión comercial.
