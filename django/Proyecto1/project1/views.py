from django.http import HttpResponse
import datetime
from django.template import Template, Context
# from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): #primera vista

    doc_externo = open('C:/Users/franc/PycharmProjects/estudios/django/Proyecto1/project1/platillas/plantilla1.html')

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)

    return HttpResponse(documento)

def saludodos(request):
    nombre = "Mi cielita"
    apellido = "Heeemoozaaa"
    fecha = datetime.datetime.now()

    p1 = Persona("Camila", "Galarza")

    #doc_externo = open('C:/Users/franc/PycharmProjects/estudios/django/Proyecto1/project1/platillas/plantilla1.html')
    # 1 plt = Template(doc_externo.read())
    # 1 doc_externo.close()

    # 2 doc_externo = loader.get_template('plantilla1.html')
    # 3 doc_externo = get_template('plantilla1.html')

    lista = ["Amor", "Boca", "Cuerpo","Paziom"]
    # 1 ctx = Context({"nombre_persona":nombre, "apellido_persona":apellido, "fecha":fecha, "nombre":p1.nombre,"apellido":p1.apellido, "todo": lista})
    # 3 ctx = {"nombre_persona":nombre, "apellido_persona":apellido, "fecha":fecha, "nombre":p1.nombre,"apellido":p1.apellido, "todo": lista}
    # 3 documento = doc_externo.render(ctx)

    # 3 return HttpResponse(documento)

    return render(request, "plantilla1.html",{"nombre_persona":nombre, "apellido_persona":apellido, "fecha":fecha, "nombre":p1.nombre,"apellido":p1.apellido, "todo": lista})
def fecha(request):

    fecha_actual = datetime.datetime.now()

    documento = """<html>
        <body>
        <h2>
        Fecha y hora actuales %s 
        </h2>
        </body>
        </html>    
        """ % fecha_actual
    return HttpResponse(documento)

def calculaEdad(request, edad, anio):

    periodo = anio - 2022
    edadFutura = periodo + edad

    documento = "<html><body><h1> En el año %s tendras %s años" %(anio,edadFutura)

    return HttpResponse(documento)


def prueba(request):

    fecha_actual = datetime.datetime.now()

    return render(request, 'prueba.html', {'fecha':fecha_actual})

def pruebahija(request):

    fecha_actual = datetime.datetime.now()

    return render(request, 'hija.html', {'fecha': fecha_actual})