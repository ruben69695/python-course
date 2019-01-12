print("""
1) Crea el siguiente módulo:
El módulo se denominará operaciones y contendrá 4 funciones para realizar una suma, una resta, un producto y una division entres dos números. 
Todas ellas devolverán el resultado. En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para evitar que se 
quede bloqueada una funcionalidad, eso incluye: 

- TypeError: En caso de que se envíen valores a las funciones que no sean números. 
Además deberá aparecer un mensaje que informe "Error: Tipo de dato no válido".
- ZeroDivisionError: En caso de realizar una división por cero. Además deberá aparecer un mensaje que informe "Error: No es posible dividir entre cero". 
""")

from operaciones import *

a, b, c, d = (10, 5, 0, "Hola")

print( "{} + {} = {}".format(a, b, suma(a, b) ) )
print( "{} - {} = {}".format(b, d, resta(b, d) ) )
print( "{} * {} = {}".format(b, b, producto(b, b) ) ) 
print( "{} / {} = {}".format(a, c, division(a, c) ) )