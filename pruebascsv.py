import csv

titanic = []
dic = {}
dic["problema1"] = {}
dic["problema1"]["vivos"] = 0
dic["problema1"]["muertos"] = 0
dic["problema3"] = {}
dic["problema3"]["Clases"] = []
dic["problema4"] = {}
dic["problema4"]["sexo"] = {"M":0,"F":0}
with open('titanic.csv') as archivo:
    datos = csv.reader(archivo,delimiter="\t")
    print(datos)

    for linea in datos:
        titanic.append(linea)

titulos = titanic[0]

del(titanic[0])
cont = 0
for i in titanic:
    cont +=1
    if i[1] == "1":
        dic["problema1"]["vivos"] +=1
    else:
        dic["problema1"]["muertos"] +=1

    if i[2] not in dic["problema3"]["Clases"]:
        dic["problema3"]["Clases"].append(i[2])

    if i[4] == 'male':
        dic["problema4"]["sexo"]["M"]+=1
    elif i[4]=='female':
        dic["problema4"]["sexo"]["F"]+=1
print(dic)
print('*'*20)
print("La cantidad que sobrevivieron fueron:",dic["problema1"]["vivos"])
print('*'*20)
porcentaje = (dic["problema1"]["vivos"]/cont)*100
print("El porcentaje de personas que sobrevivieron es:",porcentaje,"%")
print('*'*20)
print("La cantidad de clases que hay:",len(dic["problema3"]["Clases"]))
print('*'*20)

print("La cantidad de hombres son:",dic["problema4"]["sexo"]["M"])
print("La cantidad de mujeres son:",dic["problema4"]["sexo"]["F"])
