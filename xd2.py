from xd import producto_escalar,carga_vector


# print(producto_escalar(carga_vector()))

# datos = []
# x = 0
# while (x < 1):
#     aux = input("Ingrese nombre: ")
#     aux2 = int(input("Ingrese numero postal: "))
#     aux3 = float(input("Ingrese temperatura: "))
#     aux4 = True
#     lista = [aux,aux2,aux3,aux4]
#     datos.append(lista)
#     x+=1
#
# print(datos[0][4])

lista = [1,5,2,6,7,8,1,2,["hola",'chau']]

quintovalor = lista.pop()

print(lista,quintovalor)

lista.sort(reverse=True)

print(lista)
print('chau' in quintovalor)
