import numpy as np
import pandas as pd

df = pd.DataFrame(
                np.random.randint(low=0,high=10,size=(10,2)),
                index=['a','b','c','d','e','f','g','h','i','j'],
                columns=['Cod_empleado','Calificacion']
                )
print(df)
print(df.Cod_empleado)
print(df['Calificacion'].mean())

#seleccionar filas
print(df.loc['a']) #location
print(df.loc['b':'f'])#entorno de etiqueta incluyendo b y f
print(df.loc[df.index[3:7],'Cod_empleado'])#indico las filas y el nombre de la columna

print(df.iloc[0:3])#index location de 0 hasta 3 no includo
print(df.iloc[3:]) # 3 en adelante