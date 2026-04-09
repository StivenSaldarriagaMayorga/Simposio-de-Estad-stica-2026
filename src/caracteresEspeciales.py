import pandas as pd

def limpiar_texto(df, columna):
    #df = df[[columna]].copy()

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
    
    df[columna] = df[columna].apply(quitar_tildes)

    df[columna] = (
        df[columna]
        .str.lower()
        .str.replace(r"[^a-z0-9\s]", "", regex=True)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
    )
    
    return df

#Validación 
df = pd.read_csv("data/raw/entrevistas.csv", sep=";")
df_limpio = limpiar_texto(df,'NARRATIVA')
print(df_limpio.head())
