# librerias
import random

# diccionario : lista de listas
menu = { 'entrada' : [ ['ensalada', 2000], ['sopa', 3000] ],
         'principio' : [ ['arroz', 1000], ['frijoles', 2500], ['lentejas', 2000] ],
         'fuerte' : [ ['carne', 9000], ['pollo', 7500], ['pescado', 6000] ],
         'postre' : [ ['helado', 2000], ['torta', 3000], ['mazamorra', 1500] ],
         'bebida' : [ ['jugo', 500], ['gaseosa', 1500], ['vino', 2500], ['aguapanela', 500] ] }

def escoger(menu, tipo):
   """ (diccionario, string) -> lista

   Retorna una opcion aleatorio para el tipo de plato del menu

   """
   opciones = menu[tipo]
   cual = random.randint(0, len(opciones)-1)
   opcion = opciones[cual]
   return opcion

def sugerencia(menu):
   """ (diccionario) -> None

   Imprime un menu completo en forma aleatorio, incluido el total a pagar

   """
   llaves = menu.keys()
   total = 0
   print("*** Sugerencia del Día ***")
   for tipo in llaves:
      opcion = escoger(menu, tipo)
      total += opcion[1]
      print(tipo, ":", opcion[0], " x $", opcion[1])
   print("total =", total)

# Pruebas

if __name__ == '__main__':
   import doctest
   doctest.testmod()

# Principal

sugerencia(menu)