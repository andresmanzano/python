
import pickle

def promedio(lista):
    """ list(number) -> number

    Calcula el promedio de los numeros en la lista

    """
    return sum(lista) / len(lista)

def mostrar(alumnos):
    """ dict(string, tuple) -> None
    
    Muestra los datos de un diccionario formada por alumno:tupla
    
    """
    for codigo, datos in alumnos.items():
        nombre, apellido, edad, ciudad, telefono, notas = datos
        print("{0}: {1}, {2:.2f}".format(codigo, nombre+" "+apellido, promedio(notas)))

def buscar(buscado, alumnos):
    """ string, dict(string, tuple) -> tuple, None
    
    Busca un alumno un diccionario {alumno:tupla}, a traves del nombre
    
    """
    listado = []
    for codigo, datos in alumnos.items():
        nombre, apellido, edad, ciudad, telefono, notas = datos
        if buscado == nombre:
            listado.append( (nombre, edad, ciudad, telefono) )
    return listado

file = open('alumnos.pickle', 'rb')
alumnos = pickle.load(file)

mostrar(alumnos)
print('total alumnos :', len(alumnos))

buscados = buscar('simon', alumnos)
print(buscados)