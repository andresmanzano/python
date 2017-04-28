# Ejemplo del uso de SQLite3

import sqlite3

# Crear la base de datos y conectarse a ella
connector = sqlite3.connect("menu.dat")

# Usar un cursor para comunicarse con la base de datos
cursor = connector.cursor()

# Realizar una consulta
cursor.execute("""
   SELECT * 
   FROM menu
""")
# print(cursor.fetchall())

for datos in cursor:
   codigo, tipo, nombre, precio = datos
   print("{}: {}, {} = ${}".format(codigo, tipo, nombre, precio))

# Realizar una consulta: Cuantos productos hay de tipo bebida
cursor.execute("""
   SELECT COUNT(nombre)
   FROM menu
   WHERE tipo = "bebida"
""")
print("bebidas:", cursor.fetchall())

# Realizar una consulta: En promedio cuanto cuestan los platos fuertes
cursor.execute("""
   SELECT AVG(precio)
   FROM menu
   WHERE tipo = "fuerte"
""")
print("promedio:", cursor.fetchall())

# Cerrar la conexion a la base de datos
connector.close()