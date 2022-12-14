#metodo de clase
#conviene usar decoradores
class Persona():
    def __init__(self):
        pass

    def despedir(self):
        print("Chau...")
    @classmethod
    def saludar(cls,nombre):
        print("Hola...soy",nombre)
persona = Persona()
persona.despedir()

Persona.saludar("Francisco") #te deja usar el metodo de la clase sin el self
