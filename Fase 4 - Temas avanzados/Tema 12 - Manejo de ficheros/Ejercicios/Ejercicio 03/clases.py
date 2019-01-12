from io import open
import pickle

class Personaje():

    def __init__(self, clase, vida, ataque, defensa, alcance):
        self.clase = clase
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
    
    def __str__(self):
        return "{} -> {} de vida, {} de ataque, {} de defensa y {} de alcance".format(self.clase, self.vida, self.ataque, self.defensa, self.alcance)

class Gestor():

    filePath = "personajes.pckl"
    personajes = []

    def __init__(self):
        self.___cargar()
    
    def __del__(self):
        self.__guardar()                                                # We save automatically for security when the destructor is called
    
    def mostrar(self):
        for p in self.personajes:
            print(p)
    
    def ___cargar(self):
        try:
            file = open(self.filePath, "ab+")                           # Safe mode, if file does not exists we create it
            file.seek(0)                                                # Very important we opened the file with append, we need to situate the pointer at the begin of the file, to recolect all the data
            try:
                self.personajes = pickle.load(file, encoding="uf8")     # Load all the data to the list of personajes using pickle                
            except:
                print("File empty")
            print("Number of personajes loaded {}".format(len(self.personajes)))
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(str(e))

    def __guardar(self):
        try:
            file = open(self.filePath, "wb")
            pickle.dump(self.personajes, file)
        except FileNotFoundError:
            print("File not found, can't save the list of personajes")
        except Exception as e:
            print(str(e))
    
    def existsItem(self, personaje):
        for p in self.personajes:
            if p.clase == personaje.clase:
                return True
        else:
            return False
    
    def agregar(self, personaje):
        if self.existsItem(personaje):
            print("The {} already exists on the list of personajes, not added".format(personaje.clase))
        else:
            self.personajes.append(personaje)
            self.__guardar()
    
    def borrar(self, personaje):
        if (self.existsItem(personaje)):
            self.personajes.remove(personaje)
            self.__guardar()
        else:
            print("The {} does not exists on the list, we can't remove it")
    
    def borrarPorClase(self, clase):
        finded = False
        i = 0

        while (finded == False and i < len(self.personajes)):
            if (self.personajes[i].clase == clase):
                finded = True
                self.personajes.remove(self.personajes[i])
                print("The personaje {} has been deleted from the list".format(clase))
                self.__guardar()
            i += 1

        if not finded:
            print("The personaje {} does not exists on the list of personajes")
