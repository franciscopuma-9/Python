class Perro():
    def __init__(self):
        pass

    def avanzar(self):
        print("Tengo 4 patas")

class Perico():
    def avanzar(self):
        print("Volar")

def mover(animal):
    animal.avanzar()

perro = Perro()
perro.avanzar()
perico = Perico()
perico.avanzar()


print("*"*20)

mover(perico)
mover(perro)