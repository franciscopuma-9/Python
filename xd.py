# import random
#
# mat = []
#
# for i in range(3):  #[0,1,2]
#     aux = []
#     for e in range(3):
#         aux.append(random.randint(-100,100))
#     mat.append(aux)
#
# def imprimir():
#     for i in range(3):
#         print(mat[i])
#
# def sumatoria(matr):
#     sumatoria = 0
#     for i in range(3):
#         for e in range(3):
#             sumatoria += matr[i][e]
#     return sumatoria/9
#
# print("La sumatoria es", sumatoria(mat))
#
# max = mat[0][0] #valor en la posicion 0 0
# min = mat[0][0] #valor en la posicion 0 0
# pos_max = [0,0] #lista 0 0
# pos_min = [0,0] #lista 0 0
# buffer = 0
#
# for i in range(3):
#     for e in range(3):
#         buffer = mat[i][e]
#         if buffer > max:
#             max = buffer
#             pos_max = [i,e]
#
#         if buffer < min:
#             min = buffer
#             pos_min = [i,e]
#
# imprimir()
#
# print("El numero maximo es",max,"en la fila",pos_max[0], "columna", pos_max[1])
#
# print("El numero minimo es",min,"en la fila",pos_min[0], "columna", pos_min[1])

# A = [1,2,3]
# B = [5,6,7]
#
# def producto_vectorial(mat1,mat2):
#     product = 0
#     for i in range(3):
#         product += mat1[i]*mat2[i]
#     return product
#
# print(producto_vectorial(A,B))

import random

def carga_vector():
    """
    Funcion para cargar un vector de n dimensiones. Retorna una lista con los 2 vectores con numeros random.
    """
    n = int(input("Ingresa n:"))
    v = []
    w = []
    for i in range(n):
        v.append(random.randint(1,100))
        w.append(random.randint(1,100))
    x = [v,w]

    print(v)
    print(w)
    return x

def producto_escalar(x):
    """
    Funcion que recibe una lista con 2 vectores y retorna el producto escalar de esos vectores.
    """
    productoEscalar = 0
    v = x[0]
    w = x[1]
    for i in range(len(v)):
        productoEscalar += v[i] * w[i]
    return productoEscalar

#print(producto_escalar(carga_vector()))