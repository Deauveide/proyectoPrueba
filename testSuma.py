def suma(a, b):
    """
    Funcion que suma las entradas a y b y da su salida por consola
    """
    c = a + b
    return c


num1 = int(input("Ingrese primer numero"))
num2 = int(input("Ingrese segundo numero"))
print("La suma de", num1, "y", num2, "es", suma(num1, num2))
