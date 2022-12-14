class Intro():
    def __init__(self,valor):
        self.valor = valor

    def segundo(self):
        print("Segundo")

    def tercero(self):
        print("Tercero")

class Pepe():
    def saludar(self):
        print("Hola soy pepe")

pepe = Pepe()
dato = Intro("primero")

print(dir(dato))
for i in dir(dato):
    print(i)

print(isinstance(dato,Intro))
print(isinstance(dato,Pepe))

print(hasattr(dato,'valor'))
print(hasattr(dato,'pepe'))