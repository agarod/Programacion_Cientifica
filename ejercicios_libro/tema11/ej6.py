#!/usr/bin/python
# encoding: utf-8
import sys
import time
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Run this version of fibonacci and the original with a range of
 parameters and compare their run times.
   email: alu0100266382@ull.edu.es
'''
known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

def fibonacci_normal(n):
    if (n == 0) or (n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    elemento = int(sys.argv[1])
    start_time = time.time()
    print fibonacci(elemento)
    elapsed_time = time.time() - start_time
    print 'Tiempo que ha tardado', elapsed_time

    start_time = time.time()
    print fibonacci_normal(elemento)
    elapsed_time = time.time() - start_time
    print 'Tiempo que ha tardado', elapsed_time

    
  
except:
  
    print 'imprime los valores de la serie de fibonacci \n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], 'numero'
