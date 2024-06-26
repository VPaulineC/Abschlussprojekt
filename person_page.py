import streamlit as st
import read_person_data
import ekgdata
import person
from PIL import Image
import numpy as np
import datetime

def person_page():
    st.title("Personen")
    

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
    st.session_state.aktuelle_versuchsperson = st.selectbox('Wähle eine Person', options = ["Auswählen"] + person_names, key="sbVersuchsperson")

    #-------------
    if st.session_state.aktuelle_versuchsperson in person_names:
        person_dict = read_person_data.find_person_data_by_name(st.session_state.aktuelle_versuchsperson)
        selected_person = person.Person(person_dict)
        st.session_state.picture_path = selected_person.picture_path

        col1, col2 = st.columns([1, 1])

        with col2:
        # show the person Data
            st.header("Personendaten:")
            #st.write("ID: ", selected_person.id)
            st.write("Vorname: ", selected_person.firstname)
            st.write("Nachname: ", selected_person.lastname)
            st.write("Geburtsdatum: ", selected_person.date_of_birth)
            st.write("Alter: ", selected_person.age)
            st.write("Maximale Herzfrequenz: ", selected_person.max_heart_rate)
            #st.write("EKG-Daten: ", selected_person.ekg_data)

        with col1:
        # show the image
            image = Image.open(st.session_state.picture_path)
            st.image(image, caption=st.session_state.aktuelle_versuchsperson)

        #------------------------------------------------------------
        ekg_ids = [ekg["id"] for ekg in selected_person.ekg_data]
        # Show ekg in a list
        selected_id = st.selectbox("choose EKG: ", options= ekg_ids, key="sbEKG")
    
        # EKG Plot und HR Plot
        ekg_dict = ekgdata.EKGdata.load_by_id(selected_id)
        #ekg_dict = EKGdata.load_by_id(id_from_selectionbox)
        ekg_data = ekgdata.EKGdata(ekg_dict)
        #Datum des EKGs anzeigen
        ekg_date = ekg_dict.get("date", "Datum nicht verfügbar")
        st.write(f"erstellt am: {ekg_date}")
        #Dauer des EKGs anzeigen

        #------------------------------------------------------------  
        df = ekg_data.get_df()
        #print(df.head())
        peaks = ekgdata.EKGdata.find_peaks(df['EKG in mV'], 340, 5)
        #------------------------------------------------------------
        fig = ekgdata.EKGdata.plot_ekg(df, peaks)
        #fig.show()
        st.plotly_chart(fig)
        #------------------------------------------------------------
        df_hr = ekgdata.EKGdata.estimate_hr(peaks, 1000)
        #print(df_hr.head())
        
        #------------------------------------------------------------
        show_heartrate = st.checkbox("Herzrate anzeigen")

        # Wenn die Checkbox aktiviert ist, wird die Grafik der Herzratengezeigt
        if show_heartrate:
            fig = ekgdata.EKGdata.plot_hr(df_hr)
            #fig.show() 
            st.plotly_chart(fig)
        #------------------------------------------------------------
        # wenn Checkbox aktiviert ist, wird die durchschnittliche Herzfrequenz angezeigt
        show_hr = st.checkbox("Durchschnittliche Herzfrequenz anzeigen")
        if show_hr:
            st.write("Durchsnitt HF:", np.round(df_hr["Heart Rate in bpm"].mean()))
        
        #------------------------------------------------------------
        '''To-dos:
        - EKG-Dauer anzeigen
        - Nutzer kann Zeitbereich für Plots auswählen (Slider)
        - Deployment auf Heroku oder Streamlit Share
        - neue Person anlegen mit Profilbild
        - neuen Datensatz anlegen mittels Drag and Drop
        - Daten aus einer anderen Datenquelle einlesen
        - Herzrate im sinnvollen gleitenden Durchschnitt als Plot anzeigen
        - Herzratenvariabilität anzeigen
        - Informationsseite anlegen mit Informationen über EKG, Herzvariabilität, … (über Navigation zugreifbar)
        -Über Link (z.B. wenn man auf EKG klickt) auf Informationsseite gelangen'''