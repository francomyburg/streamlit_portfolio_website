import streamlit as st

st.header("Contacto 📧")

with st.form(key="email_form"):
    user_email = st.text_input(label="email")
    text_box = st.text_area(label="Escribí tu mensaje aquí")
    button = st.form_submit_button()