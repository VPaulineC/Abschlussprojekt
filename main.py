import streamlit as st

def main():
    st.title("HeartBeatAnalyzer")
    st.header("Your EKG analysis tool")
    st.write("made by Voigtsberger and Tilg")


    # Sidebar
    st.sidebar.title("Navigation")
    options = ["Home", "Upload Image", "Text Input"]
    choice = st.sidebar.selectbox("Select a page", options)

    if choice == "Home":
        home()
    elif choice == "Upload Image":
        upload_image()
    elif choice == "Text Input":
        text_input()

def home():
    st.write("This is the home page. Add your main content here.")
    st.image("image/Logo_without_backround.png", use_column_width=True)

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