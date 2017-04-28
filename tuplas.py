# Tipos de Datos compuestos: Lista, Conjunto, Diccionario

def concat(lista):
    """ (list) -> string
    
    Concatena las cadenas en la lista
    
    >>> concat(["abc", "def"])
    'abcdef'
    >>> concat(["uno", "", " ", "dos"])
    'uno dos'
    
    """
    resultado = ""
    for cadena in lista:
        resultado += str(cadena)
    return resultado

def promedio(alumno):
    """ list( apellido, nombre, fecha, notas = list( n1, n2, n3) ) -> float

    Retorna el promedio de notas para un alumno

    >>> promedio( [ "velez", "juan", 1992, [ 3.5, 4.0, 2.1] ] )
    3.09
    
    """
    ##    apellido = alumno[ 0 ]
    ##    nombre = alumno[ 1 ]
    ##    fecha = alumno[ 2 ]
    notas = alumno[ 3 ]
    return 0.3 * notas[0] + 0.3 * notas[1] + 0.4 * notas[2]  

def promedios(lista):
    """ list(alumnos) -> None

    Imprimir el listado de alumnos y su promedio

    """
    for codigo in alumnos:
        alumno = alumnos[codigo]
        print(alumno[0], alumno[1], alumno[3], "=", promedio(alumno) )
    
# Pruebas

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Principal

lst1 = ["Universidad", "Libre", "Seccional", "Cali"]
print( lst1, "=", concat(lst1) )

st1 = { 10, -5, 10, 20, 0, -45, 1, 89, 1, 7, 1, 3, 9, -4, 20, -45 }
lst2 = [ 10, -5, 10, 20, 0, -45, 1, 89, 1, 7, 1, 3, 9, -4, 20, -45 ]
print( st1 )
print( lst2 )
print( lst2[5] )

dct1 = { "ibm": "International Business Machines",
         "acm": "Association for Computer Machinery",
         "ieee": "Institute for Electric and Electronic Engineers",
         "cs": "Computer Society",
         "rgb": "Red, Green, Blue" }
print( dct1["ieee"] )

alumnos = { 1105: [ "velez", "juan", 1992, [ 3.5, 4.0, 2.1] ],
            1107: [ "perez", "julio", 1993, [ 3.7, 4.8, 3.2] ],
            1113: [ "lopez", "carlos", 1991, [ 3.9, 3.2, 3.5] ],
            1142: [ "diaz", "andres", 1990, [ 4.5, 4.1, 4.1] ] }
print( alumnos )
print( alumnos[1105] )
print( promedios(alumnos) )
print( promedio(alumnos[1105]) )

# Calcular la suma de la serie 2*N+1 desde -5 hasta 50

def suma_serie():
    acum = 0
    for N in range(-5, 51):
        acum += (2*N+1)
    return acum

print( suma_serie() )

def sumatoria(func, inicial, final):
    acum = 0
    for N in range(inicial, final+1):
        acum += func(N)
    return acum

def serie1(num):
    return 2*num+1

print( sumatoria( serie1, -5, 50) )
print( sumatoria( serie1, 50, 100) )

# Calcular la suma de la serie N**2/2 desde -100 hasta 9

def serie2(num):
    return (num**2)/2

print( sumatoria( serie2, -100, 9) )