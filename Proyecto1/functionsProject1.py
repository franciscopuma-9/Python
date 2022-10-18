from Project1BBDD import *
import time
def conectar():
    try:
        conexion()
    except sqlite3.OperationalError:
        messagebox.showerror("Conexion","Ya se creo la base de datos")

def salir(root):
    valor =messagebox.askokcancel("Salir","Desea salir de la app?")

    if valor:
        root.destroy()

def borrar_campos(id,nombre,apellido,password,direccion,textoComentario):
    id.set('')
    nombre.set('')
    apellido.set('')
    password.set('')
    direccion.set('')
    textoComentario.delete("1.0","end")

def crear(id,nombre,apellido,password,direccion,textoComentario):
    create(nombre,apellido,password,direccion,textoComentario)
    borrar_campos(id, nombre, apellido, password, direccion, textoComentario)

def leer(id,nombre,apellido,password,direccion,textoComentario):
    try:
        start = time.time()
        read(id,nombre,apellido,password,direccion,textoComentario)
        print(time.time()-start)
    except IndexError:
        messagebox.showwarning("Error","No existe ese numero de id registrado")

def actualizar(nombre,apellido,password,direccion,textoComentario,id):
    update(nombre,apellido,password,direccion,textoComentario,id)

def borrar(id,nombre,apellido,password,direccion,textoComentario):
    delete(id)
    borrar_campos(id,nombre,apellido,password,direccion,textoComentario)

def licencia():
    messagebox.showinfo("Licencia de Base de Datos","Licencia de Project1 Interfaz grafica con CRUD")

def about():
    messagebox.showinfo("Base de Datos","Project1 Interfaz grafica con CRUD")