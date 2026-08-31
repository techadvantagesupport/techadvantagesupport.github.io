---
layout: guide
lang: de
group: banklogins
permalink: /de/ratgeber/budget-teilen-ohne-bankzugang/
title: "Wie Paare ein Budget teilen, ohne Bankzugangsdaten zu teilen | BudgeTrak"
short_title: "Teilen ohne Bankzugang"
h1: "Wie du ein Budget mit deinem Partner teilst, ohne Bankzugangsdaten zu teilen"
kicker: "Datenschutz & gemeinsames Geld"
description: "Ihr könnt ein Haushaltsbudget über zwei Handys führen, ohne dass jemand irgendwo Bankzugangsdaten eingibt. So funktioniert es, das wird synchronisiert, und das sind die echten Kompromisse."
standfirst: "Gemeinsame Finanzen brauchen keine gemeinsamen Passwörter. Hier ist die Mechanik eines geteilten Budgets, das deine Bank nie berührt."
hero: /assets/guides/hero-privacy.jpg
hero_alt: "Ein Paar, jeder mit dem eigenen Handy, teilt ein Haushaltsbudget"
published: "2026-08-31"
reading_time: 7
faq:
  - q: "Kann man ein Budget teilen, ohne Bankkonten zu verknüpfen?"
    a: "Ja. Ein Budget braucht drei Eingaben — Einkommen, wiederkehrende Verpflichtungen und Ausgaben — und keine davon erfordert Bankzugriff. BudgeTrak synchronisiert diese drei Dinge direkt zwischen deinen Geräten mit Ende-zu-Ende-Verschlüsselung, es existiert also zu keinem Zeitpunkt eine Bankverbindung."
  - q: "Welche Daten werden zwischen den Partnern eigentlich synchronisiert?"
    a: "Euer Budget: Einkommen, wiederkehrende Ausgaben, Sparziele, Kategorien und Buchungen, jeweils dem Gerät zugeordnet, das sie erfasst hat. Alles Ende-zu-Ende verschlüsselt, also unlesbar auf dem Transportweg und unlesbar auf unseren Servern."
  - q: "Kann mein Partner mein persönliches Bankkonto sehen?"
    a: "Nein, denn BudgeTrak hat auf niemandes Bankkonto Zugriff. Mitglieder sehen das geteilte Haushaltsbudget und die darin erfassten Buchungen — mehr nicht."
  - q: "Ist ein geteiltes Budget ohne Bankanbindung mehr Arbeit?"
    a: "Etwas. Rechne mit rund einer Minute Erfassung am Tag oder einem wöchentlichen CSV-Import. Wenn deine Bank Kaufbenachrichtigungen schickt, kann die Subscriber-Stufe daraus automatisch offene Einträge machen, was den Großteil der Handarbeit erspart."
  - q: "Wie viele Personen können ein Budget teilen?"
    a: "Bis zu fünf Geräte in einer SYNC-Gruppe. Eine Person abonniert für 4,99 $ im Monat, alle anderen treten kostenlos bei."
related:
  - url: /de/ratgeber/budget-app-fuer-paare/
    title: "Die beste Budget-App für Paare"
    blurb: "Der vollständige Fall, auch wo wir nicht passen."
  - url: /de/ratgeber/budget-ohne-bankverbindung/
    title: "Budgetieren ohne Bankverbindung"
    blurb: "Dasselbe Prinzip für eine Person."
  - url: /de/ratgeber/haushaltsbudget-app-familie/
    title: "Ein Budget auf allen Handys"
    blurb: "Mit Jugendlichen und weiteren Erwachsenen."
  - url: /de/ratgeber/sicheres-budget-erklaert/
    title: "Was das Sichere Budget bedeutet"
    blurb: "Die Zahl, der das alles dient."
---

Die Annahme, die in fast jedem Produkt für gemeinsame Finanzen steckt, lautet: Wer das Geld zweier Menschen zusammenlegt, muss auch den Bankzugang zweier Menschen zusammenlegen. Muss man nicht. Man muss ihre *Zahlen* zusammenlegen, und das ist etwas viel Kleineres und viel weniger Sensibles.

Dieser Ratgeber ist die Mechanik: Was ein geteiltes Budget wirklich braucht, was BudgeTrak wohin sendet, und was du aufgibst, wenn du keine Bank verbindest.

## Ein Budget braucht drei Eingaben. Keine davon ist deine Bank.

Schreib auf, was ein Budget tatsächlich berechnet:

1. **Was reinkommt** — dein Einkommen und wann es eintrifft.
2. **Was bereits gebunden ist** — Miete, Versicherungen, Abos, Sparziele, die Jahresrechnung, die du jedes Jahr vergisst.
3. **Was bisher rausgegangen ist** — die Ausgaben seit Beginn des Zeitraums.

Das war's. Mit diesen dreien ist die Rechnung eindeutig. Die Bankanbindung ist eine *Eingabe-Bequemlichkeit* für Punkt 3. Sie ist nicht Teil der Berechnung und spielt bei Punkt 1 und 2 überhaupt keine Rolle — und genau dort gehen die meisten Haushaltsbudgets schief.

Anders gesagt: Die Bank zu verbinden macht das Erfassen leichter. Es macht dein Budget nicht richtiger. Das wird häufig verwechselt.

## Was „geteilt“ heißt, wenn keine Bank dazwischen ist

In einer App mit Bankanbindung läuft es so: Beide verknüpfen ihre Konten, der Aggregator zieht beide Umsatzhistorien auf einen Server, die App zeigt eine gemeinsame Ansicht. Das geteilte Objekt ist *eine serverseitige Kopie zweier Bankhistorien*.

In BudgeTrak ist das geteilte Objekt das Budgetdokument selbst — Einkommen, Rechnungen, Ziele, Buchungen — repliziert zwischen euren eigenen Geräten. Eine Person erstellt die SYNC-Gruppe, die andere tritt mit einem Code bei. Danach halten beide Handys dasselbe Budget und aktualisieren sich gegenseitig in Echtzeit.

Der Unterschied zählt vor allem im Schadensfall. Würden unsere Server morgen kompromittiert, hätten Angreifer Chiffretext: Die SYNC-Daten werden auf deinem Gerät verschlüsselt, bevor sie es verlassen, und können nur von den Geräten deiner Gruppe entschlüsselt werden. Wir können sie nicht lesen — was auch heißt, dass wir sie nicht wiederherstellen können, wenn alle Geräte der Gruppe verloren gehen.

<figure class="shot">
<img src="/assets/tour/de/sync.webp" alt="BudgeTrak-SYNC-Bildschirm mit den Haushaltsmitgliedern" width="540" height="960" loading="lazy">
<figcaption>Bis zu fünf Geräte auf einem verschlüsselten Budget, mit Zuordnung pro Mitglied.</figcaption>
</figure>

<div class="note">
<p><strong>Eine ehrliche Abgrenzung.</strong> „Ende-zu-Ende verschlüsselt“ bezieht sich auf SYNC. Es heißt nicht, dass die App nie mit dem Netz spricht — die optionalen KI-Funktionen (Belegscan, CSV-Kategorisierung, Hilfe-Chat) senden das, was du ihnen übergibst, zur Verarbeitung, und das ist der Handel, wenn du genau diese Funktionen nutzt. Alles in diesem Ratgeber funktioniert, ohne eine davon anzufassen.</p>
</div>

## Ausgaben erfassen: die drei Wege

Ohne Bankanbindung kommen Buchungen auf drei Wegen herein. Die meisten Haushalte nutzen am Ende zwei davon.

### 1. Im Moment erfassen
Das Startbildschirm-Widget nimmt eine Ausgabe mit zwei Tipps entgegen, ohne die App zu öffnen. Das klingt nach der mühsamen Variante und wird am meisten bezweifelt, kostet real aber rund 40 Sekunden am Tag — und hat einen unterschätzten Nebeneffekt: Du bemerkst, was du ausgibst, *während* du es ausgibst. Genau darin liegt ein großer Teil der Verhaltensänderung, für die Leute überhaupt eine Budget-App kaufen.

### 2. Kontoauszug importieren
Lade eine CSV bei deiner Bank herunter, wann es dir passt, und importiere sie. Die Dublettenerkennung gleicht ab, was du schon von Hand erfasst hast, der Händlerabgleich lernt deine Stammgeschäfte. Teil des einmaligen Upgrades für 9,99 $. Das ist der „sonntags aufholen“-Ablauf, und für ein Paar, das nicht täglich erfassen will, funktioniert er gut.

### 3. Die Benachrichtigungen deiner Bank nutzen
Wenn deine Banking-App dir beim Kartenzahlen ohnehin eine Push-Nachricht schickt, enthält diese bereits Händler und Betrag. BudgeTrak kann diese Benachrichtigungen auf deinem Gerät lesen und daraus **offene** Einträge machen — Sekunden nach dem Kauf, Tage bevor die Buchung in einem Kontoauszug auftauchen würde.

Das gehört präzisiert, weil es nach dem klingt, was wir gerade ausgeschlossen haben. Ist es nicht. Keine Bankzugangsdaten, kein Aggregator, keine SMS-Berechtigung. Die App liest Benachrichtigungen, die deine Bank ohnehin an dein eigenes Handy schickt, entnimmt Betrag und Händler und stellt einen offenen Eintrag in die Warteschlange, den du freigibst, bevor er das Budget berührt. Jedes Gerät sieht nur seinen eigenen Benachrichtigungsstrom. Subscriber-Stufe.

<figure class="shot">
<img src="/assets/tour/de/transactions.webp" alt="Buchungsliste in BudgeTrak" width="540" height="960" loading="lazy">
<figcaption>Wie die Einträge auch hereinkommen — sie landen im selben geteilten Buch.</figcaption>
</figure>

## Zuordnung ohne Überwachung

Jede Buchung hält fest, welches Gerät sie erfasst hat. Das ist bewusst zurückhaltend: Es existiert, damit beide sehen können, warum die Tageszahl um 80 € gefallen ist, ohne nachfragen zu müssen. Es ist keine Kontrollfunktion, und es gibt keine Rangliste der Ausgaben pro Person — das wäre ein anderes Produkt und meist eine schlechtere Beziehung.

## Was du wirklich aufgibst

Drei Dinge, klar gesagt:

- **Automatische Erfassung von allem, überall.** Die Benachrichtigungserfassung deckt Karten ab, deren Bank Meldungen schickt. Bargeld und Banken ohne Push brauchen weiterhin Erfassung oder Import.
- **Rückwirkende Historie am ersten Tag.** Ein Aggregator zieht zwölf Monate, sobald du verbindest. Hier würdest du dafür eine CSV importieren.
- **Automatischer Kontoabgleich.** BudgeTrak verfolgt das Budget, das du beschrieben hast, nicht deinen tatsächlichen Kontostand. Driften die beiden auseinander, gleichst du beim nächsten Import ab.

Wenn das für dich nicht geht, ist eine App mit Bankanbindung ehrlich das bessere Werkzeug — und ein Budget, das du wirklich pflegst, schlägt ein prinzipientreues, das du aufgibst.

## Gemeinsam einrichten

Fünfzehn Minuten, einmal, auf einem Handy:

1. Einkommen eintragen — auch das unregelmäßige; die Engine kommt mit schwankendem Verdienst und geballten Rechnungen zurecht.
2. Wiederkehrende Ausgaben mit den echten Fälligkeitsdaten eintragen.
3. Sparziele anlegen und alles Große, das du über Monate verteilst.
4. SYNC einschalten und den Partner mit dem Code beitreten lassen.

Danach schaut ihr beide auf dieselbe Tageszahl. Die erste Woche ist meist unangenehm, weil die Zahl kleiner ist als der Kontostand, den ihr beide benutzt habt. Genau diese Lücke ist der Punkt — sie sind die Verpflichtungen, die ihr doppelt ausgegeben habt.
