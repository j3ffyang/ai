from turtle import *
import random

brus= Turtle()
brus.speed(10)
brus.shape("triangle")
bgcolor("black")
brus.color("purple")
brus.pensize(1)

colores= ["Medium Purple", "Deep Sky Blue", "Slate Blue", "Green Yellow",
        "Dark Orange", "Deep Pink", "Medium Slate Blue", "Deep Sky Blue", 
        "Dark Turquoise", "Spring Green", "Gold", "Orange Red", "Violet Red", 
        "Dark Violet", "Firebrick"]

def lineav():
    for count in range(33):
        brus.forward(10)
        brus.forward(10)

brus.penup()
for y in range(330, -360, -30):
    c= random.randint(0, 14)
    brus.color(colores[c])
    brus.penup()
    brus.goto(-330, y)
    brus.pendown()
    lineav()

brus.penup()
brus.left(-90)
for x in range(330, -360, -30):
    c= random.randint(0, 14)
    brus.color(colores[c])
    brus.penup()
    brus.goto(x, 330)
    brus.pendown()
    lineav()

done()
