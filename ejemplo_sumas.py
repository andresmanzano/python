
def suma1(num1, num2):
    """ (int, int) -> int
    
    Retorna la suma de 2 numeros
    
    >>> suma1(0, 10)
    10
    >>> suma1(-5, 5)
    0
    
    """
    return num1 + num2

def suma2(lista):
    """ (list) -> int
    
    Retorna la suma de todos los numeros en la lista
    
    >>> suma2([0, 10])
    10
    >>> suma2([-5, 5])
    0
    
    """
    total = 0
    for num in lista:
        total += num            # total = total + num
    return total

# Pruebas

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Principal

print( "sumas" )
print( suma1(100, 510) )
lista = [10, -5, 20, 0, -45, 89, 1, 7, 3, 9, -4]
print( lista, "=", suma2( lista ) )