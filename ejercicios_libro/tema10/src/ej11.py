#!/usr/bin/python
# encoding: utf-8
import sys
import time
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Write a function that reads the file words.txt and builds a
   list with one element per word. Write two versions of this function, one
   using the append method and the other using the idiom t = t + [x]. Which
   one takes longer to run? Why?
   email: alu0100266382@ull.edu.es
'''

from bisect import bisect_left


def make_word_list(fichero):
    word_list = []
    fin = open(fichero)
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    i = bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False

try:
    word_list = make_word_list(sys.argv[1])
    for word in ['alien', 'allen']:
        print word, 'in list', in_bisect(word_list, word)
    
except:
    print 'El uso correcto del programa es:', sys.argv[0],' word.txt'

