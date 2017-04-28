# Constantes
MASCULINO = True
FEMENINO = False

class Persona:
    #Constructor
    def __init__(self, nombre, apellido, sexo, edad, ciudad ):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        self.ciudad = ciudad
        self.inventario = []
    #ToString
    def __str__(self):
        strres = self.nombre + " " + self.apellido
        strres += " (" + self.ciudad + "), " + str(self.edad) + ","
        if self.sexo == MASCULINO:
            strres += "M"
        else:
            strres += "F"
        strres += " : " + str(self.inventario)
        return strres
    
    #Metodos
    def agregar(self,elemento):
        self.inventario.append(elemento)
    
        
def Ejemplo():
    luis = Persona("Luis", "Perez", MASCULINO, 21, "Cali")
    diana = Persona("Diana", "Lopez", FEMENINO, 19, "Bogota")
    print(luis)
    print(diana)
    luis.agregar("Lapiz")
    luis.agregar("Borrador")
    luis.agregar("Papel")
    diana.agregar("Celular")
    print(luis)
    print(diana)
    
Ejemplo()