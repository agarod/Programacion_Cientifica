#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Write a function called is_sorted that takes a list as a
 parameter and returns True if the list is sorted in ascending order and
 False otherwise. You can assume (as a precondition) that the elements of the
 list can be compared with the relational operators <, >, etc.

For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return False. 
   email: alu0100266382@ull.edu.es
'''

def is_sort(t):
    longitud = len(t)
    longitud = int(longitud)
    aux = True
    for i in range(longitud):
        if (i != longitud -1):
            if (t[i]  < t[i +1]) and (aux == True):
                aux = True
            else:
                aux = False
        else:
            if (t[i] > t[i -1]):
               if (aux == True):
                   aux = True
               else:
                   aux = False
            else:
                aux = False
    return aux

try:
    t = []
    longitud_parametro = len(sys.argv)
    for i in range(longitud_parametro):
       if (i != 0):
           elemento = ord(sys.argv[i])
           t.append(elemento)
    print is_sort(t)
except:
    print 'El uso correcto del programa es:', sys.argv[0],' caracter1 caracter2 ...'

