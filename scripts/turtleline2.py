# -*- coding: utf-8 -*-
import turtle as t
#import random
t.setup(width=600, height=600)
t.speed(10)
t.color("lime")
t.bgcolor('black')
t.shape('turtle')
t.pu()
for i in range(-300,300,20):
    t.setpos(i,-300)
    t.pu()
    t.home()
    t.pd()
    t.setpos(i*-1,i)
for i in range(300,-300,-20):
    t.setpos(i,300)
    t.pu()
    t.home()
    t.pd()
    t.setpos(i*-1,i)
t.exitonclick()
