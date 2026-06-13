---
layout: default
title: BudgeTrak Datenschutzerklärung
lang: de
---

<p align="right"><a href="/privacy"><b>English</b></a> · <a href="/es/privacy"><b>Español</b></a> · <a href="/fr/privacy"><b>Français</b></a></p>

# BudgeTrak Datenschutzerklärung

**Gültig ab:** 11. April 2026
**Zuletzt aktualisiert:** 20. Mai 2026

> **Hinweis:** Dies ist eine deutsche Übersetzung aus Gefälligkeit. Im Falle von Abweichungen zwischen den Versionen ist die [englische Originalfassung](/privacy) maßgeblich.

## Zusammenfassung in einfacher Sprache

BudgeTrak ist eine App für die persönliche Budgetplanung. Ihre Finanzdaten verbleiben auf Ihrem Gerät. Wenn Sie die SYNC-Funktion aktivieren, um Ihr Budget über mehrere Geräte in Ihrem Haushalt hinweg zu teilen, werden diese Daten Ende-zu-Ende-verschlüsselt, bevor sie Ihr Gerät verlassen — weder wir noch ein Cloud-Anbieter können Ihre Transaktionen, Salden oder Händlernamen lesen. Wenn Sie sich für den In-App-Hilfe-Chat-Assistenten entscheiden, wird der Text, den Sie eingeben, an unseren KI-Dienstleister gesendet, um Antworten zu generieren, und wird **anonym** für bis zu 7 Tage zur Qualitätsprüfung auf unseren Servern gespeichert (nicht mit Ihrer Identität verknüpft). Ihre Finanzdaten werden niemals mit Werbetreibenden geteilt oder zur Profilbildung über Sie verwendet. Die kostenlose Stufe wird durch Werbung von Google AdMob finanziert, das die Werbe-ID Ihres Geräts verwendet, um personalisierte Werbung anzuzeigen (in den Einstellungen Ihres Geräts zurücksetzbar; Werbung wird vollständig entfernt, wenn Sie ein Upgrade durchführen oder ein Abonnement abschließen). Die vollständige Erklärung unten beschreibt genau, was erhoben wird, wohin es geht und wie Sie es löschen können.

## Wer wir sind

BudgeTrak wird von **Tech Advantage LLC** ("wir", "uns", "unser") herausgegeben. Sie können uns unter **support@techadvantageapps.com** für alle datenschutzbezogenen Fragen oder Anliegen kontaktieren.

## Welche Informationen wir erheben

Wir versuchen, so wenig wie möglich zu erheben, und behalten das meiste davon nur auf Ihrem Gerät.

### Daten auf dem Gerät (immer lokal)

Wenn Sie BudgeTrak nutzen, werden die folgenden Informationen auf Ihrem Gerät im privaten Speicher der App gespeichert:

- **Transaktionen**, die Sie erfassen: Betrag, Datum, Name des Händlers oder der Quelle, Beschreibung, Kategorie und alle Notizen, die Sie hinzufügen.
- **Budgetkonfiguration**: Ihre Einnahmequellen, wiederkehrende Ausgaben, Sparziele, Amortisationseinträge und den von Ihnen gewählten Budgetzeitraum (täglich, wöchentlich oder monatlich).
- **App-Einstellungen**: Währungssymbol, Datumsformat, Design, Spracheinstellung und ähnliche Anzeigeoptionen.
- **Belegfotos**, die Sie einer Transaktion anhängen möchten (optional).
- **Automatische Backup-Dateien**, die an einem von Ihnen gewählten Ort auf Ihrem Gerät gespeichert werden.

Diese Daten verlassen Ihr Gerät niemals, es sei denn, Sie aktivieren ausdrücklich eine Funktion, die sie an einen anderen Ort sendet (nachstehend beschrieben). Wenn Sie BudgeTrak deinstallieren, werden alle Daten auf dem Gerät von Android automatisch gelöscht.

### Cloud-Sync-Daten (nur wenn Sie sich dafür entscheiden)

BudgeTrak enthält eine optionale Funktion namens **SYNC**, mit der Sie ein einziges Haushaltsbudget über bis zu fünf Geräte hinweg teilen können. SYNC ist **standardmäßig deaktiviert** und wird nur aktiviert, wenn Sie ausdrücklich eine SYNC-Gruppe erstellen oder einer beitreten.

Wenn Sie SYNC aktivieren, geschieht Folgendes:

- Ein Verschlüsselungsschlüssel wird auf Ihrem Gerät erzeugt, wenn Sie eine Gruppe erstellen, oder beim Beitritt über einen 6-stelligen Kopplungscode sicher geteilt.
- Ihre Transaktionen, Einnahmequellen, wiederkehrenden Ausgaben, Sparziele, Amortisationseinträge, App-Einstellungen und Belegfotos werden **auf Ihrem Gerät** mit ChaCha20-Poly1305-Verschlüsselung unter Verwendung dieses Schlüssels verschlüsselt.
- Nur die verschlüsselten Daten werden zu unserem Cloud-Infrastruktur-Anbieter hochgeladen, um sie an andere Geräte in Ihrer Gruppe weiterzuleiten.
- Der Verschlüsselungsschlüssel verlässt Ihre Geräte niemals. Unser Cloud-Infrastruktur-Anbieter, unsere Server und jeder Dritte mit Zugriff auf den Cloud-Speicher **können** Ihre Finanzdaten **nicht** entschlüsseln — sie sehen nur verschlüsselte Blöcke.
- Jedes verknüpfte Gerät entschlüsselt die Daten lokal mit dem gemeinsamen Schlüssel.

Wenn Sie eine SYNC-Gruppe verlassen oder auflösen, bleiben Ihre lokalen Daten auf Ihrem Gerät erhalten, die Cloud-Kopie wird jedoch gelöscht (mit einem 90-tägigen Bereinigungsfenster für verwaiste Daten).

### Diagnose- und Absturzdaten

Um BudgeTrak stabil zu halten und Fehler zu identifizieren, verwenden wir anonyme Dienste zur **Absturzberichterstattung** und **Nutzungstelemetrie** von unserem Cloud-Infrastruktur-Anbieter. Beide sind **standardmäßig aktiviert** und teilen sich eine einzige Abmeldemöglichkeit unter **Einstellungen → Datenschutz → Absturzberichte und anonyme Nutzungsdaten senden**. Das Deaktivieren dieses Kästchens stoppt beide sofort.

Wenn diese Erhebung aktiviert ist, umfassen die von uns erhobenen Daten Folgendes:

- Absturz-Stack-Traces und Fehlermeldungen.
- Anonyme Geräteinformationen (Modell, Betriebssystemversion, App-Version).
- Eine anonyme Backend-Authentifizierungs-Benutzer-ID — nur vorhanden, wenn Sie eine Funktion verwendet haben, die eine Backend-Authentifizierung erfordert (SYNC, Hilfe-Chat, KI-Beleg-Scan, KI-CSV-Kategorisierung oder ein kostenpflichtiger Kauf). Eine bei der ersten Nutzung erzeugte zufällige Kennung, nicht Ihr Name oder Ihre E-Mail-Adresse. Nutzer, die keine dieser Funktionen verwenden, erhalten überhaupt keine Backend-Benutzer-ID.
- Diagnosezähler: die Anzahl der Transaktionen, wiederkehrenden Ausgaben und Periodenbuch-Einträge, die Sie haben; den Sync-Status (`healthy`, `dead` oder `off`); die Anzahl der Geräte in Ihrer SYNC-Gruppe; und das Datum Ihrer letzten Periodenaktualisierung.
- Eine **Einweg-Hash-Prüfsumme** Ihres verfügbaren Bargeldsaldos (lokal als Hex-Prüfsumme berechnet, bevor er gesendet wird). Der tatsächliche Bargeldwert verlässt Ihr Gerät niemals, und der Hash kann nicht umgekehrt werden, um die ursprüngliche Zahl wiederherzustellen.
- Mit Zeitstempel versehene Lebenszyklus-Ereignisse wie "Listener gestartet", "Token aktualisiert" oder "Periodengrenze überschritten", die zur Fehlersuche bei Sync-Problemen verwendet werden.
- Zwei anonyme Nutzungsereignisse: **`ocr_feedback`** erfasst, ob Sie den Händler, das Datum oder den Betrag bei einer durch KI-Beleg-Scan ausgefüllten Transaktion geändert haben (nur Differenzen und boolesche Werte — niemals die Werte selbst), und **`health_beacon`** erfasst einmal täglich, ob Ihr SYNC-Listener verbunden ist, sowie die *Anzahl* der Datensätze auf Ihrem Gerät.
- Standard-Analytics-Startereignisse (`first_open`, `session_start`, `app_update`), die erfassen, dass die App genutzt wurde, aber keine Informationen darüber, *was* Sie darin getan haben.

Absturz- und Telemetriedaten umfassen **nicht** den Inhalt Ihrer Transaktionen, Händlernamen, Beträge, Daten, Beschreibungen, Kategorien, Belegfotos, Verschlüsselungsschlüssel oder andere persönliche Finanzinformationen. Wir hashen das einzige Stück Finanzdaten, das mit der Diagnose in Berührung kommt (Ihren Bargeldsaldo), sodass selbst wir es nicht lesen können. Wir haben außerdem die IP-basierte Land-/Regionsableitung in unserer Analytics-Konfiguration deaktiviert, sodass kein ungefährer Standort erhoben wird.

Wenn Sie die Diagnoseberichterstattung deaktivieren, wird nichts von dem oben Genannten erhoben — der tägliche Heartbeat, der zur Bestätigung dient, dass Geräte funktionsfähig sind, und die OCR-Genauigkeitsereignisse, die zur Verbesserung des Beleg-Scans dienen, werden beide übersprungen. Wir empfehlen, sie aktiviert zu lassen, damit wir Fehler erkennen und beheben können, die echte Nutzer betreffen, aber die Entscheidung liegt bei Ihnen.

### Authentifizierung und Missbrauchsschutz

BudgeTrak meldet Sie bei unserem Backend mittels **anonymer Authentifizierung** an (keine E-Mail-Adresse oder kein Passwort erforderlich), und zwar nur, wenn Sie zum ersten Mal eine Funktion verwenden, die dies erfordert: **SYNC** (Beitritt zu oder Erstellung einer Haushalts-Sync-Gruppe), **Hilfe-Chat** (Senden einer Nachricht an den KI-Assistenten), **KI-Beleg-Scan**, **KI-CSV-Kategorisierung** oder den Abschluss eines **kostenpflichtigen Kaufs oder Abonnements**. Bis Sie eine dieser Funktionen verwenden, hat Ihr Gerät keine Backend-Benutzer-ID — die App läuft vollständig auf dem Gerät ohne authentifizierte Sitzung. Wenn Sie eine davon zum ersten Mal verwenden, wird ein zufälliges anonymes Token erzeugt, das für die Lebensdauer dieser Installation bestehen bleibt und nur dazu verwendet wird, die Authentifizierungsanforderung unseres Servers für die entsprechende Funktion zu erfüllen. Ihr Gerät wird außerdem mithilfe der App-Integritätsattestierung der Android-Plattform verifiziert, um zu verhindern, dass nicht autorisierte Clients auf das Cloud-Relay zugreifen. Keines dieser Systeme erhebt persönliche Informationen über Sie.

### Abonnement- und Kaufdaten

Wenn Sie ein Upgrade auf eine kostenpflichtige Stufe durchführen oder BudgeTrak Premium abonnieren, wird der Kauf vollständig über **Google Play Billing** (das standardmäßige Android-System für In-App-Käufe) abgewickelt. Wir sehen weder Ihre Zahlungsmethode, Ihre Kreditkartennummer noch Ihre Rechnungsadresse — Google Play kümmert sich um all das. Wir erhalten lediglich eine Bestätigung, dass Ihr Kauf gültig ist, die zum Freischalten der entsprechenden Funktionen in der App verwendet wird.

### Werbung (nur kostenlose Stufe)

Die kostenlose Stufe von BudgeTrak zeigt native Werbung an, die über ein Werbenetzwerk ausgeliefert wird. Das Netzwerk kann eine begrenzte Android-Werbekennung und grundlegende Geräteinformationen erheben, um Werbung auszuliefern. Sie können Ihre **Android-Werbekennung** jederzeit in den Einstellungen Ihres Geräts zurücksetzen oder einschränken. Wenn Sie ein Upgrade auf eine kostenpflichtige Stufe durchführen oder Premium abonnieren, wird die Werbung vollständig entfernt.

### Was wir **nicht** erheben

Wir möchten hier konkret sein. BudgeTrak erhebt **nicht**:

- Ihren Namen, Ihre E-Mail-Adresse, Ihre Telefonnummer oder andere direkt identifizierende personenbezogene Daten.
- Ihren physischen Standort, GPS-Koordinaten oder Ihre IP-Adresse (über das hinaus, was die Plattformdienste automatisch für das Routing erhalten).
- Ihre Kontakte, Ihren Kalender, Ihre Fotobibliothek (abgesehen von Belegfotos, die Sie ausdrücklich anhängen), Ihren Anrufverlauf, Ihre SMS-Nachrichten oder Ihren Browserverlauf.
- Ihre Bankkontozugangsdaten, Bankleitzahlen oder Anmeldedaten für ein Finanzinstitut.
- Gesundheits-, Fitness- oder biometrische Daten.

## Wie wir Informationen verwenden

Wir verwenden die begrenzten Informationen, die wir erheben, ausschließlich für genau diese Zwecke und für nichts anderes:

- **Zur Bereitstellung der Kernfunktionalität der App** (Berechnung Ihres Budgets, Synchronisierung von Daten über Ihre Geräte hinweg, falls Sie sich dafür entschieden haben, Anzeige Ihrer Transaktionen).
- **Zur Diagnose von Abstürzen und Fehlern**, damit wir sie in der nächsten Version beheben können.
- **Zur Überprüfung der Integrität Ihres Abonnements**, falls Sie ein Upgrade durchgeführt haben.
- **Zur Auslieferung von Werbung** in der kostenlosen Stufe über unser Werbenetzwerk.

Wir **werden nicht**:

- Ihre Daten an irgendjemanden verkaufen, niemals, zu keinem Zweck.
- Ihre Daten mit Datenhändlern, Marketingnetzwerken oder Analyseunternehmen teilen (über die nachstehend aufgeführten Auftragsverarbeiter hinaus).
- Ihre Finanzdaten zum Trainieren von Modellen des maschinellen Lernens oder KI-Systemen verwenden.
- Ihre Finanzdaten für Werbung oder zur Erstellung eines Profils über Sie verwenden.

## Wie wir Ihre Informationen schützen

- **Ende-zu-Ende-Verschlüsselung** für alle SYNC-Daten mittels ChaCha20-Poly1305, wobei der Verschlüsselungsschlüssel nur auf Ihren Geräten erzeugt und gespeichert wird.
- **Verschlüsselung im Ruhezustand** im Cloud-Speicher — selbst unser Cloud-Infrastruktur-Anbieter sieht stets nur Chiffretext.
- **Verschlüsselung bei der Übertragung** mittels HTTPS / TLS für die gesamte Netzwerkkommunikation.
- **App-Integritätsprüfung**, um nicht autorisierten Clients den Zugriff auf das SYNC-Backend zu verwehren.
- **Passwortverschlüsselte Backups** mittels PBKDF2-SHA256-Schlüsselableitung — jedes Backup wird mit einem von Ihnen bereitgestellten Passwort verschlüsselt; ohne dieses kann das Backup nicht entschlüsselt werden.
- **Keine serverseitige Entschlüsselungsfähigkeit** — konstruktionsbedingt können wir Ihre Daten nicht lesen, selbst wenn wir es wollten oder dazu gezwungen würden.

Kein System ist vollkommen sicher, aber wir befolgen die bewährten Verfahren der Branche und haben BudgeTrak so konzipiert, dass wir möglichst wenig Zugriff erhalten.

## Auftragsverarbeiter (Dritte)

BudgeTrak ist auf die folgenden Auftragsverarbeiter (Dritte) angewiesen. Jeder von ihnen hat seine eigene Datenschutzerklärung, die regelt, wie er mit den begrenzten Daten umgeht, die wir mit ihm teilen. Wir führen die konkreten Anbieter hier auf, damit diese Offenlegung vollständig und überprüfbar ist; im übrigen Teil dieser Erklärung beziehen wir uns auf sie nach ihrer Funktion (z. B. "unser Cloud-Infrastruktur-Anbieter"), um den Text lesbar zu halten.

| Dienst | Anbieter | Zweck | Was er sieht |
|---|---|---|---|
| Weiterleitung verschlüsselter SYNC-Daten | Google Firebase Firestore | Cloud-Datenbank für verschlüsselte Blöcke | Nur verschlüsselte Blöcke |
| Speicherung verschlüsselter Belegfotos (SYNC) | Google Firebase Cloud Storage | Cloud-Objektspeicher für verschlüsselte Bilder | Nur verschlüsselte Blöcke |
| Geräte-Präsenzverfolgung | Google Firebase Realtime Database | Online-/Offline-Anzeigen für SYNC | Anonyme Geräte-IDs |
| Backend-Authentifizierung | Google Firebase Authentication | Anonyme Anmeldung, nur ausgelöst durch erste Nutzung von SYNC, Hilfe-Chat, KI-Funktionen oder einem kostenpflichtigen Kauf | Anonymes Benutzer-Token |
| Missbrauchsschutz-Verifizierung | Google Firebase App Check + Play Integrity | Blockiert nicht autorisierte Clients | Plattform-Attestierung |
| Absturzberichterstattung | Google Firebase Crashlytics | Absturzdiagnose | Absturzdaten, keine Finanzdaten |
| Nutzungsanalyse | Google Firebase Analytics | Anonyme Nutzungsereignisse (OCR-Genauigkeit + täglicher Heartbeat) | Nur Zählungen und boolesche Werte — kein Transaktionsinhalt, kein Standort |
| KI-Verarbeitung (nur opt-in-Funktionen) | Google Gemini | Beleglesung; CSV-Transaktionskategorisierung; Hilfe-Chat-Assistent | Inhalt des Belegbildes; Händler und Betrag importierter Banktransaktionen; der Text, den Sie in den Hilfe-Chat eingeben, plus ein relevanter Auszug aus der Hilfe-Dokumentation der App |
| In-App-Käufe und Abonnements | Google Play Billing | Abonnements und einmalige Käufe | Zahlungsinformationen (vollständig von Google Play verarbeitet) |
| Werbung (nur kostenlose Stufe) | Google AdMob | Native Werbung | Werbe-ID, grundlegende Geräteinformationen |

Sie können die Datenschutzpraktiken dieser Anbieter unter [https://policies.google.com/privacy](https://policies.google.com/privacy) einsehen.

## KI-gestützte Funktionen (Opt-in)

BudgeTrak bietet drei optionale KI-gestützte Funktionen. Die ersten beiden sind für die Stufen "Kostenpflichtig" und "Abonnent" verfügbar; die dritte, der Hilfe-Chat, ist für alle Stufen verfügbar (einschließlich der kostenlosen). Alle drei sind standardmäßig deaktiviert und erfordern eine ausdrückliche Nutzeraktion zur Aktivierung.

### KI-Beleg-Scan (Abonnenten)
Wenn ein Abonnent im Transaktionsdialog auf das Funkel-Symbol tippt, sendet BudgeTrak das Belegfoto an unseren KI-Dienstleister, um Händler, Datum, Betrag und Kategorie zu extrahieren. Die Antwort wird direkt an Ihr Gerät zurückgegeben und nur in Ihrem Transaktionsdatensatz gespeichert.

### KI-CSV-Kategorisierung (Stufen "Kostenpflichtig" und "Abonnent", standardmäßig deaktiviert)
Wenn diese Funktion in den Einstellungen aktiviert ist, sendet BudgeTrak den Händlernamen und den Betrag neu importierter Banktransaktionen an unseren KI-Dienstleister, um für jede die am besten passende Kategorie auszuwählen. Das Transaktionsdatum wird **nicht** gesendet. Es werden nur Transaktionen gesendet, die der geräteinterne Kategorisierer von BudgeTrak nicht zuverlässig klassifizieren kann.

### Hilfe-Chat-Assistent (alle Stufen, standardmäßig deaktiviert)
Wenn Sie das Hilfe-Chat-Kästchen unter **Einstellungen → Datenschutz → Chatbot erlauben, Ihre Nachrichten zu übertragen und zu speichern…** aktivieren und im In-App-Einwilligungsdialog auf **Akzeptieren** tippen, können Sie mit der Hilfe-Chat-Funktion von BudgeTrak Fragen dazu eingeben, wie die App funktioniert, und KI-generierte Antworten erhalten, die auf den Hilfeseiten der App basieren. Wenn die Funktion aktiviert ist:

- Der Text, den Sie eingeben, wird an unseren KI-Dienstleister gesendet, um eine Antwort zu generieren. Jede Anfrage enthält außerdem einen kurzen Auszug aus der integrierten Hilfe-Dokumentation der App, damit die KI ihre Antwort auf dem tatsächlichen Verhalten von BudgeTrak gründen kann. Es werden keine persönlichen Finanzdaten, Transaktionsdetails, Kontostände oder Einstellungen gesendet.
- Das vollständige Chat-Transkript wird außerdem **anonym** in unserer Cloud-Infrastruktur unter einer auf Ihrem Gerät erzeugten zufälligen 128-Bit-Chat-ID gespeichert. Das Transkript ist im wörtlichen Sinne anonym: Wir erfassen **nicht** Ihre Backend-Authentifizierungs-Benutzer-ID, Geräte-ID, IP-Adresse, Ihren Namen, Ihre E-Mail-Adresse oder eine andere Kennung daneben — nur die Chat-ID, den Nachrichtentext, Zeitstempel und die App-Version. Wir verwenden diese anonym gespeicherten Transkripte, um die Genauigkeit des Chatbots regelmäßig zu überprüfen und missbräuchliche Nutzung zu erkennen; wir können sie keinem bestimmten Nutzer zuordnen. Transkripte werden nach **7 Tagen** durch eine serverseitige Time-to-Live-Richtlinie automatisch gelöscht.
- Jedes Gerät verwaltet seine Einwilligung unabhängig. Das Kästchen ist bei der Installation standardmäßig deaktiviert und wird **nicht** zwischen SYNC-Geräten synchronisiert. Das Deaktivieren zu einem beliebigen Zeitpunkt widerruft die Einwilligung — bereits auf unseren Servern befindliche Transkripte unterliegen weiterhin der oben genannten 7-tägigen TTL und werden dann automatisch gelöscht, und von Ihrem Gerät werden keine weiteren Nachrichten hochgeladen.
- Sie können jederzeit im Hilfe-Chat-Dialog auf **Löschen** tippen, um das vorhandene Transkript ein letztes Mal hochzuladen und den lokalen Puffer zu leeren, wodurch ein neuer Chat mit einer neuen anonymen Chat-ID begonnen wird. Lokale Nachrichten, die älter als 48 Stunden sind, werden auf jedem Gerät ebenfalls automatisch entfernt, unabhängig davon, ob Sie sie löschen.
- Sie benötigen **kein** kostenpflichtiges Abonnement, und der Hilfe-Chat erfordert **kein** SYNC. Wenn Sie SYNC nicht aktiviert haben, meldet sich BudgeTrak beim ersten Hochladen eines Transkripts anonym an, ausschließlich um unsere serverseitige Authentifizierungsanforderung zu erfüllen; durch diese anonyme Anmeldung werden keine personenbezogenen Daten erhoben.

### Website-Chatbot (techadvantagesupport.github.io)
Unsere Website hostet einen KI-Assistenten, der Fragen von Besuchern zu BudgeTrak beantwortet und sich dabei auf dieselbe integrierte Hilfe-Dokumentation wie der In-App-Hilfe-Chat stützt. Wenn Sie ihn verwenden:

- Der Text, den Sie eingeben, wird an unsere Server gesendet und an unseren KI-Dienstleister weitergeleitet, um eine Antwort zu generieren. Geben Sie keine persönlichen, finanziellen oder Kontoinformationen ein — der Assistent benötigt sie nicht, und wir bitten Sie, sie nicht weiterzugeben.
- Wir speichern jede Nachricht und Antwort für bis zu **7 Tage**, um die Genauigkeit des Assistenten zu überprüfen und Missbrauch zu erkennen, zusammen mit einem kryptografischen Einweg-Hash Ihrer IP-Adresse. Der Hash wird **ausschließlich** verwendet, um ein tägliches Nachrichtenlimit pro Besucher durchzusetzen; wir können Ihre IP-Adresse daraus nicht wiederherstellen, und wir speichern keinen Namen, keine E-Mail-Adresse, kein Konto und keine Gerätekennung bei den Website-Chats.
- Es ist kein Konto oder keine Anmeldung erforderlich, und die Nutzung des Website-Chatbots ist vollständig optional.

### Was niemals an den KI-Dienstleister gesendet wird
- Ihre Kontostände oder Summen
- Ihre bisherigen Transaktionen (abgesehen von den konkreten importierten Zeilen oder dem zu verarbeitenden Beleg)
- Ihre Verschlüsselungsschlüssel, Gerätekennungen oder Authentifizierungs-Token
- Ihre Belegfotos (sie werden nur durch den oben beschriebenen Beleg-Scan gesendet, niemals durch die CSV-Kategorisierung oder den Hilfe-Chat)
- Daten aus irgendeiner BudgeTrak-Funktion, es sei denn, Sie haben sich ausdrücklich für diese spezifische Funktion entschieden

### Wie Ihre Daten geschützt werden
- Alle Anfragen werden bei der Übertragung verschlüsselt (HTTPS/TLS).
- Beim Beleg-Scan und der CSV-Kategorisierung löscht der KI-Dienstleister die Anfrage- und Antwortdaten, sobald die Anfrage abgeschlossen ist; für diese Funktionen wird nichts auf den Servern des Anbieters gespeichert. Gemäß der Standardkonfiguration des Anbieters **werden Ihre Daten nicht zum Trainieren der KI-Modelle des Anbieters verwendet**.
- Beim Hilfe-Chat werden Ihre eingegebenen Nachrichten und die Antworten der KI von BudgeTrak (nicht vom KI-Dienstleister) für bis zu 7 Tage für die oben beschriebene Genauigkeits-/Missbrauchsprüfung gespeichert und danach automatisch gelöscht. Der KI-Anbieter bewahrt die Anfrage nicht auf, nachdem die Antwort generiert wurde.
- Alle KI-Funktionen können jederzeit in den Einstellungen deaktiviert werden, wodurch auf das vollständig geräteinterne Verhalten von BudgeTrak zurückgegriffen wird (oder beim Hilfe-Chat auf den In-App-E-Mail-Ausweichlink).

Nutzer der kostenlosen Stufe haben Zugriff auf den **Hilfe-Chat** (mit Einwilligung), jedoch nicht auf den **KI-Beleg-Scan** oder die **KI-CSV-Kategorisierung**.

## Ihre Rechte und Wahlmöglichkeiten

Sie haben die volle Kontrolle über Ihre Daten in BudgeTrak.

- **Alles löschen**: Durch die Deinstallation von BudgeTrak werden alle lokal gespeicherten Daten von Ihrem Gerät entfernt. Wenn Sie auch SYNC verwenden, verlassen oder lösen Sie zunächst Ihre SYNC-Gruppe über den SYNC-Bildschirm auf, um die Cloud-Kopie zu entfernen.
- **Eine SYNC-Gruppe verlassen**: Tippen Sie auf dem SYNC-Bildschirm auf "Gruppe verlassen". Ihre lokalen Daten bleiben erhalten; die mit Ihrem Gerät verknüpften Cloud-Daten werden entfernt.
- **Eine SYNC-Gruppe auflösen** (nur Administrator): Tippen Sie auf dem SYNC-Bildschirm auf "Gruppe auflösen". Alle Cloud-Daten der Gruppe werden dauerhaft gelöscht; jedes Gerät behält seine lokale Kopie.
- **Ihre Daten exportieren**: Verwenden Sie die Speicherfunktion auf dem Transaktionsbildschirm, um Ihre Transaktionen im CSV-, Excel- oder PDF-Format zu exportieren. Backups über die Einstellungen enthalten alle Ihre Budgetdaten in einer einzigen Datei.
- **Absturzberichterstattung und Nutzungstelemetrie deaktivieren**: Öffnen Sie **Einstellungen → Datenschutz → Absturzberichte und anonyme Nutzungsdaten senden** in BudgeTrak und deaktivieren Sie das Kästchen. Die Änderung tritt sofort in Kraft — sowohl die Absturzberichterstattung als auch die Analyse werden angewiesen, keine Daten mehr von Ihrem Gerät zu erheben, einschließlich des täglichen Heartbeats und der OCR-Genauigkeitsereignisse.
- **Hilfe-Chat-Einwilligung widerrufen**: Öffnen Sie **Einstellungen → Datenschutz → Chatbot erlauben, Ihre Nachrichten zu übertragen und zu speichern…** in BudgeTrak und deaktivieren Sie das Kästchen. Von Ihrem Gerät werden keine weiteren Nachrichten hochgeladen. Alle bereits anonym auf unseren Servern gespeicherten Transkripte werden weiterhin nach der oben beschriebenen 7-tägigen Aufbewahrungsfrist automatisch gelöscht; da sie ohne Ihre Identität gespeichert werden, können wir die früheren Transkripte eines bestimmten Nutzers nicht auf Anfrage löschen.
- **Werbeverfolgung einschränken**: Setzen Sie Ihre Android-Werbekennung in den Einstellungen Ihres Geräts unter Datenschutz → Werbung zurück oder schränken Sie sie ein.

Wenn Sie möchten, dass wir Ihnen bestätigen, welche Daten wir über Sie speichern (Hinweis: In nahezu allen Fällen lautet die Antwort "nichts persönlich Identifizierendes"), oder ein anderes Datenschutzanliegen haben, kontaktieren Sie uns unter **support@techadvantageapps.com**.

## Datenlöschung

Sie können die Löschung Ihrer BudgeTrak-Daten über eine der folgenden Optionen beantragen:

### 1. Löschung in der App (Administrator einer SYNC-Gruppe)
Öffnen Sie BudgeTrak → Einstellungen → SYNC → **Gruppe auflösen**. Dadurch werden alle serverseitigen Daten der Gruppe dauerhaft gelöscht: Transaktionen, Kategorien, wiederkehrende Ausgaben, Einnahmequellen, Sparziele, Amortisationseinträge, Periodenbuch, verschlüsselte Belegfotos und Gruppenmetadaten. Die Kaskade wird von einer serverseitigen Funktion ausgeführt, die Daten aus unserer Cloud-Infrastruktur entfernt. Jedes Mitgliedsgerät behält seine lokale Kopie, sofern es nicht ebenfalls die App deinstalliert.

### 2. Entfernung in der App (Mitglied einer SYNC-Gruppe)
Öffnen Sie BudgeTrak → Einstellungen → SYNC → **Gruppe verlassen**. Ihr Gerät wird im Geräteverzeichnis der Gruppe als entfernt markiert, Ihr Echtzeit-Präsenzdatensatz wird gelöscht und die Verschlüsselungsschlüssel Ihres Geräts für die Gruppe werden gelöscht. Die geteilten Daten selbst verbleiben in der Gruppe für die verbleibenden Mitglieder; wenn Sie möchten, dass die gesamte Gruppe gelöscht wird, muss der Administrator sie auflösen.

### 3. Nur lokale Löschung
Durch die Deinstallation von BudgeTrak werden alle Daten auf dem Gerät sofort entfernt (Transaktionen, Einstellungen, Belegfotos, verschlüsselte Backups, die im privaten Ordner der App gespeichert sind). Wenn Sie BudgeTrak nur im Einzelmodus (ohne SYNC) verwendet haben, existierten niemals Cloud-Daten, und die Deinstallation schließt die Löschung vollständig ab.

### 4. Automatische Löschung
SYNC-Gruppen, die 90 aufeinanderfolgende Tage lang von keinem Mitgliedsgerät geöffnet wurden, werden durch einen serverseitigen Bereinigungsprozess automatisch und dauerhaft gelöscht. Dies umfasst alle Transaktionen, verschlüsselten Fotos und Metadaten. Von dieser automatischen Bereinigung gibt es keine Wiederherstellung; stellen Sie sicher, dass Sie über ein lokales Backup verfügen, bevor Sie eine Gruppe inaktiv werden lassen.

### Warum wir keine manuelle Löschung per E-Mail anbieten
BudgeTrak verknüpft Ihre Cloud-Daten bewusst nicht mit Ihrem Namen, Ihrer E-Mail-Adresse oder einer Kennung, die wir verwenden könnten, um "Ihre" Datensätze auf Anfrage nachzuschlagen. Die anonyme Authentifizierung, die Ende-zu-Ende-Verschlüsselung und die zufällig erzeugten Gruppenkennungen sind das, was die Datenschutzgarantien in dieser Erklärung möglich macht — aber dasselbe Design bedeutet, dass wir, wenn Sie uns mit der Bitte schreiben, eine bestimmte Gruppe zu löschen, keine Möglichkeit haben, zu überprüfen, ob die Gruppe Ihnen gehört, oder sie überhaupt unter den verschlüsselten Blöcken auf unseren Servern zu finden.

Wenn Sie den Zugriff auf Ihr Gerät oder auf eine Gruppe verloren haben, deren Administrator Sie nicht mehr erreichen können, ist die oben beschriebene 90-tägige Inaktivitätsbereinigung der Löschmechanismus. Stellen Sie sicher, dass Sie über ein lokales Backup aller Daten verfügen, die Sie behalten möchten, bevor dieses Fenster abläuft.

Was die Löschung **nicht** betrifft: anonyme Absturzdatensätze (vom Absturzberichterstattungs-Anbieter gemäß seiner Standardrichtlinie für 90 Tage aufbewahrt, unabhängig von Aktionen in der App) und Werbekennungen (von Android auf Geräteebene verwaltet — zurücksetzbar über die Einstellungen Ihres Geräts).

## Datenaufbewahrung

- **Daten auf dem Gerät** werden aufbewahrt, bis Sie sie löschen oder die App deinstallieren.
- **SYNC-Cloud-Daten** werden 90 Tage nach der letzten Aktivität in einer Gruppe automatisch gelöscht und sofort gelöscht, wenn eine Gruppe aufgelöst wird.
- **Hilfe-Chat-Transkripte** werden anonym gespeichert und **7 Tage** nach der letzten Aktualisierung durch eine serverseitige Time-to-Live-Richtlinie automatisch gelöscht. Lokale Kopien auf Ihrem Gerät werden in jedem Fall nach 48 Stunden entfernt.
- **Absturzberichte** werden vom Absturzberichterstattungs-Anbieter gemäß seinen Standard-Aufbewahrungsrichtlinien aufbewahrt (derzeit 90 Tage für Absturzdaten).
- **Belegfotos im Cloud-Speicher** folgen der Aufbewahrungsfrist, die Ihr Gruppenadministrator in den Einstellungen festlegt, oder werden auf unbestimmte Zeit aufbewahrt, wenn keine Aufbewahrungsfrist konfiguriert ist. Sie werden sofort gelöscht, wenn Sie die entsprechende Transaktion oder das entsprechende Foto entfernen.

## Datenschutz von Kindern

BudgeTrak ist ein Werkzeug für die persönliche Finanzverwaltung, das für Nutzer ab 13 Jahren bestimmt ist. Wir erheben nicht wissentlich personenbezogene Daten von Kindern unter 13 Jahren. Wenn Sie glauben, dass ein Kind unter 13 Jahren uns personenbezogene Daten zur Verfügung gestellt hat, kontaktieren Sie uns bitte unter **support@techadvantageapps.com**, und wir werden Schritte unternehmen, um diese zu löschen.

## Internationale Nutzer

BudgeTrak wird aus den Vereinigten Staaten herausgegeben. Wenn Sie die App von außerhalb der Vereinigten Staaten nutzen, beachten Sie bitte, dass alle Daten, die Sie in die Cloud synchronisieren (die verschlüsselt werden, bevor sie Ihr Gerät verlassen), über Server weitergeleitet werden können, die von unseren Auftragsverarbeitern (Dritten) in den Vereinigten Staaten oder anderen Ländern betrieben werden, in denen sie Infrastruktur unterhalten. Durch die Nutzung der SYNC-Funktion von BudgeTrak willigen Sie in diese Weiterleitung ein.

## Änderungen an dieser Erklärung

Wir können diese Datenschutzerklärung von Zeit zu Zeit aktualisieren, insbesondere wenn wir Funktionen hinzufügen oder entfernen, die sich darauf auswirken, welche Daten erhoben werden. Wenn wir wesentliche Änderungen vornehmen, aktualisieren wir das Datum "Zuletzt aktualisiert" oben auf dieser Seite und benachrichtigen Sie gegebenenfalls innerhalb der App. Ihre fortgesetzte Nutzung von BudgeTrak nach einer Aktualisierung der Erklärung stellt eine Annahme der überarbeiteten Erklärung dar.

## Kontaktieren Sie uns

Wenn Sie Fragen zu dieser Datenschutzerklärung oder zu den Datenpraktiken von BudgeTrak haben, kontaktieren Sie bitte:

**Tech Advantage LLC**
E-Mail: **support@techadvantageapps.com**

Wir werden auf berechtigte Datenschutzanfragen innerhalb einer angemessenen Frist antworten, in der Regel innerhalb von 30 Tagen.
