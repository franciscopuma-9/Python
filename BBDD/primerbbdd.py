import sqlite3

miConexion = sqlite3.connect("Primera base")

miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") crea tablas

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('Pelota', 15, 'deportes')")

# variosProductos=[
#     ("Camiseta", 10, "deportes"),
#     ("Jarron", 90, "ceramica"),
#     ("Camion", 20, "Jugueteria")
#
# ]
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS WHERE PRECIO=10")

variosProductos = miCursor.fetchall() #devuelve una lista de los productos
print(variosProductos)
for valor in variosProductos:
    print(valor)



miConexion.commit()


miConexion.close()