import sqlite3
from tkinter import messagebox

def conexion():
    miConexion = sqlite3.connect("Basededatos")

    miCursor = miConexion.cursor()

    miCursor.execute('''
        CREATE TABLE BASEDEDATOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50),
        APELLIDO VARCHAR(50),
        PASSWORD VARCHAR(50),
        DIRECCION VARCHAR(50),
        COMENTARIO VARCHAR(500))
    ''')
    messagebox.showinfo("BBDD","Base de datos creada con exito")

def create(nombre,apellido,password,direccion,textoComentario):
    miConexion = sqlite3.connect("Basededatos")

    miCursor = miConexion.cursor()

    texto = f"INSERT INTO BASEDEDATOS VALUES(NULL,'%s','%s','%s','%s','%s')" %(nombre.get(),apellido.get(),password.get(),direccion.get(),textoComentario.get('1.0','end'))

    miCursor.execute(texto)

    miConexion.commit()

    messagebox.showinfo("BBDD","Registro insertado con exito")

def read(id,nombre,apellido,password,direccion,textoComentario):
    miConexion = sqlite3.connect("Basededatos")

    miCursor = miConexion.cursor()
    texto = f"SELECT * FROM BASEDEDATOS WHERE ID= '%s'" %id.get()
    miCursor.execute(texto)
    aux = miCursor.fetchall()

    nombre.set(aux[0][1])
    apellido.set(aux[0][2])
    password.set(aux[0][3])
    direccion.set(aux[0][4])
    textoComentario.delete('1.0','end')
    textoComentario.insert('1.0',aux[0][5])

    miConexion.commit()

def update(nombre,apellido,password,direccion,textoComentario,id):
    miConexion = sqlite3.connect("Basededatos")
    miCursor = miConexion.cursor()

    texto = f"UPDATE BASEDEDATOS SET NOMBRE='%s', APELLIDO='%s', PASSWORD='%s', DIRECCION='%s', COMENTARIO='%s' WHERE ID='%s'"%(nombre.get(),apellido.get(),password.get(),direccion.get(),textoComentario.get('1.0','end'),id.get())

    miCursor.execute(texto)

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con exito")

def delete(id):
    miConexion = sqlite3.connect("Basededatos")
    miCursor = miConexion.cursor()
    texto = f"DELETE FROM BASEDEDATOS WHERE ID='%s'"%id.get()

    miCursor.execute(texto)
    messagebox.showinfo("BBDD", "Registro borrado con exito")
    miConexion.commit()