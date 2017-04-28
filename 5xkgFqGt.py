#!/usr/bin/env python3

# Author: Diego Fernando Marin
# Program: estudiantes.py
# Date: Sat Sep  3 10:10:40 EDT 2016
# Description: this program do yadda-yadda-yadda

# Classes
class Materia:
    # constructor
    def __init__(self, codigo, nombre):
        # atributos
        self.codigo = codigo
        self.nombre = nombre
        self.notas = []
    # toString
    def __str__(self):
        return "{}: {} = {}\n".format(self.codigo, self.nombre, self.calculaDefinitiva())
    # Metodos
    # adicionar notas
    def adicionaNota(self, nota):
        self.notas.append(nota)
    # calcular definitiva
    def calculaDefinitiva(self):
        total = 0
        cantidad = 0
        for nota in self.notas:
            total += nota
            cantidad += 1
        return total / cantidad

class Estudiante:
    # constructor
    def __init__(self, codigo, nombre):
        # atributos
        self.codigo = codigo
        self.nombre = nombre
        self.materias = []
    # toString
    def __str__(self):
        strres = "{}: {}\n".format(self.codigo, self.nombre)
        for materia in self.materias:
            strres += str(materia)
        return strres
    # Metodos
    # adicionar materias
    def adicionaMateria(self, materia):
        self.materias.append(materia)
    # calcular promedio
    def calculaPromedio(self):
        total = 0
        cantidad = 0
        for materia in self.materias:
            total += materia.calculaDefinitiva()
            cantidad += 1
        return total / cantidad

# Programa Principal
def main():
    # crea la lista vacia de estudiantes
    estudiantes = []
    # crea cada uno de los estudiantes
    juan = Estudiante(130923, "Juan")
    maria = Estudiante(140219, "Maria")
    teresa = Estudiante(146754, "Teresa")
    alberto = Estudiante(131845, "Alberto")
    # crea las materias
    m1 = Materia(1, "Calculo")
    m1.adicionaNota(3.5)
    m1.adicionaNota(2.5)
    m1.adicionaNota(4.5)
    m2 = Materia(2, "Fisica")
    m2.adicionaNota(3.5)
    m2.adicionaNota(4.5)
    m3 = Materia(3, "Programacion")
    m3.adicionaNota(3.1)
    m3.adicionaNota(3.4)
    # Adiciona las materias a los estudiantes
    juan.adicionaMateria(m1)
    teresa.adicionaMateria(m2)
    teresa.adicionaMateria(m3)
    # adiciona los estudiantes a la lista
    estudiantes.append(juan)
    estudiantes.append(maria)
    estudiantes.append(teresa)
    estudiantes.append(alberto)
    # imprime los estudiantes
    for estudiante in estudiantes:
        print(estudiante)

# Test
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()