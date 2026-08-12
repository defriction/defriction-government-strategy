# defriction — Confirmación de Empresa en Colombia (S.A.S.)

Resumen ejecutivo extraído de `README.md` §8 y §9 para fines de constitución legal.

---

## 1. Estructura Jurídica: Sociedad por Acciones Simplificada (S.A.S.)

### 1.1 Cap Table

| Persona | Rol | % acciones | Tipo |
|---|---|---|---|
| Santiago | Founder, PO + vibe coder | 37% | Acciones ordinarias, vesting |
| Sneider | Founder, tech lead + infra | 27% | Acciones ordinarias, vesting |
| Julian | Founder, fullstack | 25% | Acciones ordinarias, vesting |
| Juan Camilo | Dev temprano | 6% | Acciones ordinarias, vesting |
| **ESOP** (pool futuros empleados) | — | **5%** | Reservado |

### 1.2 Razonamiento de la distribución

- **Santiago 37%:** mayor peso por rol de PO cara al cliente, gestión comercial y captación de clientes.
- **Sneider 27%:** founder técnico senior, autoridad técnica final en arquitectura e infraestructura.
- **Julian 25%:** founder fullstack, features core y backup de infra. Aportación técnica continua.
- **Juan Camilo 6%:** entró con riesgo parcialmente mitigado. Equity menor que founders pero significativo para alinearlo como dueño.
- **ESOP 5%:** reservado para 1-2 hires clave futuros (CSM formal, dev senior, ventas). Si la empresa crece, se amplía diluyendo parejo.

---

## 2. Vesting — Obligatorio para TODOS (Founders incluidos)

Esquema estándar: **4 años, cliff de 1 año, vesting mensual después.**

| Hito | Qué pasa |
|---|---|
| Mes 0 (firma) | 0% vested |
| Mes 12 (cliff) | 25% vested de golpe |
| Mes 13-48 | 1/48 adicional cada mes (~2.08%/mes) |
| Mes 48+ | 100% vested |

- **Santiago, Sneider, Julian:** vesting desde fecha de firma del acuerdo. Si se reconoce tiempo previo, dar crédito de 6-12 meses ya cumplido al firmar.
- **Juan Camilo:** vesting desde su fecha de ingreso real. Ya tiene ~2 meses contados al momento de firma.

---

## 3. Aportes en Dinero (registro, no ajusta equity)

Gastos ya realizados. Se registran en acta constitutiva como aportes de industria + capital de trabajo. **No modifican % accionario.** Diferencias se consideran compensadas con aporte de tiempo desigual no contabilizado.

| Socio | Concepto | Total aprox COP |
|---|---|---|
| Santiago | VPS, Claude Code, Google Workspace | ~$1.715.000 |
| Julian | Dominio defriction.org, Gemini, IA OpenCode + Hermes Agent, plan Claude Code | ~$1.044.500 |
| Sneider | Infra / herramientas | ~$664.000 |
| Julian | Certificados firma electrónica (firmapass.com) | $271.000 |
| Julian | IA OpenCode + Hermes Agent | ~$127.500 |
| Julian | Plan Claude Code (mensual, en curso) | ~$85.000 |
| Cristopher (Sneider) | Certificados firma electrónica (firmapass.com) | $282.000 |
| Juan Camilo | Certificados firma electrónica (firmapass.com) | $280.000 |
| **Total** | | **~$3.703.500** |

TRM referencia: $4.250 COP/USD. Actualizar con TRM real del día de firma.

**Devolución certificados firmapass.com ($833.000):** con liquidez suficiente (caja 3+ meses de runway) se devuelven a Juan Camilo ($280.000), Julian ($271.000) y Cristopher ($282.000), con **interés 6% efectivo anual prorrateado por mes** (~0,49% mensual) por el tiempo que tarde la devolución.

**Reglas de gastos futuros:**
1. Gastos > $200.000 COP (o $50 USD) requieren aprobación de Santiago + 1 founder más.
2. Todo gasto aprobado se registra en Notion (fecha, concepto, monto, quién pagó).
3. Con caja suficiente (3+ meses de runway), se reembolsan en orden cronológico, sin intereses — excepto certificados de firma electrónica (firmapass.com), que se devuelven con interés 6% efectivo anual prorrateado por mes (~0,49% mensual).
4. Aportes futuros > $5M COP de un socio para convertir en equity extra se negocian aparte con unanimidad.

---

## 4. Cláusulas Críticas del Acuerdo de Accionistas

### 4.1 Good leaver / bad leaver
- **Good leaver** (renuncia avisada, salud, mutuo acuerdo): conserva lo vested.
- **Bad leaver** (competencia, fraude, abandono): lo vested se recompra a valor nominal.

### 4.2 Derecho de preferencia (Right of First Refusal)
Venta siempre intra-equipo primero:
1. Ofrecer a socios actuales en proporción a su %.
2. Si nadie compra en 30 días, se puede ofrecer a externos.
3. Si externo ofrece más, se reofrece al equipo al nuevo precio antes de cerrar.

### 4.3 Drag-along
Holders del >70% pueden aprobar venta total de la empresa. Todos arrastran. Evita bloqueo por minoritario.

### 4.4 Tag-along (derecho de acompañamiento)

**Qué protege:** si un socio vende sus acciones a un tercero (comprador externo), los demás socios pueden pegarse a la venta: vender sus acciones al mismo precio y condiciones.

**Por qué:** evita que un comprador externo entre comprando solo las acciones de un fundador y deje al resto atrapado con un socio desconocido. Protege sobre todo a Juan Camilo (6%) y a cualquier minoritario futuro (hires del ESOP).

**Cómo funciona:**
1. El socio vendedor notifica por escrito la oferta del tercero (precio por acción, identidad del comprador, condiciones de pago) con mínimo 30 días antes del cierre.
2. Cada socio puede ejercer tag-along sobre el 100% de sus acciones vested, al mismo precio por acción y mismas condiciones.
3. **Prorrateo:** si el comprador no adquiere el 100% de la empresa, vendedor y tag-along venden en proporción a sus % (ej. Santiago vende su 37%, Juan Camilo se pega vendiendo su 6% en la misma operación).
4. **Cierre condicionado:** el vendedor solo puede cerrar si el comprador compra también las acciones de quienes ejercieron tag-along. Si el comprador no las toma, la venta no se concreta.

**Orden con otras cláusulas:**
- Primero ROFR (4.2): si el equipo compra, no hay venta externa y no aplica tag-along. Tag-along aplica solo a la venta externa que sobrevive al ROFR.
- Si aplica drag-along (4.3, >70% aprueba venta total), el tag-along es irrelevante: la venta total ya incluye a todos.

**Exclusiones:** no aplica a transferencias entre socios actuales, a filiales o vehículos del socio, emisiones del ESOP, prenda/garantía, ni herencia. El bad leaver (4.1) pierde el derecho a tag-along.

**En Colombia (S.A.S.):** el pacto de accionistas es válido y obliga solo a los firmantes. Para que sea oponible a terceros compradores, registrar las restricciones de transferencia en los estatutos y anotarlas en el libro de accionistas. Incluir cláusula penal por incumplimiento.

### 4.5 Vesting acelerado (Double Trigger)
Vesting acelera solo si hay adquisición Y despido. Single trigger asusta compradores.

### 4.6 IP Assignment
Todo lo construido antes y durante defriction es propiedad de la S.A.S. Firmar desde día 1 — sin esto la empresa no es vendible.

### 4.7 No competencia
12 meses post-salida, misma industria geográfica. Razonable (no excesivo — ilegal en Colombia si lo es).

### 4.8 Decisiones reservadas por voto calificado
Definir qué requiere >50%, >70% o unanimidad: venta empresa, emisión nuevas acciones, deuda >X, cambio de objeto social, salarios de socios.

---

## 5. Poder de Voto y Escenarios

Con distribución 37/27/25/6:

| Escenario | Votos | Efecto |
|---|---|---|
| Santiago + Sneider vs Julian + JC | 64% vs 31% | Pasa mayoría simple y calificada |
| Santiago + Julian vs Sneider + JC | 62% vs 33% | Pasa mayoría simple, no calificada >70% |
| Sneider + Julian vs Santiago + JC | 52% vs 43% | Pasa mayoría simple, no calificada >70% |
| 2 vs 2 combinaciones | Depende | Deadlock si se requiere >70% |

**Anti-deadlock:** decisiones operativas las resuelve Santiago (CEO). Decisiones estratégicas con empate van a mediador externo o voto de calidad de Santiago como tie-breaker. Dejar uno escrito en el acuerdo.

---

## 6. Comisiones por Referidos

### 6.1 Esquema escalonado

| Tipo de cliente | Comisión | Tope máximo |
|---|---|---|
| Automatización < $2,000 USD | 15% flat | $300 USD |
| Automatización $2,000-$10,000 USD | 10% flat | $1,000 USD |
| Proyecto > $10,000 USD | 7% flat | $3,000 USD |
| Cliente SaaS recurrente | 10% × 12 meses | $2,000 USD lifetime |

### 6.2 Comisión diferencial

| Quién refiere | Comisión |
|---|---|
| Socio fundador | 5% (o mitad del escalonado si es menor) |
| Miembro no-fundador | 10% (o escalonado completo si es menor) |
| Externo | 10-15% negociable |

### 6.3 Reglas operativas
1. Registrar lead en Slack `#clientes` o Notion antes del primer contacto formal.
2. Cliente existente en pipeline → no aplica comisión.
3. Cliente cruzado (2 referidores) → 50/50.
4. Pago contra cobro del cliente.
5. Si quien refiere se va, comisiones pendientes se pagan hasta 12 meses desde último pago del cliente.
6. Liquidación mensual, primeros 5 días hábiles.

### 6.4 Exclusiones
- No hay comisión por autoreferidos.
- Clientes en pipeline antes de esta política no generan comisión.

---

## 7. Reglas de Convivencia

1. **Amistad > empresa.** Si una decisión pone en riesgo una amistad, se detiene y se habla en persona.
2. **Sin secretos financieros.** Todo número transparente para todos los socios.
3. **Mismas reglas para todos.** Vesting, gastos, venta de acciones, código de conducta — aplican igual.
4. **Conflicto de interés se declara**, no se oculta.
5. **Separar persona y posición.** Feedback sin ataques personales.
6. **Derecho a disentir sin represalias.**
7. **No mezclar deudas personales con la empresa.**
8. **Salida limpia > salida forzada.** Si alguien sale, el equipo facilita la transición.
9. **Revisión de convivencia cada 6 meses.** 15 min extra en la weekly.
10. **Si esto falla, mediación antes que abogados.** Mediador externo neutral antes de cualquier acción legal.

---

## 8. Próximos Pasos Legales

1. Contratar abogado societario colombiano (no genérico).
2. Redactar acuerdo de accionistas con cláusulas de la sección 4.
3. Constituir S.A.S. o reformar estatutos para admitir vesting y ESOP.
4. Firmar IP assignment retroactivo de cada socio.
5. Contador: definir valor nominal de acciones y tratamiento fiscal del vesting.
6. Guardar todo en Notion + carpeta legal en Drive compartida.

---

## 9. Qué NO Hacer

- No repartir equitativo por igual. El cap table 37/27/25/6 reconoce diferencias reales.
- No saltarse vesting por "confianza". Vesting ES el mecanismo de confianza.
- No dejar a Juan Camilo sin equity real. 6% lo alinea como dueño.
- No firmar sin IP assignment.
- No ignorar el tema fiscal (renta sobre valor comercial futuro vs nominal).
- No hacer side letters verbales.

---

*Extraído de `README.md` — defriction government strategy. Última revisión: 2026-07-31.*
