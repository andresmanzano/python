#!/usr/bin/env python3

# Autor: Fulanito de Tal
# Programa: listas.py
# Fecha: Sat Mar 05 08:36:18 COT 2016
# Descripcion: Ejemplos de Listas

import random

def par(numero):
    """ (numero) -> booleano

    retorna True si numero es par, False de lo contrario
    
    >>> par(2)
    True
    >>> par(5)
    False

    """
    return (numero % 2) == 0

def multiplo3(numero):
    """ (numero) -> booleano

    retorna True si numero es multiplo de 3, False de lo contrario
    
    >>> multiplo3(6)
    True
    >>> multiplo3(5)
    False

    """
    return (numero % 3) == 0

def separar(metodo, lista):
    """ (funcion, lista) -> (lista, lista)

    retorna 2 listas, separando los valores de acuerdo al metodo
    
    >>> separar(par, [])
    ([], [])
    >>> separar(par, [2, 4, 6])
    ([2, 4, 6], [])
    >>> separar(par, [1, 3, 5])
    ([], [1, 3, 5])
    >>> separar(par, [1, 2, 3, 4, 5, 6])
    ([2, 4, 6], [1, 3, 5])

    """
    lst1 = []
    lst2 = []
    for numero in lista:
        if metodo(numero):
            lst1.append(numero)
        else:
            lst2.append(numero)
    return lst1, lst2

# Pruebas
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
# Programa Principal

numeros = random.sample(range(1000000), 10000)
pares, impares = separar(par, numeros)
print("los pares son", pares)
print("los impares son", impares)

m3, no_m3 = separar(multiplo3, numeros)
print("los multiplos de 3 son", m3)
print("los No multiplos de 3 son", no_m3)