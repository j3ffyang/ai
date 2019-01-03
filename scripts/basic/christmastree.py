# https://www.facebook.com/brus.espinal/videos/1993841287403618/UzpfSTEwMDAwMzMzMjk5NDIwNzoyNTk1MjEwMTMwNDk2NzE4/?multi_permalinks=2598626893488375&notif_id=1546049249480967&notif_t=group_highlights

from turtle import *

brus= Turtle()
brus.speed(10)
brus.shape("triangle")
bgcolor("black")
brus.color("Lime Green") 
brus.pensize(2)

def estrella():
    for i in range(5):
        brus.forward(40)
        brus.right(144)

brus.penup()
brus.goto(-20, 315)
brus.pendown()
estrella()

brus.penup()
brus.goto(0, 300)
brus.pendown()

x= 10
y= 270
for c in range(14):
    brus.goto(-x, y)
    brus.goto(x,y)
    x= x+ 20
    y= y- 20

brus.penup()
brus.goto(0, -10)
brus.pendown()
brus.pensize(10)
brus.goto(0, -100)  # loc of trunck

brus.penup()
brus.goto(0, -200)

brus.color("Red")
brus.write("Merry Christmas", False, "center", font=("Merry Christmas Flake", 50))

brus.hideturtle()
done()
