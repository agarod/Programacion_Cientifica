#!/usr/bin/python
# encoding: utf-8
import sys
'''
   __author__: "Ardiel Garcia Rodriguez"
   __email__: "alu0100266382@ull.edu.es"_
   __numero de ejercicio__: 10
   __enunciado__:Escriba una funcion que indique si un numero dado es 
   o no es perfcto.
   __status__: "Terminado"
'''
def es_perfecto(numero):
    sumatorio=0
    for i in range(1, numero):
        if numero% i == 0:
            sumatorio = sumatorio + i
    return sumatorio == numero:
try:
    numero = int(sys.argv[1])
    print es_perfecto(numero)
        
except:
    print 'Este programa comprueba si el numero es perfecto \n\n'
    print 'la forma correcta de ejecutar este programa es', sys.argv[0], 'numero'


