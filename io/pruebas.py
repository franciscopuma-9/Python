# import pandas as pd
# df = pd.read_csv("prueba.csv")
# print(df)
# import random
#
# lista1 = range(10)
# lista2 = ["Francisco", "Camila", "Santiago", "Agustin", "Valen", "Emiliano", "Lucho","Lucero","Meme","Juan"]
# lista3 = ["Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
#
# archivo_texto = open("random.csv", "w")
# archivo_texto.write("Numero, Nombre, Dia")
# for x in range(100):
#     aux = '\n'+ str(lista1[random.randint(0, 9)])+','+lista2[random.randint(0, 9)]+','+lista3[random.randint(0, 6)]
#     archivo_texto.write(aux)
# archivo_texto.close()

# import pandas as pd
# dataset = pd.read_csv("random.csv")
# print(dataset)
# texto = open("newrandom.csv", "w")
# texto.write("Numero, Nombre, Dia\n")
# for valor in dataset.values:
#     if 'Francisco' in valor:
#         text = str(valor[0])+','+ valor[1]+ ','+ valor[2]+ '\n'
#         texto.write(text)
# texto.close()
#
# import pandas as pd
#
# dataset = pd.read_csv("newrandom.csv")
# inputs = dataset.drop(columns=["Dia"])
# outputs = dataset['deporte']
#
# list = []
# cant = int(input("Ingrese cantidad de valores a ingresar: "))
# for x in range(cant):
#     aux = int(input("Ingrese valor: "))
#     list.append(aux)

# print(min(list))
# mayor = list[0]
# for x in list:
#     if mayor < x:
#         mayor = x
# print(mayor)


class TuViejaEnTanga:
    def esValido(self):
        self.edad = input("Ingrese edad:")
        while self.edad.isdigit() != True:
            self.edad = input("Ingrese edad:")
        while (int(self.edad) > 110 or int(self.edad) < 0):
            self.edad = input("Ingrese edad:")
        if 18 <= int(self.edad) <= 25:
            return True
        else:
            return False



hola = TuViejaEnTanga()
print(hola.esValido())
























