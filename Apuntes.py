# #SINTAXIS BASICA
#
# Python 100% objeto
# tipos de datos
# numericos = Enteros y Flotantes
# Texto = String
# Booleano = True/False
#
# Operadores
# Aritmeticos= suma(+) resta(-) multiplicacion(*) division(/)
# modulo(%) exponente(**) division entera (//)
# comparacion= ==  !=  >  >=   <   <=
# Logicos= and  or   not
# asignacion=  =   +=  -=    *=   /=     %=    **=    //=
# especiales= is   is not    in   not in
#
#
# variables
# ej variable = 5
# type(variable)    # devuelve el tipo de variable
# mensaje = """ Esto es un mensaje
# con tres
# saltos de linea"""
#
#
variable1 = 'hola'
variable2 = 'mundo'
resultado = variable1 + variable2
print(resultado)
print('%s como estas mi %s'%(variable1,variable2))
print('Hola {}'.format(variable2))
my_string = 'Hola como estas'
print(my_string[0]) #posicion adentro del string
print(my_string[0:7]) #entorno
print(my_string[0:7:2]) #entorno salteado(ultimo numero es cantidad de saltos)
print(my_string[::-1]) #revertir string
my_string = my_string.lower() #todo minuscula
my_string = my_string.upper() #todo mayuscula
my_string = my_string.title() #modo titulo(c/palabra empieza en mayuscula)
#BUSQUEDA
busqueda = my_string.find('como') #retorna la posicion en la que empieza la palabra
count = my_string.count('s') #recuento de cantidad de una letra
reemplazar = my_string.replace('s','x')#reemplaza las 's' por 'x'
split = my_string.split(' ')#retorna una lista de los strings separados por espacios

# FUNCIONES  #conjunto de lineas de codigo(bloque)que funcionan para realizar una tarea especifica
#             #se puede reutilizar codigo
#             #pueden tener parametros/argumentos    pueden devovler valores
# sintaxis
# def nombre_funcion(parametro):
#     haceralgo = "hola"
#     return haceralgo
#
# ejecucion
# nombre_funcion(4)
#
# ej:
# def suma(num1,num2):
#     return num1+num2
#
# almacenar_resultado = suma(4,5) #pasar por referencia
# print(almacenar_resultado)
#
# LISTAS    estructura de datos que permite almacenar varios valores
#             pueden guardar diferentes tipos de variables
#             se puede expander dinamicamente
# SINTAXIS
# nombreLista = ['hola', 1, 1.3, False]
# nombreLista2=['que', 4]*3
# indice_2 = nombreLista[2] #retorna el valor del indice 2
# indice_menos_2 = nombreLista[-2]#retorna el valor del indice 2 al reves
# print(nombreLista[0:3]) #retorna los primeros 3 valores de la lista
# print(nombreLista[2:]) #desde el 2 hasta el final
# nombreLista.append('otro valor') #agrega dato al final
# nombreLista.append(nombreLista2)#se entiende pero como una lista aparte
# nombreLista.insert(1,'mundo') #agrega dato en el indice 1, el dato 'mundo'
# nombreLista.remove(1) #remueve todos los 1 en la lista
# nombreLista.extend([3,True,'Valor'])#extiende la lista (se puede usar otra lista para unirlas)
# nombreLista.index('mundo') #devuelve el indice de 'mundo'
# ultimo_valor = nombreLista.pop() #elimina y devulve el ultimo valor de la lista
# cuarto_valor = nombreLista.pop(4) #elimina el valor en la posicion 4 y lo devuelve
# print("mundo" in nombreLista) #devuelve True/False si se encuentra en la lista
#  #repite 3 veces la lista
# nombreLista3 = nombreLista + nombreLista2 #concatena 2 listas
# nombreLista.sort() # ordena la lista de menor a mayor
# nombreLista.sort(reverse=True) #ordena la lista de mayor a menor
# print(nombreLista)
#
# TUPLAS #listas inmutables, no cambian

# tupla = (1,2,'hola',True,2)
# lista = list(tupla) #convierte una tupla en lista
# tupla = tuple(lista) #convierte una lista en tupla
# print(tupla[2]) #para buscar un indice
# print(tupla.count(2)) # devuelve contador del numero 2
# print(len(tupla)) #devulve la cantidad de elementos(longuitud)
# print('hola' in tupla)#para saber si esta adentro
# tupla_unitaria = ("hola",) #tupla unitaria, si o si la coma al final
# mitupla = ("Fran", 21, 5, 1999)
# nombre, dia, mes, anio = mitupla #desempaquetado de tuplas sirve para
#                                 #asignar variables a los elementos de la tupla
# print(nombre,anio,mes,dia)

# # DICCIONARIOS   #clave : valor #cada valor tiene una clave
#                  # no tienen indice
# print(len(diccionario))#longitud del diccionariodiccionario = {'a':1,'b':2,'c':3}
# print(diccionario['a'])#para imprimir un valor, hay que poner la clave
# diccionario['d']= 7 #crear otra clave
# diccionario['d']= 4 #sobrescribe el valor en una clave
# del diccionario['c'] #para borrar una clave/valor
# print(diccionario)
# tupla = (1,2,3,4) #se puede usar una tupla para las claves y le asignamos valores
# midiccionario = {tupla[0]:'a',tupla[1]:'b',tupla[2]:'c',tupla[3]:'d'}
# print(midiccionario)
# diccionario1= {'a':1,'b':2,'c':{'diccionario':(3,4,5,6)}}#diccionario dentro de diccionario y adentro tupla
# print(diccionario1['c'])
# print(diccionario.keys())#imprime todas las claves\
# print(diccionario.values())#imprime todos los valores

#CONDICIONALES
# #IF   #si pasa tal cosa
# def evaluacion(nota):
#     valoracion = 'aprobado'
#     if nota < 6:
#         valoracion = 'desaprobado'
#     return valoracion
# nota = int(input("ingrese nota")) #introducion un valor por teclado(en este caso es un int)
#                                   #input siempre es str predeterminado, por eso hay que poner int
# print(evaluacion(nota))
#
# def mayor_edad(edad):
#     if (edad<18):
#         return "Es menor"
#     else: #y si no
#         return "Es mayor"
# edad = int(input("Ingresa la edad pa: "))
# print(mayor_edad(edad))

# def adulto(edad):
#     if (edad < 1 or edad > 100):#validacion de datos correctos #operador or: si una de las condiciones es verdadera, la condicion es verdadera
#         return "O no naciste o tas muerto wachin"
#     elif (17<edad<50): #edad<50 and edad>17 #opeador and: tienen que ser correctas todas las condiciones para que la condicion sea verdadera
#         return "es adulto"
#     elif (edad>49): #es un else junto a un if, se pone otra condicion anidada
#         return "es viejo"
#     else:
#         return 'es joven'
# edad = int(input("ingrese edad"))
# print(adulto(edad))

lista= [1,2,3,4,5]
if 1 in lista: #operador in: devuelve verdadero si esta dentro
    print("esta en la lista")