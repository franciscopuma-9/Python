# # i = 0
# # diccionario = {}
# # while i < 6:
# #     clave = input("Ingrese su nombre: ")
# #     valor = int(input("Ingrese su sueldo"))
# #     diccionario[clave] = valor
# #     i+=1
# # print(diccionario)
# # diccionario1 = {'a':100000000,'b':5,'c':4000000000}
# # max_sueldo = 0
# # empleado_max_sueldo = 0
# # lista = []
# # for clave in diccionario1:
# #     if diccionario1[clave] > max_sueldo:
# #         max_sueldo = diccionario1[clave]
# #         empleado_max_sueldo = clave
# #         print(diccionario1[clave])
# #     if diccionario1[clave] > 100000:
# #         lista.append(clave)
# # diccionario1['Mariano'] = 102000
# # print(empleado_max_sueldo)
# # print(lista)
# # print(diccionario1)
# # lista_aux = diccionario1.keys()
# # lista_aux = list(lista_aux)
# # print(lista_aux[0])
# # valor = lista_aux[0]
# #
# # primer_elemento = lista_aux.pop(str(valor))
# # print(lista_aux)
# # print(diccionario1)
#
# class Articulo:
#     def datos(self):
#         self.nombre = input("Nombre: ")
#         self.cantidad = int(input('Cantidad de stock: '))
#         self.precio = int(input('Precio: '))
# a = Articulo()
# class Vendido:
#     def ventas(self):
#         self.nombre = input("Ingrese su compra: ")
#         self.cantidad = int(input("Cantidad de productos: "))
# v = Vendido()
#
# list = []
# list_total = []
# list_venta = []
# i = 0
# while i != 7:
#     print('''\n1- INTRODUCIR UN NUEVO ARTÍCULO
# 2- VENTA
# 3- MOSTRAR INFORMACION DE LA VENTA
# 4- MOSTRAR STOCK
# 5- BORRAR UN ARTÍCULO del STOCK
# 6- BORRAR TODO EL STOCK
# 7- SALIR''')
#     i = int(input('Elija la opcion que desea realizar: '))
#     if 1 <= i <= 7:
#         if i == 1:
#             lista = []
#             a.datos()
#             lista.append(a.nombre)
#             lista.append(a.cantidad)
#             lista.append(a.precio)
#             list.append(lista)
#         elif i == 2:
#             v.ventas()
#             for x in list:
#                 if v.nombre in x and v.cantidad <= x[1]:  #aca verifico si existe el producto y hay
#                     list_vent = []
#                     subtotal = v.cantidad * x[2]
#                     x[1] -= v.cantidad
#                     list_total.append(subtotal)
#                     list_vent.append(v.nombre)
#                     list_vent.append(v.cantidad)
#                     list_vent.append(x[2])
#                     list_vent.append(subtotal)
#                     list_venta.append(list_vent)
#         elif i == 3:
#             total = 0
#             for x in list_total:
#                 total += x
#             for z in list_venta:
#                 print('\nNombre: ', z[0], '\nCantidad: ', z[1], '\nPrecio Unitario: ', z[2], '\nSubtotal: ', z[3])
#                 print('--------------------------')
#             print('Total', total)
#         elif i == 4:
#             for x in list:
#                 print('\nNombre: ', x[0], '\nCantidad: ', x[1], '\nPrecio Unitario: ', x[2])
#                 print('---------------------------')
#         elif i == 5:
#             print(list)
#             nombre = input("\nIngresa el articulo a eliminar: ")
#             for x in list:
#                 indice = list.index(x)
#                 if nombre in x:
#                     list.pop(indice)
#         elif i == 6:
#             list.clear()
#             print("\nSe ha borrado todo el stock")
#     else:
# #         print("\nNumero ingresado incorrecto. Ingrese nuevamente")
#
# list = [1,2,3,4]
# print(list[-2])
# palabra = "Hola mundo"
# palabra2 = palabra[::-1]
# print(palabra2)

palabra = "Hola mundo"
newpalabra = ""
x = len(palabra) - 1
while (x >= 0):
    newpalabra += palabra[x]
    x-=1
print(newpalabra)