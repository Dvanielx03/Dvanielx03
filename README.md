<h1>
<picture>
  <source media="(max-width: 600px) and (prefers-reduced-motion: reduce)" srcset="./assets/profile/aurora-name-mobile-static.svg">
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/profile/aurora-name-static.svg">
  <source media="(max-width: 600px)" srcset="./assets/profile/aurora-name-mobile.svg">
  <img src="./assets/profile/aurora-name.svg" width="100%" alt="Daniel Santiago Mayorga · Junior Backend Developer">
</picture>
</h1>

Soy Daniel, **Junior Backend Developer** y Técnico Laboral en Desarrollo de Software. Construyo APIs y bases de datos con **Java, Spring Boot, Python, FastAPI y PostgreSQL**, y me gusta probar ideas nuevas hasta ver qué puedo crear con lo que aprendo.

Español nativo · Inglés B2<br>
[LinkedIn](https://www.linkedin.com/in/daniel-santiago-mayorga-tellez-5bb0463a0/) · [Correo](mailto:danielsantiagomayorga03@gmail.com) · [Discord](https://discord.com/users/1445751258022416415)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile/divider-noche.svg">
  <img src="./assets/profile/divider-papel.svg" width="100%" alt="">
</picture>

## Proyectos

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="./assets/profile/projects-noche-mobile.svg">
  <source media="(max-width: 600px)" srcset="./assets/profile/projects-papel-mobile.svg">
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile/projects-noche.svg">
  <img src="./assets/profile/projects-papel.svg" width="100%" alt="Tres viñetas: XEON, la IA interpreta y el backend decide; Tool Rental, del catálogo a la devolución; Motion Studio, cada fotograma es una función del tiempo.">
</picture>

### [XEON · Cotizaciones asistidas por IA](https://github.com/Dvanielx03/Xeon-agente-cotizaciones)

Recibe solicitudes por WhatsApp o terminal, busca productos y prepara borradores de cotización. El modelo interpreta la conversación; el backend calcula precios, descuentos y disponibilidad con `Decimal`, dentro de una arquitectura hexagonal con FastAPI.

**Compruébalo:** [arquitectura](https://github.com/Dvanielx03/Xeon-agente-cotizaciones/blob/develop/docs/ARCHITECTURE.md) y [CI aprobado con Ruff, mypy y Pytest](https://github.com/Dvanielx03/Xeon-agente-cotizaciones/actions/runs/40413280218).<br>
**Estado:** prototipo con catálogo sintético. El borrador no reserva inventario ni equivale a una cotización aprobada.

### [Tool Rental Platform · Alquiler de herramientas](https://github.com/Dvanielx03/Tool-rental-platform)

Proyecto en equipo con **Java 21, Spring Boot y PostgreSQL**: catálogo, reservas, pagos académicos y operaciones de cliente, proveedor y administrador. Mi aporte fue la integración del MVP, Docker Compose y la verificación de recorridos y persistencia.

**Compruébalo:** [responsabilidades e integración](https://github.com/Dvanielx03/Tool-rental-platform/blob/develop/docs/mvp.md) y [persistencia por roles](https://github.com/Dvanielx03/Tool-rental-platform/blob/develop/docs/provider-persistence.md).<br>
**Estado:** validado en local; demo pública pendiente y pagos simulados.

### [Motion Studio · Video programable para agentes](https://github.com/Dvanielx03/motion-studio-design)

Skill abierta con licencia MIT para crear video con HTML y JavaScript, del guion al MP4. Cada fotograma depende de `window.seek(t)` y se renderiza con **Playwright, Chrome y FFmpeg**.

**Compruébalo:** [video de ejemplo](https://github.com/Dvanielx03/motion-studio-design/tree/main/ejemplo) y [pruebas 2.5D](https://github.com/Dvanielx03/motion-studio-design/blob/main/docs/analysis/2026-11-06-make-short-integrado.md).<br>
**Estado:** render validado principalmente en Windows 11 con RTX 3050.

## Tecnologías

<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="./assets/profile/technologies-noche-mobile.svg">
  <source media="(max-width: 600px)" srcset="./assets/profile/technologies-papel-mobile.svg">
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile/technologies-noche.svg">
  <img src="./assets/profile/technologies-papel.svg" width="100%" alt="Tecnologías principales: Java, Spring Boot, Python, FastAPI, PostgreSQL y Docker.">
</picture>

- **Java:** Spring Boot, JPA/Hibernate y Maven en Tool Rental y el [backend clínico](https://github.com/Dvanielx03/SpringBootDataJPA-DDD).
- **Python:** FastAPI, Pydantic y Typer en XEON, con Pytest, Ruff, mypy y GitHub Actions.
- **Datos:** PostgreSQL y Flyway; SQLite y SQLAlchemy en [Campus Control](https://github.com/Dvanielx03/soluciones-rocket); SQL y PL/pgSQL en la [plataforma multiempresa de seguridad laboral y vial](https://github.com/Dvanielx03/Plataforma_multi-tenant_de_gesti-n_SST-PESV).
- **Interfaces y video:** JavaScript y React en Tool Rental y [WildLens AI](https://github.com/Dvanielx03/fiftyone_pruebas); JavaFX en Formula1Simulator; Playwright y FFmpeg en Motion Studio.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile/divider-noche.svg">
  <img src="./assets/profile/divider-papel.svg" width="100%" alt="">
</picture>

## Colaboración y método

**[Campus Control](https://github.com/Dvanielx03/soluciones-rocket)**: hackatón de cinco integrantes. Me encargué de la persistencia, los datos iniciales, el inventario, la importación y Docker Compose. [Responsabilidades del equipo](https://github.com/Dvanielx03/soluciones-rocket/blob/main/docs/teamResponsibilities.md) · [PR integrado](https://github.com/Dvanielx03/soluciones-rocket/pull/3).

**[Formula1Simulator](https://github.com/CondezJuan8/Formula1Simulator)**: aporté una refactorización a arquitectura hexagonal y correcciones del menú JavaFX. [PR integrado](https://github.com/CondezJuan8/Formula1Simulator/pull/4).

**Cómo trabajo:**

- Separo las reglas del negocio de los frameworks y servicios externos.
- Versiono los cambios de base de datos con migraciones.
- Documento el alcance, las pruebas disponibles y lo que queda pendiente.
- Trabajo con agentes de IA mediante instrucciones escritas y revisión de cambios.

<a href="mailto:danielsantiagomayorga03@gmail.com">
<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="./assets/profile/contact-noche-mobile.svg">
  <source media="(max-width: 600px)" srcset="./assets/profile/contact-papel-mobile.svg">
  <source media="(prefers-color-scheme: dark)" srcset="./assets/profile/contact-noche.svg">
  <img src="./assets/profile/contact-papel.svg" width="100%" alt="¿Construimos algo juntos? Escríbeme con tu idea, tu reto o una oportunidad.">
</picture>
</a>

Escríbeme a [danielsantiagomayorga03@gmail.com](mailto:danielsantiagomayorga03@gmail.com) o por [LinkedIn](https://www.linkedin.com/in/daniel-santiago-mayorga-tellez-5bb0463a0/).

<!-- Responsable: Daniel Santiago Mayorga. Revisión: 2026-11-11.
Dirección visual «Fuera de registro»: docs/PROFILE-DESIGN.md. Generar los SVG: python assets/profile/generate.py
Portafolio web y hoja de vida: añadir sus enlaces junto al contacto cuando estén publicados.
-->
