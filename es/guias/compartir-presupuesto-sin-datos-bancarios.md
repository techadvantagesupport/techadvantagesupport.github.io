---
layout: guide
lang: es
group: banklogins
permalink: /es/guias/compartir-presupuesto-sin-datos-bancarios/
title: "Cómo compartir un presupuesto en pareja sin compartir las claves del banco | BudgeTrak"
short_title: "Compartir sin claves del banco"
h1: "Cómo compartir un presupuesto con tu pareja sin compartir las claves del banco"
kicker: "Privacidad y dinero compartido"
description: "Podéis llevar un presupuesto del hogar entre dos móviles sin que ninguno introduzca credenciales bancarias en ningún sitio. Esto es cómo funciona, qué se sincroniza y cuáles son las renuncias reales."
standfirst: "Las finanzas conjuntas no exigen contraseñas conjuntas. Así funciona por dentro un presupuesto compartido que nunca toca tu banco."
hero: /assets/guides/hero-privacy.jpg
hero_alt: "Una pareja, cada uno con su móvil, compartiendo un presupuesto del hogar"
published: "2026-08-31"
reading_time: 7
faq:
  - q: "¿Se puede compartir un presupuesto sin vincular cuentas bancarias?"
    a: "Sí. Un presupuesto necesita tres datos —ingresos, compromisos recurrentes y gasto— y ninguno requiere acceso bancario. BudgeTrak sincroniza esos tres datos directamente entre tus dispositivos con cifrado de extremo a extremo, así que en ningún momento existe una conexión con el banco."
  - q: "¿Qué datos se sincronizan exactamente entre la pareja?"
    a: "Vuestro presupuesto: ingresos, gastos recurrentes, metas de ahorro, categorías y transacciones, cada una atribuida al dispositivo que la registró. Va cifrado de extremo a extremo, es decir, ilegible en tránsito e ilegible en reposo en nuestros servidores."
  - q: "¿Puede mi pareja ver mi cuenta bancaria personal?"
    a: "No, porque BudgeTrak no tiene acceso a la cuenta bancaria de nadie. Los miembros ven el presupuesto compartido del hogar y las transacciones registradas en él, nada más."
  - q: "¿Da más trabajo un presupuesto compartido sin banco?"
    a: "Algo más. Cuenta con un minuto al día de registro, o una importación CSV semanal. Si tu banco envía notificaciones de compra, el plan Suscriptor puede convertirlas en entradas pendientes automáticamente, lo que elimina casi todo el trabajo manual."
  - q: "¿Cuántas personas pueden compartir un presupuesto?"
    a: "Hasta cinco dispositivos en un grupo SYNC. Una persona se suscribe por 4,99 $ al mes y el resto se une gratis."
related:
  - url: /es/guias/app-de-presupuesto-para-parejas/
    title: "La mejor app de presupuesto para parejas"
    blurb: "El caso completo, incluido dónde no encajamos."
  - url: /es/guias/presupuesto-sin-conectar-banco/
    title: "Presupuesto sin conectar el banco"
    blurb: "El mismo principio, para una sola persona."
  - url: /es/guias/app-de-presupuesto-familiar/
    title: "Un presupuesto en todos los móviles"
    blurb: "Añadir adolescentes y más adultos."
  - url: /es/guias/cuanto-puedo-gastar-hoy/
    title: "Cuánto puedo gastar hoy"
    blurb: "El número al que sirve todo esto."
---

La suposición implícita en casi todos los productos de finanzas compartidas es que juntar el dinero de dos personas exige juntar el acceso bancario de dos personas. No es así. Exige juntar sus *números*, que es algo mucho más pequeño y mucho menos sensible.

Esta guía es la mecánica: qué necesita de verdad un presupuesto compartido, qué envía BudgeTrak y a dónde, y a qué renuncias por no conectar un banco.

## Un presupuesto necesita tres datos. Ninguno es tu banco.

Escribe qué está calculando realmente un presupuesto:

1. **Lo que entra** — tus ingresos y cuándo llegan.
2. **Lo que ya está comprometido** — alquiler, seguros, suscripciones, metas de ahorro, la factura anual que olvidas cada año.
3. **Lo que ha salido** — el gasto desde que empezó el periodo.

Ya está. Con esos tres, la aritmética es determinista. La agregación bancaria es una *comodidad para introducir* el dato 3. No forma parte del cálculo, y no interviene en absoluto en los datos 1 y 2 — que son justamente donde se tuercen la mayoría de los presupuestos domésticos.

Dicho de otro modo: conectar el banco facilita el registro. No hace tu presupuesto más correcto. Se confunden con frecuencia.

## Qué significa «compartido» cuando no hay banco de por medio

En una app con agregación funciona así: ambos vinculáis vuestras cuentas, el agregador descarga los dos historiales a un servidor y la app muestra una vista conjunta. El objeto compartido es *una copia en servidor de dos historiales bancarios*.

En BudgeTrak el objeto compartido es el propio documento del presupuesto — ingresos, gastos recurrentes, metas, transacciones — replicado entre vuestros dispositivos. Una persona crea el grupo SYNC; la otra se une con un código. Desde ahí ambos móviles tienen el mismo presupuesto y se actualizan mutuamente en tiempo real.

La diferencia importa sobre todo en el caso malo. Si mañana asaltaran nuestros servidores, lo que el atacante tendría es texto cifrado: SYNC cifra en tu dispositivo antes de salir, y solo los dispositivos de tu grupo pueden descifrar. Nosotros no podemos leerlo — lo que también significa que no podemos recuperarlo si pierdes todos los dispositivos del grupo.

<figure class="shot">
<img src="/assets/tour/es/sync.webp" alt="Pantalla SYNC de BudgeTrak con los miembros del hogar" width="540" height="960" loading="lazy">
<figcaption>Hasta cinco dispositivos con un presupuesto cifrado y atribución por miembro.</figcaption>
</figure>

<div class="note">
<p><strong>Un límite honesto.</strong> «Cifrado de extremo a extremo» se refiere a SYNC. No significa que la app nunca use la red: las funciones de IA opcionales (escaneo de recibos, categorización de CSV, chat de ayuda) envían lo que les entregas para procesarlo, y ese es el trato al usar esas funciones concretas. Todo lo de esta guía funciona sin tocar ninguna de ellas.</p>
</div>

## Registrar el gasto: las tres vías

Sin conexión bancaria, las transacciones llegan de tres formas. Casi todos los hogares acaban usando dos.

### 1. Anotarlo en el momento
El widget de la pantalla de inicio acepta un gasto en dos toques sin abrir la app. Suena a la opción tediosa y es de la que más se desconfía, pero el coste real ronda los 40 segundos al día — y tiene un efecto secundario que se subestima: te fijas en lo que gastas *mientras* lo gastas, que es buena parte del cambio de conducta por el que la gente compra una app de presupuesto.

### 2. Importar un extracto
Descarga un CSV de tu banco cuando te venga bien y ábrelo en la app. La detección de duplicados concilia lo que ya anotaste a mano y el reconocimiento de comercios aprende tus habituales. Va en la mejora única de 9,99 $. Es el flujo de «ponerse al día el domingo», y para una pareja que no quiere anotar a diario funciona bien.

### 3. Dejar que trabajen las notificaciones de tu banco
Si tu app bancaria ya te avisa cuando pagas con la tarjeta, ese aviso ya contiene el comercio y el importe. BudgeTrak puede leer esas notificaciones en tu dispositivo y convertirlas en entradas **pendientes** segundos después de la compra, días antes de que aparecieran en un extracto.

Conviene ser preciso, porque suena a lo que hemos dicho que no hacemos. No lo es. No hay credenciales bancarias, ni agregador, ni permiso de SMS. La app lee avisos que tu banco ya envía a tu propio móvil, extrae importe y comercio, y encola un registro pendiente que tú apruebas antes de que toque el presupuesto. Cada dispositivo ve solo sus propias notificaciones. Plan Suscriptor.

<figure class="shot">
<img src="/assets/tour/es/transactions.webp" alt="Lista de transacciones de BudgeTrak" width="540" height="960" loading="lazy">
<figcaption>Lleguen como lleguen, todas acaban en el mismo registro compartido.</figcaption>
</figure>

## Atribución sin vigilancia

Cada transacción guarda qué dispositivo la registró. Es deliberadamente ligero: existe para que cuando la cifra diaria baje 80 €, cualquiera de los dos vea por qué sin preguntar. No es una función de control y no hay clasificación de gasto por persona, porque eso es otro producto y normalmente una relación peor.

## A qué renuncias de verdad

Tres cosas, dichas claramente:

- **Captura automática de todo, en todas partes.** Las notificaciones cubren tarjetas cuyo banco avisa. El efectivo, y los bancos que no notifican, siguen necesitando registro o importación.
- **Histórico retroactivo desde el primer día.** Un agregador descarga doce meses en cuanto conectas. Aquí importarías un CSV para lo mismo.
- **Conciliación automática con el saldo del banco.** BudgeTrak sigue el presupuesto que le contaste, no tu saldo literal. Si se separan, se concilia al importar.

Si esas tres son inaceptables, una app con agregación es sinceramente la mejor herramienta y deberías usarla.

## Configurarlo juntos

Quince minutos, una vez, en un móvil:

1. Mete los ingresos — también los irregulares; el motor gestiona ingresos variables y facturas agrupadas.
2. Mete los gastos recurrentes con sus fechas reales de cargo.
3. Añade metas de ahorro y cualquier gasto grande que estés repartiendo en meses.
4. Activa SYNC y que tu pareja se una con el código.

A partir de ahí los dos miráis la misma cifra diaria. La primera semana suele incomodar, porque el número es menor que el saldo bancario que ambos usabais. Esa diferencia es justo el objetivo: son los compromisos que estabais gastando dos veces.
