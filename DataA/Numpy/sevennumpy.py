import numpy as np

a = np.array(range(64)).reshape((8,8))
print(a)

print(a[1,1])#elemento 1 x 1

print(a[0:7:2,])#filas de 0 a 7, saltando de a 2

print(a[1,3:]) #fila 1, desde el 3 elemento para adelante

print(a[[1,3,5],[3,6,7]]) #trae fila 1,3,5 y elementos 3,6,7

print(a[[1,3,5],::3]) #trae fila 1,3,5 de 3 en 3


#indexacion booleana
data = np.arange(8)
print(data)

print(data < 4) #devuelve true/false dependiendo si es mayor o menor

print(data[data < 4])#cortar el array con los elementos que cumplen con la condicion

print(data[np.array([ True , True,  True  ,True, False, False, False, False])])#lo mismo que el anterior

amigos = np.array(['Cami','Santi','Fugi','Io'])

print('Cami' in amigos)

print(amigos[amigos!='Santi']) #devuelve el array sin 'Santi'

print(amigos[amigos=='Cami']) #devuelve array con 'Cami'