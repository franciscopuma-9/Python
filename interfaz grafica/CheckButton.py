from tkinter import *


root = Tk()

root.title("Ejemplo")

playa = IntVar()
montania = IntVar()
turismo = IntVar()

def opcionesViaje():
    opcionEscogida=""

    if(playa.get()==1):
        opcionEscogida+=" Playa "

    if (montania.get() == 1):
        opcionEscogida += " Montania "

    if (turismo.get() == 1):
        opcionEscogida += " Turismo Rural "
    textoFinal.config(text=opcionEscogida)



foto = PhotoImage(file="viaje.png")
Label(root,image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame,text="Elige destinos", width=50).pack()

Checkbutton(frame,text=" Playa ",variable=playa,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text=" Montania ",variable=montania,onvalue=1,offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text=" Turismo rural ",variable=turismo,onvalue=1,offvalue=0,command=opcionesViaje).pack()


textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()
