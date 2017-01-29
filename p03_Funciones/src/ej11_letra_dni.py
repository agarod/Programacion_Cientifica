#!/usr/bin/python
# encoding: utf-8
import sys
'''
   __author__: "Ardiel Garcia Rodriguez"
   __email__: "alu0100266382@ull.edu.es"_
   __numero de ejercicio__: 11
   __enunciado__:Escriba una funcion llamada letra_dni que, dado
   dado un numero de DNI, devuelva la letra que le corresponde.
   __status__: "Terminado"
'''
NUM_LETRAS = 23
LETRAS =  'TRWAGMYFPDXBNJZSQVHLCKE'
def letra_dni(numero):
    resultado = numero % NUM_LETRAS
    return LETRAS[resultado]

try:
    numero = int(sys.argv[1])
    print letra_dni(numero)
        
except:
    print 'Este programa resuelve la letra del DNI \n\n'
    print 'la forma correcta de ejecutar este programa es', sys.argv[0], 'numero'


