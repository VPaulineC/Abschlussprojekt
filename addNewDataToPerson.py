#------------------------------------------------------------ NEUE DATENSÄTZE HINZUFÜGEN ------------------------------------------------------------
import streamlit as st
import json
import os
from datetime import datetime

# Funktion zum Laden der JSON-Daten
def load_data():
    with open('data/person_db.json', 'r') as file:
        return json.load(file)

# Funktion zum Speichern der JSON-Daten
def save_data(data):
    with open('data/person_db.json', 'w') as file:
        json.dump(data, file, indent=4)

# Streamlit App
def add_ekg_data():
    st.title("Weitere EKG-Daten hinzufügen")

    # Laden der vorhandenen Daten
    data = load_data()

    # Dropdown zur Auswahl der Person
    selected_person = st.selectbox("Person auswählen", options=[f"{person['firstname']} {person['lastname']}" for person in data])

    # Suche die Person in den Daten
    person_id = None
    for person in data:
        if f"{person['firstname']} {person['lastname']}" == selected_person:
            person_id = person['id']
            break

    if person_id is None:
        st.error("Person nicht gefunden")
        return

    # EKG-Tests per Drag-and-Drop hochladen
    ekg_files = st.file_uploader("EKG-Tests hochladen", type=["txt", "fit"], accept_multiple_files=True)

    # Button zum Hinzufügen der neuen EKG-Daten
    if st.button("Neue EKG-Daten hinzufügen"):
        if ekg_files:
            # EKG-Tests speichern und Informationen sammeln
            for ekg_file in ekg_files:
                ekg_path = os.path.join("data/ekg_data", ekg_file.name)
                with open(ekg_path, "wb") as f:
                    f.write(ekg_file.getbuffer())

                if ekg_file.name.endswith(".txt"):
                    # txt-Datei verarbeiten (z.B. nur speichern)
                    new_ekg_test = {
                        "id": len(person['ekg_tests']) + 1,  # eine einfache ID für jeden EKG-Test
                        "date": datetime.now().strftime("%d.%m.%Y"),  # aktuelles Datum als Beispiel
                        "result_link": ekg_path
                    }
                    person['ekg_tests'].append(new_ekg_test)

                elif ekg_file.name.endswith(".fit"):
                    # fit-Datei verarbeiten
                    # Hier müsste die Verarbeitung der FIT-Datei entsprechend deiner Anforderungen erfolgen
                    # Beispiel: fit_data = read_heart_rate_from_fit(ekg_path)
                    # Annahme: FIT-Datei enthält bereits Datum und Result Link
                    new_ekg_test = {
                        "id": len(person['ekg_tests']) + 1,
                        "date": datetime.now().strftime("%d.%m.%Y"),
                        "result_link": ekg_path,
                        # Weitere Daten je nach Bedarf hinzufügen
                    }
                    person['ekg_tests'].append(new_ekg_test)

            # Daten speichern
            save_data(data)
            st.success("EKG-Daten wurden hinzugefügt!")
        else:
            st.error("Bitte eine Datei auswählen")

# Beispielverwendung
if __name__ == "__main__":
    add_ekg_data()
