#Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
#Construye los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas
#de datos.
# mostrar(): Muestra los datos de la persona.
# esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad

class Persona:
    def __init__(self, *args):
        self.nombre = args[0]
        self.edad = args[1]
        self.dni = args[2]

    def setNombre(self):
        self.nombre = input("Ingrese nombre: ")
        while (self.nombre.isalpha() != True):
            if '/' in self.nombre:
                break
            else:
                self.nombre = input("Solo puede ingresar letras: ")

    def setEdad(self):
        self.edad = input("Ingrese edad: ")
        while (self.edad.isdigit() != True):
            self.edad = input("Solo puede ingresar numeros: ")
        while (int(self.edad) > 120 or int(self.edad) < 0):
            self.edad = input("Ingrese edad valida: ")

    def setDni(self):
        self.dni = input("Ingrese DNI: ")
        while (self.dni.isdigit() != True or (len(str(self.dni)) not in [6,7,8])):
            if self.dni.isdigit() and len(str(self.dni)) in [6,7,8]:
                break
            else:
                self.dni = input("Ingrese DNI valido: ")

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getDni(self):
        return self.dni

    def mostrar(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nDNI:", self.dni)

    def esMayorDeEdad(self):
        if int(self.edad) < 18:
            return "Es menor de edad"
        else:
            return "Es mayor de edad"
#init
person = Persona("1fg23", "34fg", "4523fg146")
#getters
# print(person.getNombre())
# print(person.getEdad())
# print(person.getDni())
#setters
#person.setNombre()
# person.setEdad()
person.setDni()
#mostrar
person.mostrar()
#esMayor
# print(person.esMayorDeEdad())
# persona = Persona(1,2,3)
# persona.setNombre()
# persona.setEdad()
# persona.setDni()

