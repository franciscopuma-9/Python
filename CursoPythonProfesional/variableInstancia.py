#se relaciona con la variable de una clase
# edad funciona en todas las personas sin tener que instanciar un objeto
#nombre y nacionalidad solo en el objeto instanciado
class Persona():
    edad = 20 #variable de clase
    def __init__(self,nombre, nacionalidad): #constructor
        self.nombre = nombre #variable de instancia
        self.nacionalidad = nacionalidad # "  "  "


persona1 = Persona("Francisco","Argentina")
print(persona1.nombre,persona1.nacionalidad,persona1.edad)
print(Persona.edad)# imprimimos variable de clase