import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración general
st.set_page_config(page_title="Dashboard Psicológico", layout="wide")
st.title("📊 Dashboard Psicológico por Género")
st.markdown("Este panel muestra gráficas divididas por género sobre variables psicológicas y hábitos.")

# Carga de datos
uploaded_file = st.file_uploader("Carga tu archivo CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Diccionarios para decodificar variables
    genero_dict = {1: 'Hombre', 2: 'Mujer'}
    fumador_dict = {0: 'No Fuma', 1: 'Fuma'}
    ansiedad_dict = {0: 'Nunca', 1: 'Diario o semanal', 2: 'Mensualmente o algunas veces'}
    depresion_dict = ansiedad_dict
    adaptacion_dict = {0: 'Sin dificultades', 1: 'Con dificultades'}

    # Mapeo de valores
    df['Genero'] = df['Genero'].map(genero_dict)
    df['Fumadores'] = df['Fumadores'].map(fumador_dict)
    df['Frecuencia de ansiedad'] = df['Frecuencia de ansiedad'].map(ansiedad_dict)
    df['Frecuencia de depresión'] = df['Frecuencia de depresión'].map(depresion_dict)
    df['Dificultades de adaptación'] = df['Dificultades de adaptación'].map(adaptacion_dict)

    # Descripción en la barra lateral
    with st.sidebar:
        st.header("📘 Descripciones de Variables")
        st.markdown("""
        - **Fumadores**: 0 = No Fuma; 1 = Fuma  
        - **Frecuencia de ansiedad**: 0 = Nunca; 1 = Diario o semanal; 2 = Mensualmente o algunas veces  
        - **Frecuencia de depresión**: 0 = Nunca; 1 = Diario o semanal; 2 = Mensualmente o algunas veces  
        - **Dificultades de adaptación**: 0 = Sin dificultades; 1 = Con dificultades
        """)
        st.markdown("Selecciona la variable a analizar:")

        variable = st.radio(
            "Variable a visualizar:",
            ['Fumadores', 'Frecuencia de ansiedad', 'Frecuencia de depresión', 'Dificultades de adaptación']
        )

    # Función para graficar
    def graficar_variable(variable, titulo):
        plt.figure(figsize=(8,5))
        colores = ['#FFC0CB', '#FFB6C1', '#FF69B4', '#FF1493', '#DB7093']  # Tonos rosados

        ax = sns.countplot(data=df, x=variable, hue='Genero', palette=colores)
        plt.title(titulo, fontsize=16)
        plt.xlabel(variable)
        plt.ylabel("Frecuencia")
        plt.legend(title='Género')
        st.pyplot(plt.gcf())
        plt.clf()

    # Mostrar la gráfica seleccionada
    graficar_variable(variable, f"{variable} por Género")

else:
    st.warning("Por favor, sube un archivo CSV con las columnas especificadas.")
