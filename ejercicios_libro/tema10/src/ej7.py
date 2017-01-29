#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Two words are anagrams if you can rearrange the letters from one
   to spell the other. Write a function called is_anagram that takes two
   strings and returns True if they are anagrams
   email: alu0100266382@ull.edu.es
'''

def is_anagram(cadena1, cadena2):
    if (len(cadena1) == len(cadena2)):
        if sorted(cadena1) == sorted(cadena2):
           return True
        else:
            return False
    else:
        return False
        
try:
    cadena1 = (sys.argv[1])
    cadena2 = (sys.argv[2])
    print is_anagram(cadena1, cadena2)
except:
    print 'El uso correcto del programa es:', sys.argv[0],' palabra1 palabra2'

