import streamlit as st
import read_person_data
import ekgdata
import person
from PIL import Image
import numpy as np


def person_page():
    st.title("Person Page")
    st.write("Willkommen, {}!".format(st.session_state['username']))

    # Anlegen diverser Session States
    if 'aktuelle_versuchsperson' not in st.session_state:
        st.session_state.aktuelle_versuchsperson = None
    ## Anlegen des Session State. Bild, wenn es kein Bild gibt
    if 'picture_path' not in st.session_state:
        st.session_state.picture_path = None
    #------------------------------------------------
    if 'ekg_data_path' not in st.session_state:
        st.session_state.ekg_data_path = None


    # Lade alle Personen
    person_names = read_person_data.get_person_list(read_person_data.load_person_data())
    # Auswahlbox, wenn Personen anzulegen sind
    st.session_state.aktuelle_versuchsperson = st.selectbox('choose a person', options = ["choose"] + person_names, key="sbVersuchsperson")
    

    #-------------
    if st.session_state.aktuelle_versuchsperson in person_names:
        person_dict = read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)
        selected_person = person.Person(person_dict)
        st.session_state.picture_path = selected_person.picture_path

        # Weitere Daten wie Geburtsdatum etc. schön anzeigen
        st.header("Personendaten:")
        st.write("ID: ", selected_person.id)
        st.write("Vorname: ", selected_person.firstname)
        st.write("Nachname: ", selected_person.lastname)
        st.write("Geburtsdatum: ", selected_person.date_of_birth)
        st.write("Alter: ", selected_person.age)
        st.write("Maximale Herzfrequenz: ", selected_person.max_heart_rate)
        st.write("EKG-Daten: ", selected_person.ekg_data)