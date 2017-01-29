#!/usr/bin/python
# encoding: utf-8
import sys
import random
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:In this example, ties are broken by comparing words, so words
 with the same length appear in reverse alphabetical order. For other
 applications you might want to break ties at random. Modify this example so
 that words with the same length appear in random order. Hint: see the
 random function in the random module
   email: alu0100266382@ull.edu.es
'''

def most_frequent(s):
    d = dict()
    inv = dict()
    for char in s:
        if char in string.ascii_letters:
            letter = char.lower()
            d[letter] = d.get(letter,0) +1
        
    for letter, freq in d.items():
        inv.setdefault(freq, []).append(letter)

    for freq in sorted(inv, reverse = True):
        print ('{:.2%}:'.format(freq/(sum(list(inv)*len(inv[freq])))),','.join(inv[freq]))

def make_histogram(s):
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


def read_file(filename):

    return open(filename).read()

try:
    t = []
    longitud_parametro = len(sys.argv)
    for i in range(longitud_parametro):
       if (i != 0):
           elemento = (sys.argv[i])
           t.append(elemento)
    u = most_frequent(read_file(sys.argv[1]))
    for x in u:
        print x
except:

    print 'Ordena una lista de palabras de forma inversa \n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], 'lista de palabras separadas por espacio'

