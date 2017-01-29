#!/usr/bin/python
# encoding: utf-8
import sys
import time
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Two words are a “reverse pair” if each is the reverse of the
 other. Write a program that finds all the reverse pairs in the word list
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

def reverse_pair(word_list, word):
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)

try:
    word_list = make_word_list(sys.argv[1])
    for word in word_list:
        if reverse_pair(word_list,word):
            print word, word[::-1]
    
except:
    print 'El uso correcto del programa es:', sys.argv[0],' words.txt'

