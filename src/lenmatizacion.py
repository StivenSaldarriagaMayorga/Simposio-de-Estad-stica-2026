import nltk #Para la eliminación de las stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import spacy #Para la lenmatización
import pandas as pd

df =  pd.read_csv("data/raw/Entrevistas.csv", sep = ";")
print(df["NARRATIVA"].head())

def stopwords_delete(df, columna):
    
    df = df[[columna]].copy()

    def eliminar(texto):
        texto = word_tokenize(texto)
        stop_words = stopwords.words("spanish")
        tokenizados = []

        for word in texto:
            if word not in stop_words:
                tokenizados.append(word)
        return tokenizados
    
    df[columna] = df[columna].apply(eliminar)

    return df

df =  pd.read_csv("data/raw/Entrevistas.csv", sep = ";")
df_stop = stopwords_delete(df, "NARRATIVA")
print(df_stop["NARRATIVA"].head())
    

def lematizacion(df, columna):
    nlp = spacy.load("es_core_news_lg")

    df = df[[columna]].copy()

    def procesar_texto(texto):
        doc = nlp(texto)
        return " ".join([token.lemma_ for token in doc])

    df[columna] = df[columna].apply(procesar_texto)

    return df

df =  pd.read_csv("data/raw/Entrevistas.csv", sep = ";")
df_lenmatizado = lematizacion(df, "NARRATIVA")
print(df_lenmatizado["NARRATIVA"])