#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Write a function called remove_duplicates that takes a list and
 returns a new list with only the unique elements from the original.
   email: alu0100266382@ull.edu.es
'''

def remove_duplicates(t):
    a = []
    a = t
    print a
    a.sort()
    for i in t:
        if (i != 0):
            if (a[i] == a[i -1]):
                del.a[i]
    return a
           
   
    
        
try:
    t = []
    longitud_parametro = len(sys.argv)
    for i in range(longitud_parametro):
       if (i != 0):
           elemento = int(sys.argv[i])
           t.append(elemento)
    print remove_duplicates(a)
except:
    print 'El uso correcto del programa es:', sys.argv[0],' valor1 valor2 ...'

