#!/usr/bin/env python3

# Autor: Fulanito de Tal
# Programa: consultar_ciudades.py
# Fecha: Sat Apr 2 07:48:18 COT 2016
# Descripcion: este programa consulta una base de datos SQLite

# Libreria SQLite3
import sqlite3

# Conectarse con la base de datos
connector = sqlite3.connect("C:\\Python\\Code\\ciudades.sqlite")

# Usar un cursor para comunicarse con la base de datos
cursor = connector.cursor()

# Realizar la consulta
cursor.execute("""
    SELECT *
    FROM ciudades
    WHERE poblacion > 2000000
    ORDER BY 4
""")

# traer la lista con todos los resultados de la consulta
ciudades = cursor.fetchall()

# recorrer la lista para procesarla
for ciudad in ciudades:
    codigo, nombre, poblacion, latitud, longitud = ciudad
    print("{} [{},{}] = {}".format(nombre, latitud, longitud, poblacion))

# Cerrar la conexion con la base de datos
connector.close()