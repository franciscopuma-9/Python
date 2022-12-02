import os

ruta = os.getcwd() #ruta en la que estamos parados
print(ruta)

nueva_carpeta = input("Ingrese nombre de la carpeta: ")
path = os.path.join(ruta,nueva_carpeta) #crear el path

if os.path.exists(path): #si existe esa carpeta
    print("La carpeta ya existe")
else:
    os.mkdir(path)
    print("Carpeta creada")



