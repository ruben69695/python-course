# ================== Math module ===============
print("\n================== Math module ===============\n")

import math

pi = 3.14341

print(round(pi))

print(math.floor(pi))                   # redondear siempre a la baja
print(math.ceil(pi))                    # redondear siempre al alza

abs(-10)                                # distancia del -10 al 0
abs(5)                                  # distancia del 5 al 0
abs(1)                                  # distancia del 1 al 0

numeros = [1, 2, 3]
suma = sum(numeros)                     # suma de todos los elementos de la lista
print(suma)

numeros = [0.99999789, 1, 2, 3]
suma_precisa = math.fsum(numeros)       # suma de todos los elementos de la lista pero esta vez la suma es mas precisa y retorna un flotante
print(suma_precisa)

numero_decimal = 100.123456
t = math.trunc(numero_decimal)          # elimina la parte decimal y retorna un entero
print(t)

pow = math.pow(2, 3)                    # potencia 2 elevado a 3 (2^3), devuelve un floatante para ser más ajustado
print(pow)

sqrt = math.sqrt(9)                     # raíz cuadrada, raíz cuadrada de 9 = 3, devuelve un flotante para ser más ajustado
print(sqrt)

pi = math.pi                            # obtener el numero pi
e = math.e                              # obtener el numero e

print(pi)
print(e)