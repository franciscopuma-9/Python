import numpy as np
import pandas as pd

d = [np.random.randint(50,size=10)]#se pone en corchetes para que lo ponga en una lista
print(d)

df = pd.DataFrame(d)
print(df)
df = pd.DataFrame(d).T #transpuesta
print(df)

#añadir una nueva columna
df['nueva_col'] = 10
print(df)
df['experiencia'] = 5
print(df)
df['perdidas'] = [(i+2)*np.e for i in range(10)]#crear una columna a partir de un bucle
print(df)

df['columna'] = df['perdidas'] * 100 #crear una columna a partir de otra
print(df)

df.columns = ['codigo_id','anios_exp','indice','eficiencia','eficiencia agregada']#cambiar de nombre a las columnas
print(df)

print(df['codigo_id'])

df['indice'] = df['indice'] / 200 #modifica los valores de una columna
print(df)

del df['eficiencia'] #elimina columna
print(df)

c = df.drop([2,3,5],axis=0) #descarta valores de filas a columnas dependiendo del axis 0=filas 1=colum
print(c)

df.drop(['eficiencia agregada'],axis=1,inplace=True)#primer parametro es la columna, segundo el eje, el inplace es para que se reemplace True cambia, False retorna
print(df.head())
print(df)

i = ['a','b','c','d','e','f','g','h','i','j']
df.index = i #cambiar el indice
print(df)
#una vez que tenemos las columnas podemos realizar todos los calculas con numpy
print(df['codigo_id'])
print(df['codigo_id'].mean())
print(df['codigo_id'].sum())
print(df['codigo_id'].min())
print(df['codigo_id'].max())