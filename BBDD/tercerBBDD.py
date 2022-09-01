import sqlite3

miConexion = sqlite3.connect("GestionProduccion")

miCursor = miConexion.cursor()

# miConexion.execute('''  #CREATE
#     CREATE TABLE PRODUCTO (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#     PRECIO INTEGER,
#     SECCION VARCHAR(20))
# ''')
#
# productos = [
#     ("pelota", 20, "jugueteria"),
#     ("pantalon", 15, "confeccion"),
#     ("destornillador", 25, "ferreteria"),
#     ("jarron", 45, "ceramica"),
#     ("pantalones", 35, "confeccion"),
# ]
# miCursor.executemany("INSERT INTO PRODUCTO VALUES (NULL,?,?,?)",productos)

# miCursor.execute("SELECT * FROM PRODUCTO WHERE SECCION= 'confeccion'") #READ
#
# productos = miCursor.fetchall()
# print(productos)

# miCursor.execute("UPDATE PRODUCTO SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'") #UPDATE

miCursor.execute("DELETE FROM PRODUCTO WHERE ID=5")
miConexion.commit()

miConexion.close()