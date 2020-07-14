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

board()
done()