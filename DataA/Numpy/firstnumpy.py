import numpy as np

arreglo = np.array([0,1,2,3,4,5])
print(type(arreglo),arreglo)

notas = [10,11,12,13,14,15]

ar_notas = np.array(notas,dtype=float) #dtype es el tipo de dato

print(ar_notas,type(ar_notas[0]))

ar_notas_todas = np.array(([0,1,2,3,4,5],notas)) #arreglo bidimensional, una tupla donde cada elemento es una dimension

print(ar_notas_todas)

print(ar_notas_todas.ndim)#dimensiones en un array

print(ar_notas_todas.shape)#el tamanio de cada dimension del array (primer elemento = filas, segundo elemento = cantidad de elementos de filas)


arr = np.zeros((2,3),dtype=float) #arreglo de 2 filas con 3 columnas de ceros
print(arr)

ar2 = np.ones((3,4),dtype=float)#arreglo de 3 filas con 4 columnas de unos
print(ar2)

ar3 = np.identity((4),dtype=float) #matriz identidad rango 4
#ar4 = np.eye((4),dtype=float) #matriz identidad rango 4
print(ar3)

ar5 = np.arange(1,10) #arreglo como un range
print(ar5)

