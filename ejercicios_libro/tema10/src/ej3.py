#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Write a function that takes a list of numbers and returns the
   cumulative sum; that is, a new list where the ith element is the sum of the
   first i+1 elements from the original list. For example, the cumulative sum
   of [1, 2, 3] is [1, 3, 6]. 
   email: alu0100266382@ull.edu.es
'''

def acumulative_sum(t):
    res = []
    for i in range(len(t)):
        if (i == 0):
            res.append(t[0])
        else:
            res.append(res[i-1]+t[i])
    return res


try:
    t = []
    longitud_parametro = len(sys.argv)
    for i in range(longitud_parametro):
       if (i != 0):
           numero = int(sys.argv[i])
           t.append(numero)
    print acumulative_sum(t)
except:
    print 'El uso correcto del programa es:', sys.argv[0],' valor1 valor2 ...'

