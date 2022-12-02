import numpy as np
import pandas as pd
#dataframe

# s = pd.DataFrame(data,...)



data = {
    'cuidades':['Caracas','Guadalajara','La habana','Cancun','Guasdalito'],
    'poblacion': [100000,200000,340000,210000,300000],
    'infectados': [6000,4000,35000,430,3002]
}

df = pd.DataFrame(data)#crear el dataframe
print(df)

print(df.columns)#acceder o seleccionar columnas
print(df['cuidades']) #llamamos columnas
print(df.poblacion) #llamamos columas
print(df.dtypes)#devuelve el tipo de dato de cada columna

