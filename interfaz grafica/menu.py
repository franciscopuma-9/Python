from tkinter import *
from tkinter import messagebox #ventana emergente


root=Tk()

def infoAdicional(): #funcion para ventana emergente info
    messagebox.showinfo("Procesador de Fran","Prueba de interfaz grafica 2022")

def avisoLicencia(): #funcion de ventana emergente warning
    messagebox.showwarning("Licencia de Fran","Prueba de licencia")

def salirAplicacion(): #funcion de ventana emergente si/no
    #valor = messagebox.askquestion("Salir","Queres salir de la app?") #almacena en valor yes/no
    valor = messagebox.askokcancel("Salir","Queres salir de la app?") #almacena en valor true/false

    if valor: #sale cuando pones aceptar
        root.destroy()

def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar","No es posible cerrar documento")#retorna true/false (reintentar/cancelar)

    if valor==False:
        root.destroy()

barraMenu = Menu(root) #crea menu
root.config(menu=barraMenu,width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0) #crea teclas del menu  #desaparece la lagrima(separador por defecto)
archivoMenu.add_command(label="Nuevo") #crea sub teclas del menu
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()#crea barra de separadora
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_command(label="Salir",command=salirAplicacion)


archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")


archivoHerramientas=Menu(barraMenu,tearoff=0)


archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia",command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...",command=infoAdicional)



barraMenu.add_cascade(label="Archivo", menu=archivoMenu) #aniade las teclas del menu
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()