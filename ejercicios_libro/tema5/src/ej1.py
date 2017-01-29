#!/usr/bin/python
# encoding: utf-8
from swampy.Lumpy import Lumpy
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio: Draw a stack diagram for print_n called with s = 'Hello' and
 n=2. 
   email: alu0100266382@ull.edu.es
'''

def countdown(n,s):
    if n > 0:
        print s
        countdown(n-1, s)
    lumpy.object_diagram()


lumpy = Lumpy()
lumpy.make_reference()
s = 'hello'
n= 2;
countdown(n,s)
