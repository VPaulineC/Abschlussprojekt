import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd
import plotly.express as px

def add_new_data():
    '''Funktion zum Hinzufügen neuer Personendaten.'''
    # Funktion zum Laden der JSON-Daten
    def load_data():
        '''Lädt die JSON-Daten aus der Datei person_db.json und gibt sie zurück.'''
        with open('data/person_db.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    # Funktion zum Speichern der JSON-Daten
    def save_data(data):
        '''Speichert die JSON-Daten in der Datei person_db.json.'''
        with open('data/person_db.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    # Funktion zur Ermittlung der nächsten ID
    def get_next_free_id(data):
        if not data:
            return 1
        return max(person['id'] for person in data) + 1
    
    def get_next_free_id_ekg(data):
        '''Ermittelt die nächste freie ID für einen EKG-Test.'''
        if not data:
            return 1
        return max(ekg_test['id'] for ekg_test in data) + 1

    # JSON-Daten laden
    data = load_data()

    # Streamlit App
    st.title("Neue Person hinzufügen")

    # Eingabefelder für die Personendaten
    id = get_next_free_id(data)
    date_of_birth = st.number_input("Geburtsjahr", min_value=1900, max_value=datetime.now().year, step=1)
    firstname = st.text_input("Vorname")
    lastname = st.text_input("Nachname")
    # Bild per Drag-and-Drop hochladen
    picture = st.file_uploader("Bild hochladen", type=["jpg", "jpeg", "png"])
    # EKG-Tests per Drag-and-Drop hochladen
    ekg_files = st.file_uploader("EKG-Tests hochladen", type=["txt", "fit"], accept_multiple_files=True)

    # Button zum Hinzufügen der neuen Person

    if st.button("Neue Person hinzufügen"):
        if id and date_of_birth and firstname and lastname and picture and ekg_files:
            # Bild speichern
            picture_dir = os.path.join("data", "pictures")
            picture_path = os.path.join(picture_dir, picture.name)
            with open(picture_path, "wb") as f:
                f.write(picture.getbuffer())

            # EKG-Tests speichern und Informationen sammeln
            ekg_tests = []
            for ekg_file in ekg_files:
                ekg_dir = os.path.join("data","ekg_data")
                ekg_path = os.path.join(ekg_dir, ekg_file.name)
                with open(ekg_path, "wb") as f:
                    f.write(ekg_file.getbuffer())
 

                # Unterscheidung zwischen txt- und fit-Dateien
                if ekg_file.name.endswith(".txt"):
                    # txt-Datei verarbeiten 
                    ekg_tests.append({
                        "id": get_next_free_id_ekg(data),  # eine einfache ID für jeden EKG-Test
                        "date": datetime.now().strftime("%d.%m.%Y"),  # aktuelles Datum als Beispiel
                        "result_link": ekg_path
                    })
                elif ekg_file.name.endswith(".fit"):
                    # fit-Datei verarbeiten
                    ekg_tests.append({
                        "id": get_next_free_id_ekg(data),  # eine einfache ID für jeden EKG-Test
                        "date": datetime.now().strftime("%d.%m.%Y"),  # aktuelles Datum als Beispiel
                        "result_link": ekg_path,
                    })
                    

            # Neue Person erstellen
            new_person = {
                "id": id,
                "date_of_birth": date_of_birth,
                "firstname": firstname,
                "lastname": lastname,
                "picture_path": picture_path,
                "ekg_tests": ekg_tests
            }

            # Zur JSON-Datei hinzufügen
            data.append(new_person)
            save_data(data)
            st.success("Person wurde hinzugefügt!")
        else:
            st.error("Bitte alle Felder ausfüllen!")

if __name__ == "__main__":
    add_new_data()
