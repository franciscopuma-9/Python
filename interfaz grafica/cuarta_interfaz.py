from tkinter import *


root = Tk()

miFrame= Frame(root,width=1200, height=600)
miFrame.pack()

miNombre = StringVar()


cuadroNombre = Entry(miFrame,textvariable=miNombre)
#cuadroTexto.place(x=100,y=100)
cuadroNombre.grid(row=0,column=1)#grilla
cuadroNombre.config(fg='red',justify="center")#justify justicar


cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=3,column=1)
cuadroPass.config(show='*')#para que no se vean las contrasenias

passLabel = Label(miFrame,text="Password")
passLabel.grid(row=3,column=0)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=2,column=1)

nombreLabel=Label(miFrame,text="Nombre:")
#nombreLabel.place(x=100,y=100)
nombreLabel.grid(row=0,column=0,sticky='w')#sticky para posicionar con puntos cardinales s/e/n/w

apellidoLabel = Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=1,column=0,sticky='w',pady=10,padx=10)#pady/padx es la separacion con los otros elementos

direccionLabel = Label(miFrame,text="Direccion:")
direccionLabel.grid(row=2,column=0,sticky='w')


comentarioLabel = Label(miFrame,text="Comentarios")
comentarioLabel.grid(row=4,column=0)

textoComentario = Text(miFrame,width=15,height=5)
textoComentario.grid(row=4,column=1)

scrollVert=Scrollbar(miFrame,command=textoComentario.yview)#creo scroll
scrollVert.grid(row=4,column=2,sticky='nsew')#se adapta al tamanio del texto y se puede mover el scroll

textoComentario.config(yscrollcommand=scrollVert.set)#indicar en todo momento la posicion del scroll

def codigoBoton():

    miNombre.set("Francisco")


botonEnvio = Button(root,text="Enviar",command=codigoBoton)
botonEnvio.pack()





root.mainloop()