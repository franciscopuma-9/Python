from tkinter import *
from tkinter import filedialog


root = Tk()

def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir",initialdir="C:/Users/franc/Desktop/Nueva carpeta",filetypes=(("Ficheros de Excel","*.xlsx"),
                                                                                                                    ("Ficheros de texto","*.txt"),
                                                                                                                    ("Todos los ficheros","*.*")))

    print(fichero)

Button(root,text="Abrir fichero",command=abreFichero).pack()
root.mainloop()