if __name__ == '__main__':
    with open(
            'data/auftrag_onlineshop.json',
            'r'
    ) as file:  # öffnet die als erstes Argument angegebene Datei im Lese-Modus ("r")
        content = file.read()  # schreibt den Inhalt der Datei in die Variable "content"

        print(content)  # gibt den Inhalt der Variable "content" auf der Konsole aus
