import json  # importiert das Paket für den Umgang mit dem JSON-Datenformat

if __name__ == '__main__':
    with open(
            'data/auftrag_onlineshop.json',
            'r'
    ) as file:
        content = file.read()
        order_data = json.loads(
            content)  # liest die Daten welche als Text (string) vorliegen in eine neue Datenstruktur (dict) ein. Diese Datenstruktur hat den Vorteil, dass wir nun auf alle Werte innerhalb der Struktur gezielt zugreifen können

        order_number = order_data[
            "orderReference"]  # der Wert welcher unter "orderReference steht, wird in die Variable order_number geschrieben

        first_name = order_data["shippingAddress"][
            "firstName"]  # hier wird auf den Wert zugegriffen welcher unter dem Pfad shippingAddress->firstName erreichbar ist
        last_name = order_data["shippingAddress"]["lastName"]

        for order_item in order_data['orderItems']:  # for-schleife welche alle Elemente einer Liste durchläuft. In jedem Durchlauf wird das aktuelle Element in die Variable order_item geschrieben
            print(order_item['name'])  # Ausgabe des Artikelnamens
