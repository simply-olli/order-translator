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

        sku_sum = {} # wir legen uns ein neues Dict an, in welches wir die SKUs mit ihrer Bestellmenge speichern
        for order_item in order_data['orderItems']:  # for-schleife welche alle Elemente einer Liste durchläuft. In jedem Durchlauf wird das aktuelle Element in die Variable order_item geschrieben
            if order_item['sku'] not in sku_sum.keys(): # hier prüfen wir, ob die SKU schon in unserem Dict vorkommt
                sku_sum[order_item['sku']] = 1 # falls die SKU noch nicht vorkommt ist der Startwert 1
            else:
                sku_sum[order_item['sku']] = sku_sum[order_item['sku']] + 1 # ist die SKU bereits im Dict geführt, addieren wir 1 zum aktuellen Wert

        items = [] # eine neue Liste wird angelegt. In diese wollen wir die Items in der gewünschten Struktur hinterlegen
        for sku, sum in sku_sum.items(): # wir durchlaufen das oben angelegte Dict (jedes Element durch .items()). Dabei wird der linke Wert (key) jedes Elements in die Variable sku geschrieben. Der Rechte Wert (value) jedes Elements in die Variable sum
            items.append( # fügt ein neues Element unsere Liste hinzu
                {
                    'gtin': sku, # die SKU soll als gtin übertragen
                    'quantity': sum #die sum soll als Quantity übertragen werden
                }
            )

        # in den nächsten Zeilen werden die Werte in die von der Logistik geforderte Struktur gebracht
        request_payload = {
            "customerCity": order_data['shippingAddress']['city'],
            "pickingDateFrom": "2022-07-22", # wird im nächsten Schritt bearbeitet
            "pickingDateTo": "2022-07-22", # wird im nächsten Schritt bearbeitet
            "customerCountryCode": order_data['shippingAddress']['countryCode'],
            "customerZipCode": order_data['shippingAddress']['zipCode'],
            "orderNo": order_data['orderReference'],
            "customerStreet": order_data['shippingAddress']['address1'] + ' ' + order_data['shippingAddress']['address2'],
            "customerName": order_data["shippingAddress"]["firstName"] + ' ' + order_data["shippingAddress"]["lastName"],
            "packingCategory": "b2c",
            "items": items,
            "orderDate": "2022-07-22", # wird im nächsten Schritt bearbeitet
            "customerNo": order_data['customerReference']
        }

        print(request_payload)

