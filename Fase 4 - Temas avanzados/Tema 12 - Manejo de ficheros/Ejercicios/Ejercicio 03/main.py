from clases import Personaje, Gestor

personajes = [
    Personaje("Caballero", 4, 2, 4, 2),
    Personaje("Guerrero", 2, 4, 2, 4),
    Personaje("Arquero", 2, 4, 1, 8)
]

gestor = Gestor()

for p in personajes:
    gestor.agregar(p)

gestor.mostrar()
gestor.borrarPorClase("Guerrero")
gestor.mostrar()
