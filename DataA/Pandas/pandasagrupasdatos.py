import numpy as np
import pandas as pd

data = pd.read_csv(r'C:\Users\franc\PycharmProjects\estudios\DataA\Pandas\data_celular.csv',
                   header=0,
                   index_col=0,
                   names=['indice','fecha','duracion','item','mes','red','tipo_red'],
                   parse_dates=['fecha'])
print(data.head())
print(data.shape)

print('Cuantas filas tiene el DataFrame: ')
print(data['item'].count())

print('El tiempo total (en segundos) registrado en llamadas es:')
print(data["duracion"][data["item"] == 'call'].sum())

print('Con cuantas redes telefonis se contactos en el periodo 2014/11 al 2015/03: ')
print(data['red'].nunique())#cantidad de valores unicos

#agrupar datos
print(data.groupby('mes'))
print(data.groupby('mes').groups.keys())
print(data.groupby('mes').groups.values())

print(data.groupby('mes').sum())

print("Cantidad de entradas por mes \n segregadas en llamadas, sms y datos: \n \n")

print(data.groupby(['mes','item'])['duracion'].count())

print('La duracion total de las llamdas realizadas a cada una de las operadoras: ')

print(data[data['item']=='call'].groupby('red')['duracion'].sum())

print('Cuantas llamadas, sms, y datos son enviados a cada operadora por mes?: ')

print(data.groupby(['mes','tipo_red'])['fecha'].count())