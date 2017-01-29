#!/usr/bin/python
# encoding: utf-8
import sys
'''
   __author__: "Ardiel Garcia Rodriguez"
   __email__: "alu0100266382@ull.edu.es"_
   __numero de ejercicio__: 9
   __enunciado__:Escriba una fucnion que reciba una cadena y devuelva
   cierto si empieza por minuscula y falso en caso contrario
   __status__: "Terminado"
'''
def comprobar_cadena(cadena):
    return ((ord(cadena[0]) >= ord('A')) and (ord(cadena[0]) <= ord('Z')))

try:
    cadena = sys.argv[1]
    print comprobar_cadena(cadena)
except:
    print 'Este programa dice si una cadena empieza por mayuscula o minuscula \n\n'
    print 'la forma correcta de ejecutar este programa es', sys.argv[0], 'cadena'


