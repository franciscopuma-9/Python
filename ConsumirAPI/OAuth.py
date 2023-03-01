import json
import matplotlib as plt
import requests


def graficar(archivo):
   with open(archivo) as data_file:
       data = json.load(data_file)
   for i in range(len(data["results"])):
       plt.plot(data["results"][i]["x"], data["results"][i]["y"], label="Fold " + str(i+1))
   plt.legend()
   plt.show()



