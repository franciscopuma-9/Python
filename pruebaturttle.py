# from turtle import *
#
# bgcolor('black')
# pensize(2)
# speed(100)
# hideturtle()
#
# while(True):
#     for i in range(6):
#         for colors in ['blue','magenta','green','yellow','white','red']:
#             color(colors)
#             circle(100)
#             left(10)

from turtle import *

hideturtle()
bgcolor('black')
speed(50)
colormode(255)
colors = [(78,253,84),
          (32,210,244),
          (255,7,58)]

counter = 0
penup()
backward(100)
left(90)
forward(100)
right(90)
pendown()

def drawSpiral(length):
    global counter
    counter+=1
    color(colors[counter%3])
    forward(length)
    right(90)
    drawSpiral(length-5)

drawSpiral(200)