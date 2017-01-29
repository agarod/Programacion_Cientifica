#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Write a function called sumall that takes any number of
 arguments and returns their sum.
   email: alu0100266382@ull.edu.es
'''

def sumall(elements):
    total = 0

    for i in range(len(elements)):
        total = total + elements[i]
    return total


try:
    t = []
    longitud_parametro = len(sys.argv)
    for i in range(longitud_parametro):
       if (i != 0):
           elemento = int(sys.argv[i])
           t.append(elemento)
    print sumall(t)
except:
    print 'Coge un numero de parametros y los suma \n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], 'numero 1 numero 2...'

