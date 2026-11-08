# Individuell-uppgift-p2

# Individuell-uppgift-p2

## Vad gör appen?

Appen visar en meny där du väljer en stad och får väderprognosen för den. Appen visar:

- Aktuell temperatur och hur många grader det känns som
- Prognos för de kommande 3 dagarna
- Två grafer:
  - Högsta och lägsta temperatur per dag
  - Temperaturen timme för timme

---

## Installation

### 1. Förberedelser

1. Se till att du har **Python 3.10 eller senare** installerat.
2. Hämta appen på repositoryts sida: klicka på den gröna knappen **Code** och välj **Download ZIP**. Du kan också klona repot med `git clone` i terminalen.
3. Öppna mappen i en kodeditor (den här guiden använder Visual Studio Code). Kontrollera att filerna `requirements.txt` och `requirements.dev.txt` finns.
4. Öppna terminalen i VS Code med `Ctrl+J` (Windows/Linux) eller `Cmd+J` (Mac).

### 2. Skapa en virtuell miljö

```bash
python3 -m venv venv
```

Aktivera den:

| Operativsystem | Kommando |
|---|---|
| Windows | `venv\Scripts\activate` |
| Mac / Linux | `source venv/bin/activate` |

När miljön är aktiv syns `(venv)` i början av terminalraden.

### 3. Installera beroenden

```bash
pip install -r requirements.txt
pip install -r requirements.dev.txt
```

### 4. Starta appen

```bash
flask run
```

Avsluta appen med `Ctrl+C`.

När du är klar kan du stänga av den virtuella miljön med:

```bash
deactivate
```

> **OBS!** Den virtuella miljön måste vara aktiv när du kör appen.

---

## Köra tester

1. Aktivera den virtuella miljön (`venv`).
2. Starta appen med `flask run` i en terminal.
3. Öppna en ny terminal, aktivera `venv` även där och kör:

```bash
pytest
```

Om alla tester går igenom visas grön text. Om något misslyckas visas röd text med information om vad som är fel.

---

## Vilket API används?

Appen använder **[Open-Meteo](https://open-meteo.com/)** för väderdata.
## Frågor
### 1. Varför mockar du anropen mot API:et i dina tester, och vad skulle hända om du inte gjorde det?
*API mockas för att kunna köra tester utan behov av nätverk. Om du hade bara vanliga tester utan en mockade API skulle alla tester misslycka förutom de som testar något specifik funktion som inte behöver nätverket på.*
### 2. Vad gör timeout och raise_for_status(), och varför behövs de?
*timeout sätter en timer när vi t.ex anropar en API så att efter ett viss tid som specifieras i sekunder kommer funktionen sluta vänta på ett svar frånAPI:et och göra det som skrivs i koden som ska hända i den fall. raise_for_status() läser vilket HTTP response status kod som har svaret anrop man har gjort medans appen kördes, om den har en status kod på 400 eller 500 betyder det visas en httperror. T.ex om man lyckas att anropa APIet kommer man få statuskoden 200 OK eller om man försöker uppnå en endpoint som inte finns i en appen så kommer status 404 att visas. Det finns status koder från 100 till 500 och varje hundratal betyder något olika. 200 är ok, 400 bad request etcetera.*
### 3. Hur fungerar mallarv i Jinja2? Förklara med exempel från dina egna mallar.
*mallar skapas i en "template" mapp där man använder en markup språk som html för att skapa en sida. I den sida kan man visa all data man vill och har. Ett bra stt att göra det är att använda en "base.html" som basmall och använd den som basen på allting. efter man har en bas mall så kan man extenderas med hjälp av jinja och deras {%extends "base.html"%} vilket behåller det innehåll som finns i bas html. i en ny mall skapar man en så kallas "block content" som kan sedan visas i bas mallen med hjälp av att skriva {%block content%} och {%endblock%} i både ny mall och bas mallen, så kommer jinja2 veta att när man vill visa nya template kommer jinja att använda strukturen från bas mallen och lägga nya mallen till bas mallen. med jinja kan man använda python i själva html filen*
### 4. Vad är en fixture, och vilken använder du?
*en fixture är somm ett verktyg som förbereder min app för en test. Man skapar den en gång och sedan man behöver inte skriva den om varje gång man vill testa något för att koden redan finns och programmet vet det, så man kan använda den fixture som en argument till en test funktion. I min fall jag skapade en test klient som används varje gång jag vill skicka en förfrågan till en av mina endpoints för att testa ett visst scenario. till exempel i min test test_ingen_formdata använder jag både mock och klient för att testa det som händer när klienten skickar en post förfrågan till "/" endpoint, vilket borde ge error 400 Bad Request*

---