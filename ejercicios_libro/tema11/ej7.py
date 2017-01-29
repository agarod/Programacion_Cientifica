#!/usr/bin/python
# encoding: utf-8
import sys
import time
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Memoize the Ackermann function from Exercise 5 and see if
   memoization makes it possible to evaluate the function with bigger
   arguments.
   email: alu0100266382@ull.edu.es
'''
cache = {}

def ackermann(m, n):

    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]

try:
    elemento = int(sys.argv[1])
    elemento2 = int(sys.argv[2])
    print ackermann(elemento, elemento2)
    
  
except:

    print 'Programa Funcion de ackerman con memoria \n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], 'numero1 y numero2'
