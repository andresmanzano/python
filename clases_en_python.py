
class Mueble:
    # Constructor
    def __init__(self, material, color, altura, ancho, fondo, patas):
        # Atributos
        self.material = material
        self.color = color
        self.altura = altura
        self.ancho = ancho
        self.fondo = fondo
        self.patas = patas
    # ToString
    def __str__(self):
        strres = "Mueble de " + self.material
        strres += ", de color " + self.color
        strres += " con " + str(self.patas) + " patas"
        return strres
    # Metodos
    def darPrecio(self):
        return self.altura * self.ancho * self.fondo * 50
    def cambiarColor(self, nuevo_color):
        self.color = nuevo_color
        
class Silla(Mueble):
    # Constructor
    def __init__(self, material, color, altura, ancho, fondo, patas, base, espaldar, ruedas):
        super(Silla, self).__init__(material, color, altura, ancho, fondo, patas)
        self.base = base
        self.espaldar = espaldar
        self.ruedas = ruedas
    # ToString
    def __str__(self):
        strres  = "Silla de " + str(self.patas) + " patas "
        if self.base:
            strres += "con base, "
        else:
            strres += "sin base, "
        if self.espaldar:
            strres += "con espaldar, "
        else:
            strres += "sin espaldar, "
        strres += "fabricada con " + self.material + " y "
        strres += "de color " + self.color + "."
        return strres
    
mueble1 = Mueble("madera", "amarillo", 2, 1, 1, 4)
mueble2 = Mueble("aluminio", "plata", 3, 2, 1, 6)
silla1 = Silla("hierro", "negro", 0.8, 0.5, 0.5, 1, True, True, False)
silla2 = Silla("plastico", "blanco", 0.8, 0.5, 0.5, 4, True, False, False)

print(mueble1)
print(mueble2, " y su precio es ", mueble1.darPrecio())

print(silla1)
print(silla2, " y su precio es ", silla2.darPrecio())