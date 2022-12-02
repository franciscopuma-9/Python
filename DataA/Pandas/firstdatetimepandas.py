import numpy as np
import pandas as pd
import datetime

fecha = pd.to_datetime('24th April, 2020')
print(fecha)
print(type(fecha))

print(fecha.year)

fecha = datetime.datetime.now()
print(fecha)

print('La fecha de hoy es: ', fecha)
print('Y la fecha en 4 dias sera: ',fecha+pd.to_timedelta(4,unit='D'))#indica 4 y la unidad es dias

fechas_inicio = pd.date_range(start='24/4/2020',end='24/5/2020',freq='D')#rango de fechas por dia
print(fechas_inicio)
fechas_fin = pd.date_range(start='24/5/2020',end='24/6/2020',freq='D')#rango de fechas por dia
print(fechas_fin)

lista_equis = []

for i in range(15):
    lista_equis.append(np.random.randint(2))

df = pd.DataFrame()
df['Inicio_campaña'] = fechas_inicio[:15]
df['Fin_campaña'] = fechas_fin[:15]
df['Target'] = lista_equis
print(df)

df['Día de inicio'] = df['Inicio_campaña'].dt.day


df['Mes de inicio'] = df['Inicio_campaña'].dt.month


df['Año de inicio'] = df['Inicio_campaña'].dt.year


df['Hora_inicio'] = df['Inicio_campaña'].dt.hour


df['Minuto_inicio'] = df['Inicio_campaña'].dt.minute


df['Segundo_inicio'] = df['Inicio_campaña'].dt.second


df['Nombre del día de inicio'] = df['Inicio_campaña'].dt.weekday


df['Semana del año de inicio'] = df['Inicio_campaña'].dt.week


df['Duración'] = df['Fin_campaña']-df['Inicio_campaña']

print(df)
df.columns = ['Inicio_campaña', 'Fin_campaña', 'Target','Día de inicio','Mes de inicio','Año de inicio','Hora_inicio',
              'Minuto_inicio','Segundo_inicio','Día de la semana del inicio','Semana del año de inicio','Duración']

print(df)

from datetime import timedelta

df['Días de duración'] = df['Duración']/timedelta(days=1)

df['Minutos de duración'] = df['Duración']/timedelta(minutes=1)

df['Segundos de duración'] = df['Duración']/timedelta(seconds=1)

print(df)
