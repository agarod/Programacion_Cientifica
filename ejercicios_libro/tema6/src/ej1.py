#!/usr/bin/python
# encoding: utf-8

'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio: Write a compare function that returns 1 if x > y,
   0 if x == y, and -1 if x < y
   email: alu0100266382@ull.edu.es
'''
import sys

def compare(x,y):
    if (x > y):
        return 1
    if (x == y):
        return 0
    if (x < y):
        return -1

try:
    x = sys.argv[1]
    y = sys.argv[2]
    print (compare(x,y))
except:
    print 'Introduzca primero el valor de x y luego el valor de y '
    print 'El uso correcto del programa es:', sys.argv[0] ,' valor de x valor de y'



