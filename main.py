import streamlit as st
from login import check_credentials

def main():
    st.markdown("<h1 style='text-align: center; color: black;'>HeartBeatAnalyzer</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Your EKG analysis tool</h2>", unsafe_allow_html=True)
    

    # Sidebar
    st.sidebar.title("Navigation")
    st.sidebar.image("image/Logo_without_backround.png", width=150)
    options = ["Home", "Person", "Information"]
    choice = st.sidebar.selectbox("Select a page", options)

    if choice == "Home":
        home()
    elif choice == "Person":
        chose_Person()
    elif choice == "Information":
        read_information()

def home():
    #Image.open("image/Logo_without_backround.png")
    st.image("image/Logo_without_backround.png", use_column_width=True, caption="made by Voigtsberger and Tilg")

def chose_Person():
    ## creating login page
    st.title("Login Page")
    # create input box for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    # Login-Button
    login_button = st.button("Login")
    # check login informtion
    if login_button:
        if check_credentials(username, password):
            st.success("Login successful")
            # Hier kannst du die Logik für den erfolgreichen Login hinzufügen
            st.write("Willkommen, {}!".format(username))
        else:
            st.error("Login failed. Please check your username and password.")

def read_information():
    st.write("Enter some text below:")
    user_input = st.text_input("Your text here:")
    if user_input:
        st.write("You entered:", user_input)

if __name__ == "__main__":
    main()