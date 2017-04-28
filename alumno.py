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
        lista.append( dato )
        
    # devuelve la lista
    return lista

def promedioTotal(alumnos):
    """ list(Alumno) -> number

    Calcula el promedio total de las notas de los alumnos en la lista

    >>> alumnos = list()
    >>> alumnos.append(Alumno(51706891, "maria", "galarza", 19, "medellin", 3317692, [3.8, 2.6, 1.0, 2.5, 3.2]))
    >>> alumnos.append(Alumno(41380016, "beatriz", "jacome", 21, "cali", 8871130, [3.7, 3.6, 1.5, 4.1, 1.7]))
    >>> promedioTotal(alumnos)
    2.77
    >>> alumnos = list()
    >>> alumnos.append(Alumno(4148316, "jaime", "diaz", 20, "cali", 4459988, [2.2, 4.2, 4.9, 4.5, 3.1]))
    >>> alumnos.append(Alumno(98523512, "rodrigo", "romero", 21, "cali", 4481870, [4.6, 4.9, 3.9, 4.1, 5.0]))
    >>> promedioTotal(alumnos)
    4.140000000000001
    
    """
    suma = 0.0
    cantidad = 0
    # recorrer toda la lista
    for alumno in alumnos:

        print(alumno)
        # calcular la suma de las notas, y la cantidad
        #suma += alumno.promedio()
        #cantidad += 1
    # devuelve el promedio
    #return suma / cantidad

# Pruebas

if __name__ == "__main__":
    import doctest
    doctest.testmod()
   
# Programa Principal

alumnos = cargar('alumnos.pickle')
prom_total = promedioTotal(alumnos)
print('promedio total de notas  :', prom_total)