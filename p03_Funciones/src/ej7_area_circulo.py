#!/usr/bin/python
# encoding: utf-8
import sys

'''
   __author__: "Ardiel Garcia Rodriguez"
   __email__: "alu0100266382@ull.edu.es"_
   __numero de ejercicio__: 7
   __enunciado__: Escriba una funcion llamada area_circulo que devuelva el
     valor de su area.
     Utilice el valor 3,1416 como aproximación de PI, y tenga en cuenta que
     el area del circulo es πr^2
   __status__: "Terminado"
'''
PI = 3.1416
def area_circle(radio):
    area = PI * (radio ** 2)
    return area

try:
    radio = int(sys.argv[1])
    print area_circle(radio)
except:
    print 'Este programa calcula el radio de un circulo \n\n'
    print 'la forma correcta de ejecutar este programa es', sys.argv[0], 'valor del radio'


