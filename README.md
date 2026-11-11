# Daniel Santiago Mayorga

**Desarrollador backend junior · Java, Python y SQL**

Construyo APIs para gestionar alquileres, cotizaciones e inventarios con **Spring Boot**, **FastAPI** y bases de datos relacionales. Mi trabajo público combina reglas de negocio separadas de la infraestructura, migraciones de datos y pruebas. También desarrollo herramientas para que agentes de IA creen video con código.

**Empieza por [XEON](https://github.com/Dvanielx03/Xeon-agente-cotizaciones):** un agente de cotización para ferreterías en el que la IA interpreta la conversación y el backend calcula precios, descuentos y disponibilidad.

**Trabajo reciente:** [actualización de capacidades y límites de Motion Studio](https://github.com/Dvanielx03/motion-studio-design/commit/1ebed6c5fef0cc8c5dfdd47b1bdc7bce92c68b42), publicada el 6 de noviembre de 2026.

## Proyectos destacados

### [XEON · Cotizaciones asistidas por IA](https://github.com/Dvanielx03/Xeon-agente-cotizaciones)

Un agente que recibe solicitudes por WhatsApp o terminal, busca productos y prepara borradores de cotización. Las reglas comerciales viven en los casos de uso; los importes se calculan con `Decimal`.

- **Trabajo técnico:** arquitectura hexagonal, API con FastAPI, interfaz de terminal y adaptadores para mensajería y modelos de IA.
- **Evidencia:** [arquitectura](https://github.com/Dvanielx03/Xeon-agente-cotizaciones/blob/develop/docs/ARCHITECTURE.md) y [ejecución aprobada de CI](https://github.com/Dvanielx03/Xeon-agente-cotizaciones/actions/runs/40413280218) con Ruff, mypy y Pytest.
- **Alcance:** prototipo; el catálogo predeterminado es sintético. Un borrador no representa una cotización aprobada ni reserva inventario.

### [Tool Rental Platform · Alquiler de herramientas](https://github.com/Dvanielx03/Tool-rental-platform)

Proyecto en equipo con **Java 21, Spring Boot y PostgreSQL**: catálogo, reservas, pagos académicos y operaciones de cliente, proveedor y administrador.

- **Mi participación documentada:** integración del MVP, entorno con Docker Compose y verificación de recorridos y persistencia, dentro de una arquitectura hexagonal compartida.
- **Evidencia:** [responsabilidades e integración](https://github.com/Dvanielx03/Tool-rental-platform/blob/develop/docs/mvp.md) y [verificación de persistencia por roles](https://github.com/Dvanielx03/Tool-rental-platform/blob/develop/docs/provider-persistence.md).
- **Alcance:** validación local documentada; la demo pública sigue pendiente y los pagos son simulados.

### [Motion Studio · Video programable para agentes](https://github.com/Dvanielx03/motion-studio-design)

Una skill abierta con licencia MIT que guía la creación de video con HTML y JavaScript, desde el guion hasta la exportación. Cada fotograma depende de `window.seek(t)` y se renderiza con **Playwright, Chrome y FFmpeg**.

- **Trabajo técnico:** composición reproducible, render por segmentos y guías de revisión audiovisual.
- **Evidencia:** [ejemplo de video](https://github.com/Dvanielx03/motion-studio-design/tree/main/ejemplo) y [pruebas del flujo 2.5D](https://github.com/Dvanielx03/motion-studio-design/blob/main/docs/analysis/2026-11-06-make-short-integrado.md).
- **Alcance:** la validación de render se concentra en Windows 11 con RTX 3050; las comprobaciones técnicas se complementan con revisión visual y escucha.

## Tecnologías aplicadas

| Área | Tecnologías | Dónde las aplico |
| --- | --- | --- |
| Backend Java | Java, Spring Boot, JPA/Hibernate, Maven | Tool Rental y backend clínico |
| Backend Python | Python, FastAPI, Pydantic, Typer | XEON |
| Datos relacionales | PostgreSQL, Flyway | Tool Rental y backend clínico |
| Persistencia Python | SQLite, SQLAlchemy | Campus Control |
| Lógica de datos | SQL, PL/pgSQL | Plataforma SST/PESV |
| Calidad | Pytest, Ruff, mypy, GitHub Actions | XEON |
| Entorno reproducible | Docker Compose | Tool Rental y Campus Control |
| Interfaces web | JavaScript, React | Tool Rental y WildLens AI |
| Escritorio | Java, JavaFX | Formula1Simulator |
| Video con código | HTML, JavaScript, Playwright, FFmpeg | Motion Studio |

## Colaboración y aportes

- **[Campus Control](https://github.com/Dvanielx03/soluciones-rocket):** hackatón de cinco integrantes. Mi área abarcó persistencia, datos iniciales, inventario, importación y Docker Compose, según la [matriz de responsabilidades](https://github.com/Dvanielx03/soluciones-rocket/blob/main/docs/teamResponsibilities.md). También integré una [corrección de disponibilidad y detalles de reservas](https://github.com/Dvanielx03/soluciones-rocket/pull/3).
- **[Formula1Simulator](https://github.com/CondezJuan8/Formula1Simulator):** aporté una [refactorización a arquitectura hexagonal y correcciones del menú JavaFX](https://github.com/CondezJuan8/Formula1Simulator/pull/4), integrada en el repositorio del equipo.

## Recorrido en proyectos

Estas fechas corresponden a la creación de los repositorios, no a experiencia laboral.

| Etapa | Proyecto | Trabajo publicado |
| --- | --- | --- |
| Enero de 2026 | [Préstamo comunitario de herramientas](https://github.com/Dvanielx03/Sistema-Prestamo-Herramientas) | Gestión de usuarios, inventario y préstamos en Python con persistencia JSON |
| Junio de 2026 | [WildLens AI](https://github.com/Dvanielx03/fiftyone_pruebas) | Prototipo de análisis de fauna con FastAPI, React, FiftyOne y YOLOv8 |
| Septiembre de 2026 | [Gestión SST/PESV](https://github.com/Dvanielx03/Plataforma_multi-tenant_de_gesti-n_SST-PESV) | Base multiempresa para seguridad y salud en el trabajo y planes de seguridad vial; PostgreSQL, normalización y lógica SQL |
| Octubre de 2026 | [Backend clínico](https://github.com/Dvanielx03/SpringBootDataJPA-DDD) | Persistencia JPA y esquema versionado con Flyway en módulos de dominio, aplicación e infraestructura |

## Cómo trabajo

- Separo las reglas del negocio de los frameworks y servicios externos.
- Versiono los cambios de base de datos con migraciones.
- Documento el alcance, las pruebas disponibles y lo que queda pendiente.
- Trabajo con agentes de IA mediante instrucciones escritas y revisión de los cambios.

## Contacto

Puedes escribirme por [LinkedIn](https://www.linkedin.com/in/daniel-santiago-mayorga-tellez-5bb0463a0/) o [Discord](https://discord.com/users/1445751258022416415). Para preguntas técnicas sobre un proyecto, abre un issue en su repositorio.

<!-- Responsable: Daniel Santiago Mayorga. Última revisión: 2026-11-11.
Revisar al publicar un proyecto o una versión importante, cambiar de rol o iniciar una búsqueda laboral.
Formación, experiencia laboral, certificaciones e idiomas se incorporarán cuando el titular confirme los datos.
Los recursos visuales anteriores se conservan en assets/; la decoración de esta versión está pendiente de elección.
-->
