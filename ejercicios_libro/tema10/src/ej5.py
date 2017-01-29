#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Write a function called chop that takes a list, modifies it by
 removing the first and last elements, and returns None.
   email: alu0100266382@ull.edu.es
'''

def chop(t):
    longitud = len(t)
    longitud = int(longitud)
    del t[longitud - 1]
    del t[0]
    return None

try:
    t = []
    longitud_parametro = len(sys.argv)
    for i in range(longitud_parametro):
       if (i != 0):
           elemento = int(sys.argv[i])
           t.append(elemento)
    print chop(t)
except:
    print chop(t)
    print 'El uso correcto del programa es:', sys.argv[0],' valor1 valor2 ...'

