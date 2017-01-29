#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Write a function called nested_sum that takes a nested list of
 integers and add up the elements from all of the nested lists.
   email: alu0100266382@ull.edu.es
'''

def nested_sum(lista):
    total = 0
    for i in range(len(lista)):
        total = total + lista[i]
    return total


try:
    lista = []
    longitud_parametro = len(sys.argv)
    
    for i in range(longitud_parametro):
       if (i != 0):
           numero = int(sys.argv[i])
           lista.append(numero)
    print nested_sum(lista)
except:
    nested_sum(lista)
    print 'El uso correcto del programa es:', sys.argv[0],' valor1 valor2 ...'

