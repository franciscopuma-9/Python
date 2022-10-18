from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("adivinador matematico")
root.config(width=700,height=500)

Textobienvenida = Label(root, font="arial,13", fg="White", background="Black",
                                text="bienvenido\nSelecciona el idioma que quieres jugar\nWelcomen\n Select the language you want to play")
Textobienvenida.place(x=75, y=7)


lenguage = IntVar()
Radiobutton(root,text="Español/Spanish",variable=lenguage, value=1,font="verdana, 10", fg="Red", bg="Black").place(x=60, y=340)
Radiobutton(root, variable=lenguage, text="Ingles/English", value=2,font="verdana, 10", fg="Red", bg="Black").place(x=160, y=340)

def Ventanaidioma():
    if lenguage.get() == 1:
        ventana = Toplevel()
        ventana.geometry("500x400+370+50")
        ventana.title("Adivinador")
        ventana.config(bg="Black")

        Label(ventana, text="Pensá un número de dos cifras (que no sean iguales)", bg="black",
                         font="verdana 13", fg="white").grid(row=0,column=0)
        Label(ventana, text="Invertí el orden de las cifras", bg="black", font="verdana,13",
                          fg="white").grid(row=1,column=0)
        Label(ventana,text="El nuevo numero es meyor o menor que el primero", bg="black", font="verdana,13",
                          fg="white").grid(row=2,column=0)
        Label(ventana, text="Restale ese número al primero que pensaste", bg="Black",
                             font="verdana,13", fg="White").grid(row=3,column=0)
        Label(ventana, text="Ingrese numero aqui-->", bg="Black", font="verdana, 13",
                                fg="white").grid(row=4,column=0,sticky='w')
        Label(ventana, text="Ahora sumá las cifras del número que pensaste al principio",
                           bg="black", font="verdana, 13", fg="White").grid(row=5,column=0)

        Label(ventana, text="-Ingresa ese numero aquí-->", bg="black", font="verdana,13",
                                fg="white").grid(row=6,column=0)

        numero1 = IntVar()
        Entry(ventana, textvariable=numero1).grid(row=4,column=1)


        numero2 = IntVar()
        Entry(ventana, textvariable=numero2).grid(row=6,column=1)


        def adivinar_numero():
            if 1 <= int(numero2.get()) <=18 and int(numero1.get()) % 9 == 0:
                div9 = numero1.get()/9
                op1 = int((numero2.get() - div9) / 2)
                op2 = int((numero2.get() + div9) / 2)
                text = "Tu numero es " + str(op1)+str(op2)
                messagebox.showinfo(title="¡Ya esta!", message=(text))
            elif int(numero1.get()) % 9 != 0:
                messagebox.showerror("Le erraste wachin", "Flaco tu primer numero ta mal")
            else:
                messagebox.showerror("Le erraste wachin", "Flaco tu segundo numero ta mal")


        Button(ventana, text="Adiviná mi número", cursor="hand2", font="verdana, 13",
                               bg="lawn green", bd=5, command=adivinar_numero).grid(row=11,column=0)


    elif lenguage.get() == 2:
        window = Toplevel()
        window.geometry("500x400+370+50")
        window.title("Guess")
        window.config(bg="Black")

        consigna = Label(window, text="Pensá un número de dos cifras (que no sean iguales)", bg="black",
                         font="verdana 13", fg="white")
        consigna.place(x=20, y=20)
        Invertido = Label(window, text="Invertí el orden de las cifras", bg="black", font="verdana,13",
                          fg="white")
        Invertido.place(x=20, y=60)

        Restarnumero = Label(window, text="Restale ese número al primero que pensaste", bg="Black",
                             font="verdana,13", fg="White")
        Restarnumero.place(x=20, y=100)
        Ingresarnumero1 = Label(window, text="Ingrese numero aqui-->", bg="Black", font="verdana, 13",
                                fg="white")
        Sumacifras = Label(window, text="Ahora sumá las cifras del número que pensaste al principio",
                           bg="black", font="verdana, 13", fg="White")
        Sumacifras.place(x=20, y=180)
        Ingresarnumero2 = Label(window, Text="-Ingresa ese numero aquí-->", bg="black", font="verdana,13",
                                fg="white")

        numero1 = IntVar(Value="")
        Caja1 = Entry(window, textvariable=numero1)
        Caja1.place(x=245, y=142)
        numero2 = IntVar(value="")
        caja2 = Entry(window, textvariable=Ingresarnumero2)
        caja2.place(x=245, y=225)

        resultado = StringVar()

        numero1 = IntVar(Value="")
        Caja1 = Entry(window, textvariable=numero1)
        Caja1.place(x=245, y=142)
        numero2 = IntVar(value="")
        caja2 = Entry(window, textvariable=Ingresarnumero2)
        caja2.place(x=245, y=225)

        resultado = StringVar()


        def adivinar_numero():
            division9 = Ingresarnumero1.get() / 9
            op1 = (Ingresarnumero2.get() - division9) / 2
            op2 = (Ingresarnumero2.get() + division9) / 2
            a = int(op1)
            b = int(op2)

            messagebox.showinfo(title="¡Ya esta!", message=(b, a))


        botonAdivinar = Button(root, text="Adiviná mi número", cursor="hand2", font="verdana, 13",
                               bg="lawn green", bd=5, command=adivinar_numero)
        botonAdivinar.place(x=160, y=280)

botonSeleccionar = Button(root, text="Seleccionar/select", command=Ventanaidioma, cursor="hand2",
                          bd=7, font="arial, 12", fg="lawn green", bg="grey27")
botonSeleccionar.place(x=270, y=330)

root.mainloop()