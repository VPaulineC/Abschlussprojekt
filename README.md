# Abschlussprojekt (HeartBeatAnalyser)
## Funktion
Diese App, ist eine Benutzeroberfläche zur Visualisierung und Analyse von Datensätzen wie EKG Aufzeichnungen und FIT-Files mehrerer Personen, die in einer JSON-Datenbank gespeichert sind. 
Der Benutzer der APP kann Person aus einer Liste auswählen, die aus der JSON-Datenbank geladen werden. Es werden dann grundlegende Informationen über die ausgewählte Person angezeigt, einschließlich ihres Profilbildes, falls eines vorhanden ist.
Falls mehrere Datensätze bei einer Person vorhanden sind, kann ausgewählt werden, welcher angezeigt werden soll.
Für .fit-Dateien werden Herzfrequenzdaten aus der FIT-Datei gelesen und visualisiert.
Für .txt-Dateien werden verschiedene Informationen zum EKG angezeigt: EKG-Dauer, Peaks und ein interaktiver Plot des EKG-Signals basierend auf dem ausgewählten Zeitbereich vom Benutzer.
Außerdem wird die Herzfrequenz, die Herzratenvariabilität und der Durchschnitt über die Zeit angezeigt oder visualisiert.  

zur App gelangen (streamlit share): https://abschlussprojekt-n7hgm5ryhyfnwhvgh2fsnn.streamlit.app/

Die Basis-Aufgaben wurden alle bearbeitet. Folge zusätzlichen Aufgaben wurden in die App implementiert:
- login feld 
- neue Person anlegen mit Profilbild  -> Drag and Drop
- neue Person anlegen mit Datensatz -> Drag and Drop
- Datensätze zu bereits erstellten Personen hinzufügen -> Drag and Drop
- Daten aus einer anderen Datenquelle einlesen (.fit-Datei) 
    -> den Personen dürfen nur entweder .txt oder .fit Datensätze zugewiesen werden, nicht beides. Ansonsten neue/zweite Person erstellen
- neue Datensätze mit Personen verknüpfen
- Herzrate in sinnvoll gleitenden Durchschnitt als Plot (rolling window)
- Herzratenvariabilität anzeigen
- Informationsseite mit Informationen über EKG und Herzrate 

Information: wird eine neue Person erstellt erscheint folgende Fehlermeldung:ParserError: Error tokenizing data. C error: Expected 2 fields in line 2, saw 3
Doch sobald eine zweite Person neu erstellt wird, funktioniert alles einwandfrei

Login Daten:

Nutzername: jasper.v

Passwort: LaufinZone5

![Screenshot](image/sticker.jpg)