#metodo de instancia
class Persona():
    nacionalidad = "Argentina"
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def correr(self):
        print("Estoy corriendo")

print(Persona.nacionalidad)
persona1 = Persona("Francisco",23)
persona1.correr()