#Librerias
import pandas as pd
import csv 

from caracteresEspeciales import limpiar_texto, quitar_tildes
from lexico import limpiar_dataframe, diccionario
from preprocesamiento import contar_palabras

#Leer las bases de datos 
df_entrevistas = pd.read_csv("data/raw/entrevistas.csv", sep=";")
#df_limpio = limpiar_texto(df,'NARRATIVA')
df_jerga = pd.read_csv("data/lexico/jerga.csv", sep=";")
#df_limpio = limpiar_dataframe(df)


     

