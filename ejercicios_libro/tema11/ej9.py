#!/usr/bin/python
# encoding: utf-8
import sys
import time
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Use a dictionary to write a faster, simpler version of
   has_duplicates. 
   email: alu0100266382@ull.edu.es
'''
cache = {}

def has_duplicate(d):
    print d

    return len(set(d)) < len(d)

try:
    d = dict()
    longitud_parametro = len(sys.argv)
    for i in range(longitud_parametro):
       if (i != 0):
           elemento = int(sys.argv[i])
           d[i-1] =  elemento
          
    print has_duplicate(d)
   
except:
    print has_duplicate(d)	
    print 'Programa Funcion de has duplicated 2 memoria \n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], 'lista de numeors'
