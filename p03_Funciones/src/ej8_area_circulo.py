#!/usr/bin/python
# encoding: utf-8
import sys
import math
'''
   __author__: "Ardiel Garcia Rodriguez"
   __email__: "alu0100266382@ull.edu.es"_
   __numero de ejercicio__: 8
   __enunciado__: Escriba una funcion llamada area_circulo que devuelva el
     valor de su area.
     Utilice el modulo math para el valor de PI
   __status__: "Terminado"
'''
def area_circle(radio):
    area = math.pi * (radio ** 2)
    return area

try:
    radio = int(sys.argv[1])
    print area_circle(radio)
except:
    print math.PI
    print 'Este programa calcula el radio de un circulo \n\n'
    print 'la forma correcta de ejecutar este programa es', sys.argv[0], 'valor del radio'


