import numpy as np

arr = np.arange(1,9)
print(arr)

arr.shape = (2,4)#reorganiza en 2 filas con 4 columnas
print(arr)

ar1 = arr + arr #sumatoria de matrices
print(ar1)

ar2 = arr - ar1 #resta de matrices
print(ar2)

ar3 = arr * arr #producto de matrices
print(ar3)

ar4 = arr ** arr #potencia de matrices
print(ar4)

ar5 = ar1 / arr #division de matrices
print(ar5)