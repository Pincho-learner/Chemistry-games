import pandas as pd
import streamlit as st

st.title("Sistema de Puntajes - Chemistry Games")

# Cargar datos
try:
    df = pd.read_csv("data/puntajes.csv")
except:
    df = pd.DataFrame(columns=["Equipo", "Puntos"])

st.dataframe(df)

# Agregar puntos
equipo = st.text_input("Equipo")
puntos = st.number_input("Puntos", step=1)

if st.button("Agregar"):
    nuevo = pd.DataFrame([[equipo, puntos]], columns=df.columns)
    df = pd.concat([df, nuevo], ignore_index=True)
    df.to_csv("data/puntajes.csv", index=False)
    st.success("Puntaje agregado")