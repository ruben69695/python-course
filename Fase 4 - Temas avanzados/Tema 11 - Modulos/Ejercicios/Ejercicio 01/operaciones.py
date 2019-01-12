def suma(a, b):
    try:
        return a + b
    except TypeError:
        raise TypeError("Error: parametros incorrectos, debés pasar numeros")

def resta(a, b):
    try:
        return a - b
    except TypeError:
        raise TypeError("Error: parametros incorrectos, debés pasar numeros")

def producto(a, b):
    try:
        return a * b
    except TypeError:
        raise TypeError("Error: parametros incorrectos, debés pasar numeros")        

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: no puedes dividir un numero popr 0")
    except TypeError:
        raise TypeError("Error: parametros incorrectos, debés pasar numeros")        

