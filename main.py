import streamlit as st
from login import check_login
from person_page import person_page

def main():
    st.markdown("<h1 style='text-align: center; color: black;'>HeartBeatAnalyzer</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Ihr EKG Analyse Tool</h2>", unsafe_allow_html=True)
    

    # Sidebar
    st.sidebar.title("Navigation")
    st.sidebar.image("image/Logo_without_backround.png", width=150)
    options = ["Home", "Personen", "Informationen"]
    choice = st.sidebar.selectbox("Wähle eine Seite", options)

    if choice == "Home":
        home()
    elif choice == "Personen":
        chose_Person()
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
    st.write("Enter some text below:")
    user_input = st.text_input("Your text here:")
    if user_input:
        st.write("You entered:", user_input)

if __name__ == "__main__":
    main()