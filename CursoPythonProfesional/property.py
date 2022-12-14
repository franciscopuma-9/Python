class Circulo:

    def __init__(self,radio):
        self.radio = radio

    @property
    def area(self):
        return 1.004545*(self.radio**2)


c = Circulo(10)
print(c.area)
