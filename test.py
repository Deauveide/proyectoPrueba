def mcd(a, b):
    """
    Funcion que calcula el maximo comun divisor
    Dos numeros como entrada y el mcd de ambos como salida.
    """
    resto = 0
    while (b > 0):
        resto = b
        b = a % b
        a = resto
    return a


num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce el tercer numero: "))

print("El máximo común divisor de ", num1, " y ", num2, " es ", mcd(num1, num2))
