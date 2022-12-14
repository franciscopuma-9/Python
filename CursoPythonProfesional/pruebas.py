class Persona():
    def __init__(self, nombre, edad, nacionalidad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.DNI = DNI

    def devuelve_nombre(self):
        return self.nombre

    def devuelve_edad(self):
        return self.edad

    @classmethod
    def devuelve_DNI(cls,DNI):
        return DNI

    @classmethod
    def devuelve_nacionalidad(cls):
        return cls.nacionalidad

    def __str__(self):
        return f'Nombre:{self.nombre} Edad:{self.edad} DNI:{self.DNI} Nacionalidad: {self.nacionalidad}'