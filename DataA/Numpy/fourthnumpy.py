import numpy as np
#funciones universales unarias
a = np.array([2,4,9],float)

print(np.sqrt(a)) #devuelve array con raices cuadradas

print(np.exp(a))# exponencial de e^x

print(np.log(a))#logaritmo natural
print(np.log10(a))#logaritmo base 10
print(np.log2(a))#logaritmo base 2
print(np.log1p(a))#logaritmo(x+1)

print(np.sin(a))#seno x
print(np.cos(a))#coseno x
print(np.tan(a))#tangente x

print(np.mean(a))#media aritmetica
print(np.std(a))#variacion estandar
print(np.var(a))#varianza
print(np.median(a))#mediana


#funciones universales unarias

ar1 = np.array([5,36,17,18,9])
ar2 = np.array([8,24,17,19,9])

print(np.add(ar1,ar2))#suma entre elementos correspondientes de los arrays
print(np.subtract(ar1,ar2))#resta entre elementos correspondientes de los arrays
print(np.multiply(ar1,ar2))#producto entre elementos correspondientes de los arrays
print(np.divide(ar1,ar2))#division entre elementos correspondientes de los arrays
print(np.floor_divide(ar1,ar2))#division truncada entre elementos correspondientes de los arrays

print(np.power(ar1,ar2))#eleva cada elemento del primer array a la potencia indicada en el segundo array
print(np.array_equal(ar1,ar2))#devulve bool si son iguales
print(np.array_equal(ar1,ar1))#devulve bool si son iguales

print(np.fmin(ar1,ar2))#deuelve array con los valores minimos al realizar la comparacion
print(np.fmax(ar1,ar2))#deuelve array con los valores maximos al realizar la comparacion

