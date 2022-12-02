import numpy as np


arr_ent = np.random.randint(10,size=(3,4))
print(arr_ent)

arr_float = arr_ent.astype(float)#transforma el tipo de dato del arreglo
print(arr_float)

arr_ent.sort() #ordena de manera ascendente por fila
print(arr_ent)

arr_ent.sort(axis=0) #ordena de manera ascendente por columna
print(arr_ent)

arr_ent = arr_ent.reshape(4,3)#reforma las dimensiones de una array(tiene que ser un array equilavente, tener la misma cantidad de elementos)
print(arr_ent)


plano_arr = arr_ent.flatten()#crea un arreglo unidimensional desde otro
print(arr_ent)
print(plano_arr)

lista_arr = plano_arr.tolist()#pasarlo a lista
print(lista_arr)

arrays = np.split(arr_ent,4)#separar un array en 4 partes(crea lista de arrays)
print(arrays)

concate = np.concatenate((arrays[1],arrays[0]),axis=0)#concatena arrays en forma vertical
print(concate)

t_arr = arr_ent.T#hace la transpuesta
print(t_arr)
