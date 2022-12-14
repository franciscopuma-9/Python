class Libro():
    def __init__(self,nombre,autor,paginas):
        self.nombre = nombre
        self.autor = autor
        self.paginas = paginas

    def describir(self):
        print(f'Hola desde escribir, {self.nombre}')

    def __str__(self): #imprimir el nombre
        return f'{self.nombre} escrito por {self.autor} de {str(self.paginas)} paginas'

    def __len__(self): #retorna el len
        return self.paginas


    def __del__(self): #para que el del haga algo mas
        print("Destrui el libro")

libro1 = Libro("Curso de Python","Francisco",110)
#print(libro1.describir())
print(libro1) #__str__
print(len(libro1)) #__len__

del libro1 #delete un objeto
