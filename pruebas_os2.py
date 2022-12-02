import os

ruta = os.getcwd()

contenido = os.listdir(path=ruta)#lista en la ruta actual o una ruta que pongamos
print(contenido)

with os.scandir(path=ruta) as itr:

    for i in itr:
        #print(i.name)#nombre de cada archivo
        if i.is_file():
            print("Es un archivo", i.name)
        elif i.is_dir():
            print("Es una carpeta", i.name)