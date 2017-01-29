#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Dictionaries have a method called get that takes a key and a
 default value. If the key appears in the dictionary, get returns the
 corresponding value; otherwise it returns the default value.
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




try:
    elemento = sys.argv[1]
    print histogram(elemento)
except:
  
    print 'Uso de la funcion get en un diccionario \n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], 'palabra como por ejemplo abbcccdddd'
