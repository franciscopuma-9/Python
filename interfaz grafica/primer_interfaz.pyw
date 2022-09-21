from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(0,0)#no se puede cambiar el tamaño de la ventana(True,False) si a lo ancho, no a lo largo

raiz.iconbitmap("muerte.ico") #icono

#raiz.geometry("650x350") #alto y ancho

raiz.config(bg="black")#fondo

miFrame = Frame()

#miFrame.pack(side="right",anchor="n")#side = right/left/bottom/top y si necesito otro uso anchor n/e/o/s (puntos cardinales)
#miFrame.pack(fill="x") #expande horizontalmente
#miFrame.pack(fill="y", expand="True") #expande verticalmente
#miFrame.pack(fill="both", expand="True") # se expande para todos lados
miFrame.pack()

miFrame.config(bg='blue')

miFrame.config(width="650",height="350")

miFrame.config(bd=35)#tamanio borde

miFrame.config(relief="sunken")# borde diferente

miFrame.config(cursor="pirate")#cambia el cursor en el frame hand2

raiz.mainloop()