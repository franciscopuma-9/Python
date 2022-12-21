import sqlite3


conexion = sqlite3.connect("Una base de datos")


cursor = conexion.cursor()



conexion.commit()


conexion.close()