import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Empleados')

sidebar = st.sidebar
sidebar.title("Menu:")

DATA_URL = ('/content/Employees.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, encoding_errors='ignore')
    return data

data = load_data(500)

mostrardatos = sidebar.checkbox("Mostrar todos los datos? ",key ="Dataframe")
if mostrardatos:
  data = load_data(500)
  st.text('Todos los datos:')
  st.dataframe(data)

@st.cache
def load_data_byID(id):
  filtered_data_byID = data[data['Employee_ID'].str.contains(id)]
  return filtered_data_byID

@st.cache
def load_data_byHometown(hometown):
  filtered_data_byHome = data[data['Hometown'].str.contains(hometown)]
  return filtered_data_byHome

@st.cache
def load_data_byUnit(unit):
  filtered_data_byUnit = data[data['Unit'].str.contains(unit)]
  return filtered_data_byUnit

IDciudad = sidebar.text_input('Ingrese el id o ciudad o el trabajo: ')
FiltrarID = sidebar.button('Buscar por ID')
FiltrarCiudad = sidebar.button('Buscar por Ciudad natal')
FiltrarTrabajo = sidebar.button('Buscar por Trabajo')

if (FiltrarID):
  st.write ("ID buscado: " + IDciudad)
  filterbyID = load_data_byID(IDciudad)
  count_row = filterbyID.shape[0]
  st.write(f'Total: {count_row}')
  st.dataframe(filterbyID)

if (FiltrarCiudad):
  st.write ("Ciudad buscada: " + IDciudad)
  filterbyHome = load_data_byHometown(IDciudad)
  count_row = filterbyHome.shape[0]
  st.write(f'Total: {count_row}')
  st.dataframe(filterbyHome)

if (FiltrarTrabajo):
  st.write ("Trabajo buscado: "+ IDciudad)
  filterbyUnit = load_data_byUnit(IDciudad)
  count_row = filterbyUnit.shape[0]
  st.write(f'Total: {count_row}')
  st.dataframe(filterbyUnit)

@st.cache
def load_data_bynivel(level):
  filtered_data_byLevel = data[data['Education_Level'] == level]
  return filtered_data_byLevel

EducationLevel = sidebar.selectbox("Selecciona el Nivel educativo", data['Education_Level'].unique())
NivelEDU = sidebar.button('Filtrar por Nivel educativo')

if (NivelEDU): 
  st.write("Empleados con nivel educativo "+ str(EducationLevel))
  filterbylevel = load_data_bynivel(EducationLevel)
  count_row = filterbylevel.shape[0]
  st.write(f'Total: {count_row}')
  st.dataframe(filterbylevel)

@st.cache
def load_data_byhome(home):
  filtered_data_byHome = data[data['Hometown'] == home]
  return filtered_data_byHome

CiudadNatal = sidebar.selectbox("Selecciona la ciudad natal", data['Hometown'].unique())
Ciudad = sidebar.button('Filtrar por Ciudad')

if (Ciudad): 
  st.write("Empleados con Ciudad natal "+ str(CiudadNatal))
  filterbyHome = load_data_byhome(CiudadNatal)
  count_row = filterbyHome.shape[0]
  st.write(f'Total: {count_row}')
  st.dataframe(filterbyHome)

SelectTrabajo = sidebar.selectbox("Selecciona el trabajo", data['Unit'].unique())
Trabajo = sidebar.button('Filtrar por Trabajo')

if (Trabajo): 
  st.write("Empleados con el trabajo "+ str(SelectTrabajo))
  filterbyUnit = load_data_byUnit(SelectTrabajo)
  count_row = filterbyUnit.shape[0]
  st.write(f'Total: {count_row}')
  st.dataframe(filterbyUnit)

Edades = sidebar.checkbox("Histograma de edades ",key = "edades")

if Edades:
  fig, ax = plt.subplots()
  ax.hist(data['Age'])
  ax.set_xlabel("Edad")
  ax.set_ylabel("Numero de empleados")
  st.header("Histograma de empleados por edad")
  st.pyplot(fig)

Frec = sidebar.checkbox("Frecuencia por trabajo ",key = "frecuencia")

if Frec:
  fig, ax = plt.subplots()
  ax.hist(data['Unit'])
  ax.set_xlabel("Trabajo")
  ax.set_ylabel("Numero de empleados")
  st.header("Frecuencia de Empleados por Trabajo ")
  plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
  st.pyplot(fig)

Descercion = sidebar.checkbox("Indice de deserción por ciudad ",key = "desercion")

if Descercion:
  fig, ax = plt.subplots()
  y_pos = data['Attrition_rate']
  x_pos = data['Hometown']
  ax.bar(x_pos, y_pos)
  ax.set_ylabel("Desercion")
  ax.set_xlabel("Ciudad natal")
  ax.set_title('empleados que desertaron por ciudad')
  st.header("Indice de deserción por ciudad")
  st.pyplot(fig)

DescercionEdadDes = sidebar.checkbox("Indice de deserción por edad ", key = "desEdad")

if DescercionEdadDes:
  fig, ax = plt.subplots()
  y_pos = data['Attrition_rate']
  x_pos = data['Age']
  ax.barh(x_pos, y_pos)
  ax.set_xlabel("Desercion")
  ax.set_ylabel("Edad")
  ax.set_title('empleados que desertaron por edad')
  st.header("Indice de deserción por edad")
  st.pyplot(fig)

DescercionTime = sidebar.checkbox("Indice de deserción por Tiempo de servicio ",key = "service")

if DescercionTime:
  fig, ax = plt.subplots()
  y_pos = data['Attrition_rate']
  x_pos = data['Time_of_service']
  ax.bar(x_pos, y_pos)
  ax.set_ylabel("Desercion")
  ax.set_xlabel("Tiempo de servicio")
  ax.set_title('¿Cuantos empleados desertaron por tiempo de servicio?')
  st.header("Indice de deserción por tiempo de servicio")
  st.pyplot(fig)
