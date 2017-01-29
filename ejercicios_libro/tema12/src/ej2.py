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

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word),word))
    t.sort(reverse = True)
    res = []
    for length, word in t:
        res.append(word)
    i = 0
    final = []
    while i <= len(res)-2:
        if len(res[i]) == len(res[i + 1]):
            y_list = [res[i],res[i + 1]]
            random.shuffle(y_list)
            final = final + y_list
            i = i + 2
        else:
            final.append(res[i])
            i = i + 1
    if i == len(res) - 1:
        final.append(res[i])
    return final

try:
    t = []
    longitud_parametro = len(sys.argv)
    for i in range(longitud_parametro):
       if (i != 0):
           elemento = (sys.argv[i])
           t.append(elemento)
    print sort_by_length(t)
except:
    print 'Ordena una lista de palabras de forma inversa \n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], 'lista de palabras separadas por espacio'

