#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Read the documentation of the dictionary method setdefault and use it to write a more concise version of invert_dict.
   email: alu0100266382@ull.edu.es
'''

def store(fichero):
    fin = open(fichero)
    d1=dict()
    i=0
    for line in fin:
        words=line.split()
        for i in range(len(words)):
            d1[words[i]]=i
    return d1

def histogram(s):
    d = dict()
    for c in s:
        d[c]=d.get(c,0)+1
    return d

def invert_dict(d):
    inverse = {}
    for key, val in d.iteritems():
        inverse.setdefault(val, []).append(key)
    return inverse

try:
    elemento = sys.argv[1]
    h = histogram(elemento)
    d = dict(h)
    inverse = invert_dict(d)
    for val, keys in inverse.iteritems():
        print val, keys
    
except:
  
    print 'imprime los valores de las claves alfabeticamente \n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], 'palabra como por ejemplo parrot'
