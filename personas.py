# Constantes

# CAMPOS
NIT = 0
NOMBRES = 1
APELLIDO1 = 2
APELLIDO2 = 3
SEXO = 4
TELEFONO = 5
DIRECCION = 6
CIUDAD = 7
FECHA_NAC = 8
LUGAR_NAC = 9
CORREO = 10

# SEXO
MASCULINO = True
FEMENINO = False

# Persona
class Persona:
    # Atributos
    nit = 0
    nombres = ""
    apellido1 = ""
    apellido2 = ""
    sexo = MASCULINO
    telefono = ""
    direccion = ""
    ciudad = ""
    fecha_nac = ""
    lugar_nac = ""
    correo = ""
    # Constructor
    def __init__(self, lista):
        self.nit = int(lista[NIT])
        self.nombres = lista[NOMBRES]
        self.apellido1 = lista[APELLIDO1]
        self.apellido2 = lista[APELLIDO1]
        self.sexo = lista[SEXO]== 'M'
        self.telefono = lista[TELEFONO]
        self.direccion = lista[DIRECCION]
        self.ciudad = lista[CIUDAD]
        self.fecha_nac = lista[FECHA_NAC]
        self.lugar_nac = lista[LUGAR_NAC]
        self.correo = lista[CORREO]
    # ToString
    def __str__(self):
        strres = str(self.nit) + ", "
        strres += self.nombres + " " + self.apellido1 + " " + self.apellido2 + ", "
        if self.sexo == MASCULINO:
            strres += "M, "
        else:
            strres += "F, "
        strres += self.telefono + ", " + self.direccion + " - " + self.ciudad + ", " 
        strres += self.fecha_nac + " " + self.lugar_nac + ", " + self.correo
        return strres
    # Metodos
    def dar(self, campo):
        if campo == NIT:
            return self.nit
        elif campo == NOMBRES:
            return self.nombres
        elif campo == APELLIDO1:
            return self.apellido1
        elif campo == APELLIDO2:
            return self.apellido2
        elif campo == SEXO:
            return self.sexo
        elif campo == TELEFONO:
            return self.telefono
        elif campo == DIRECCION:
            return self.direccion
        elif campo == CIUDAD:
            return self.ciudad
        elif campo == FECHA_NAC:
            return self.fecha_nac
        elif campo == LUGAR_NAC:
            return self.lugar_nac
        elif campo == CORREO:
            return self.correo


def cargarPersonas(nombre_archivo):
    ''' String -> list
    Retorna la lista de Personas cargadas desde el archivo
    '''
    archivo = open(nombre_archivo, "r")
    personas = []
    for linea in archivo:
        lista = linea.split("|")
        personas.append(Persona(lista))
    return personas

def contar(lista):
    ''' list -> int
    Retorna la cantidad de Personas en la lista
    '''
    return len(lista)

def seleccionar(personas, campo, valor):
    ''' list, string, string -> lista
    Retorna una lista con las Personas seleccionadas cuyo campo sea igual a valor
    '''
    seleccionadas = []
    for persona in personas:
        if persona.dar(campo) == valor:
            seleccionadas.append(persona)
    return seleccionadas

def diferentes(personas, campo):
    ''' list, string -> conjunto
    Retorna un conjunto con todos los valores diferentes de Campo en Personas
    '''
    difs = set() # Conjunto Vacio
    for persona in personas:
        difs.add(persona.dar(campo))
    return difs

def dominios(personas):
    ''' list -> conjunto
    Retorna un conjunto con todos los dominios diferentes en Personas
    '''
    doms = set() # Conjunto Vacio
    for persona in personas:
        pos = persona.dar(CORREO).find("@") + 1
        doms.add(persona.dar(CORREO)[pos:])
    return doms

# Principal
personas = cargarPersonas("personas.txt")

print("Cuantas Personas hay? ", contar(personas))

print("Cuantos Hombres hay? ", contar(seleccionar(personas, SEXO, MASCULINO)))
print("Cuantas Mujeres hay? ", contar(seleccionar(personas, SEXO, FEMENINO)))

print("Cuantas Personas hay en Cali? ", contar(seleccionar(personas, CIUDAD, "CALI")))
print("Cuantas Personas hay en Medellin? ", contar(seleccionar(personas, CIUDAD, "MEDELLIN")))
print("Cuantas Mujeres hay en Medellin? ", contar(seleccionar(seleccionar(personas, CIUDAD, "MEDELLIN"), SEXO, FEMENINO)))

print("Cuantas Ciudades diferentes hay? ", contar(diferentes(personas, CIUDAD)))
print("Cuantos Lugares de nacimiento diferentes hay? ", contar(diferentes(personas, LUGAR_NAC)))
print("Cuantos Dominios de correo diferentes hay? ", contar(dominios(personas)))

print("Cuantos Dominios son '.co'? ")

print("Cuantos tienen menos de 30 anos? ")
print("Quienes tienes entre 30 y 40 anos? ")
print("Quienes nacieron entre Junio y Agosto? ")

print("Cuales Mujeres tiene Apellidos que comiencen por 'B' o 'V'? ")
print("Cuales Hombres, de Medellin, tienen Nombres que comiencen por 'D'? ")

print("Quienes tienen ambos Apellidos iguales? ")
print("Quienes nacidos en Jamundi, viven en Cali? ")
print("Quienes nacidos en Cali, viven en una Ciudad diferente? ")
print("Quienes son Mujeres y tienen cuenta de correo en Hotmail? ")