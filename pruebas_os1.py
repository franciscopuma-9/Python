import os

eliminar_carpeta = input("Nombre de la carpeta a eliminar: ")
ruta = os.getcwd()

path = os.path.join(ruta,eliminar_carpeta)

if os.path.exists(path):
    os.rmdir(path) #eliminar carpetas
    print("Carpeta borrada")
else:
    print("La carpeta no existe")