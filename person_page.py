import streamlit as st

def person_page():
    st.title("Person Page")
    st.write("Willkommen, {}!".format(st.session_state['username']))