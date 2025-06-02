# La libreria stremlit permitira ver los graficos como en una página web
# >pip install streamlit
# Para ejecutar el script de streamlit, guardarlo en un archivo .py y ejecutar el siguiente comando en la terminal:
# streamlit run nombre_del_archivo.py
# Para ver el resultado en la web, abrir el navegador y escribir la dirección http://localhost:8501

import streamlit as st

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Datos originales
datos  = {
    'Comercial': ['Pedro', 'Ana', 'Marta', 'Carlos', 'Sonia'] * 10,
    'Importe': np.random.randint(100, 1200, size=50)
}

# Creamos el DataFrame original
df = pd.DataFrame(datos)
#Aplicamos un incremento del 15% al Importe
df['Importe'] = df['Importe'] * 1.15
#Agrupar + crear DAtaFrame
df2 = df.groupby(['Comercial']).Importe.sum()  # Agrupamos por mes y comercial y sumamos los importes
df2 = pd.DataFrame(df2).reset_index()
# Configuramos el estilo de los gráficos
#Titulo del Streamlite
st.title('Análisis de Importes por Comercial')  # Título del Streamlit
st.subheader("Datos")  # Subtítulo para la sección de datos
st.dataframe(df2)  # Mostramos el DataFrame en Streamlit
# Barplot
st.subheader("Gráfico de columnas de Importe por Comercial")     # Subtítulo para el gráfico de barras
fig1, ax1 = plt.subplots()
sns.barplot(data=df2, x='Comercial', y='Importe', ax=ax1)
ax1.set_title('Importe por Comercial')  # Título del gráfico
st.pyplot(fig1)  # Mostramos el gráfico de barras en Streamlit

