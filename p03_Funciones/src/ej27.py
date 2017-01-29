#!/usr/bin/python
# encoding: utf-8
import sys
import random
'''
   __author__: "Ardiel Garcia Rodriguez"
   __email__: "alu0100266382@ull.edu.es"_
   __numero de ejercicio__: 11
   __enunciado__:Escriba una funcion que sea un dado electronico que
devuelva valores entre 1 y 6 aleatoriamente
   __status__: "Terminado"
'''

def sin_repetidos ( lista ) :
    resultado = [ ]
    for elemento in lista :
        if elemento not in resultado :
            resultado.append ( elemento )
    return resultado


sin_repetidos ( [ 9 , 3 , 7 , 0 , 9 , 1 , 0 , 3 , 0 ] )
print resultado
