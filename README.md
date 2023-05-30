# Order-Translator Schulprojekt

Mit diesem Projekt soll ein Service erstellt werden, welcher Aufträge aus verschiedenen Quellsystemen (Onlineshop, ERP)
entgegennimmt und diese an die Logistik zur Auslieferung überträgt.

## Aufgabenstellung

In der Logistik werden Aufträge aus verschiedenen Quellsystemen bearbeitet. Diese Quellsysteme exportieren die Aufträge
in unterschiedlichen Formaten:

* Die Aufträge des Onlineshops sind im JSON-Format ([Beispiel](data/auftrag_onlineshop.json))
* Die Aufträge aus dem EPR-System liegen im XML-Format vor ([Beispiel](data/auftrag_erp.xml))

Das Logistiksystem verlangt die Aufträge in einem einheitlichen Format. Das Format ist in
dieser [Datei](data/logistik/input_schema.json) als JSON-Schema beschreiben.
Eine [Beispiel-Datei](data/logistik/beispiel_input.json) für den Request liegt ebenfalls vor.
Mit [diesem Online-Tool](https://www.jsonschemavalidator.net/s/GBmB5hf7) lassen sich die Daten gegen das Schema testen
Die Daten müssen dem System per REST-Request mit der Methode Post übergeben werden. Dafür existiert eine Test-API welche
wir eingerichtet haben. Der Zugang wird den Projektteilnehmern bereitgestellt.

![Projektaufbau](docs/project.jpeg)



## Wie starten wir?

1. Nachdem ihr einen persönlichen GitHub-Account erstellt habt, könnt ihr dieses Repository forken. Damit legt ihr
   eine "verbundene" Kopie auf euren Account.
2. Diese Kopie könnt ihr das Repository jetzt von eurem Account auschecken (runterladen)
3. Jetzt könnt ihr lokal entwickeln und die Änderungen anschließend auf euren Account pushen (hochladen)
4. Wenn ihr mit eurem Ergebnis zufrieden seid, reicht ihr einen Pull-Request ein. Damit kann der Code aus von eurem
   GitHub-Account in das Repository im simplicity-GitHub-Account übertragen werden.

## Lesson 01

Das Programm soll über die Kommandozeile gestartet werden. Dazu soll der Einstiegspunkt erstellt werden, welche uns zuerst nur mit einem Hallo begrüßt.

### Lösung

Wir rufen das Script über die Kommandozeile mit dem Befehl `python3 main.py` auf:

Ausgabe:
```
Hallo
```

## Lesson 02

Ziel dieser Lektion ist es den Inhalt einer Datei auszulesen. Wir starten mit der Datei `auftrag_onlineshop.json` welche im Verzeichnis `data` liegt. 
Der Inhalt dieser Datei soll auf der Konsole ausgegeben werden.

### Lösung

Wir rufen das angepasste [Script](main.py) über die Kommandozeile mit dem Befehl `python3 main.py` auf:

Ausgabe:
```
{
  "orderReference": "32345423",
  "currency": "EUR",
  "customerReference": "7788997",
  "orderDate": "2023-04-24T08:48:07",
  "shippingAddress": {
    "firstName": "Mia",
    "lastName": "Mustermann",
    "address1": "Hauptstr.",
    "address2": "1",
    "address3": "",
    "city": "Berlin",
    "zipCode": "10115",
    "countryCode": "DE"
  },
  "orderItems": [
    {
      "sku": "4251238918483",
      "name": "Silani"
    },
    {
      "sku": "4059117317163",
      "name": "Sarion"
    },
    {
      "sku": "4059117317163",
      "name": "Sarion"
    },
    {
      "sku": "4251200728256",
      "name": "Sanika"
    }
  ]
}
```

## Lesson 03

Als Nächstes möchten wir auf einzelne Werte in den Auftragsdaten zugreifen. Ziel dieser Übung ist die Ausgabe der Auftragsnummer und des vollständigen Namen der Kundin.

### Lösung

Wir rufen das angepasste [Script](main.py) über die Kommandozeile mit dem Befehl `python3 main.py` auf:

Ausgabe:
```
Auftragsnummer: 32345423
Name der Kundin: Mia Mustermann
```

Um Variablen und fest definierten Text gemeinsam auszugeben wurde hier die [f-string-Funktion](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) genutzt.

## Lession 04

In den nächsten Übungen schauen wir uns die bestellten Artikel, also die Auftragspositionen, an. Zuerst möchten wir die Namen aller bestellten Artikel ausgeben.

Gewünschte Ausgabe:
```
Silani
Sarion
Sarion
Sanika
```

Bei den Auftragspositionen handelt es sich um eine Liste unbestimmter Größe (jede Bestellung kann 1 bis n Artikel enthalten).
So eine Liste durchlaufen wir in einer For-Schleife.

## Lesson 05

Der Artikel Sarion (sku 4059117317163) wurde in unserem Beispielauftrag doppelt bestellt. Die Logistik möchte gleiche Artikel zusammengefasst, unter Angabe der Bestellmenge, übergeben bekommen. Dazu möchten wir die SKU mit ihrer jeweiligen Mengen ausgeben

Gewünschte Ausgabe:

```
{'4251238918483': 1, '4059117317163': 2, '4251200728256': 1}
```

## Lesson 06

Jetzt soll der Payload zur Übertragung an die Logistik aufgebaut werden. Die Struktur können wir der [Beispieldatei](data%2Flogistik%2Fbeispiel_input.json), oder dem Data-Contract entnehmen:

Gewünschte Ausgabe in neuer Struktur:

```
{
  "customerCity": "Berlin",
  "pickingDateFrom": "2022-07-22",
  "pickingDateTo": "2022-07-22",
  "customerCountryCode": "DE",
  "customerZipCode": "10115",
  "orderNo": "32345423",
  "customerStreet": "Hauptstr. 1",
  "customerName": "Mia Mustermann",
  "packingCategory": "b2c",
  "items": [
    {
      "gtin": "4251238918483",
      "quantity": 1
    },
    {
      "gtin": "4059117317163",
      "quantity": 2
    },
    {
      "gtin": "4251200728256",
      "quantity": 1
    }
  ],
  "orderDate": "2022-07-22",
  "customerNo": "7788997"
}
```

In dieser Übung werden die Datumsfelder noch nicht betrachtet