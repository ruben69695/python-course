import random

def leer_numero():
    numerosCorrectos = False

    while(not numerosCorrectos):
        try:
            numIni = int(input("Introduce el numero inicial: "))
            numFinal = int(input("Introduce el numero final: "))
            mensaje = input("Introduce el mensaje a mostrar: ")

            if(numIni > numFinal):
                print("El numero inicial tiene que ser mas pequeño que el final, para que puedas continuar con al ejecucicón del programa")
            elif (mensaje == ""):
                print("Es necesario escribir un mensaje")
            else:
                numerosCorrectos = True
        except TypeError:
            raise TypeError("los parametros son incorrectos, revisalos")
    
    num = generarNumero(numIni, numFinal)

    print("{}\n{}".format(mensaje, num))


def generarNumero(n1, n2):
    return random.randrange(n1, n2)

leer_numero()