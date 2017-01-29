#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio: A number, a, is a power of b if it is divisible by b 
and a/b is a power of b. Write a function called is_power that
 takes parameters a and b and returns True if a is a power of b.
   email: alu0100266382@ull.edu.es
'''

def is_power(a,b):
   if ((a == 1) or (b == 1)):
       return True
   elif ((a == 0) or (b == 0)):
       return True
   elif (((a%b) == 0) and ((c%b) == 0)):
       return True
   else:
       return False
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print is_power(a,b)
except:

    print 'Este programa calcula si una palabra es palindroma\n\n'
    print 'Debe seguir el modo de uso', argv[0], ' pal'

