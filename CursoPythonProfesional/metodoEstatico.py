#la funcionalidad esta estrechamente relacionada con la clase


class Persona():
    def __init__(self):
        pass

    def saltar(self): #metodo de instancia
        print("Estoy saltando")

    @classmethod
    def correr(cls): #metodo de clase
        print("Estoy corriendo")

    @staticmethod
    def nadar(): #metodo estatico
        print("Estoy nadando")

pedro = Persona()
pedro.nadar()