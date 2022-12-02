lista = []
for i in range(9):
    lista.append(i)
print(lista)

lista2 = [i for i in range(9)]
print(lista2)

lista3 = [i for i in range(9) if i%2==0]
print(lista3)

lista4 = [i/2 for i in range(9)]
print(lista4)

nombre = ["Andres","Sebastian","John","Peter"]
nombre = [i.upper() for i in nombre]
print(nombre)
nombre = [i.lower() for i in nombre]
print(nombre)

import random
class Estudiante():
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

estudiantes = list()
for i in nombre:
    nota = random.randint(0,5)
    e = Estudiante(i,nota)
    estudiantes.append(e)
print(estudiantes)

suma = sum(e.nota for e in estudiantes)
print(suma)

maximo = max(e.nota for e in estudiantes)
print(maximo)