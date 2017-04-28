#!/usr/bin/env python3

# Autor: Fulanito de Tal
# Programa: crear_tabla.py
# Fecha: Sat Apr 2 07:48:18 COT 2016
# Descripcion: este programa crea una tabla en la base de datos SQLite

# Libreria SQLite3
import sqlite3

# Conectarse con la base de datos
connector = sqlite3.connect("C:\\Python\\Code\\ciudades.sqlite")

# Usar un cursor para comunicarse con la base de datos
cursor = connector.cursor()

# Ejecutar un comando para crear la tabla Ciudades
cursor.execute("""
    CREATE TABLE ciudades (
        codigo integer PRIMARY KEY,
        nombre stringvar(30),
        poblacion integer,
        latitud real,
        longitud real
    )
""")

# Insertar los datos en la tabla
cursor.execute(""" INSERT INTO ciudades VALUES (1,"New York",8175133,40.71455,-74.007124) """)
cursor.execute(""" INSERT INTO ciudades VALUES (2,"Los Angeles",3792621,34.05349,-118.245323) """)
cursor.execute(""" INSERT INTO ciudades VALUES (3,"Chicago",2695598,45.37399,-92.888759) """)
cursor.execute(""" INSERT INTO ciudades VALUES (4,"Houston",2099451,41.337462,-75.733627) """)
cursor.execute(""" INSERT INTO ciudades VALUES (5,"Philadelphia",1526006,37.15477,-94.486114) """)
cursor.execute(""" INSERT INTO ciudades VALUES (6,"Phoenix",1445632,32.46764,-85.000823) """)
cursor.execute(""" INSERT INTO ciudades VALUES (7,"San Antonio",1327407,37.706576,-122.440612) """)
cursor.execute(""" INSERT INTO ciudades VALUES (8,"San Diego",1307402,37.707815,-122.466624) """)
cursor.execute(""" INSERT INTO ciudades VALUES (9,"Dallas",1197816,40.636,-91.168309) """)
cursor.execute(""" INSERT INTO ciudades VALUES (10,"San Jose",945942,41.209716,-112.003047) """)
cursor.execute(""" INSERT INTO ciudades VALUES (11,"Jacksonville",821784,30.2887,-81.391794) """)
cursor.execute(""" INSERT INTO ciudades VALUES (12,"Indianapolis",820445,39.766911,-86.149963) """)
cursor.execute(""" INSERT INTO ciudades VALUES (13,"Austin",790390,28.973405,-95.961284) """)
cursor.execute(""" INSERT INTO ciudades VALUES (14,"San Francisco",805235,28.371795,-82.187909) """)
cursor.execute(""" INSERT INTO ciudades VALUES (15,"Columbus",787033,41.258735,-91.374424) """)
cursor.execute(""" INSERT INTO ciudades VALUES (16,"Fort Worth",741206,38.0016,-89.066334) """)
cursor.execute(""" INSERT INTO ciudades VALUES (17,"Charlotte",731424,39.09931,-76.817799) """)
cursor.execute(""" INSERT INTO ciudades VALUES (18,"Detroit",713777,42.408871,-83.002647) """)
cursor.execute(""" INSERT INTO ciudades VALUES (19,"El Paso",649121,41.645415,-91.599794) """)
cursor.execute(""" INSERT INTO ciudades VALUES (20,"Memphis",646889,35.149681,-90.04892) """)
cursor.execute(""" INSERT INTO ciudades VALUES (21,"Boston",617594,41.202364,-112.032315) """)
cursor.execute(""" INSERT INTO ciudades VALUES (22,"Seattle",608660,45.520615,-123.873929) """)
cursor.execute(""" INSERT INTO ciudades VALUES (23,"Denver",600158,32.96438,-102.829919) """)
cursor.execute(""" INSERT INTO ciudades VALUES (24,"Baltimore",620961,39.284664,-76.62022) """)
cursor.execute(""" INSERT INTO ciudades VALUES (25,"Washington",601723,38.899101,-77.028999) """)
cursor.execute(""" INSERT INTO ciudades VALUES (26,"Nashville Davidson",601222,45.304048,-121.756365) """)
cursor.execute(""" INSERT INTO ciudades VALUES (27,"Louisville Jefferson",597337,45.304048,-121.756365) """)
cursor.execute(""" INSERT INTO ciudades VALUES (28,"Milwaukee",594833,43.041809,-87.906837) """)
cursor.execute(""" INSERT INTO ciudades VALUES (29,"Portland",583776,45.52186,-123.882594) """)
cursor.execute(""" INSERT INTO ciudades VALUES (30,"Oklahoma City",579999,39.05514,-96.816104) """)
cursor.execute(""" INSERT INTO ciudades VALUES (31,"Las Vegas",583756,40.4879,-85.609999) """)
cursor.execute(""" INSERT INTO ciudades VALUES (32,"Albuquerque",545852,35.084179,-106.648643) """)
cursor.execute(""" INSERT INTO ciudades VALUES (33,"Tucson",520116,41.644727,-91.601947) """)
cursor.execute(""" INSERT INTO ciudades VALUES (34,"Fresno",494665,38.645741,-77.321863) """)
cursor.execute(""" INSERT INTO ciudades VALUES (35,"Sacramento",466488,38.915291,-121.594651) """)
cursor.execute(""" INSERT INTO ciudades VALUES (36,"Long Beach",462257,29.748022,-94.827603) """)
cursor.execute(""" INSERT INTO ciudades VALUES (37,"Kansas City",459787,39.016682,-96.864303) """)
cursor.execute(""" INSERT INTO ciudades VALUES (38,"Mesa",439041,30.686452,-97.700842) """)
cursor.execute(""" INSERT INTO ciudades VALUES (39,"Virginia Beach",437994,36.767408,-76.047707) """)
cursor.execute(""" INSERT INTO ciudades VALUES (40,"Atlanta",420003,37.691375,-122.454979) """)
cursor.execute(""" INSERT INTO ciudades VALUES (41,"Colorado Springs",416427,40.17676,-75.547839) """)
cursor.execute(""" INSERT INTO ciudades VALUES (42,"Raleigh",403892,41.132609,-73.977405) """)
cursor.execute(""" INSERT INTO ciudades VALUES (43,"Omaha",408958,41.260689,-95.94059) """)
cursor.execute(""" INSERT INTO ciudades VALUES (44,"Miami",399457,41.63636,-91.501889) """)
cursor.execute(""" INSERT INTO ciudades VALUES (45,"Tulsa",391906,39.095215,-121.613384) """)
cursor.execute(""" INSERT INTO ciudades VALUES (46,"Oakland",390724,38.334108,-87.345139) """)
cursor.execute(""" INSERT INTO ciudades VALUES (47,"Cleveland",396815,36.640475,-82.582569) """)
cursor.execute(""" INSERT INTO ciudades VALUES (48,"Minneapolis",382578,44.979031,-93.264931) """)
cursor.execute(""" INSERT INTO ciudades VALUES (49,"Wichita",382368,37.686981,-97.335579) """)
cursor.execute(""" INSERT INTO ciudades VALUES (50,"Arlington",365438,41.29525,-88.25278) """)

# Grabar los datos al disco
connector.commit()

# Cerrar la conexion con la base de datos
connector.close()