#!/usr/bin/python
# encoding: utf-8
import sys
import string
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Two words are “rotate pairs” if you can rotate one of them and
   get the other. 
   email: alu0100266382@ull.edu.es
'''
    
def create_word_dict(fichero):
    d = dict()
    fin = open(fichero)
    for line in fin:
        word = line.strip().lower()
        d[word] = word
    return d

def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res

def rotate_pairs(word, word_dict):
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print word, i, rotated

try:
    fichero = sys.argv[1]
    dictionary = create_word_dict(fichero)
    for word in dictionary:
        rotate_pairs(word, dictionary)
except:
    dictionary = create_word_dict(fichero)
    for word in dictionary:
        rotate_pairs(word, word_dict)
    print 'Este programa es una modificacion sobrel el ejercicio 12 del tema 8 \n\n'
    print 'Modo de funcionamiento: ',sys.argv[0], 'nombre de fichero, ej:words.txt'
