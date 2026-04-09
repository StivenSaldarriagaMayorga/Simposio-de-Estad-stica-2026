import pandas as pd
import csv

#-----Organizar la base de datos de la jerga-----#
def limpiar_dataframe(df):
    df = df.copy()
    def quitar_tildes(texto):
        diccionario = {
            "á":"a",
            "é":"e",
            "í":"i",
            "ó":"o",
            "ú":"u"
        }
        for viejo, nuevo in diccionario.items():
            texto = texto.replace(viejo, nuevo)
        return texto
    
    for col in df.columns:
        if df[col].dtype == "object":  # solo columnas de texto
            df[col] = (
                df[col]
                .str.lower()    
                .str.replace(r"[^a-zñ0-9\s,]", "", regex=True)
                .str.replace(r"\s+", " ", regex=True)
                .str.strip()
            )
    return df

#Validación
df = pd.read_csv("data/lexico/jerga.csv", sep=";")
df_limpio = limpiar_dataframe(df)
print(df_limpio.head())


#---- Transforma un archivo csv a un diccionario----#
def diccionario(df):
    return df.to_dict(orient="records")

#Validación
df_diccionario = df_limpio
df_diccionario = diccionario(df_diccionario)
print(type(df_diccionario))


