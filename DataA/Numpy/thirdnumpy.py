import numpy as np

a = np.array([1,2,3], float)
b = np.array([0,1,1], float)

punto = np.dot(b,a) #producto escalar
print(punto)
print(a.dot(b))#producto escalar

a = np.array([[5,2],[4,8]],float)
b = np.array([[2,4],[5,3]],float)

print(a,"\n------------------")
print(b,"\n------------------")

c= np.dot(a,b) #multiplicacion de matrices pero no es el metodo recomendado
print(c)

d = a @ b #operador para multiplicacion de matrices
print(d)

f = np.array([[0,1,4],[5,2,3],[1,4,8]],float)
g = np.array([2,3,5],float)
h = np.dot(f,g)
print(h)
j = g @ f #???????????
print(j)

print(np.matmul(f,g))#multiplicacion de matrices


t = np.array([[8,5],[3,4]])

print(t,"\n---------")
print(np.linalg.det(t))#determinante

vals, vecs = np.linalg.eig(t)
print(vals,"\n---------------") #autovalor
print(vecs,"\n---------------") #autovector
