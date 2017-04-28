#!/usr/bin/env python3
 
# Autor: Fulanito de Tal
# Curso: Estructuras de Datos - Universidad Libre - Seccional Cali
# Programa: parcial1.py
# Fecha: Sat Sep 13 10:15:28 COT 2014
# Descripcion: este programa bla,bla,bla,bla

# Librerias
import pickle

# Constantes

# Clases

class Alumno:
    def __init__(self, codigo, nombre, apellido, edad, ciudad, telefono, notas):
        self.apellido = apellido
        self.ciudad   = ciudad
        self.codigo   = codigo
        self.edad     = edad
        self.nombre   = nombre
        self.notas    = notas
        self.telefono = telefono
    def __str__(self):
        strres = self.nombre + " " + self.apellido
        strres += " (" + self.ciudad + "), " + str(self.edad) + ","

        return strres
    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def promedioEdad(self):
    	return 0

# Variables

# Metodos
def cargar(nombre_archivo):
    """ (string) -> lista
    
    Carga los datos desde el archivo, y retorna una lista de objetos Alumno
    
    """
    lista = list()
    archivo = open(nombre_archivo, 'rb')
    datos = pickle.load(archivo)    
    # ciclo para recorrer datos
    for codigo, dato in datos.items():
        # crear cada objeto
        nombre, apellido, edad, ciudad, telefono, notas = dato
        
        # agregarlo a la lista
        lista.append( Alumno(codigo, nombre, apellido, edad, ciudad, telefono, notas) )
        
    # devuelve la lista
    return lista

def promedioTotal(alumnos):
    
    suma = 0.0
    cantidad = 0
    # recorrer toda la lista
    for alumno in alumnos:
        
        # calcular la suma de las notas, y la cantidad
        suma += alumno.promedio()
        cantidad += 1
    # devuelve el promedio
    return suma / cantidad

def edadPromedioTotal(alumnos):
	suma = 0.0
    cantidad = 0
    # recorrer toda la lista
    for alumno in alumnos:
        
        # calcular la suma de las edades, y la cantidad
        suma += alumno.promedio()
        cantidad += 1
    # devuelve el promedio
    return suma / cantidad

# Pruebas

if __name__ == "__main__":
    import doctest
    doctest.testmod()
   
# Programa Principal

alumnos = cargar('alumnos.pickle')
prom_total = promedioTotal(alumnos)
print('promedio total de notas  :', prom_total)