from tkinter import *
from functionsProject1 import *

root = Tk()

root.title("BBDD")
#CREATE MENU
menu = Menu(root)
root.config(menu=menu)

#CREATE MENU-BBDD
archivoBBDD = Menu(menu,tearoff=0)
menu.add_cascade(label="BBDD", menu=archivoBBDD)
archivoBBDD.add_command(label="Conectar",command=conectar)
archivoBBDD.add_command(label="Salir",command=lambda : salir(root))

#CREATE MENU-BORRAR
archivoBorrar = Menu(menu,tearoff=0)
menu.add_cascade(label="Borrar", menu=archivoBorrar)
archivoBorrar.add_command(label="Borrar campos",command=lambda : borrar_campos(id,nombre,apellido,password,direccion,textoComentario))

#CREATE MENU-CRUD
archivoCRUD = Menu(menu,tearoff=0)
menu.add_cascade(label="CRUD", menu=archivoCRUD)
archivoCRUD.add_command(label="Crear",command=lambda :crear(id,nombre,apellido,password,direccion,textoComentario))
archivoCRUD.add_command(label="Leer",command=lambda :leer(id,nombre,apellido,password,direccion,textoComentario))
archivoCRUD.add_command(label="Actualizar")
archivoCRUD.add_command(label="Borrar")

#CREATE MENU-AYUDA
archivoAyuda = Menu(menu,tearoff=0)
menu.add_cascade(label="Ayuda", menu=archivoAyuda)
archivoAyuda.add_command(label="Licencia",command=licencia)
archivoAyuda.add_command(label="Acerca de...",command=about)

#CREATE FRAME

miFrame = Frame(root)
miFrame.pack()

#ALL LABEL
labelID = Label(miFrame,text="ID",)
labelID.grid(row=0,column=0,pady=4,padx=4)
labelNombre = Label(miFrame,text="Nombre")
labelNombre.grid(row=1,column=0,pady=4,padx=4)
labelApellido = Label(miFrame,text="Apellido")
labelApellido.grid(row=2,column=0,pady=4,padx=4)
labelPass = Label(miFrame,text="Password")
labelPass.grid(row=3,column=0,pady=4,padx=4)
labelDir = Label(miFrame,text="Direccion")
labelDir.grid(row=4,column=0,pady=4,padx=4)
labelCom = Label(miFrame,text="Comentario")
labelCom.grid(row=5,column=0,pady=4,padx=4)

#ALL ENTRY

id = StringVar()
entryID = Entry(miFrame,textvariable=id)
entryID.grid(row=0,column=1,pady=4,padx=4)

nombre = StringVar()
entryNombre = Entry(miFrame,textvariable=nombre)
entryNombre.grid(row=1,column=1,pady=4,padx=4)

apellido = StringVar()
entryApellido = Entry(miFrame,textvariable=apellido)
entryApellido.grid(row=2,column=1,pady=4,padx=4)

password = StringVar()
entryPass = Entry(miFrame,textvariable=password)
entryPass.grid(row=3,column=1,pady=4,padx=4)
entryPass.config(show='?')

direccion = StringVar()
entryDir = Entry(miFrame,textvariable=direccion)
entryDir.grid(row=4,column=1,pady=4,padx=4)

textoComentario = Text(miFrame,width=15,height=5)
textoComentario.grid(row=5,column=1,pady=4,padx=4)
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=5,column=2,sticky='nsew')
textoComentario.config(yscrollcommand=scrollVert.set)

#Frame CRUD

frameCRUD = Frame(root)
frameCRUD.pack()

#Botones CRUD

botonCreate = Button(frameCRUD,text="CREATE",command=lambda :crear(id,nombre,apellido,password,direccion,textoComentario))
botonCreate.grid(row=0,column=0,pady=4,padx=4)
botonRead = Button(frameCRUD,text="READ",command=lambda :leer(id,nombre,apellido,password,direccion,textoComentario))
botonRead.grid(row=0,column=1,pady=4,padx=4)
botonUpdate = Button(frameCRUD,text="UPDATE",command=lambda :actualizar(nombre,apellido,password,direccion,textoComentario,id))
botonUpdate.grid(row=0,column=2,pady=4,padx=4)
botonDelete = Button(frameCRUD,text="DELETE",command=lambda :borrar(id,nombre,apellido,password,direccion,textoComentario))
botonDelete.grid(row=0,column=3,pady=4,padx=4)

root.mainloop()