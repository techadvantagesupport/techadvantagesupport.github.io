---
layout: guide
lang: es
group: safetospend
permalink: /es/guias/cuanto-puedo-gastar-hoy/
title: "Cuánto puedo gastar hoy: qué es el Presupuesto seguro y cómo se calcula | BudgeTrak"
short_title: "Cuánto puedo gastar hoy"
h1: "Cuánto puedo gastar hoy — qué significa y cómo se calcula"
kicker: "Cómo funciona"
description: "Casi todas las apps te enseñan un saldo y lo llaman dinero para gastar. Esta es la aritmética de una cifra diaria segura: fondos de reserva para cada factura, metas de ahorro, gastos amortizados y por qué el número es menor que tu saldo bancario."
standfirst: "Tu saldo bancario no es dinero para gastar. Esta es la aritmética que lo convierte en un número con el que puedes actuar."
hero: /assets/guides/hero-dashboard.jpg
hero_alt: "El panel de BudgeTrak con el Efectivo Disponible y el presupuesto seguro diario"
published: "2026-08-31"
reading_time: 8
cta_title: "Mira tu propio número"
cta_text: "El motor de presupuesto es gratis para siempre: sin cuenta y sin periodo de prueba."
faq:
  - q: "¿Qué significa «cuánto puedo gastar hoy»?"
    a: "Es la cantidad que puedes gastar hoy sin romper un compromiso financiero que ya has adquirido. A diferencia de un saldo bancario, ya lleva restada la parte diaria de cada factura próxima, meta de ahorro y gasto amortizado, así que gastarlo hasta cero es sostenible por diseño."
  - q: "¿Cómo se calcula el Presupuesto seguro?"
    a: "BudgeTrak lo calcula en dos capas. El Presupuesto base son tus ingresos del periodo menos una reserva diaria prorrateada por cada gasto recurrente. El Presupuesto seguro resta después las aportaciones a metas de ahorro, los gastos puntuales amortizados y cualquier recuperación acelerada. El resultado es la cifra que muestra el panel."
  - q: "¿Por qué mi número es mucho menor que mi saldo bancario?"
    a: "Porque tu saldo incluye dinero que ya tiene dueño. La diferencia entre ambas cifras es exactamente el total de tus compromisos próximos: alquiler, seguros, suscripciones, ahorro. Esa diferencia no es pesimismo de la app; es el dinero que corrías el riesgo de gastar dos veces."
  - q: "¿Qué diferencia hay entre Efectivo Disponible y Presupuesto seguro?"
    a: "El Efectivo Disponible es un saldo: lo que queda ahora mismo. El Presupuesto seguro es una tasa: lo que puedes gastar por día. La cifra grande del panel es el saldo; la pequeña de debajo es la tasa."
  - q: "¿Qué pasa si gasto más de la cantidad segura?"
    a: "No se rompe nada. La cifra del día siguiente lo absorbe y baja, porque los mismos compromisos deben cubrirse con menos dinero. El número se autocorrige en lugar de regañarte."
related:
  - url: /es/guias/app-de-presupuesto-para-parejas/
    title: "La mejor app de presupuesto para parejas"
    blurb: "Dos personas, un número honesto."
  - url: /es/guias/presupuesto-sin-conectar-banco/
    title: "Presupuesto sin conectar el banco"
    blurb: "Por qué la aritmética nunca necesitó tu banco."
  - url: /es/guias/app-de-presupuesto-familiar/
    title: "Un presupuesto en todos los móviles"
    blurb: "La versión para el hogar."
  - url: /es/guias/alternativa-privada-a-ynab/
    title: "Alternativa privada a YNAB"
    blurb: "Cómo se compara con el método de sobres."
---

Abre tu app del banco. El número que ves no es tu dinero para gastar, y tratarlo como si lo fuera provoca la mayoría de los presupuestos domésticos fallidos.

El saldo incluye tu alquiler. Incluye el seguro que se renueva en once días, la cuota anual que llevas sin recordar desde marzo y el dinero que te dijiste que era para las vacaciones. Todo está en la misma cuenta, indistinguible del dinero que puedes gastarte de verdad en comer fuera.

El **Presupuesto seguro** es el intento de producir un número distinto: **lo que puedes gastar hoy sin romper un compromiso ya adquirido.**

Así llega BudgeTrak hasta él. Este es el método completo, no hay puntuaciones ocultas.

## Capa 1: Presupuesto base — ingresos menos las reservas

Empieza por los ingresos del periodo. Si presupuestas a diario, son tus ingresos anuales entre 365,25. El motor mantiene los ingresos como anuales teóricos a propósito: evita que tu presupuesto dé bandazos cuando un año tiene 27 pagas quincenales en vez de 26.

Después cada gasto recurrente se convierte en un **fondo de reserva**.

Esta es la parte que casi todas las apps se saltan, y es la que importa. En lugar de dejar que una prima de seguro de 1.200 € permanezca invisible once meses y luego detone, el motor reserva una porción cada día:

```
reserva diaria = importe de la factura ÷ días reales de su ciclo
```

La duración del ciclo es el intervalo real del calendario, no una media: febrero tiene 28 días, así que una factura mensual reserva algo más por día en febrero que en marzo. Es un detalle pequeño, pero es la diferencia entre un número que se desvía y uno que no.

Suma eso en todas las facturas, multiplica por los días de tu periodo y resta:

```
Presupuesto base = ingresos del periodo − Σ (reserva diaria × días del periodo)
```

**El Presupuesto base todavía no es tu número seguro.** Son ingresos menos facturas — una cifra útil, y en la que muchas apps se detienen etiquetándola mal como dinero disponible.

<div class="note">
<p><strong>Sobre las facturas con fecha futura.</strong> Una factura que añades hoy y no vence hasta dentro de tres meses no descuenta de golpe todo su ritmo: la reserva sube progresivamente desde su fecha de creación hasta el primer vencimiento. Si no, añadir una factura hundiría tu número diario de la noche a la mañana por un pago que tienes meses para preparar.</p>
</div>

## Capa 2: Presupuesto seguro — el número que gastas

Salen tres cosas más:

```
Presupuesto seguro = max(0, Presupuesto base − amortización − metas de ahorro − recuperación acelerada)
```

- **Metas de ahorro.** Dinero que le has dicho a la app que reservas para algo concreto. Está comprometido, así que no es gastable.
- **Amortización.** Lo contrario de una meta: un gasto que *ya ocurrió* y se reparte en los meses siguientes. La reparación del coche que pagaste la semana pasada no tiene por qué arruinar el mes entero; puede costarte un poco al día durante seis meses.
- **Recuperación acelerada.** Si vas atrasado en el fondo de una factura —la añadiste tarde, o se saltó un periodo— el motor recupera en lugar de llegar corto al vencimiento.

El resultado es la cifra del panel, y el objetivo de diseño es concreto: **debería ser seguro gastarla hasta cero cada día.** No «seguro si tienes cuidado». Seguro porque todo lo que podía emboscarte ya se restó.

<figure class="shot">
<img src="/assets/tour/es/dashboard.webp" alt="Panel de BudgeTrak: pantalla Solari con el Efectivo Disponible y la cifra diaria debajo" width="540" height="960" loading="lazy">
<figcaption>La pantalla Solari muestra el Efectivo Disponible — el saldo. La cifra menor de debajo es la tasa diaria segura.</figcaption>
</figure>

## Saldo frente a tasa — la distinción que conviene aprender

Dos números, y confundirlos es la forma más común de malinterpretar un presupuesto:

| | Qué es | A qué responde |
|---|---|---|
| **Efectivo Disponible** | Un **saldo** — créditos del periodo más todo lo gastado | «¿Cuánto queda de verdad?» |
| **Presupuesto seguro** | Una **tasa** — por día, semana o mes | «¿Cuánto puedo gastar *hoy*?» |

Solo la tasa debería tratarse como dinero para gastar. El Efectivo Disponible parece mayor y más alentador, y es el número que mete a los hogares en problemas, porque un saldo no dice nada sobre lo que está a punto de salir de él.

## Por qué al principio te parecerá mal

Casi todo el mundo reacciona el primer día pensando que la cifra es demasiado baja.

Normalmente es correcta, y la diferencia es diagnóstica. La distancia entre tu saldo bancario y tu cifra diaria segura es exactamente el total de los compromisos que llevabas invisibles. Verlo escrito incomoda igual que incomoda la primera báscula honesta.

Dos cosas sí la hacen salir baja de verdad, y conviene comprobarlas:

- **Ingresos que faltan.** Ingresos irregulares o secundarios sin introducir. El motor gestiona pagas variables, pero solo de lo que conoce.
- **Facturas contadas dos veces.** Una factura registrada como recurrente *y además* anotada a mano cada mes se reserva dos veces.

Si no es ninguna de las dos, el número te está diciendo algo cierto.

## Todo se actualiza desde una fuente

Como el cálculo es determinista, cada dispositivo con los mismos datos obtiene el mismo resultado por su cuenta — que es lo que hace posibles los presupuestos compartidos sin que un móvil sea «la autoridad». Anota un gasto en cualquier dispositivo y tanto el saldo como la tasa se mueven en todos, en tiempo real, sin paso de conciliación.

<div class="duo">
<figure class="shot">
<img src="/assets/tour/es/goals.webp" alt="Pantalla de metas de ahorro de BudgeTrak" width="540" height="960" loading="lazy">
<figcaption>Las metas de ahorro salen antes del número seguro.</figcaption>
</figure>
<figure class="shot">
<img src="/assets/tour/es/calendar.webp" alt="Vista de calendario con las facturas e ingresos próximos" width="540" height="960" loading="lazy">
<figcaption>El calendario enseña para qué se está preparando la reserva diaria.</figcaption>
</figure>
</div>

## La versión corta

Tu saldo bancario responde a una pregunta que no hiciste. Una cifra de gasto seguro responde a la que sí: *¿puedo comprar esto?*

La aritmética no es ingeniosa, y ese es justamente el punto — es la disciplina de restar cada compromiso futuro poco a poco, todos los días, en vez de fingir que no va a llegar.
