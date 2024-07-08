import streamlit as st
from login import check_login
from person_page import person_page
from add_data_page import add_new_data

def main():
    st.markdown("<h1 style='text-align: center; color: black;'>HeartBeatAnalyzer</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Ihr EKG Analyse Tool</h2>", unsafe_allow_html=True)
    

    # Sidebar
    st.sidebar.title("Navigation")
    st.sidebar.image("image/Logo_without_backround.png", width=150)
    options = ["Home", "Personen", "Informationen", "Datensätze Hinzufügen"]
    choice = st.sidebar.selectbox("Wähle eine Seite", options)



    if choice == "Home":
        home()
    elif choice == "Personen":
        chose_Person()
    elif choice == "Datensätze Hinzufügen":
        add_new_data()
    elif choice == "Informationen":
        read_information()


def home():
    #Image.open("image/Logo_without_backround.png")
    st.image("image/Logo_without_backround.png", use_column_width=True, caption="made by Voigtsberger and Tilg")

def chose_Person():
    ## creating login page
    def login_page():
        st.title("Login")
        # create input box for username and password
        username = st.text_input("Nutzername")
        password = st.text_input("Passwort", type="password")
        # Login-Button
        login_button = st.button("Login")
        # Initialize login attempt state
        if 'login_attempted' not in st.session_state:
            st.session_state['login_attempted'] = False
        # check login informtion
        if login_button:
            st.session_state['login_attempted'] = True
            if check_login(username, password):
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.experimental_rerun()
        # Show error message only if login was attempted and failed
        if st.session_state['login_attempted'] and not st.session_state['logged_in']:
            st.error("Login failed. Please check your username and password.")


    #check login state
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    #show person_page
    if st.session_state['logged_in']:
        person_page()
    else:
        login_page()

def read_information():
    st.title("Informationen")
    st.header("EKG")
    st.subheader("Was ist ein EKG?")
    st.write("EKG steht für Elektrokardiogramm und bezeichnet eine Untersuchungsmethode, bei der die elektrische Aktivität des Herzens gemessen wird. Die sogenannte Herzaktion wird dabei über Elektroden abgeleitet und in Form von Kurven aufgezeichnet. Anhand dieser kann man beurteilen, ob das Herz störungsfrei funktioniert.")
    st.subheader("Welche Arten von EKGs gibt es?")
    st.write("Das klassische EKG wird am liegenden, entspannten Patienten durchgeführt und deshalb als Ruhe-EKG bezeichnet. Im Gegensatz dazu steht das Belastungs-EKG: Hier erfolgt die EKG-Ableitung während körperlicher Anstrengung – der Patient bewegt sich auf einem Laufband oder einem Fahrrad. Beim Langzeit-EKG wird die elektrische Herzaktivität über einen längeren Zeitraum, meist 24 Stunden, aufgezeichnet.")
    st.write("Quelle: https://www.netdoktor.de/diagnostik/ekg/")

    st.header("Herzfrequenz/Herzrate und Herzratenvariabilität")
    st.subheader("Warum misst man die Herzfrequenz?")
    st.write("Die Herzfrequenz beschreibt die Anzahl der Herzschläge pro Minute und ist ein wichtiger Vitalparameter zur Beurteilung der Herzgesundheit. Ärzte verwenden sie, um Herzprobleme zu diagnostizieren. Die Herzfrequenz kann aus einem EKG abgelesen werden, während Laien den Puls am Handgelenk oder der Halsschlagader zählen können. Abweichungen können auf Gesundheitsprobleme hinweisen, z. B. ein plötzliches Herzrasen oder eine dauerhaft niedrige Herzfrequenz.")
    st.write("Quelle: https://www.bing.com/chat?form=NTPCHB")
    st.subheader("Was sind Ruhepuls, Maximalpuls und Erholungspuls?")
    st.write("Ruhepuls: Der Ruhepuls verrät, wie schnell das Herz im Ruhezustand schlägt und kann im Ruhe-EKG gemessen werden. Er ist von Mensch zu Mensch sehr unterschiedlich, kann aber einiges über das Fitnesslevel, die Regenerationsfähigkeit und den Gesundheitszustand aussagen eines Menschen. Der Ruhepuls kann von diversen Faktoren beeinflusst werden, etwa Stress, Wetter, körperliche Aktivität, Koffein, Hormone, Schwangerschaft, Tageszeit, etc. Der Ruhepuls ist auch ein Gradmesser für unseren Trainingsstand. Ein trainierter Athlet hat einen deutlich niedrigeren Ruhepuls als eine Person, die wenig Sport treibt — das gilt besonders für Ausdauersport. Da das Herz ein Muskel ist, wächst es wie alle anderen Muskeln auch durch regelmäßiges Training. Ein größeres Herz wiederum fasst mehr Blut und kann somit innerhalb eines Herzschlags mehr Blut ausstoßen. Das bedeutet, dass das Herz nicht so oft wie ein kleineres Herz schlagen muss, um die Gefäße mit Blut zu versorgen, daher der niedrigere Ruhepuls. m Allgemeinen kann man sagen: Untrainierte Athleten haben im Durchschnitt einen Ruhepuls von 60-80 Schlägen pro Minute, bei trainierten Athleten liegt er eher bei 40-50 Schlägen pro Minute und einige Profi-Ausdauersportler haben sogar einen Ruhepuls von 20-30.")
    st.write("Maximalpuls: Der Maximalpuls ist die Anzahl der Herzschläge pro Minute, die ein Mensch unter größtmöglicher körperlicher Anstrengung erreichen kann. Mit dem Maximalpuls kann man seine individuellen Herzfrequenzzonen je nach Trainingsintensität bestimmen. Diese wiederum können dann genutzt werden, um das Training in einem effektiven Bereich, je nach Ziel, zu absolvieren. Um den Maximalpuls zu bestimmen gibt es verschiedene Formeln, die jedoch nicht sehr genau sind. Zum Beispiel: Maximalpuls = 220 – Alter. Eine genauere Methode Um den Maximalpuls zu bestimmen gibt es verschiedene Formeln. Zum Beispiel: Maximalpuls = 220 – Alter. Eine genauere Methode wäre ein Leistungstest bei einem Sportwissenschaftler oder Arzt")
    st.write("Erholungspuls: Der Erholungspuls ist ein Gradmesser für die allgemeine sportliche Leistungsfähigkeit. Er gibt Auskunft darüber, wie schnell der Herzschlag nach körperlicher Belastung wieder in seinen Normalzustand zurückkehrt. Bei geringer Intensität gelangt der Puls z. B. wieder relativ schnell zurück in den Normalzustand, bei hoher Intensität dauert es dementsprechend länger. Dies wiederum hängt damit zusammen, wie gut der Körper mit einem Sauerstoffmangel zurechtkommt. Je fitter und trainierter ein Athlet ist, d. h. je größer seine aerobe Kapazität ist, desto schneller erholt er sich nach körperlicher Belastung.")
    st.write("Quelle: https://www.freeletics.com/de/blog/posts/herzfrequenzzonen/")
    st.subheader("Was ist die Herzfrequenzvariabilität?")
    st.write("Die Herzfrequenzvariabilität (HRV) beschreibt die zeitlichen Abstände zwischen den einzelnen Herzschlägen und wird durch das autonome Nervensystem reguliert. Eine höhere HRV ist ein Zeichen für ein gut funktionierendes, anpassungsfähiges Herz-Kreislauf-System und zeigt eine gute Balance zwischen Sympathikus (aktivierend) und Parasympathikus (entspannend). Faktoren wie Stress, Schlafmangel und Übertraining können die HRV negativ beeinflussen. Sportler nutzen die HRV-Messung, um den Trainingszustand und die Erholung zu überwachen und Übertraining zu vermeiden. Eine niedrige HRV kann auf Überlastung oder Erschöpfung hinweisen.")
    st.write("Quelle: https://www.runnersworld.de/training-basiswissen/was-ist-eigentlich-die-herzfrequenzvariabilitaet/")




if __name__ == "__main__":
    main()