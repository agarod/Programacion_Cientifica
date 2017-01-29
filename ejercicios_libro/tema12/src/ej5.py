#!/usr/bin/python
# encoding: utf-8
import sys
import random
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Two words form a “metathesis pair” if you can transform one
 into the other by swapping two letters; for example, “converse” and
 “conserve.” Write a program that finds all of the metathesis pairs in the
 dictionary. 
   email: alu0100266382@ull.edu.es
'''



def create_dict(fichero):
    fin = open(fichero)
    res = {}
    
    for line in fin:
        word = line.strip()
        res[word] = []

    return res


def find_pairs(d):
        res = []
        
        for key, value in d.items():
            k = list(key)
            for i in range(len(key) - 1):
                for j in range(1, len(key)):
                    k[i], k[j] = k[j],  k[i]
                    candidate = make_string(k)
                    if candidate in d:
                        print key, candidate
        return res

def make_string(k):
    res = ""
    for element in k:
        res += element
    return res

try:
    d = create_dict(sys.argv[1])
    print find_pairs(d)

except:
    print 'Intercambia letas\n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], 'fichero con lista de palabras, ej: words.txt'

