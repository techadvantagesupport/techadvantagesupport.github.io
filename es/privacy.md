---
layout: default
title: Política de Privacidad de BudgeTrak
lang: es
---

<p align="right"><a href="/privacy"><b>English</b></a> · <a href="/de/privacy"><b>Deutsch</b></a> · <a href="/fr/privacy"><b>Français</b></a></p>

# Política de Privacidad de BudgeTrak

**Fecha de entrada en vigor:** 11 de abril de 2026
**Última actualización:** 20 de mayo de 2026

> **Nota:** Esta es una traducción de cortesía al español. En caso de discrepancia entre versiones, prevalece la [versión original en inglés](/privacy).

## Resumen en Lenguaje Sencillo

BudgeTrak es una aplicación personal de presupuesto. Sus datos financieros se guardan en su dispositivo. Si decide activar la función SYNC para compartir su presupuesto entre varios dispositivos de su hogar, esos datos se cifran de extremo a extremo antes de salir de su dispositivo — ni nosotros ni ningún proveedor de la nube podemos leer sus transacciones, saldos o nombres de comercios. Si opta por usar el asistente de Chat de Ayuda dentro de la app, el texto que escribe se envía a nuestro proveedor de servicio de IA para generar respuestas y se almacena **de forma anónima** en nuestros servidores hasta 7 días para revisión de calidad (sin vincularse a su identidad). Sus datos financieros nunca se comparten con anunciantes ni se usan para crear un perfil de usted. El nivel gratuito se financia con anuncios de Google AdMob, que usa el identificador de publicidad de su dispositivo para mostrar anuncios personalizados (puede restablecerlo en la configuración de su dispositivo; los anuncios se eliminan por completo si actualiza o se suscribe). La política completa a continuación explica exactamente qué se recopila, a dónde va y cómo eliminarlo.

## Quiénes Somos

BudgeTrak es publicada por **Tech Advantage LLC** ("nosotros", "nuestro"). Puede contactarnos en **support@techadvantageapps.com** para cualquier consulta o solicitud relacionada con la privacidad.

## Información que Recopilamos

Tratamos de recopilar lo menos posible, y la mayor parte se mantiene únicamente en su dispositivo.

### Datos en el Dispositivo (Siempre Locales)

Cuando usa BudgeTrak, la siguiente información se almacena en su dispositivo dentro del almacenamiento privado de la aplicación:

- **Transacciones** que registra: monto, fecha, nombre del comercio o fuente, descripción, categoría y cualquier nota que agregue.
- **Configuración del presupuesto**: sus fuentes de ingreso, gastos recurrentes, metas de ahorro, entradas de amortización y el período de presupuesto que eligió (diario, semanal o mensual).
- **Configuración de la aplicación**: símbolo de moneda, formato de fecha, tema, preferencia de idioma y otras opciones de visualización similares.
- **Fotos de recibos** que decida adjuntar a una transacción (opcional).
- **Archivos de respaldo automático** guardados en una ubicación que usted elige en su dispositivo.

Estos datos nunca salen de su dispositivo a menos que active explícitamente una función que los envíe a otro lugar (descritas a continuación). Si desinstala BudgeTrak, Android elimina automáticamente todos los datos del dispositivo.

### Datos de Sincronización en la Nube (Solo si Usted Opta)

BudgeTrak incluye una función opcional llamada **SYNC** que le permite compartir un único presupuesto familiar entre hasta cinco dispositivos. SYNC está **desactivada de forma predeterminada** y solo se activa si usted explícitamente crea un grupo SYNC o se une a uno.

Si activa SYNC, ocurre lo siguiente:

- Se genera una clave de cifrado en su dispositivo cuando crea un grupo, o se comparte de manera segura mediante un código de emparejamiento de 6 caracteres cuando se une a uno.
- Sus transacciones, fuentes de ingreso, gastos recurrentes, metas de ahorro, entradas de amortización, configuración de la aplicación y fotos de recibos se cifran **en su dispositivo** usando cifrado ChaCha20-Poly1305 con esa clave.
- Solo los datos cifrados se cargan a nuestro proveedor de infraestructura en la nube para retransmitirlos a otros dispositivos de su grupo.
- La clave de cifrado nunca sale de sus dispositivos. Nuestro proveedor de infraestructura en la nube, nuestros servidores y cualquier tercero con acceso al almacenamiento en la nube **no pueden** descifrar sus datos financieros — solo pueden ver bloques cifrados.
- Cada dispositivo vinculado descifra los datos localmente usando la clave compartida.

Cuando abandona un grupo SYNC o lo disuelve, sus datos locales se conservan en su dispositivo, pero la copia en la nube se elimina (con una ventana de limpieza de 90 días para datos huérfanos).

### Datos de Diagnóstico y Errores

Para mantener BudgeTrak estable e identificar errores, usamos servicios anónimos de **reporte de fallos** y **telemetría de uso** proporcionados por nuestro proveedor de infraestructura en la nube. Ambos están **activados de forma predeterminada** y comparten un único interruptor de salida en **Configuración → Privacidad → Enviar reportes de fallos y datos de uso anónimos**. Desmarcar esa casilla detiene ambos inmediatamente.

Cuando esta recopilación está habilitada, los datos que recopilamos incluyen:

- Trazas de errores y mensajes de fallo.
- Información anónima del dispositivo (modelo, versión del sistema operativo, versión de la aplicación).
- Un ID anónimo de usuario de autenticación del backend — presente únicamente si ha usado una función que requiere autenticación del backend (SYNC, Chat de Ayuda, Lectura de Recibos con IA, Categorización CSV con IA, o una compra pagada). Un identificador aleatorio generado al primer uso, no su nombre ni su correo. Los usuarios que nunca usan ninguna de esas funciones jamás reciben un ID de usuario del backend.
- Contadores de diagnóstico: la cantidad de transacciones, gastos recurrentes y entradas del libro mayor de período que tiene; estado de la sincronización (`healthy`, `dead` u `off`); la cantidad de dispositivos en su grupo SYNC; y la fecha de su última actualización de período.
- Un **resumen unidireccional con hash** del saldo de efectivo disponible (calculado localmente como un dígito hexadecimal antes de enviarse). El valor real del efectivo nunca sale de su dispositivo, y el hash no puede revertirse para recuperar el número original.
- Eventos de ciclo de vida con marca de tiempo como "listener iniciado", "token renovado" o "límite de período cruzado", usados para depurar problemas de sincronización.
- Dos eventos de uso anónimos: **`ocr_feedback`** registra si usted cambió el comercio, la fecha o el monto en una transacción completada por la lectura de recibos con IA (solo diferencias y valores booleanos — nunca los valores en sí), y **`health_beacon`** registra una vez al día si su listener de SYNC está conectado y la *cantidad* de registros en su dispositivo.
- Eventos estándar de inicio de la analítica (`first_open`, `session_start`, `app_update`) que registran que se usó la aplicación, pero no información sobre *qué* hizo dentro de ella.

Los datos de fallos y telemetría **no** incluyen el contenido de sus transacciones, nombres de comercios, montos, fechas, descripciones, categorías, fotos de recibos, claves de cifrado ni ninguna otra información financiera personal. Aplicamos hash al único dato financiero que toca los diagnósticos (su saldo de efectivo) de modo que ni siquiera nosotros podamos leerlo. También hemos desactivado la derivación de país/región por IP en nuestra configuración de analítica, así que no se recopila ninguna ubicación aproximada.

Si desactiva los reportes de diagnóstico, nada de lo anterior se recopila — el latido diario que se usa para confirmar que los dispositivos están sanos y los eventos de precisión OCR utilizados para mejorar la lectura de recibos se omiten ambos. Recomendamos dejarlo activado para que podamos detectar y corregir errores que afectan a usuarios reales, pero la decisión es suya.

### Autenticación y Anti-abuso

BudgeTrak lo inicia sesión en nuestro backend mediante **autenticación anónima** (no se requiere correo ni contraseña) solamente cuando usa por primera vez una función que la requiere: **SYNC** (unirse o crear un grupo de sincronización del hogar), **Chat de Ayuda** (enviar un mensaje al asistente de IA), **Lectura de Recibos con IA**, **Categorización CSV con IA**, o completar una **compra o suscripción pagada**. Hasta que use una de esas funciones, su dispositivo no tiene un ID de usuario del backend — la app se ejecuta totalmente en el dispositivo sin sesión autenticada. La primera vez que sí use alguna, se genera un token anónimo aleatorio, persiste durante la vida de esa instalación y se usa únicamente para satisfacer el requisito de autenticación de nuestro servidor en la función correspondiente. Su dispositivo también se verifica con la atestación de integridad de la plataforma Android para evitar que clientes no autorizados accedan al relevo en la nube. Ninguno de estos sistemas recopila información personal sobre usted.

### Datos de Suscripción y Compra

Si actualiza a un nivel pagado o se suscribe a BudgeTrak Premium, **Google Play Billing** (el sistema estándar de compras dentro de la app en Android) procesa la compra en su totalidad. No vemos su método de pago, número de tarjeta de crédito ni dirección de facturación — Google Play se encarga de todo eso. Solo recibimos una confirmación de que su compra es válida, que se usa para desbloquear las funciones correspondientes en la aplicación.

### Publicidad (Solo en el Nivel Gratuito)

El nivel gratuito de BudgeTrak muestra anuncios nativos servidos a través de una red publicitaria. La red puede recopilar un identificador limitado de publicidad de Android e información básica del dispositivo para mostrar anuncios. Puede restablecer o limitar su **identificador de publicidad de Android** en la configuración de su dispositivo en cualquier momento. Si actualiza a un nivel pagado o se suscribe a Premium, los anuncios se eliminan por completo.

### Lo Que **No** Recopilamos

Queremos ser específicos en esto. BudgeTrak **no** recopila:

- Su nombre, dirección de correo electrónico, número de teléfono ni cualquier otra información personal directamente identificable.
- Su ubicación física, coordenadas GPS o dirección IP (más allá de lo que los servicios de la plataforma reciben automáticamente para enrutamiento).
- Sus contactos, calendario, biblioteca de fotos (aparte de las fotos de recibos que usted adjunte explícitamente), historial de llamadas, mensajes SMS o historial de navegación.
- Las credenciales de su cuenta bancaria, números de ruta o datos de acceso de cualquier institución financiera.
- Datos de salud, estado físico ni datos biométricos.

## Cómo Usamos la Información

Usamos la información limitada que recopilamos exclusivamente para estos propósitos, y nada más:

- **Para brindar la funcionalidad básica de la aplicación** (calcular su presupuesto, sincronizar datos entre sus dispositivos si usted optó por ello, mostrar sus transacciones).
- **Para diagnosticar fallos y errores** y así corregirlos en la próxima versión.
- **Para verificar la integridad de su suscripción** si actualizó.
- **Para mostrar anuncios** en el nivel gratuito a través de nuestra red publicitaria.

**No**:

- Vendemos sus datos a nadie, jamás, por ningún motivo.
- Compartimos sus datos con corredores de datos, redes de marketing o empresas de análisis (más allá de los terceros encargados del tratamiento enumerados a continuación).
- Usamos sus datos financieros para entrenar modelos de aprendizaje automático o sistemas de IA.
- Usamos sus datos financieros con fines publicitarios ni para crear un perfil de usted.

## Cómo Protegemos su Información

- **Cifrado de extremo a extremo** para todos los datos de SYNC usando ChaCha20-Poly1305, con la clave de cifrado generada y almacenada únicamente en sus dispositivos.
- **Cifrado en reposo** en el almacenamiento en la nube — incluso nuestro proveedor de infraestructura en la nube solo ve texto cifrado.
- **Cifrado en tránsito** usando HTTPS / TLS para toda la comunicación de red.
- **Verificación de integridad de la app** para bloquear el acceso de clientes no autorizados al backend de SYNC.
- **Respaldos cifrados con contraseña** usando derivación de clave PBKDF2-SHA256 — cada respaldo se cifra con una contraseña que usted proporciona; sin ella, el respaldo no se puede descifrar.
- **Sin capacidad de descifrado del lado del servidor** — por diseño, no podemos leer sus datos aun si quisiéramos o si fuéramos obligados a hacerlo.

Ningún sistema es perfectamente seguro, pero seguimos las mejores prácticas de la industria y hemos diseñado BudgeTrak para minimizar lo que llegamos a ver.

## Terceros Encargados del Tratamiento

BudgeTrak depende de los siguientes terceros encargados del tratamiento. Cada uno tiene su propia política de privacidad que regula cómo maneja los datos limitados que compartimos con ellos. Listamos los proveedores específicos aquí para que esta divulgación sea exhaustiva y verificable; el resto de esta política se refiere a ellos por su función (p. ej., "nuestro proveedor de infraestructura en la nube") para mantener la prosa legible.

| Servicio | Proveedor | Propósito | Lo que ve |
|---|---|---|---|
| Relevo de datos cifrados de SYNC | Google Firebase Firestore | Base de datos en la nube para bloques cifrados | Solo bloques cifrados |
| Almacenamiento de fotos de recibos cifradas (SYNC) | Google Firebase Cloud Storage | Almacenamiento de objetos en la nube para imágenes cifradas | Solo bloques cifrados |
| Presencia de dispositivos | Google Firebase Realtime Database | Indicadores en línea/desconectado para SYNC | IDs anónimos de dispositivo |
| Autenticación del backend | Google Firebase Authentication | Inicio de sesión anónimo activado solo al primer uso de SYNC, Chat de Ayuda, funciones de IA o una compra pagada | Token de usuario anónimo |
| Verificación anti-abuso | Google Firebase App Check + Play Integrity | Bloquea clientes no autorizados | Atestación de la plataforma |
| Reporte de fallos | Google Firebase Crashlytics | Diagnóstico de fallos | Datos de fallos, sin datos financieros |
| Analítica de uso | Google Firebase Analytics | Eventos anónimos de uso (precisión OCR + latido diario) | Solo conteos y valores booleanos — sin contenido de transacciones, sin ubicación |
| Procesamiento de IA (solo funciones opcionales) | Google Gemini | Lectura de recibos; categorización CSV; asistente de Chat de Ayuda | Contenido de la imagen del recibo; comercio y monto de transacciones bancarias importadas; el texto que escribe en el Chat de Ayuda más un extracto relevante de la documentación de ayuda de la app |
| Compras y suscripciones | Google Play Billing | Suscripciones y compras únicas | Información de pago (gestionada en su totalidad por Google Play) |
| Publicidad (solo nivel gratuito) | Google AdMob | Publicidad nativa | ID de publicidad, información básica del dispositivo |

Puede consultar las prácticas de privacidad de estos proveedores en [https://policies.google.com/privacy](https://policies.google.com/privacy).

## Funciones Asistidas por IA (Opcionales)

BudgeTrak ofrece tres funciones opcionales asistidas por IA. Las dos primeras están disponibles para los niveles Pagado y Suscriptor; la tercera, Chat de Ayuda, está disponible para todos los niveles (incluido el Gratuito). Las tres están desactivadas por defecto y requieren una acción explícita del usuario para habilitarse.

### Lectura de Recibos con IA (Suscriptores)
Cuando un suscriptor toca el ícono de chispa en el diálogo de transacción, BudgeTrak envía la foto del recibo a nuestro proveedor de servicio de IA para extraer el comercio, la fecha, el monto y la categoría. La respuesta se devuelve directamente a su dispositivo y se guarda solo en su registro de transacción.

### Categorización CSV con IA (Niveles Pagado y Suscriptor, desactivada por defecto)
Cuando se activa en Configuración, BudgeTrak envía el nombre del comercio y el monto de las transacciones bancarias recién importadas a nuestro proveedor de servicio de IA para que elija la categoría que mejor coincida con cada una. La fecha de la transacción **no** se envía. Solo se envían las transacciones que el categorizador local de BudgeTrak no puede clasificar con confianza.

### Asistente de Chat de Ayuda (Todos los niveles, desactivado por defecto)
Si activa la casilla del Chat de Ayuda en **Ajustes → Privacidad → Permitir que el chatbot transmita y almacene sus mensajes…** y toca **Aceptar** en el diálogo de consentimiento dentro de la app, la función de Chat de Ayuda le permite escribir preguntas sobre cómo funciona la app y recibir respuestas generadas por IA basadas en las páginas de ayuda de la app. Cuando la función está habilitada:

- El texto que escribe se envía a nuestro proveedor de servicio de IA para generar una respuesta. Cada solicitud también incluye un breve extracto de la documentación de ayuda incorporada de la app para que la IA pueda fundamentar su respuesta en el comportamiento real de BudgeTrak. No se envían datos financieros personales, detalles de transacciones, saldos de cuentas ni configuraciones.
- La transcripción completa del chat también se almacena **de forma anónima** en nuestra infraestructura en la nube bajo un identificador de chat aleatorio de 128 bits generado en su dispositivo. La transcripción es anónima en sentido literal: **no** registramos su ID de usuario de autenticación del backend, ID de dispositivo, dirección IP, nombre, correo ni ningún otro identificador junto a ella — solo el ID del chat, el texto de los mensajes, marcas de tiempo y la versión de la app. Usamos estas transcripciones anónimas para revisar periódicamente la precisión del chatbot y detectar usos abusivos; no podemos vincularlas a ningún usuario específico. Las transcripciones se eliminan automáticamente después de **7 días** mediante una política de tiempo de vida del lado del servidor.
- Cada dispositivo gestiona su consentimiento de forma independiente. La casilla está desactivada por defecto al instalar y **no** se sincroniza entre dispositivos SYNC. Desmarcarla en cualquier momento revoca el consentimiento — las transcripciones que ya estén en nuestros servidores siguen sujetas al TTL de 7 días descrito arriba y luego se eliminarán automáticamente, y no se subirán más mensajes desde su dispositivo.
- Puede tocar **Borrar** en el diálogo del Chat de Ayuda en cualquier momento para subir la transcripción existente una última vez y borrar el búfer local, comenzando un nuevo chat con un nuevo identificador anónimo. Los mensajes locales con más de 48 horas también se eliminan automáticamente en cada dispositivo, sin importar si los borra.
- **No** necesita una suscripción pagada, y el Chat de Ayuda **no** requiere SYNC. Si no ha habilitado SYNC, BudgeTrak iniciará sesión de forma anónima la primera vez que necesite subir una transcripción, únicamente para satisfacer el requisito de autenticación del lado del servidor; no se recopila información personal identificable mediante este inicio de sesión anónimo.

### Chatbot del sitio web (techadvantagesupport.github.io)
Nuestro sitio web aloja un asistente de IA que responde preguntas de los visitantes sobre BudgeTrak, basándose en la misma documentación de ayuda integrada que el Chat de Ayuda dentro de la app. Si lo usa:

- El texto que escribe se envía a nuestros servidores y se reenvía a nuestro proveedor de servicio de IA para generar una respuesta. No ingrese información personal, financiera ni de cuentas — el asistente no la necesita y le pedimos que no la comparta.
- Almacenamos cada mensaje y respuesta hasta por **7 días** para revisar la precisión del asistente y detectar abusos, junto con un hash criptográfico unidireccional de su dirección IP. El hash se usa **únicamente** para aplicar un límite diario de mensajes por visitante; no podemos recuperar su dirección IP a partir de él, y no almacenamos nombre, correo, cuenta ni identificador de dispositivo con los chats del sitio web.
- No se requiere cuenta ni inicio de sesión, y usar el chatbot del sitio web es completamente opcional.

### Lo que nunca se envía al proveedor de servicio de IA
- Sus saldos o totales
- Su historial de transacciones (más allá de las filas importadas o el recibo específico que se esté procesando)
- Sus claves de cifrado, identificadores de dispositivo o tokens de autenticación
- Sus fotos de recibos (solo se envían en la Lectura de Recibos arriba descrita, nunca por la Categorización CSV ni por el Chat de Ayuda)
- Cualquier dato de cualquier función de BudgeTrak salvo que haya optado explícitamente por esa función específica

### Cómo se protegen sus datos
- Todas las solicitudes se cifran en tránsito (HTTPS/TLS).
- Para la Lectura de Recibos y la Categorización CSV, el proveedor de servicio de IA elimina los datos de solicitud y respuesta una vez que la solicitud se completa; nada se almacena en los servidores del proveedor para estas funciones. Según la configuración por defecto del proveedor, **sus datos no se usan para entrenar los modelos de IA del proveedor**.
- Para el Chat de Ayuda, sus mensajes escritos y las respuestas de la IA se almacenan (por BudgeTrak, no por el proveedor de servicio de IA) hasta 7 días para la revisión de precisión/abuso descrita arriba, y luego se eliminan automáticamente. El proveedor de IA no retiene la solicitud después de generar la respuesta.
- Todas las funciones de IA pueden desactivarse en Configuración en cualquier momento, y la aplicación vuelve al comportamiento totalmente en el dispositivo (o al enlace de escape por correo dentro de la app para el Chat de Ayuda).

Los usuarios del nivel gratuito tienen acceso al **Chat de Ayuda** (con consentimiento) pero no a la **Lectura de Recibos con IA** ni a la **Categorización CSV con IA**.

## Sus Derechos y Opciones

Usted tiene control total sobre sus datos en BudgeTrak.

- **Eliminar todo**: Desinstalar BudgeTrak elimina todos los datos almacenados localmente en su dispositivo. Si además usa SYNC, abandone o disuelva su grupo SYNC desde la pantalla de SYNC primero para eliminar la copia en la nube.
- **Abandonar un grupo SYNC**: Toque "Abandonar grupo" en la pantalla de SYNC. Sus datos locales se conservan; se eliminan los datos en la nube vinculados a su dispositivo.
- **Disolver un grupo SYNC** (solo administrador): Toque "Disolver grupo" en la pantalla de SYNC. Todos los datos en la nube del grupo se eliminan de forma permanente; cada dispositivo conserva su copia local.
- **Exportar sus datos**: Use la función Guardar en la pantalla de Transacciones para exportar sus transacciones en formato CSV, Excel o PDF. Los respaldos desde Configuración incluyen todos sus datos de presupuesto en un solo archivo.
- **Desactivar reportes de fallos y telemetría de uso**: Abra **Configuración → Privacidad → Enviar reportes de fallos y datos de uso anónimos** en BudgeTrak y desmarque la casilla. El cambio entra en vigor inmediatamente — se les indica al servicio de reporte de fallos y al de analítica que dejen de recopilar datos de su dispositivo, incluyendo el latido diario y los eventos de precisión OCR.
- **Revocar el consentimiento del Chat de Ayuda**: Abra **Ajustes → Privacidad → Permitir que el chatbot transmita y almacene sus mensajes…** en BudgeTrak y desmarque la casilla. No se subirán más mensajes desde su dispositivo. Cualquier transcripción anónima ya en nuestros servidores se seguirá eliminando automáticamente tras el período de retención de 7 días descrito arriba; como se almacenan sin su identidad, no podemos eliminar las transcripciones pasadas de un usuario específico bajo solicitud.
- **Limitar el seguimiento de anuncios**: Restablezca o limite su identificador de publicidad de Android en la configuración de su dispositivo en Privacidad → Anuncios.

Si quiere que le confirmemos qué datos tenemos sobre usted (nota: en casi todos los casos, la respuesta es "nada que lo identifique personalmente") o tiene cualquier otra solicitud de privacidad, contáctenos en **support@techadvantageapps.com**.

## Eliminación de Datos

Puede solicitar la eliminación de sus datos de BudgeTrak a través de cualquiera de las siguientes opciones:

### 1. Eliminación desde la aplicación (administrador de un grupo SYNC)
Abra BudgeTrak → Configuración → SYNC → **Disolver grupo**. Esto elimina permanentemente todos los datos del lado del servidor para el grupo: transacciones, categorías, gastos recurrentes, fuentes de ingreso, metas de ahorro, entradas de amortización, libro mayor de período, fotos de recibos cifradas y metadatos del grupo. La cascada la realiza una función del lado del servidor que elimina los datos de nuestra infraestructura en la nube. Cada dispositivo miembro conserva su copia local a menos que también desinstale la aplicación.

### 2. Eliminación desde la aplicación (miembro de un grupo SYNC)
Abra BudgeTrak → Configuración → SYNC → **Abandonar grupo**. Su dispositivo se marca como eliminado en el listado de dispositivos del grupo, se borra su registro de presencia en tiempo real y se eliminan las claves de cifrado de su dispositivo para ese grupo. Los datos compartidos en sí permanecen en el grupo para los miembros restantes; si quiere que se elimine el grupo entero, el administrador debe disolverlo.

### 3. Eliminación solo local
Desinstalar BudgeTrak elimina inmediatamente todos los datos del dispositivo (transacciones, configuración, fotos de recibos, respaldos cifrados guardados en la carpeta privada de la aplicación). Si solo usó BudgeTrak en modo individual (sin SYNC), nunca existieron datos en la nube y la desinstalación completa la eliminación.

### 4. Eliminación automática
Los grupos SYNC que no han sido abiertos por ningún dispositivo miembro durante 90 días consecutivos se eliminan automática y permanentemente mediante un proceso de limpieza del lado del servidor. Esto incluye todas las transacciones, fotos cifradas y metadatos. No hay recuperación de esta limpieza automática; asegúrese de tener un respaldo local antes de dejar que un grupo quede inactivo.

### Por qué no ofrecemos eliminación manual por correo
BudgeTrak intencionalmente no asocia sus datos en la nube con su nombre, correo electrónico o cualquier identificador que pudiéramos usar para localizar "sus" registros bajo solicitud. La autenticación anónima, el cifrado de extremo a extremo y los identificadores de grupo generados aleatoriamente son lo que hace posibles las garantías de privacidad de esta política — pero el mismo diseño significa que si nos escribe pidiendo que eliminemos un grupo específico, no tenemos forma de verificar que el grupo sea suyo ni de localizarlo entre los bloques cifrados de nuestros servidores.

Si perdió el acceso a su dispositivo o a un grupo cuyo administrador ya no puede contactar, la limpieza por inactividad de 90 días arriba descrita es el mecanismo de eliminación. Asegúrese de tener un respaldo local de los datos que quiera conservar antes de que esa ventana expire.

Lo que la eliminación **no** afecta: los registros anónimos de reporte de fallos (retenidos por el proveedor del servicio durante 90 días según su política estándar, independientemente de las acciones dentro de la aplicación) y los identificadores de publicidad (gestionados por Android a nivel de dispositivo — restablézcalos desde la configuración de su dispositivo).

## Retención de Datos

- **Los datos en el dispositivo** se conservan hasta que usted los elimine o desinstale la aplicación.
- **Los datos en la nube de SYNC** se eliminan automáticamente 90 días después de la última actividad en un grupo, y se eliminan inmediatamente cuando se disuelve un grupo.
- **Las transcripciones del Chat de Ayuda** se almacenan de forma anónima y se eliminan automáticamente **7 días** después de la última actualización mediante una política de tiempo de vida del lado del servidor. Las copias locales en su dispositivo se eliminan tras 48 horas en cualquier caso.
- **Los reportes de fallos** son retenidos por el proveedor del servicio de reporte de fallos según sus políticas estándar de retención (actualmente 90 días para datos de fallos).
- **Las fotos de recibos en almacenamiento en la nube** siguen el período de retención que el administrador de su grupo configure en Configuración, o se conservan indefinidamente si no se configura un período. Se eliminan inmediatamente cuando elimina la transacción o foto correspondiente.

## Privacidad de los Menores

BudgeTrak es una herramienta de finanzas personales destinada a usuarios de 13 años o más. No recopilamos a sabiendas información personal de menores de 13 años. Si cree que un menor de 13 nos ha proporcionado información personal, contáctenos en **support@techadvantageapps.com** y tomaremos medidas para eliminarla.

## Usuarios Internacionales

BudgeTrak se publica desde los Estados Unidos. Si usa la aplicación desde fuera de los Estados Unidos, tenga en cuenta que cualquier dato que decida sincronizar a la nube (que se cifra antes de salir de su dispositivo) puede ser retransmitido a través de servidores operados por nuestros terceros encargados del tratamiento en los Estados Unidos o en otros países donde mantienen infraestructura. Al usar la función SYNC de BudgeTrak, usted consiente esta retransmisión.

## Cambios a esta Política

Podemos actualizar esta política de privacidad de vez en cuando, en particular cuando agregamos o eliminamos funciones que afectan qué datos se recopilan. Cuando hagamos cambios sustanciales, actualizaremos la fecha de "Última actualización" en la parte superior de esta página y, cuando sea apropiado, le notificaremos dentro de la aplicación. Su uso continuado de BudgeTrak después de una actualización de política constituye aceptación de la política revisada.

## Contáctenos

Si tiene preguntas sobre esta política de privacidad o las prácticas de datos de BudgeTrak, contáctenos:

**Tech Advantage LLC**
Correo: **support@techadvantageapps.com**

Responderemos a las consultas legítimas sobre privacidad dentro de un plazo razonable, normalmente dentro de 30 días.
