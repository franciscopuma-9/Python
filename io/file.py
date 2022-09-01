# from io import open

# archivo_texto = open("archivo.txt","w") #crear y abrir el archivo "w" modo escritura
# frase = "Estupendo dia para estudiar python\nhoy jueves"
# archivo_texto.write(frase) #escribe adentro del archivo
#
# archivo_texto = open("archivo.txt","r")#crear y abrir el archivo "r" modo lectura
# # texto = archivo_texto.read()# crea una variable con el contenido del archivo
#
# # texto = archivo_texto.readline()#crea una variable con la primera linea del archivo
# texto = archivo_texto.readlines()#crea una lista con todas las lineas del archivo
# print(texto[0])#primer elemento de la lista
# archivo_texto = open("archivo.txt","a") # modo append/agregar
#
# archivo_texto.write("\nManiana viernes tambien ta piola pa estudiar")#agrega contenido al archivo
archivo_texto = open("archivo.txt","r+") #lectura y escritura
# print(archivo_texto.read(11))#lee hasta el caracter 11 (solo lee) y deja ahi el puntero
# archivo_texto.seek(11)#el puntero se situa en la posicion 0 (se posiciona)
# print(archivo_texto.read())
# archivo_texto.seek(len(archivo_texto.read())/2)#se posiciona a la mitad del texto
# archivo_texto.seek(len(archivo_texto.readline()))#se posiciona al final de la primera linea
# archivo_texto.write("Comienzo del texto")
# print(archivo_texto.read())
# lineas = archivo_texto.readlines()
#
# lineas[1]= "Esta linea ha sido incluida desde el exterior\n"
#
# archivo_texto.seek(0)
# print(lineas)
# archivo_texto.writelines(lineas)
# archivo_texto.close() #cerrar archivo


import json
import timeit

with open("output.json", "r") as f:
    data = json.load(f)

def inputs():

    print("Escoja parámetro por el que desee filtrar.\n1- Nombre\n2- País")

    choice = input("Ingrese 1 ó 2 para continuar:")

    if choice == "1":
        name = input("Ingrese el nombre que desee filtrar: ")
        if name.title() in ["Fran","Harmy","Gun","Enzo","Rodri"]:
            value = "Name"
            return filter(name,value)
        else:
            print("El nombre ingresado no se encuentra en la base de datos, vuelva a intentarlo.")

    elif choice == "2":
        name = input("Ingrese el país que desee filtrar: ")
        if name.title() in get_countries(data):
            value = "Country"
            return filter(name,value)
        else:
            print("El país ingresado no se encuentra en la base de datos, vuelva a intentarlo.")

    else:
        print("Parámetro incorrecto, inténtelo de nuevo.")

def filter(name, value):

    new_output_name = [x for x in data if x[value] == name.title()]

    with open("new_output_%s.json" % name, "w") as file:
        json.dump(new_output_name, file , indent=2)

def get_unique_items(iterable):
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def get_countries(data):
    lista_paises=[]

    for x in data:
        lista_paises.append(x["Country"])

    return get_unique_items(lista_paises)

def main():
    start = timeit.default_timer()

    inputs()

    print("Al programa le llevo %s segundos terminar" %round(timeit.default_timer()-start,2))
if __name__ == "__main__":
    main()
