#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Use capitalize_all to write a function named capitalize_nested that takes a nested list of strings and returns a new nested list with all strings capitalize
   email: alu0100266382@ull.edu.es
'''

def capitalize_all(t):
    res = []
    for i in t: 
        res.append(i.capitalize())
    return res


try:
    t = []
    longitud_parametro = len(sys.argv)
    for i in range(longitud_parametro):
       if (i != 0):
           caracter = (sys.argv[i])
           t.append(caracter)
    print capitalize_all(t)
except:
    print 'El uso correcto del programa es:', sys.argv[0],' palabra1 palabra2 ...'

