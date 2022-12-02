import numpy as np
import pandas as pd

def CrearDataSet(Num = 1):

    Output = []

    for i in range(Num):

        # Crear un rango de fechas semanal(de lunes a lunes)
        rng = pd.date_range(start='1/1/2016',end='12/31/2020',freq="W-MON")#W-MON frecuencia semanala de lunes a lunes

        #Crear valores aleatorios
        data = np.random.randint(low=25,high=1000,size=len(rng))

        #Estatus posibles
        status = [1,2,3]

        #lista de estatus aleatorios
        random_status = [status[np.random.randint(low=0,high=len(status))] for i in range(len(rng))]

        # locales posibles
        states = ['Libertador','El Hatillo', 'El hatillo','Chacao','Baruta','Sucre']

        # lista de locales aleatorios
        random_states = [states[np.random.randint(low=0, high=len(states))] for i in range(len(rng))]

        Output.extend(zip(random_states,random_status,data,rng)) #zip hace una lista con cada objeto iterable con cada indice

    return Output

dataset = CrearDataSet(4)

df = pd.DataFrame(data=dataset,
                  columns=['Local','Estatus_local','Cantidad_Clientes','Fecha_Status'])

print(df)

rows = np.random.choice(df.index,10,replace=False)#df.index pasa los indices, el siguente numero son las cantidad de pruebas, replace no deja repetir valores cuando esta en False

print(rows)

print(df.loc[rows])#para mostrar un dataframe de las filas que se pasaron como muestra

