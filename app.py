from turtle import *

side = 80

def square():
    for i in range(4):
        fd(side)
        left(90)

def board():
    for i in range(3):
        for j in range(3):
            pd()
            square()
            pu()
            fd(side)
        bk(side*3)
        left(90)
        fd(side)
        right(90)

def cross(x,y):
    pu()
    setx(x*side + side/2)
    sety(y*side + side/2)
    pd()
    left(45)
    for i in range(4):
        fd(side/4)
        bk(side/4)
        left(90)
    right(45)
    pu()

def round(x,y):
    pu()
    setx(x*side + side/2)
    sety(y*side + side/2 - side/4)
    pd()
    circle(side/4)

done()