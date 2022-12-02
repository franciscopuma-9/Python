import numpy as np
import pandas as pd

df = pd.DataFrame({
    'VarA':['aa',None,'cc'],
    'VarB':[20,30,None],
    'VarC':[1234,3456,6789]
    },
    index=['Caso1','Caso2','Caso3']
)
print(df)

print(pd.isnull(df)) #devuelve otro dataframe remplazados por valores booleanos (los true son los valores ausentes)

print(df.dropna(subset=["VarA",'VarB']))#descartamos las filas que incluyen valores nulos en las columnas que les indicamos

print(df.fillna("")) #llenas nulos con espacios vacios
print(df.fillna(23)) #reemplaza los valores nulos con 23

print(df.fillna(df.mean()))#se suele reemplazar con la media aritmetica

