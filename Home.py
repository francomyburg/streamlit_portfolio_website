import streamlit as st
import pandas as pd
#informacion de proyectos en csv
data_pro = pd.read_csv("data.csv",delimiter=";")


st.set_page_config(layout="wide")

col1,col2 = st.columns(spec=[0.6,0.4])

with col1:
    st.image("images/profile.png",width=400)
with col2:
    st.title("Franco Jonas Myburg Terragno")
    cuerpo = """¡Bienvenidos a mi Portfolio!

Aquí encontrarás un acceso directo a mi apasionante viaje como aspirante a Python Developer, Data Engineer y Data Analyst. Este sitio web es mucho más que un simple portfolio; es un reflejo de mi dedicación a la tecnología  y al análisis de datos.
Aquí iré subiendo mis proyectos de GitHub. Desde scripts y aplicaciones hasta análisis de datos en profundidad, cada proyecto es un testimonio de mi crecimiento y evolución como profesional.
Este sitio es un espacio interactivo. Si tienes alguna pregunta, sugerencia o simplemente quieres entablar una conversación sobre cualquier proyecto, no dudes en ponerte en contacto conmigo. Estoy aquí para aprender, crecer y colaborar.

Gracias por visitar mi sitio web.
Franco Myburg
"""
    st.info(cuerpo)

st.write("lista de apps creadas con python 🐍🐍 :  ")

#Columnas con los proyectos
col3,col4 = st.columns(2,gap="medium")

with col3:
    for index,row in data_pro.iterrows():
        if index % 2 ==0:
            st.header(row["title"])
            st.image("images/"+row["image"])
            st.write(row["description"])
            st.text("Source code: "+ row["url"])

with col4:
    for index,row in data_pro.iterrows():
        if index % 2 !=0:
            st.header(row["title"])
            st.image("images/"+row["image"])
            st.write(row["description"])
            st.write("Source code: "+ row["url"])
            
