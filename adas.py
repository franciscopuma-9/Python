
def operacion(operator):
    global operador
    global primeraparte
    primeraparte = numeropantalla.get()
    operador = operator
    numeropantalla.set("")

def igual(primernum,operador):
    segundonumero = numeropantalla.get()
    if operador == '+':
        suma = int(primernum) + int(segundonumero)
        numeropantalla.set(str(suma))
    if operador == '-':
        suma = int(primernum) - int(segundonumero)
        numeropantalla.set(str(suma))
    if operador == '/':
        suma = int(primernum) / int(segundonumero)
        numeropantalla.set(str(suma))
    if operador == '*':
        suma = int(primernum) * int(segundonumero)
        numeropantalla.set(str(suma))