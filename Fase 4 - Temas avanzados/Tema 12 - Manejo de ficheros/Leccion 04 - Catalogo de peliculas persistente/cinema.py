from io import open
import pickle

class Pelicula:
    
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:',self.titulo)
        
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:
    
    peliculas = []
    
    # Constructor de clase
    def __init__(self):
        self.cargar()
        
    def agregar(self,p):
        self.peliculas.append(p)
        
    def mostrar(self):
        for p in self.peliculas:
            print(p)

    def cargar(self):
        file = open("catalog.pckl", "ab+")
        file.seek(0)
        try:
            self.peliculas = pickle.load(file)
        except:
            print("El fichero esta vacío")
        finally:
            print("Se han cargado {} peliculas".format(len(self.peliculas)))
            file.close()

    def guardar(self):
        file = open("catalog.pckl", "wb")
        pickle.dump(self.peliculas, file)
        file.close()
    
    def __del__(self):
        print("Guardado automático de las peliculas")
        self.guardar()