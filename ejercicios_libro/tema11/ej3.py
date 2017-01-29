#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Dictionaries have a method called keys that returns the keys of
 the dictionary, in no particular order, as a list.
   Modify print_hist to print the keys and their values in alphabetical
   order. 
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

def print_hist(s):
    h=histogram(s)
    k=h.keys()
    k.sort()
    for j in k:
        print j, h[j]


try:
    elemento = sys.argv[1]
     print_hist(elemento)
  
except:
  
    print 'imprime los valores de las claves alfabeticamente \n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], 'palabra como por ejemplo parrot'
