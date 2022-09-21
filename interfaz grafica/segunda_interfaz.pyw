from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(0,0)#no se puede cambiar el tamaño de la ventana(True,False) si a lo ancho, no a lo largo

raiz.iconbitmap("muerte.ico") #icono

raiz.geometry("650x350") #alto y ancho

raiz.config(bg="lightblue")

raiz.mainloop()