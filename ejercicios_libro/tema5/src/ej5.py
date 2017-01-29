#!/usr/bin/python
# encoding: utf-8

'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio: Read the following function and see if you can figure out
 what it does. Then run it
   email: alu0100266382@ull.edu.es
'''
from swampy.TurtleWorld import *

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)


world = TurtleWorld()
bob = Turtle()
print bob
draw(bob,2,10)


