import numpy as np
import pandas as pd
#series
#s = pd.Series(data,index=index)#crear la serie

serie = pd.Series([1979,1980,1981,1982])# creo la serie
print(serie)#muestra los indices, valores y dtype
print(serie.values)#valores de valores
print(serie.index)#devulve objeto clase index

series = pd.Series([1989,1990,1991,1992],index=['Francisco','Camila','Santi','Fugi'])
print(series)
print(series.index)

seriee = pd.Series(np.random.rand(10))
print(seriee)

dicci = {'Cuadrado de {}'.format(i):i*i for i in range(11)}#genero un diccionario con su cuadrado
print(dicci)

serie_dic = pd.Series(dicci) #las keys se vuelven index con sus valores
print(serie_dic)
