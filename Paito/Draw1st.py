#faz um desenho usando turtle (muito bom inclusive)

import turtle
from random import randint
colors = ["#FF00CF","#00FDFF","#FFFD00","#1BFF00","#00F8FF", "#9A00FF"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(900):
   my_pen.pencolor(colors[x%6])
   my_pen.width(x/1000 + 0.002)
   my_pen.forward(x)
   my_pen.left(59)
