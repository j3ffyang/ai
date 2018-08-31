# -*- coding: utf-8 -*-
import turtle as t
import random
t.setup(width=600, height=600)
t.speed(500)
t.bgcolor('black')
t.color('lime')  #comment out for random colors
d = 120
colors = ["maroon","olive","blue","orange","purple","coral","khaki"]
for i in range(140,0,-20):
    d = d-20
    for j in range(0,380,10):
        #color = random.choice(colors)  #uncomment for random colors
        #t.color(color)  #uncomment for random colors
        #rndw = random.randint(2,5)  #uncomment for random widths
        #t.width(rndw)  #uncomment for random widths
        t.pu()
        t.fd(i)
        t.pd()
        t.circle(d)
        t.pu()
        t.home()
        t.rt(j)
t.ht()
t.exitonclick()