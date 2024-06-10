import streamlit as st
from PIL import Image

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
    elif choice == "Upload Image":
        upload_image()
    elif choice == "Text Input":
        text_input()

def home():
    #Image.open("image/Logo_without_backround.png")
    st.image("image/Logo_without_backround.png", use_column_width=True, caption="made by Voigtsberger and Tilg")

def upload_image():
    st.write("Upload an image below:")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

def text_input():
    st.write("Enter some text below:")
    user_input = st.text_input("Your text here:")
    if user_input:
        st.write("You entered:", user_input)

if __name__ == "__main__":
    main()