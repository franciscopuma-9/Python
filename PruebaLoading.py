from colorama import init,Fore,Back,Style,Cursor
init()
print('Recursos Python')
print(Back.BLUE + Fore.BLACK + "Recursos Python")

print(Back.RESET + Fore.RESET+ 'SANTI LA CONCHA DE TU MADRE')

from time import sleep
print("Recursos Python")
sleep(3)
print(Cursor.BACK(15) + Cursor.UP(1) + "www.recursospython.com")
import time

from tqdm import trange,tqdm
import time

for x in trange(250):
    time.sleep(0.025)

texto = ""
for caracter in tqdm(["a", "b", "c", "d"]):
    texto = texto + caracter

barra1 = tqdm(["a", "b", "c", "d"])
for caracter in barra1:
    barra1.set_description("Procesando %s" % caracter)
    time.sleep(3)
from colorama import init,Fore
init()

numeros = tqdm(range(100))
for caracter in numeros:
    caracter = caracter+1
    numeros.set_description(Fore.BLUE+"Procesando %s" % caracter)
    time.sleep(0.25)

import time
import progressbar

for i in progressbar.progressbar(range(100)):
    time.sleep(0.02)

from time import sleep
from tqdm import tqdm
for i in tqdm(range(100)):
    sleep(0.02)




import sys


def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size * j / count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#" * x, "." * (size - x), j, count))
        file.flush()
        file.write("\n")

    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
        file.write("\n")
    file.flush()


import time

for i in progressbar(range(15), "Computing: ", 40):
    time.sleep(0.1)

import time
# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))
