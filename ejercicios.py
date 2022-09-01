# 1
# lista = ['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua']
# print(lista)

#2
# lista = ['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua']
# for valor in lista:
#     print('Yo estudio', valor)

#3
# lista = ['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua']
# notas = []
# for valor in lista:
#     nota = int(input('Nota en {}:'.format(valor)))
#     notas.append(nota)
# i = 0
# for valor in lista:
#     print('En', valor, 'has sacado', notas[i])
#     i = i + 1

#4
# numeros_ganadores = int(input('Cuantos numeros ganadores hay?'))
# i = 0
# numeros = []
# while i<numeros_ganadores:
#     numero = int(input('Ingrese el numero ganador: '))
#     numeros.append(numero)
#     i = i + 1
# numeros.sort()
# print(numeros)
#
#5
# i = 0
# lista = []
# while i < 10:
#     i = i + 1
#     lista.append(i)
# lista.sort(reverse=True)
# print(lista)

# lista = []
# for i in range(1, 11):
#     lista.append(i)
# lista.sort(reverse=True)
# print(lista)

#6
# lista = ['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua']
# lista_2 = ['Matematica', 'Fisica', 'Quimica', 'Historia', 'Lengua']
#
# for valor in lista_2:
#     nota = int(input('Nota en {}:'.format(valor)))
#     if nota > 5:
#         lista.remove(valor)
#
# print('Debe repetir', lista)

#7
# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# abc_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# i = 0
# for valor in abc_2:
#     i = i +1
#     if i % 3 == 0:
#         abc.remove(valor)
# print(abc)

# 8
# palabra_1 = input('Ingrese palabra:')
# if palabra == palabra[::-1]:
#     print("Es palindromo")
# else:
#     print("No es palindromo")


#9
# precios = [50, 75, 46, 22, 80, 65, 8]
# precios.sort()
# mayor = precios.pop()
# menor = precios.pop(0)
# print('El menor precio es:', menor, '\nEl mayor precio es:', mayor)
#
# 10
# vector_1 = [1, 2, 3]
# vector_2 = [-1, 0, 2]
# producto_vectorial = vector_1[0]*vector_2[0] + vector_1[1]*vector_2[1] + vector_1[2]*vector_2[2]
# print(producto_vectorial)


