import streamlit as st

def main():
    st.title("My Streamlit App")
    st.header("Welcome to my customized Streamlit app!")

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