#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:The (so-called) Birthday Paradox:

    Write a function called has_duplicates that takes a list and returns True
 if there is any element that appears more than once. It should not modify
 the original list.
    If there are 23 students in your class, what are the chances that two of
 you have the same birthday? You can estimate this probability by generating
 random samples of 23 birthdays and checking for matches. Hint: you can
 generate random birthdays with the randint function in the random module. 
   email: alu0100266382@ull.edu.es
'''

def has_duplicates(t):
    a = []
    a = t
    print a
    a.sort()
    for i in t:
        if (i != 0):
            if (a[i] == a[i -1]):
                return True
            else:
                return False
    
        
try:
    t = []
    longitud_parametro = len(sys.argv)
    for i in range(longitud_parametro):
       if (i != 0):
           elemento = int(sys.argv[i])
           t.append(elemento)
    print has_duplicates(t)
except:
    print 'El uso correcto del programa es:', sys.argv[0],' valor1 valor2 ...'

