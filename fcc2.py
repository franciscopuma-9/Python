def add_time(start, duracion, dia=False):
    indice_semana = {"monday": 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
    dias_semana = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    duracion_sep = duracion.partition(":")
    duracion_horas = int(duracion_sep[0])
    duracion_min = int(duracion_sep[2])

    start_sep = start.partition(":")
    start_horas = int(start_sep[0])
    start_sep_min = start_sep[2].partition(' ')
    start_min = int(start_sep_min[0])
    am_pm = start_sep_min[2]
    cantidad_dias = int(duracion_horas/24)


    minutos = start_min + duracion_min
    if minutos >= 60:
        start_horas +=1
        minutos = minutos % 60

    horas = (start_horas + duracion_horas) % 12
    vuelta_am_pm = int((start_horas+duracion_horas)/12)

    if minutos < 9:
        minutos = "0"+str(minutos)
    if horas == 0:
        horas = 12
    if (am_pm == "PM" and start_horas + duracion_horas % 12 >= 12):
        cantidad_dias +=1
    if vuelta_am_pm % 2 != 0:
        if am_pm == "PM":
            am_pm = "AM"
        elif am_pm == "AM":
            am_pm = "PM"

    new_time = str(horas) + ":" + str(minutos) + " " + am_pm

    if (dia):
        dia = dia.lower()
        indice = int((indice_semana[dia])+cantidad_dias) % 7
        nuevo_dia = dias_semana[indice]
        new_time += ', ' + nuevo_dia
    if cantidad_dias == 1:
        new_time += " (next day)"
    elif cantidad_dias > 1:
        new_time += " ({} days later)".format(cantidad_dias)



    return new_time

print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:40 AM", "0:25"))
print(add_time("2:59 AM", "24:00"))
print(add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02"))
print(add_time("5:01 AM", "0:00"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02", "tuesday"))
