#!/usr/bin/python
# encoding: utf-8
import sys
import random
'''
   __author__: "Ardiel Garcia Rodriguez"
   __email__: "alu0100266382@ull.edu.es"_
   __numero de ejercicio__: 11
   __enunciado__:Escriba una funcion sin argumentos que genere un numeor aleatorio entre -10 y 10 y luego genere otra funcion a la que se le pase un valor MIN y otro MAX
   __status__: "Terminado"
'''
MIN = -10
MAX = 10
def random_generator():
    return random.randint(MIN,MAX)


def random_generator_con_limites_definidos(numero1, numero2):
    return random.randint(numero1,numero2)
try:
    longitud_argumento = len(sys.argv)
    print longitud_argumento
    if (longitud_argumento == 1):
        print random_generator()
    else:
        numero1 = int(sys.argv[1])
        numero2 = int(sys.argv[2])
        print random_generator_con_limites_definidos(numero1, numero2)
except:
    if (longitud_argumento <= 1):
        print random_generator()
    else:
        numero1 = sys.argv[1]
        numero2 = sys.argv[2]
        print random_generator_con_limites_definidos(numero1, numero2)
    print 'Este programa genera un numero aleatorio \n\n'
    print 'la forma correcta de ejecutar este programa es', sys.argv[0], 'min max'
