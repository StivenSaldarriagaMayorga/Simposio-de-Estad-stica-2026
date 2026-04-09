import pandas as pd 
df = pd.read_csv("data/raw/entrevistas.csv", sep=";")

def contar_palabras(df, columna):
    lista_palabras=[]
    total_palabras=[]
    frecuencias = []

    for texto in df[columna]:
        palabras = texto.split() 
        lista_palabras.append(palabras)
        total_palabras.append(len(palabras)) 
        
        conteo={}
        for palabra in palabras:
            if palabra in conteo:
                conteo[palabra] += 1 #Si exite la palabra le suma 1  
            else:
                conteo[palabra] = 1 #Si no existe crea nuevapalabra  
        frecuencias.append(conteo)

    return lista_palabras, total_palabras, frecuencias

resultado = contar_palabras(df,"NARRATIVA")
resultado_frecuencia = resultado
print(resultado[0])
print(resultado_frecuencia[0])