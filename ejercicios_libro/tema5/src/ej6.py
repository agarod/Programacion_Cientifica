#!/usr/bin/python
# encoding: utf-8

'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio: The Koch curve is a fractal that looks something like Figure
 5.2. To draw a Koch curve with length x, all you have to do is
   email: alu0100266382@ull.edu.es
'''
from swampy.TurtleWorld import *



def koch(t, n):
    if n<3:
        fd(t, n)
        return
    m = n/3.0
    koch(t, m)
    lt(t, 60)
    koch(t, m)
    rt(t, 120)
    koch(t, m)
    lt(t, 60)
    koch(t, m)


def snowflake(t, n):
    
    for i in range(3):
        koch(t, n)
        rt(t, 120)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0

bob.x = -150
bob.y = 90
bob.redraw()

snowflake(bob, 300)

world.mainloop()
