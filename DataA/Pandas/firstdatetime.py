from datetime import date

d1 = date(2013,5,20)

print(d1)

print(type(d1))

print("Dia: ",d1.day)

print("Mes: ",d1.month)

print("Anio: ",d1.year)

d2 = date.today()
print(d2)

print("Dia: ",d2.day)

print("Mes: ",d2.month)

print("Anio: ",d2 .year)

from datetime import time

t1 = time(15,20,13,40)#hora,minutos,segundos,microsegundos

print(t1)
print(type(t1))

print('Hora: ',t1.hour)
print('Minuto: ',t1.minute)
print('Segundo: ',t1.second)
print('Microsegundo: ',t1.microsecond)

import datetime

h1 = datetime.datetime.now()
print(h1)

print("Dia: ",h1.day)
print("Mes: ",h1.month)
print("Anio: ",h1 .year)
print('Hora: ',h1.hour)
print('Minuto: ',h1.minute)
print('Segundo: ',h1.second)
print('Microsegundo: ',h1.microsecond)

print(h1.weekday())#devuelve un numero dependiendo del dia de la semana empezando por lunes

print(h1.isoweekday())#devuelve un numero dependiendo del dia de la semana empezando por domingo

print(h1.isocalendar())#devuelve tupla con anio, semana y dia de la semana

d1_datetime = date.fromisoformat('2022-04-23')#convierte en la clase datetime.date
print(d1_datetime)
print(type(d1_datetime))

d1_ISO = date(2020,4,23).isoformat()#convierte una clase datetime a str
print(d1_ISO)
print(type(d1_ISO))

date = '22 April, 2020 13:20:13'

d3 = datetime.datetime.strptime(date, '%d %B, %Y %H:%M:%S') #indica el tipo para leer strings
print(d3)
print(type(d3))
''' strptime
%a	Nombre del día de la semana abreviado
%A	Nombre del día de la semana completo
%w	Día de la semana como número decimal
%d	Día del mes como número de dos dígitos
%-d	Día del mes como número decimal
%b	Nombre del mes abreviado
%B	Nombre del mes completo
%m	Mes del año número de dos dígitos
%-m	Mes del año como número decimal
%y	Año sin centenas como número de dos dígitos
%-y	Año sin centenas como número decimal
%Y	Año completo
%H	Hora en 24 hrs. con dos dígitos
%-H	Hora en 24 hrs. como número decimal
%I	Hora en 12 hrs. con dos dígitos
%-I	Hora en 12 hrs. como número decimal
%M	Minutos con dos dígitos
%-M	Minutos como número decimal
%S	Segundos con dos dígitos
%-S	Segundos como número decimal
'''

d1 = datetime.datetime.now()
print(d1)

d2 = d1 + datetime.timedelta(days=2)#suma de dias
print("Fecha: 2 dias a partir de hoy: ",d2)

d3 = d1 + datetime.timedelta(weeks=2)#suma de semanas
print("Fecha: 2 semanas a partir de hoy: ",d3)

d2 = d1 - datetime.timedelta(days=2)#resta de dias
print("Fecha: 2 dias antes de hoy: ",d2)

d3 = d1 - datetime.timedelta(weeks=2)#resta de semanas
print("Fecha: 2 semanas a antes de hoy: ",d3)