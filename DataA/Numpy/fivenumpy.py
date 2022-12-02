import numpy as np

arr = np.arange(0,20,2)
print(arr)

arr_flot = np.random.rand(4,3)#numeros random entre 0 y 1 de 4 filas y 3 columnas
print(arr_flot)

arr_int = np.random.randint(10,size=(2,3))#numeros random hasta 10, de 2 filas y 3 columnas
print(arr_int)

arr_6 = np.full((3,3),6)#tabla 3x3 de todos 6
print(arr_6)

arr = np.append(arr,[12,13,14,51])#agrega valores al final del array
print(arr)

arr = np.insert(arr,2,[42,34])#agrega los valores en la posicion 2 y lo vuelve unidimensional
print(arr)

arrint = np.delete(arr_int,1,axis=0)# 1 es la posicion que deseamos eliminar, y el eje (0 horizontal, 1 vertical)
print(arrint)