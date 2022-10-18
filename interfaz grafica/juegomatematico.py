from cProfile import label
from pydoc import text
from tkinter import *
from sqlite3 import Cursor
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
import tkinter as tk


# --------------------------------------#

class menuprincipal(ttk.Frame):

    def __init__(self, Menu_Principal):
        super().__init__(Menu_Principal)
        Menu_Principal.title("Adivinador Matematico")

        Menu_Principal.configure(width=1080, height=920)

        self.place(relwidth=1, relheight=1)
        # Img=tk.PhotoImage(file="ISAUI.png")
        # Img=tk.Label(Menu_principal, image=Img).place(x=100, y=100)
        # img.pack()
        Textobienvenida = Label(Menu_Principal, font="arial,13", fg="White", background="Black",
                                text="bienvenido\nSelecciona el idioma que quieres jugar\nWelcomen\n Select the language you want to play")
        Textobienvenida.place(x=75, y=7)

        self.Language = IntVar()
        es_Es = tk.Radiobutton(Menu_Principal, variable=self.Language, text="Español/Spanish", value=1,
                               font="verdana, 10", fg="White", bg="Black")
        es_Es.place(x=60, y=340)
        en_En = tk.Radiobutton(Menu_Principal, variable=self.Language, text="Ingles/English", value=2,
                               font="verdana, 10", fg="White", bg="Black")
        en_En.place(x=160, y=340)

        def Ventanaidioma():
            if self.Language.get() == 1:
                ventana = Toplevel()
                ventana.geometry("500x400+370+50")
                ventana.resizable(width=False, heigth=False)
                ventana.title("Adivinador")
                ventana.config(bg="Black")

                consigna = Label(ventana, text="Pensá un número de dos cifras (que no sean iguales)", bg="black",
                                 font="verdana 13", fg="white")
                consigna.place(x=20, y=20)
                Invertido = label(ventana, text="Invertí el orden de las cifras", bg="black", font="verdana,13",
                                  fg="white")
                Invertido.place(x=20, y=60)

                Restarnumero = label(ventana, text="Restale ese número al primero que pensaste", bg="Black",
                                     font="verdana,13", fg="White")
                Restarnumero.place(x=20, y=100)
                Ingresarnumero1 = label(ventana, text="Ingrese numero aqui-->", bg="Black", font="verdana, 13",
                                        fg="white")
                Sumacifras = label(ventana, text="Ahora sumá las cifras del número que pensaste al principio",
                                   bg="black", font="verdana, 13", fg="White")
                Sumacifras.place(x=20, y=180)
                Ingresarnumero2 = label(ventana, Text="-Ingresa ese numero aquí-->", bg="black", font="verdana,13",
                                        fg="white")

                numero1 = IntVar(Value="")
                Caja1 = Entry(ventana, textvariable=numero1)
                Caja1.place(x=245, y=142)
                numero2 = IntVar(value="")
                caja2 = Entry(ventana, textvariable=Ingresarnumero2)
                caja2.place(x=245, y=225)

                resultado = StringVar()

                numero1 = IntVar(Value="")
                Caja1 = Entry(ventana, textvariable=numero1)
                Caja1.place(x=245, y=142)
                numero2 = IntVar(value="")
                caja2 = Entry(ventana, textvariable=Ingresarnumero2)
                caja2.place(x=245, y=225)

                resultado = StringVar()

                def adivinar_numero():
                    div9 = Ingresarnumero1.get
                    op1 = (Ingresarnumero2.get() - div9) / 2
                    op2 = (Ingresarnumero2.get() + div9) / 2
                    a = int(op1)
                    b = int(op2)

                    messagebox.showinfo(title="¡Ya esta!", message=(b, a))

                botonAdivinar = Button(menuprincipal, text="Adiviná mi número", cursor="hand2", font="verdana, 13",
                                       bg="lawn green", bd=5, command=adivinar_numero)
                botonAdivinar.place(x=160, y=280)

            elif self.Language.get() == 2:
                window = tk.Toplevel()
                window.geometry("500x400+370+50")
                window.resizable(width=False, heigth=False)
                window.title("Guess")
                window.config(bg="Black")

                consigna = Label(window, text="Pensá un número de dos cifras (que no sean iguales)", bg="black",
                                 font="verdana 13", fg="white")
                consigna.place(x=20, y=20)
                Invertido = label(window, text="Invertí el orden de las cifras", bg="black", font="verdana,13",
                                  fg="white")
                Invertido.place(x=20, y=60)

                Restarnumero = label(window, text="Restale ese número al primero que pensaste", bg="Black",
                                     font="verdana,13", fg="White")
                Restarnumero.place(x=20, y=100)
                Ingresarnumero1 = label(window, text="Ingrese numero aqui-->", bg="Black", font="verdana, 13",
                                        fg="white")
                Sumacifras = label(window, text="Ahora sumá las cifras del número que pensaste al principio",
                                   bg="black", font="verdana, 13", fg="White")
                Sumacifras.place(x=20, y=180)
                Ingresarnumero2 = label(window, Text="-Ingresa ese numero aquí-->", bg="black", font="verdana,13",
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

                botonAdivinar = Button(menuprincipal, text="Adiviná mi número", cursor="hand2", font="verdana, 13",
                                       bg="lawn green", bd=5, command=adivinar_numero)
                botonAdivinar.place(x=160, y=280)

        botonSeleccionar = Button(Menu_principal, text="Seleccionar/select", command=Ventanaidioma, cursor="hand2",
                                  bd=7, font="arial, 12", fg="lawn green", bg="grey27")
        botonSeleccionar.place(x=270, y=330)


Menu_principal = tk.Tk()
app = menuprincipal(Menu_principal)
app.mainloop()
