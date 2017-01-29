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

def mostrar(elemento):
    indice = len(elemento) - 1
    while indice >=0:
        print elemento[indice]
        indice = indice - 1

try:
    elemento = sys.argv[1]
    mostrar(elemento)

except:
    mostrar(elemento)
    print 'Este programa es un dado electronico \n\n'
    print 'la forma correcta de ejecutar este programa es', sys.argv[0]
