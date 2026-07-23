# defriction — Gobierno, Organización y Gitflow

Startup 4 personas, todas developers. Colombia. Productos: Sinnet App, Finance Tracker Bot, Smart Inventory Bot, automatizaciones custom (Telegram/WhatsApp/Airtable/Stripe). Somos **IA-first**: la IA es parte del equipo, no un add-on. Documento define cómo nos gobernamos y cómo entregamos software.

---

## 1. Estructura de Gobierno

4 personas, todos con empleo, todos developers. Gobierno mínimo: 1 reunión semanal, todo lo demás async.

### 1.1 Principios

- **IA-first.** Antes de escribir código a mano, preguntar: ¿la IA lo hace, lo acelera, o me desbloquea? Default es trabajar asistido por IA (Copilot, Cursor, Claude, ChatGPT). Escribir todo manual es la excepción justificada, no la norma.
- **Todos somos developers.** No hay rol sin teclado. Santiago, Sneider, Julian, Juan Camilo y el CSM están habilitados para tirar código, con IA o sin IA. Los roles definen responsabilidad y criterio de aprobación, no permiso para codear.
- **Code ownership.** Cada proyecto tiene 1 code owner con criterio final sobre su codebase: qué entra, qué no, cuándo sube a `main`. Ownership = responsabilidad, no territorio. Cualquiera puede abrir PR a cualquier repo; el owner decide el merge.
- **IA responsable.** El código generado por IA lo firma un humano. Quien hace commit es 100% responsable del diff, igual que si lo hubiera escrito a mano (ver §1.6).
- **Async o no pasa.** Reuniones síncronas = costo altísimo. Default: escrito, grabado, o no existe.
- **Una decisión, un dueño.** Toda decisión tiene exactamente 1 persona responsable. Otros opinan, dueño decide.
- **Disagree and commit.** Si no hay consenso en 24h async, dueño decide y todos ejecutan.
- **Bloqueo se grita, progreso se calla.** Si estás bloqueado, ping inmediato en Slack. Si todo va bien, no interrumpas — se ve en los PRs.

### 1.2 Foros de gobierno

Mínimo absoluto. Solo 2 eventos sincrónicos recurrentes/eventuales:

| Foro | Frecuencia | Duración | Modalidad | Qué se hace |
|---|---|---|---|---|
| Weekly review (planning + review + daily) | Lunes no festivos | 60 min máx | Videollamada | Contexto de TODOS los proyectos, revisar semana pasada, planificar esta, levantar bloqueos |
| Kickoff de proyecto nuevo | Cuando entra proyecto nuevo | 90 min | Videollamada | Definir arquitectura, infraestructura, stack y code owner del proyecto (ver §1.5) |
| Async check-in | Cada vez que trabajes | 2 min | Slack `#defriction` | Al empezar: "hoy avanzo X". Al terminar: "quedé en Y, sigo Z" |

**Lo que NO existe:** dailys, standups, retros separadas, sprint planning larga, gobierno estratégico mensual, incident reviews sincrónicas. Todo eso está fusionado en la weekly review o es async.

### 1.3 Weekly review — la única reunión recurrente

Lunes no festivos. 60 minutos. Agenda fija, timeboxed:

| Min | Bloque | Qué |
|---|---|---|
| 0-10 | Contexto de proyectos | Tour rápido: estado de CADA proyecto activo (Sinnet, bots, automatizaciones, clientes). Todos salen sabiendo en qué está todo, no solo lo suyo |
| 10-25 | Review semana pasada | Qué se entregó por proyecto, demo rápida (screen share o Loom), qué no quedó y por qué |
| 25-45 | Planning semana actual | Qué entra por proyecto, quién lo toma, estimado en horas reales disponibles |
| 45-55 | Bloqueos y decisiones | Solo los que no se resolvieron async en la semana |
| 55-60 | Retro 1-cosa | Cada quien: 1 cosa a mejorar. Se anota, se revisa próxima semana |

**Por qué el bloque de contexto importa:** con 4 personas y múltiples proyectos, cualquiera puede necesitar saltar a cualquier repo cualquier semana. Si solo sabes de tu proyecto, eres cuello de botella. Los 10 min de contexto garantizan que todos pueden cubrir a todos.

**Reglas duras:**
- Si lunes es festivo, la reunión se mueve al siguiente día hábil o se hace async. No se salta.
- Quien no pueda asistir deja update por escrito 2h antes. Grabación recomendada si alguien falta.
- Si no hay nada sincrónico que discutir, se cancela y todo va async. Mejor cancelar que alargar.

### 1.4 Async check-in

Canal Slack `#defriction`. Formato libre pero sugerido:

```
🟢 inicio: voy a [tarea] — estimado [X horas]
🔴 bloqueado: [qué me frena] — necesito [qué/de quién]
✅ cierre: hice [X] — PR: [link] — sigo con [Y]
```

Regla real: **si trabajaste y nadie sabe en qué, fallaste comunicación. Si estás bloqueado >2h y no lo dijiste, fallaste equipo.**

### 1.5 Kickoff de proyecto nuevo

Cada vez que entra un proyecto nuevo (producto propio o cliente custom), antes de escribir 1 línea de código:

**Asistentes:** todo el equipo (4 personas).

**Agenda (90 min):**

1. **Problema y alcance** (Santiago, 15 min): qué se resuelve, para quién, qué NO se hace.
2. **Arquitectura técnica** (30 min): stack, módulos principales, integraciones, diagrama en Excalidraw/pizarra. Propone quien será code owner, aprueba el equipo.
3. **Infraestructura** (Sneider, 20 min): dónde corre, CI/CD, secretos, monitoreo, costos estimados.
4. **Code owner + equipo** (10 min): quién es owner, quiénes contribuyen.
5. **Plan de entrega** (15 min): milestones, primer entregable, riesgos.

**Output obligatorio (documentado en Notion antes de terminar la reunión):**
- [ ] Nombre del proyecto y repo (convención `defriction/<proyecto>`).
- [ ] Code owner asignado.
- [ ] Diagrama de arquitectura.
- [ ] Stack y justificación de cada pieza no-estándar.
- [ ] Infraestructura: ambientes, deploy, costos.
- [ ] Primer milestone con fecha tentativa.

Sin este output, el proyecto no arranca. 90 min de alineación ahorran semanas de refactor.

### 1.6 Uso responsable de IA

Somos IA-first, pero la IA no firma commits. Reglas:

**Permitido y alentado:**
- Generar features completos con IA, siempre que el autor entienda el diff línea por línea.
- Boilerplate, tests, migraciones, documentación, refactor asistido.
- Debugging asistido, explicación de código legacy, exploración de APIs.
- Prototipos rápidos de Santiago (vibe coding) en automatizaciones.

**Obligatorio:**
- **Entender antes de commitear.** Si no puedes explicar qué hace un bloque en review, no va.
- **Revisar el diff completo.** Nada de "la IA lo generó, seguro está bien". Los bugs de IA son bugs tuyos.
- **Tests pasan local antes de PR.** La IA alucina APIs; el test es el filtro.
- **Nunca pegar secretos, datos de clientes, ni credenciales en prompts.** Nada de datos productivos en herramientas externas sin anonimizar.
- **Marcar código 100% generado si es sustancial** con comentario `// ai-generated, reviewed by @autor` en el archivo o descripción del PR. Ayuda a reviewers a mirar con más lupa.

**Prohibido:**
- Commit de código IA sin leer el diff completo.
- Mergear a `main` código IA que no pasó review humana normal (sin excepción).
- Subir código con claves de API que la IA "rellenó" de ejemplo.
- Confiar validación de seguridad (auth, pagos, sanitización) a código IA sin test manual del camino crítico.

**Responsabilidad:** el autor del commit responde por el código en review, en incidentes y en deuda técnica. "La IA lo escribió" no es defensa.

### 1.7 Matriz de decisión (RACI de dominio)

| Dominio | Decide | Consulta | Informa |
|---|---|---|---|
| Roadmap producto / prioridades | Santiago (PO) | Sneider + Julian | Todos |
| Arquitectura técnica, stack global | Sneider | Julian, Juan Camilo | Santiago |
| Arquitectura de proyecto nuevo | Equipo en kickoff (facilita Sneider) | Todos | Todos |
| Merge a `main` de cada proyecto | Code owner del proyecto | Equipo | Todos |
| Infraestructura, CI/CD, seguridad | Sneider | Julian | Todos |
| Experiencia cliente, bugs reportados | CSM | Santiago | Equipo |
| Pricing, contratos, facturación | Santiago (PO) | Sneider | Todos |
| Contratación | Santiago + Sneider (consenso) | Todos | Todos |
| Estándares de código, convenciones, política IA | Sneider | Todos | Todos |

---

## 2. Roles y Code Ownership

4 personas, todos developers, todos con IA habilitada. Rol define responsabilidad extra, no permiso de código.

### 2.1 Code ownership por proyecto

| Proyecto | Code owner | Backup | Notas |
|---|---|---|---|
| Sinnet App | Sneider | Julian | Producto flagship, backend pesado |
| Finance Tracker Bot | Santiago | Juan Camilo | Bot Telegram, vibe-coded |
| Smart Inventory Bot | Santiago | Julian | Bot Telegram |
| Automatizaciones custom clientes | Santiago | quien esté libre | n8n/Make/Airtable |
| Infraestructura global (CI/CD, servers, secretos) | Sneider | Julian | Cross-proyecto |
| QA y releases | Juan Camilo | Julian | Checklist humo, regresión |

**Criterio del code owner:**
- Aprueba o rechaza PRs a su proyecto.
- Decide cuándo `development` está listo para subir a `main` (ver §3).
- Mantiene el README, la arquitectura y la deuda técnica de su proyecto bajo control.
- Responde primero cuando su proyecto se rompe.

**Regla anti-cuello-de-botella:** si el owner no responde en 24h (part-time, pasa), el backup puede aprobar y mergear. Se registra en el PR: "approved by backup, owner afk".

### 2.2 Santiago — Product Owner + Vibe Coder

**Como Product Owner:**
- Dueño del roadmap y backlog de todos los productos.
- Define y prioriza historias de usuario con criterios de aceptación.
- Habla con clientes. Traduce dolor de negocio a tickets.
- Decide qué NO se hace.
- Gestiona expectativas de clientes custom (alcance, cambios, plazos).
- Facilita la weekly review y los kickoffs.

**Como Vibe Coder:**
- Construcción rápida con IA de prototipos y automatizaciones custom (Telegram bots, n8n/Make/Airtable, Stripe).
- Code owner de Finance Tracker Bot e Inventory Bot.
- Documenta cada automatización: qué hace, qué toca, cómo se apaga.

**Restricciones por conflicto de rol:**
1. **Santiago NO aprueba su propio código.** Sus PRs los aprueba el code owner del proyecto o su backup. Si él es el owner (bots), aprueba el backup (Juan Camilo o Julian).
2. Lo que codea pasa DoR normal (ticket, criterios, estimado). No se auto-prioriza sin ticket.
3. En conflicto de tiempo: PO gana. Su código es lo primero que se pospone.

### 2.3 Sneider — Infrastructure Engineer + Backend Lead + DevOps

**El dev más senior. Autoridad técnica final. Code owner de Sinnet e infraestructura global.**

**Responsabilidades:**
- Arquitectura de Sinnet y facilita arquitectura de proyectos nuevos (kickoffs).
- Backend: APIs, base de datos, colas, autenticación, pagos.
- Infraestructura: servidores, secretos, backups, monitoreo, alertas.
- CI/CD: pipelines de `development` y `main`, ambientes, deploys.
- Seguridad: credenciales, OWASP básico, dependencias.
- Define estándares de código, política de uso de IA, linting, tests mínimos.
- Review obligatorio de todo PR a `main` que toque payments, auth, migraciones DB o infra (cualquier proyecto).

**Tiempo objetivo:** 60% código, 25% review/mentoría, 15% infra.

### 2.4 Julian — Full Stack Developer + DevOps secundario

**Responsabilidades:**
- Features end-to-end de Sinnet (frontend + backend).
- Backup de Sneider en DevOps e infra: puede deployar, revisar pipelines, atender alertas.
- Backup de Santiago en Inventory Bot.
- Review de PRs cuando los owners están saturados.
- Tests automatizados de caminos críticos (registro, pago, scoring).
- Refactor de deuda técnica priorizada por el owner de cada proyecto.

### 2.5 Juan Camilo — Full Stack Developer + QA Manual

**Responsabilidades:**
- Features end-to-end, foco en frontend y UX.
- Code owner de QA y releases: checklist de humo pre-release, exploratorio post-deploy.
- Backup de Santiago en Finance Tracker Bot (aprueba sus PRs).
- Mantiene el checklist de regresión (§4.5).
- Reproduce y documenta bugs reportados por CSM con pasos exactos.
- Automatiza tests E2E cuando un flujo manual se repite 3+ veces.

### 2.6 Customer Success Manager

**Nota:** el CSM también es developer habilitado (ver §1.1), aunque su foco no es código diario.

**Responsabilidades:**
- Primera línea de contacto con clientes: onboarding, training, dudas.
- Clasifica y prioriza bugs reportados (P0-P3, ver §4.4).
- Documenta FAQs y playbooks de uso.
- Alimenta a Santiago con señales de churn, features pedidos, fricción.
- Ejecuta demos y capacitaciones.
- **Acepta tickets terminados de Santiago** contra criterios (porque Santiago como PO no puede aceptarse a sí mismo).
- Cuando codea: fixes menores, scripts internos, automatizaciones de soporte. Sus PRs los aprueba el owner del proyecto correspondiente.

**No hace:** definir roadmap, prometer features sin pasar por Santiago.

---

## 3. Gitflow — Modelo Simplificado

Dos ramas permanentes. Nada más.

```
main          → producción (clientes reales)
development   → desarrollo + pruebas (integración, QA)
```

### 3.1 Flujo

```
feature/xxx  →  PR  →  development  →  PR  →  main
     ↑                    ↑                    ↑
  cualquiera        todo el equipo        code owner decide
  crea ramas        integra y prueba      cuándo subir
```

1. Todo el trabajo se hace en ramas `feature/`, `fix/`, etc. desde `development`.
2. PR a `development`: 1 aprobación de cualquier dev (no el autor) + CI verde. Aquí se integra y se prueba todo junto.
3. `development` deploya automático al ambiente de pruebas.
4. Cuando el code owner considera que `development` está estable y listo: PR de `development` → `main`.
5. PR a `main`: requiere aprobación del code owner del proyecto + CI verde + checklist de humo pasado en el ambiente de pruebas (Juan Camilo).
6. `main` deploya a producción.

**Reglas duras:**
1. `main` siempre deployable. Si producción se rompe, prioridad absoluta.
2. Nadie pushea directo ni a `main` ni a `development`. Todo por PR.
3. Hotfix P0: rama `hotfix/xxx` desde `main`, PR directo a `main` (aprobación code owner o Sneider), merge, luego backmerge de `main` → `development` para no perder el fix.
4. El code owner tiene criterio para decidir qué sube a `main`, pero **respetando el flujo**: nada entra a `main` que no haya pasado por `development` y por QA. El criterio es cuándo y qué conjunto de features, no saltarse el proceso.
5. Ramas cortas: < 3 días de trabajo. Si es más grande, partirla.

### 3.2 Convención de ramas

```
<tipo>/<ticket>-<descripcion-corta>

Tipos:
  feature/    nueva funcionalidad
  fix/        bug no crítico
  hotfix/     bug P0 en producción (desde main)
  chore/      deps, configs, limpieza
  refactor/   cambio interno sin cambio de comportamiento
  docs/       solo documentación
  test/       solo tests

Ejemplos:
  feature/SIN-142-live-scoring-websockets
  fix/BOT-38-duplicate-expense-log
  hotfix/SIN-201-payment-webhook-replay
```

### 3.3 Convención de commits

Conventional Commits, preferido inglés:

```
<type>(<scope>): <descripción en imperativo>

type: feat | fix | chore | refactor | docs | test | perf | ci
scope: módulo afectado (sinnet, finance-bot, inventory-bot, infra, api, web, auth, payments)

Ejemplos:
  feat(sinnet): add live scoring websocket channel
  fix(payments): handle stripe webhook retry idempotently
```

**Reglas:**
- Commits atómicos: 1 commit = 1 cambio lógico.
- Mensaje explica POR QUÉ si no es obvio del diff.
- No commits `wip`, `asdf`. Checkpoint con `git commit --fixup` y autosquash antes del PR.
- Si el commit es 100% generado por IA y sustancial, agregar trailer: `AI-Generated: claude` (o la herramienta). Transparencia, no vergüenza.

### 3.4 Pull Requests

**Template mínimo (`.github/pull_request_template.md`):**

```markdown
## Qué
<1-2 líneas>

## Por qué
<link a ticket / contexto>

## Cómo probar
<pasos manuales o "tests automatizados cubren">

## IA
- [ ] Parte de este código fue generado con IA (herramienta: ___) y revisado línea por línea

## Checklist
- [ ] Tests pasan local
- [ ] Diff leído completo (también lo generado por IA)
- [ ] Sin `console.log` / `print` olvidados
- [ ] Migraciones DB reversibles (si aplica)
- [ ] Sin secretos / credenciales en el diff
```

**Reglas de review:**

| PR | Approvers mínimos | Quién |
|---|---|---|
| feature/fix → `development` | 1 | Cualquier dev (no el autor) |
| `development` → `main` | 1 | Code owner del proyecto (obligatorio) |
| `main` tocando payments/auth/DB/infra | +1 adicional | Sneider (obligatorio, cualquier proyecto) |
| hotfix → `main` | 1 | Code owner o Sneider, async OK |
| PR de Santiago (cualquier) | 1 | Owner del proyecto o su backup — nunca él mismo |

**SLA de review:** primer comentario < 24h (equipo part-time). Si pasan 48h, autor ping directo o backup aprueba.

**Merge:**
- Squash and merge en PRs a `development`.
- Merge commit en PR `development` → `main` (preserva historia de qué features entraron juntas).
- Autor mergea tras aprobación. Quien mergea a `main` monitorea el deploy 15 min.

### 3.5 Ambientes y deploys

| Ambiente | Rama | Deploy | Uso |
|---|---|---|---|
| local | cualquiera | manual | desarrollo |
| testing | `development` (auto) | auto en push | integración, QA de Juan Camilo, demos internas |
| production | `main` (auto) | auto en push a `main` | clientes reales |

**Proceso de release (development → main):**

1. Code owner evalúa `development`: features completas, CI verde.
2. Juan Camilo corre checklist de humo en ambiente testing (§4.5).
3. Si pasa: code owner abre PR `development` → `main`, aprueba, mergea.
4. Deploy automático a producción. Notifica en Slack `#deploys`.
5. Code owner (o quien mergeó) monitorea logs/errores 15 min.

**Rollback:** revert del merge en `main` + redeploy. < 10 min. Prohibido "arreglar en caliente" en P0 sin rollback primero.

### 3.6 Versionado

- Tags en `main` con CalVer `vYYYY.MM.DD[-N]` después de cada deploy relevante a producción.
- Changelog auto-generado: `git log <tag-anterior>..HEAD --oneline`.

### 3.7 Protección de ramas (GitHub settings)

En `main`:
- Require PR: 1 approval mínimo.
- Require status checks: CI (lint + test + build).
- Restrict pushes: nadie pushea directo.
- Require conversation resolution.

En `development`:
- Require PR: 1 approval.
- Require status checks: CI verde.
- Restrict pushes: nadie pushea directo.

### 3.8 Repos

**Un repo por producto** (cada uno con su code owner):
- `defriction/sinnet` — Sneider
- `defriction/finance-bot` — Santiago
- `defriction/inventory-bot` — Santiago
- `defriction/clientes` — Santiago (carpeta por cliente para automatizaciones)
- `defriction/infra` — Sneider (IaC, pipelines compartidos)

Cada repo tiene el mismo modelo de 2 ramas (`main` + `development`), mismas convenciones, mismo CI base.

---

## 4. Proceso Ágil y Entrega Continua

### 4.1 Cadencia

- **Ciclos semanales anclados a la weekly review de lunes.** No sprints clásicos — nadie tiene 40h/semana.
- Estimación en **horas reales disponibles**, no story points ni días ideales.
- Si algo no cabe en la semana con las horas disponibles, se parte o se pospone. Nunca comprometer de más.

### 4.2 Capacidad semanal (referencia)

| Persona | Horas/semana típicas | Cuándo trabaja |
|---|---|---|
| Santiago (PO + vibe coder) | 8-10 | Noches, fines de semana |
| Sneider (senior + infra) | 8-12 | Noches |
| Julian (fullstack) | 6-10 | Flexible |
| Juan Camilo (fullstack + QA) | 6-10 | Flexible |
| CSM | 4-8 | Horario comercial |

**Total: ~30-40h/semana.** Planificar contra eso, no contra fantasía full-time.

### 4.3 Definiciones

**Definition of Ready (DoR):** un ticket entra al ciclo solo si:
- [ ] Descripción clara del problema.
- [ ] Criterios de aceptación medibles.
- [ ] Estimado en horas por quien lo va a hacer.
- [ ] Dependencias identificadas.
- [ ] Santiago disponible para resolver dudas.

**Definition of Done (DoD):** un ticket se cierra solo si:
- [ ] Código mergeado a `development`.
- [ ] CI verde.
- [ ] Diff revisado por humano (incluyendo lo generado por IA).
- [ ] Verificado en ambiente testing.
- [ ] Documentación actualizada si cambia comportamiento visible.
- [ ] Aceptado por Santiago (o por CSM si el autor es Santiago).

### 4.4 Severidad de bugs

SLAs ajustados a part-time. Nadie on-call 24/7:

| Sev | Definición | Ejemplo | SLA respuesta | SLA fix |
|---|---|---|---|---|
| P0 | Producción caída, pérdida de datos, pagos fallando | Webhook Stripe rechazando pagos | 4 horas (quien pueda) | 24-48h según disponibilidad |
| P1 | Feature crítica rota, workaround manual posible | Live scoring no actualiza | 24h | Próximo ciclo semanal |
| P2 | Bug visible, workaround claro | Botón mal alineado mobile | 48h | Cuando haya capacidad |
| P3 | Cosmético, mejora | Tipografía inconsistente | Backlog | Cuando haya hueco |

**Comunicación de P0 a cliente:** CSM avisa en <24h con workaround o ETA honesto. Nunca prometer fix "hoy" sin confirmar disponibilidad.

**Prevención > reacción:** con SLAs largos, la defensa es no romper. CI verde, checklist humo y review de owners no son negociables.

**Quién decide severidad:** CSM al recibir, escala a Sneider si hay duda técnica.

### 4.5 Checklist de humo (Juan Camilo, pre-release a main)

Para Sinnet (adaptar por producto):
- [ ] Login / logout.
- [ ] Crear torneo nuevo.
- [ ] Registrar jugador.
- [ ] Procesar pago de prueba (Stripe test).
- [ ] Actualizar score de partido.
- [ ] Ver resultados públicos sin login.
- [ ] Recibir notificación.
- [ ] Sin errores 500 en consola.
- [ ] Sin queries N+1 obvios en logs.

Tiempo objetivo: < 20 min. Si toma más, automatizar el paso más lento.

### 4.6 Métricas de entrega (DORA, adaptadas)

Mensual, sin obsesión:

| Métrica | Objetivo | Herramienta |
|---|---|---|
| Deploy frequency a `main` | ≥ 1 por semana | GitHub Actions |
| Lead time (commit a prod) | < 3 días | Timestamps PR |
| Change failure rate | < 15% | Hotfixes / total deploys |
| Time to restore | < 24h | Incident log |

No para medir individuos. Para detectar fricción del proceso.

---

## 5. Herramientas

| Categoría | Herramienta | Razón |
|---|---|---|
| Repos + CI | GitHub + GitHub Actions | Estándar, suficiente |
| Tickets | GitHub Issues + Projects | Un solo lugar |
| Pair programming IA | Cursor / Copilot / Claude | IA-first, elección personal |
| Comunicación | Slack | Estándar |
| Docs largas | Notion | Wiki, procesos, kickoffs |
| Docs de código | Markdown en el repo | Vive junto al código |
| Monitoreo | Sentry + Uptime Robot | Errores + uptime, barato |
| Secretos | Doppler / 1Password | No `.env` en Slack ni en prompts de IA |

**Regla:** antes de agregar herramienta nueva, justificar por qué la actual no sirve. Cada SaaS es factura y contexto.

---

## 6. Onboarding

Checklist en `docs/ONBOARDING.md`:
- [ ] Acceso GitHub org, Slack, Notion, Sentry, Doppler.
- [ ] Clonar repos, setup local < 15 min.
- [ ] Leer este documento (gobierno + política IA + gitflow).
- [ ] Configurar herramienta IA de preferencia con acceso del equipo.
- [ ] Primer PR: fix de typo en docs (día 1, mergeado a `development`).
- [ ] Shadow de 1 review con el code owner del proyecto asignado.
- [ ] Primera feature pequeña (semana 1).

---

## 7. Qué NO hacemos (todavía)

- **No dailys, no retros separadas, no planning separada.** Todo en la weekly review de lunes.
- **No sprints clásicos.** Ciclos semanales con horas reales disponibles.
- **No ramas release/, no hotfix branches permanentes.** Solo `main` + `development` + ramas cortas.
- **No story points.** Horas reales (< 2h, 4h, 8h, partir-si-más).
- **No Jira.** GitHub Projects suficiente.
- **No on-call 24/7.** Prevención (CI, checklist, review de owner) en vez de reacción rápida.
- **No prohibir código IA ni tampoco mergearlo sin revisar.** IA-first con firma humana.
- **No code coverage mínimo impuesto.** Tests donde importa (pagos, auth, scoring), no porcentaje vanidoso.
- **No Kubernetes / microservicios.** Docker Compose en VPS + monolitos modulares hasta que duela.
- **No comités de arquitectura.** Kickoff de proyecto nuevo + criterio del code owner.

---

## 8. Comisiones por Referidos

Política para miembros del equipo y externos que refieran clientes a defriction. Aprobada por acuerdo del equipo — se revisa cada 6 meses o cuando el modelo de negocio cambie significativamente.

### 8.1 Esquema escalonado por tipo de cliente

| Tipo de cliente | Comisión | Tope máximo |
|---|---|---|
| Automatización custom < $2,000 USD (< $8.5M COP) | 15% flat | $300 USD (~$1.275M COP) |
| Automatización custom $2,000-$10,000 USD ($8.5M-$42.5M COP) | 10% flat | $1,000 USD (~$4.25M COP) |
| Proyecto grande > $10,000 USD (> $42.5M COP) | 7% flat | $3,000 USD (~$12.75M COP) |
| Cliente SaaS recurrente (Sinnet, bots) | 10% × primeros 12 meses | $2,000 USD lifetime (~$8.5M COP) |

**TRM referencia:** $4,250 COP/USD.

### 8.2 Comisión diferencial por referidor

| Quién refiere | Comisión | Nota |
|---|---|---|
| Socio fundador | **5%** (o mitad del porcentaje escalonado si es menor) | Ya tiene equity en la empresa |
| Miembro no-fundador (Juan Camilo, CSM) | **10%** (o el porcentaje escalonado completo si es menor) | Menos equity, mayor incentivo |
| Externo (freelance, otra agencia, conocido) | **10-15%** | Negociable caso a caso |

**Regla:** el porcentaje diferencial remplaza al escalonado cuando es menor. Ej: un socio fundador refiere un proyecto de $5,000 USD. El escalonado da 10% ($500), el diferencial da 5% ($250) — se paga el menor, porque el socio ya es dueño.

### 8.3 Reglas operativas

1. **Registro de lead.** Quien refiere debe registrar el lead en Slack `#clientes` o Notion antes del primer contacto formal. Sin registro no hay comisión.

2. **Cliente existente.** Si el lead ya estaba en el pipeline o es cliente previo de defriction, la comisión no aplica.

3. **Cliente cruzado.** Si dos personas refieren al mismo cliente, la comisión se divide 50/50 entre quienes lo registraron.

4. **Pago contra cobro.** La comisión se paga cuando el cliente paga, no cuando se firma. Si el cliente no paga, no hay comisión.

5. **Exit.** Si quien refiere se va de defriction, las comisiones pendientes se pagan hasta el final del período acordado (máximo 12 meses desde el último pago del cliente referido). Comisiones no devengadas al momento de la salida se pierden.

6. **Periodicidad.** Las comisiones se liquidan mensualmente, dentro de los primeros 5 días hábiles del mes siguiente. Pago vía transferencia o por el medio que acuerden los socios.

### 8.4 Exclusiones

- **Autoreferidos.** No hay comisión por traer tu propio proyecto como socio. Eso es trabajo, no referido.
- **Clientes existentes antes de esta política.** Se respeta el pipeline previo a la fecha de aprobación. Un lead en conversación antes de esta política no genera comisión.

### 8.5 Vigencia

Esta política rige desde su aprobación por el equipo. Se revisa cada 6 meses o cuando el modelo de negocio cambie. Cambios requieren aprobación de Santiago (pricing/contratos según RACI §1.7) + mayoría del equipo.

---

## 9. Distribución Accionaria (S.A.S.)

Estructura societaria como Sociedad por Acciones Simplificada (S.A.S.) colombiana. Propuesta base — ajustar con abogado antes de firmar.

### 9.1 Cap table propuesto

| Persona | Rol | % acciones | Tipo | Justificación |
|---|---|---|---|---|
| Santiago | Founder, PO + vibe coder | 37% | Acciones ordinarias, vesting | Founder. Cara al cliente, roadmap, revenue. Mayor peso por gestión comercial y captación de clientes |
| Sneider | Founder, tech lead + infra | 27% | Acciones ordinarias, vesting | Founder. Arquitectura, producto flagship, DevOps |
| Julian | Founder, fullstack | 25% | Acciones ordinarias, vesting | Founder. Features core, backup DevOps |
| Juan Camilo | Dev temprano | 6% | Acciones ordinarias, vesting | No-founder pero early. Equity real, no solo sueldo |
| **ESOP** (pool futuros empleados) | — | **5%** | Reservado | Hires futuros: CSM formal, dev senior, ventas |
| **Total** | | **100%** | | |

**Razonamiento:**
- **Santiago 37%:** mayor peso por su rol como PO cara al cliente, gestión comercial y captación de clientes. Reconoce el trabajo de tracción comercial que no está medido en horas de código.
- **Sneider 27%:** founder técnico senior, autoridad técnica final. Su aporte en arquitectura e infraestructura es crítico para la empresa.
- **Julian 25%:** founder fullstack, features core y backup de infra. Aportación técnica continua.
- **Juan Camilo 6%:** entró cuando el riesgo ya estaba parcialmente mitigado (producto existe, clientes existen). Equity menor que founders pero significativo para alinearlo como dueño.
- **ESOP 5%:** reservado para 1-2 hires clave futuros. Si la empresa crece, se puede ampliar diluyendo parejo.

### 9.1.1 Aportes en dinero a la fecha (registro, no ajusta equity)

Gastos ya hechos por socios para defriction. Se registran en acta constitutiva / acuerdo de accionistas como aportes de industria + capital de trabajo. Decisión del equipo: **no modificar % accionario** por estos montos. Diferencias se consideran compensadas con aporte de tiempo desigual no contabilizado.

| Socio | Concepto | Monto COP | Monto USD | Total aprox COP* |
|---|---|---|---|---|
| Santiago | VPS | $600.000 | — | $600.000 |
| Santiago | Claude Code | — | $220 | ~$935.000 |
| Santiago | Google Workspace | $180.000 | — | $180.000 |
| **Santiago total** | | | | **~$1.715.000** |
| Julian | Dominio defriction.org | — | $12 | ~$51.000 |
| Julian | Gemini | — | $120 | ~$510.000 |
| **Julian total** | | | | **~$561.000** |
| Sneider | Infra / herramientas | — | $90 | ~$382.000 |
| **Sneider total** | | | | **~$382.000** |
| Juan Camilo | — | — | — | $0 |
| **Total aportado** | | | | **~$2.658.000 COP** |

*TRM referencia: $4.250 COP/USD. Actualizar con TRM real del día de firma del acta.

**Reglas futuras sobre gastos:**
1. Gastos > $200.000 COP (o $50 USD) requieren aprobación previa de Santiago + 1 founder más antes de ejecutarse.
2. Todo gasto aprobado se registra en Notion (fecha, concepto, monto, quién pagó) — sin registro no hay reconocimiento.
3. Cuando haya caja suficiente (definir: 3+ meses de runway), se reembolsan en orden cronológico de registro, sin intereses.
4. Si algún socio quiere convertir aportes futuros significativos (> $5M COP) en equity extra, se negocia aparte y requiere unanimidad (§10).

### 9.2 Vesting — obligatorio para TODOS (founders incluidos)

**Esquema estándar: 4 años, cliff de 1 año, vesting mensual después.**

| Hito | Qué pasa |
|---|---|
| Mes 0 (firma) | 0% vested. Acciones comprometidas, no ganadas |
| Mes 12 (cliff) | 25% vested de golpe. Si sales antes del año, 0% |
| Mes 13-48 | 1/48 adicional cada mes (~2.08%/mes) |
| Mes 48+ | 100% vested. Acciones tuyas, salgas o te quedes |

**Aplicación por persona:**
- **Santiago, Sneider, Julian:** vesting corre desde la fecha de firma del acuerdo de accionistas (no retroactivo al día 1 del proyecto). Si quieren reconocer tiempo previo, dar crédito de 6-12 meses de vesting ya cumplido al firmar — negociar entre ustedes.
- **Juan Camilo:** vesting corre desde su fecha de ingreso real (hace 2 meses). Esos 2 meses ya cuentan — al firmar ya tiene ~4% vested de su 12%.

**Por qué founders también con vesting:** protege a los que se quedan. Si un founder se va al mes 6, no se lleva 26% de la empresa para siempre — se lleva lo ganado y el resto vuelve al pool.

### 9.3 Cláusulas críticas en el acuerdo de accionistas

Negociar con abogado, no saltarse:

1. **Good leaver / bad leaver.** Si sales bien (renuncia avisada, salud, mutuo acuerdo): conservas lo vested. Si sales mal (competencia, fraude, abandono): lo vested se recompra a valor nominal.
2. **Derecho de preferencia (right of first refusal).** Si alguien quiere vender, primero ofrece a los demás socios al mismo precio. Evita que un tercero random entre al cap table.
3. **Drag-along.** Si holders del >70% aprueban venta de la empresa, todos arrastran. Evita que minoritario bloquee exit.
4. **Tag-along.** Si un founder vende a tercero, minoritarios pueden pegarse a la venta al mismo precio. Protege a Juan Camilo.
5. **Vesting acelerado en adquisición (single vs double trigger).** Recomendado **double trigger**: vesting acelera solo si te adquieren Y te despiden. Single trigger (acelera con solo adquisición) asusta compradores.
6. **IP assignment.** Todo lo que cada quien construyó antes y durante defriction es de la S.A.S., no personal. Firmar desde día 1 — sin esto no hay empresa vendible.
7. **No competencia razonable.** 12 meses post-salida, misma industria geográfica. No más amplio (ilegal en Colombia si es excesivo).
8. **Decisiones reservadas.** Qué requiere voto calificado (>50%, >70% o unanimidad): venta empresa, emisión nueva acciones, deuda >X, cambio de objeto social, salarios de socios.

### 9.4 Decisiones y poder de voto

Con 26/26/26/12, escenarios:

| Escenario | Votos | Resultado |
|---|---|---|
| 3 founders de acuerdo, JC en contra | 78% vs 12% | Pasa cualquier decisión |
| 2 founders de acuerdo, 1 en contra + JC | 52% vs 38% | Pasa mayoría simple, no calificada >70% |
| 2 founders vs 2 (split) | 50/50 o 52/48 | **Deadlock** — ver abajo |

**Anti-deadlock:** decisiones operativas las resuelve Santiago (CEO/PO). Decisiones estratégicas split 50/50 van a mediador externo (definir nombre en el acuerdo) o voto de calidad de Santiago como tie-breaker. Elegir uno y dejarlo escrito.

**Recomendación:** considerar que Santiago tenga 1 voto extra simbólico o acción con voto múltiple como CEO. Evita deadlocks sin cambiar económico. Alternativa: mantener 26/26/26 económico pero acuerdo que Santiago decide empates operativos.

### 9.5 Qué NO hacer

- **No repartir 25/25/25/25.** "Equitativo" ≠ "igual" cuando riesgo y tiempo invertido difieren. Resentimiento futuro garantizado.
- **No saltarse vesting por "confianza".** La confianza de hoy no protege del conflicto de mañana. Vesting ES el mecanismo de confianza.
- **No dejar a Juan Camilo sin equity real.** Un early dev con 2% es empleado disfrazado. 12% lo alinea como dueño.
- **No firmar sin IP assignment.** Sin eso, el código es de cada quien y la empresa es un cascarón.
- **No ignorar el tema fiscal.** En Colombia, acciones en S.A.S. a valor nominal hoy vs. valor comercial futuro tiene implicaciones en renta. Hablar con contador antes de escriturar.
- **No hacer side letters verbales.** Todo por escrito en el acuerdo de accionistas o no existe.

### 9.6 Próximos pasos legales

1. Contratar abogado societario colombiano (no genérico).
2. Redactar acuerdo de accionistas con cláusulas §9.3.
3. Constituir S.A.S. (si aún no) o reformar estatutos para admitir vesting y ESOP.
4. Firmar IP assignment retroactivo de cada socio.
5. Contador define valor nominal de acciones y tratamiento fiscal del vesting.
6. Guardar todo en Notion + carpeta legal en Drive compartida.

**Costo estimado:** $3-8M COP abogado + contador para dejar esto bien. No escatimar — un pleito societario cuesta 10x más.

---

## 10. Revisión de este documento

Lo revisa todo el equipo cada 3 meses o cuando duela. Cambios por PR a este archivo, aprobación de Santiago + Sneider. La sección accionaria (§9) requiere acuerdo unánime de los 4.

Última revisión: 2026-07-22
