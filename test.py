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