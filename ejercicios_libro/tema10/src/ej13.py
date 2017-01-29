#!/usr/bin/python
# encoding: utf-8
import sys
import time
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Two words “interlock” if taking alternating letters from each
 forms a new word. For example, “shoe” and “cold” interlock to form
 “schooled.” 
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

def interlock(word_list, word):
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds) 

def interlock_general(word_list, word, n=3):
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True

try:
    word_list = make_word_list(sys.argv[1])

    for word in word_list:
        if interlock(word_list,word):
            print word, word[::2], word[1::2]
    
except:
    print 'El uso correcto del programa es:', sys.argv[0],' words.txt'

