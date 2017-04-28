# Ejemplo del uso de SQLite3

import sqlite3

# Crear la base de datos y conectarse a ella
connector = sqlite3.connect("menu.dat")

# Usar un cursor para comunicarse con la base de datos
cursor = connector.cursor()

# Ejecutar un comando, crear la tabla
cursor.execute("""
   CREATE TABLE menu (
      codigo integer PRIMARY KEY,
      tipo stringvar(20),
      nombre stringvar(30),
      precio integer
   )
""")

# Insertar datos en la base de datos
cursor.execute(""" INSERT INTO menu VALUES (10, "entrada", "ensalada", 2000) """)
cursor.execute(""" INSERT INTO menu VALUES (11, "entrada", "sopa", 3000) """)
cursor.execute(""" INSERT INTO menu VALUES (20, "principio", "arroz", 1000) """)
cursor.execute(""" INSERT INTO menu VALUES (21, "principio", "frijoles", 2500) """)
cursor.execute(""" INSERT INTO menu VALUES (22, "principio", "lentejas", 2000) """)
cursor.execute(""" INSERT INTO menu VALUES (30, "fuerte", "carne", 9000) """)
cursor.execute(""" INSERT INTO menu VALUES (31, "fuerte", "pollo", 7500) """)
cursor.execute(""" INSERT INTO menu VALUES (32, "fuerte", "pescado", 6000) """)
cursor.execute(""" INSERT INTO menu VALUES (40, "postre", "helado", 2000) """)
cursor.execute(""" INSERT INTO menu VALUES (41, "postre", "torta", 3000) """)
cursor.execute(""" INSERT INTO menu VALUES (42, "postre", "mazamorra", 1500) """)
cursor.execute(""" INSERT INTO menu VALUES (50, "bebida", "jugo", 500) """)
cursor.execute(""" INSERT INTO menu VALUES (51, "bebida", "gaseosa", 1500) """)
cursor.execute(""" INSERT INTO menu VALUES (52, "bebida", "vino", 2500) """)
cursor.execute(""" INSERT INTO menu VALUES (53, "bebida", "aguapanela", 500) """)

# Grabar los datos al disco
connector.commit()

# Cerrar la conexion a la base de datos
connector.close()