#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Write a function called middle that takes a list and returns a
   new list that contains all but the first and last elements. So middle
   ([1,2,3,4]) should return [2,3].
   email: alu0100266382@ull.edu.es
'''

def middle(t):
    res = []
    res = t[1:len(t)-1]
    return res

try:
    t = []
    longitud_parametro = len(sys.argv)
    for i in range(longitud_parametro):
       if (i != 0):
           numero = int(sys.argv[i])
           t.append(numero)
    print middle(t)
except:

    print 'El uso correcto del programa es:', sys.argv[0],' valor1 valor2 valor3 valor4'

