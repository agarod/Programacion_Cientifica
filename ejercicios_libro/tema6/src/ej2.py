#!/usr/bin/python
# encoding: utf-8

'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio: Use incremental development to write a function called
   hypotenuse that returns the length of the hypotenuse of a right 
   triangle given the lengths of the two legs as arguments. Record 
    each stage of the development process as you go.
   email: alu0100266382@ull.edu.es
'''

import sys
import math

def hypotenuse(l1,l2):
    
    valor = ((l1 ** 2) + (l2 ** 2))
    valor2  = math.sqrt(valor)
    return valor2
   
try:
    l1 = float(sys.argv[1])
    l2 = float(sys.argv[2])
    print hypotenuse(l1,l2)
except:
    print 'Introduzca dos valores para el lado 1 y lado 2'
    print 'El uso correcto del programa es:', sys.argv[0], 'lado1 lado2' 
