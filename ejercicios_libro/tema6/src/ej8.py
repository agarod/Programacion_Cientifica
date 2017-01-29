#!/usr/bin/python
# encoding: utf-8
import fractions
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio: Write a function called gcd that takes parameters a and b and returns their greatest common divisor.
   email: alu0100266382@ull.edu.es
'''


def gcd2(a,b):
   if (a == 0):
       return b
   elif (b == 0):
       return a
   else:
       return fractions.gcd(a,b)
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print gcd2(a,b)
except:
    print gcd2(a,b)
    print 'Este programa calcula si una palabra es palindroma\n\n'
    print 'Debe seguir el modo de uso', argv[0], ' pal'

