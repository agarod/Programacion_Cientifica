#!/usr/bin/python
# encoding: utf-8

'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio: Write a function named ack that evaluates Ackermann’s 
function. Use your function to evaluate ack(3, 4), which should be 125. 
What happens for larger values of m and n? 
   email: alu0100266382@ull.edu.es
'''
import sys

def ackermann(n, m):
    if n == 0:
        return m + 1
    elif m == 0:
        return ackermann(n - 1,1)
    else:
        return ackermann(n - 1, ackermann(n, m - 1))

try:
    n = float(sys.argv[1])
    m = float(sys.argv[2])
    print (ackermann(n, m))
except:
    if (len(sys.argv) <= 2):
        print 'Escriba ej5.py [numero1] [numero2]'    
    elif (len(sys.argv) > 3):
        print 'Escriba ej5.py [numero1] [numero2]'    
    elif (sys.exc_info()[0] != 0):
        print 'El numero introducido es demasiado grande'

