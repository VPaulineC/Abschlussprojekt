import streamlit as st
import read_person_data
import ekgdata
import person
import numpy as np
import plotly.express as px
import json
import os
import matplotlib.pyplot as plt
import json
import os
import matplotlib.pyplot as plt
import read_fit_file
from PIL import Image
from datetime import datetime

def get_next_free_id_ekg(data):
        if not data:
            return 1
        return max(ekg_test['id'] for ekg_test in data) + 1

# Funktion zum Laden der JSON-Daten
def load_data():
    with open('data/person_db.json', 'r') as file:
        return json.load(file)

# Funktion zum Speichern der JSON-Daten
def save_data(data):
    with open('data/person_db.json', 'w') as file:
        json.dump(data, file, indent=4)

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
            st.write("Vorname: ", selected_person.firstname)
            st.write("Nachname: ", selected_person.lastname)
            st.write("Geburtsdatum: ", selected_person.date_of_birth)
            st.write("Alter: ", selected_person.age)
            st.write("Maximale Herzfrequenz: ", selected_person.max_heart_rate)

        with col1:
        # show the image
            image = Image.open(st.session_state.picture_path)
            st.image(image, caption=st.session_state.aktuelle_versuchsperson)

        #------------------------------------------------------------
        ekg_ids = [ekg["id"] for ekg in selected_person.ekg_data]
        # Show ekg in a list
        selected_id = st.selectbox("Wähle ein EKG aus: ", options= ekg_ids, key="sbEKG")

        result_link = selected_person.ekg_data[0]["result_link"]
        
        if result_link.endswith(".fit"):
            st.write("FIT-Datei ist hier irgendwo...")
            fit_df = read_fit_file.read_heart_rate_from_fit(result_link)
            fig = read_fit_file.plot_fit_file(fit_df, result_link)
            st.plotly_chart(fig)

        if result_link.endswith(".txt"):
            
            # EKG Plot und HR Plot
            ekg_dict = ekgdata.EKGdata.load_by_id(selected_id)
                
            #ekg_dict = EKGdata.load_by_id(id_from_selectionbox)
            ekg_data = ekgdata.EKGdata(ekg_dict)
        
            
            #Datum des EKGs anzeigen
            ekg_date = ekg_dict.get("date", "Datum nicht verfügbar")
            st.write("erstellt am:", ekg_date)
            
            #Dauer des EKGs anzeigen
            ekg_length = ekg_data.get_df()['Time in s'].iloc[-1]
            st.write("EKG-Dauer: ", round(ekg_length), "sek", "|", round(ekg_length/60), "min")
            #------------------------------------------------------------  
            #Dataframe aufrufen
            df = ekg_data.get_df()
            #peaks aufrufen
            peaks = ekgdata.EKGdata.find_peaks(df['EKG in mV'], 340, 5)
            # min_time und max_time für Slider festlegen
            min_time = 0.0
            max_time = df['Time in s'].iloc[-1]
            default_start_time = 30.0
            default_end_time = 60.0

            #slider für Zeitbereich erstellen
            start_time = st.slider("Startzeit", min_value=min_time, max_value=max_time, value=default_start_time)
            end_time = st.slider("Endzeit", min_value=min_time, max_value=max_time, value=default_end_time)


            # DataFrame basierend auf dem ausgewählten Zeitbereich filtern
            filtered_df = df[(df['Time in s'] >= start_time) & (df['Time in s'] <= end_time)]
            #Fehlermeldung, wenn Startzeit größer als Endzeit
            if start_time>end_time:
                st.error("Die Startzeit muss vor der Endzeit liegen.")
            # Plot des EKGs für den ausgewählten Zeitbereich
            fig = px.line(filtered_df, x='Time in s', y='EKG in mV', title='EKG Plot')
            st.plotly_chart(fig)

            if df['Time in s'].iloc[0] > 0:
                st.write("Die Aufzeichnung beginnt bei 0 Sekunden, aber die ersten Messdaten wurden erst nach einigen Sekunden erfasst. Beachten Sie dies bei ihrer Analyse.")
            
            #------------------------------------------------------------
            df_hr = ekgdata.EKGdata.estimate_hr(peaks, 1000)
            #print(df_hr.head())


            #------------------------------------------------------------
            show_heartrate = st.checkbox("Herzrate anzeigen")

            # Wenn die Checkbox aktiviert ist, wird die Grafik der Herzrate gezeigt
            if show_heartrate:
                fig = ekgdata.EKGdata.plot_hr(df_hr)
                #fig.show() 
                st.plotly_chart(fig)
            

            #------------------------------------------------------------
            # wenn Checkbox aktiviert ist, wird die durchschnittliche Herzfrequenz angezeigt
            show_hr = st.checkbox("Durchschnittliche Herzfrequenz anzeigen insgesamt")
            if show_hr:
                st.write("Durchsnitt HF:", np.round(df_hr["Heart Rate in bpm"].mean()), "bpm")
            
            #------------------------------------------------------------
            # checkbox für HRV 
            show_hrv = st.checkbox("Herzfrequenzvariabilität anzeigen")
            if show_hrv: 
            # Herzratenvaribalitität berechnen und anzeigen
                def calculate_hrv(peaks):
                    if len(peaks) < 2:
                        return None
                    
                    rr_intervals = np.diff(peaks) 

                    hrv = np.std(rr_intervals)
                    return hrv
                st.write("Herzratenvariabilität: ", np.round(calculate_hrv(peaks)), "ms")

                    # rolling window für Herzfrequenz
            show_rolling_heartrate = st.checkbox("Herzrate als gleitender Durchschnitt anzeigen")
            # Wenn die Checkbox aktiviert ist, wird die Grafik der Herzrate gezeigt (im rolling window)
            if show_rolling_heartrate: 
                def calculate_rolling_window(df, window_size):
                    df['Rolling Mean HR in bpm'] = df['Heart Rate in bpm'].rolling(window=window_size).mean()
                    return df

                def plot_rolling_mean(df):
                    fig = px.line(df, x='Time in s', y='Rolling Mean HR in bpm',
                                title='Herzrate als gleitender Durchschnitt',
                                labels={'Rolling Mean HR in bpm': 'Rolling Mean HR in bpm', 'Time in s': 'Time in seconds'})
                    st.plotly_chart(fig)

                def filter_by_time_window(df, start_time, end_time):
                    return df[(df['Time in s'] >= start_time) & (df['Time in s'] <= end_time)]

                # slider für Größe des rolling window
                window_size = st.slider('Größe des angezeigten Fensters', min_value=1, max_value=10, value=3)

                # rolling window berechnen
                df_hr = calculate_rolling_window(df_hr, window_size)

                # sliders für Zeit des rolling in window
                #start_time = st.slider('Startzeit', min_value=float(df_hr['Time in s'].min()), max_value=float(df_hr['Time in s'].max()), value=float(df_hr['Time in s'].min()))
                start_time = st.slider('Startzeit', min_value=0.0, max_value=float(df_hr['Time in s'].max()), value=30.0)
                end_time = st.slider('Endzeit', min_value=0.0, max_value=float(df_hr['Time in s'].max()), value=60.0)

                if start_time < end_time:
                    df_filtered = filter_by_time_window(df_hr, start_time, end_time)
                    # Plot des rolling window
                    plot_rolling_mean(df_filtered)
                    st.write("Durchschnittliche Herzrate im angezeigten Bereich: ", np.round(df_filtered['Heart Rate in bpm'].mean()), "bpm")
                else:
                    st.error("Die Startzeit muss vor der Endzeit liegen.")

        #------------------------------------------------------------

        # weiteren Datensatz hinzufügen
        # Hole die aktuelle ausgewählte Person aus dem Session State
        '''data = load_data()
     
        # Button zum Hinzufügen von neuen Datensätzen
        ekg_files = st.file_uploader("Neuen Datensatz hochladen", type=["txt", "fit"], accept_multiple_files=True)
        if st.button("Neuen Datensatz hinzufügen"):
            
        
            # EKG-Tests speichern und Informationen sammeln
            
            for ekg_file in ekg_files:
                ekg_path = os.path.join("data/ekg_data", ekg_file.name)
                with open(ekg_path, "wb") as f:
                    f.write(ekg_file.getbuffer())


            new_test = {
                'id': get_next_free_id_ekg(data),
                'date': datetime.now().strftime("%d.%m.%Y"),
                'result_link': ekg_path
            }
            # Zur JSON-Datei hinzufügen
            data.append(new_test)
            save_data(data)
            st.success("Datensatz wurde hinzugefügt!")'''
    
        data=load_data()
        def add_ekg_test(person_id, new_test, data):
            for person in data:
                if person['id'] == person_id:
                    person['ekg_tests'].append(new_test)
                    return person
            return None

        person_id = st.selectbox("Wähle eine Person aus:", [person['id'] for person in data])
        uploaded_file = st.file_uploader("Lade eine neue EKG Test Datei hoch", type=["txt", "fit"])

        if st.button("Neuen EKG-Test hinzufügen"):
            if uploaded_file is not None:
                # Speicherort für hochgeladene Datei
                save_dir = "data/ekg_data"
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)

                file_path = os.path.join(save_dir, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                # Neuen EKG-Test Eintrag erstellen
                new_test_entry = {
                    "id": max(test['id'] for test in person_dict['ekg_tests']) + 1,
                    "date": datetime.now().strftime("%d.%m.%Y"),
                    "result_link": file_path
                }

                # Neuen Eintrag hinzufügen
                updated_person = add_ekg_test(person_id, new_test_entry, data)

                if updated_person:
                    st.success(f"Neuer EKG-Test Eintrag hinzugefügt für {updated_person['firstname']} {updated_person['lastname']}")
                    # Aktualisierte Daten speichern
                    save_data( data)
                    
                else:
                    st.error("Person mit dieser ID wurde nicht gefunden.")




    






        
        



'''To-dos:
        - zusätzlichen Datensatz bei Person hinzufügen
        - Deployment auf Heroku oder Streamlit Share
        - Daten aus einer anderen Datenquelle einlesen
      '''