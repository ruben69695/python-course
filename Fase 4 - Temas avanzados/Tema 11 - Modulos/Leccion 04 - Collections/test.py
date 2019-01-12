# ===================== Counter =========================
print("\n===================== Counter =========================\n")

from collections import Counter

l = [1,2,3,4,1,2,3,1,2,1]
print(Counter(l))

p = "palabra"
print(Counter(p))

animales = "gato perro canario perro canario perro"
print(Counter(animales))

print(animales.split(" "))
print(Counter(animales.split(" ")))

c = Counter(animales.split(" "))
print(c.most_common(1))
print(c.most_common(2))

l = [10,20,30,40,10,20,30,10,20,10]
c = Counter(l)
print(c.items())
print(c.keys())
print(c.values())
print(sum(c.values()))
print(list(c))
print(list(c.values()))

# ===================== Dictionaries with default values =========================
print("\n\n===================== Dictionaries with default values =========================\n")

from collections import defaultdict

d = defaultdict(float)
print(d['something'])
print(d)
d = defaultdict(str)
print(d['something'])
print(d)

d['something'] = 'something'
print(d)

# ===================== Ordered Dictionaries =========================
print("\n\n===================== Ordered Dictionaries =========================\n")

from collections import OrderedDict

n1 = OrderedDict()
n1["uno"] = "one"
n1["dos"] = "two"
n1["tres"] = "three"
n1["cuatro"] = "four"
print(n1)

n2 = OrderedDict()
n2["dos"] = "two"
n2["uno"] = "one"
n2["tres"] = "three"
n2["cuatro"] = "four"

print(n1 == n2)

# ===================== Named tuples =========================
print("\n\n===================== Named tuples =========================\n")

from collections import namedtuple

t = (20,40,60)
print(t[0])
print(t[-1])

Persona = namedtuple("Persona", "nombre apellido edad")
p = Persona("Ruben", "Arrebola", 22)
print(p.nombre)
print(p.apellido)
print(p.edad)

print(p)

print(p[0])
print(p[1])
print(p[-1])

# Recordad que las tuplas con inmutables

