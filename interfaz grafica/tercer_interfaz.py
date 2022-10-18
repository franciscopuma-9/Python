from tkinter import *

root= Tk()

miFrame = Frame(root, width=500,height=400)

miFrame.pack()

miImagen=PhotoImage(file='fondogif.gif')

#miLabel = Label(miFrame,text="este es el texto",fg='red',bg="black",font=("Comic Sans MS",18))
#miLabel.place(x=100,y=200)#ponerlo en algun lugar cualquiera

Label(miFrame,image=miImagen).place(x=100,y=100)

#Label(miFrame,text="este es el texto").place(x=100,y=200)#abreviado
root.mainloop()