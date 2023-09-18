import streamlit as st
from Send_Email import send_email

st.header("Contacto 📧")

with st.form(key="email_form",clear_on_submit=True):
    user_email = st.text_input(label="email")
    text_box = st.text_area(label="Escribí tu mensaje aquí")
    button = st.form_submit_button("Enviar")
    if button:
        send_email(user_email,text_box)