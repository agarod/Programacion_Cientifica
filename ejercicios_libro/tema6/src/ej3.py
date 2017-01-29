#!/usr/bin/python
# encoding: utf-8

'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio: Write a function is_between(x, y, z) that returns
   True if x ≤ y ≤ z or False otherwise.
   email: alu0100266382@ull.edu.es
'''

import sys

def is_between(x,y,z):
    if ((x <=y) & (y <= z)):
        return True
    else:
        return False

try:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    z = float(sys.argv[3])
    print (is_between(x, y, z))
except:
    print 'Introduzca primero el valor de x, luego y y luego z'
