#!/usr/bin/python
# encoding: utf-8

'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio: Write a function called do_n that takes a function 
object and a number, n, as arguments, and that calls the given 
function n times.
   email: alu0100266382@ull.edu.es
'''

def countdown(f,n):
    if n > 0:
        f()
        countdown(f, n-1)

def imprimir():
    print 'hola'

n= 2;
countdown(imprimir,n)
