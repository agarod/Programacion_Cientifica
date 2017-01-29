#!/usr/bin/python
# encoding: utf-8
import sys
from Funciones_Matematicas import *
'''
   __author__: "Ardiel Garcia Rodriguez"
   __email__: "alu0100266382@ull.edu.es"_
   __numero de ejercicio__: 11
   __enunciado__:Escribir un programa haciendo uso de un modulo creado previamente que realice la interseccion, union
   ... y luego haga uso de dos
   __status__: "Terminado"
'''

A = [1, 2, 3, 4, 5]
B = [1, 3, 5, 7, 9]
C = [2, 4]



print 'A', A
print 'B', B
print 'C', C
print '\n\n'
print 'Union de A y C', union(A,C)
print 'Intersección A,B', intersection(A, B)

