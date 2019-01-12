# ================== Random module ===============
print("\n================== Random module ===============\n")

import random

aleat = random.random()                         # >= 0. y < 1.0 (retorna un flotante)
print(aleat)

aleat = random.uniform(1, 10)                   # >= 1 y < 10.0 (retorna un flotante)
print(aleat)

aleat = random.randrange(10)                    # >= 0 y < 10 (retorna un entero)
print(aleat)

aleat = random.randrange(0, 101)                # >= 0 y < 101 (retorna un entero)
print(aleat)

aleat = random.randrange(0, 101, 2)             # >= 0 y < 101 (pero siemopre retorna un numero par, retorna numeros multiples de 2
print(aleat)

aleat = random.randrange(0, 101, 5)             # >= 0 y < 101 (retorna numero multiples de 5)
print(aleat)

cadena = "Hola Mundo!"
char = random.choice(cadena)                    # Nos retorna un caracter aleatorio de la cadena
print(char)

numeros = [1,2,3,4,5,6,7,8,9,10]
numero = random.choice(numeros)                 # Nos retorna un elemento aleatorio de la lista
print(numero)

numeros = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(numeros)                         # Nos desordena de forma aleatoria la lista
print(numeros)

numeros = [1,2,3,4,5,6,7,8,9,10]
selected = random.sample(numeros, 4)            # Nos retorna una lista con n (4) elementos escogidos de forma aleatoria de la lista
print(selected)