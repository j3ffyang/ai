from turtle import *

brus= Turtle()
brus.shape("circle")
bgcolor("black")
brus.pensize(2)

colores= ["Medium Purple", "Deep Sky Blue", "Slate Blue", "Green Yellow",
        "Orange", "Deep Pink", "Medium Slate Blue", "Deep Sky Blue", 
        "Dark Turquoise", "Spring Green", "Gold", "Orange Red", "Violet Red", 
        "Dark Violet", "Firebrick"]

x= 0
y= 0 
xdir= 10
ydir= 10
xlimit= 300
ylimit= 330
col= 0

for c in range(1350):
    x= x+ xdir
    y= y+ ydir

    if col== 15:
        col= 0

    brus.color(colores[col])

    if not -xlimit < x < xlimit:
        xdir= -xdir
    if not -ylimit < y < ylimit:
        ydir= -ydir 

    col= col+ 1

    if c % 2 == 0:
        brus.penup()
    else:
        brus.pendown()
    brus.goto(x, y)

done()
