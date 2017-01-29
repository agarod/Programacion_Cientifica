#!/usr/bin/python
# encoding: utf-8
import sys
import time
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Two words are “rotate pairs” if you can rotate one of them and
   get the other. 
   email: alu0100266382@ull.edu.es
'''
    
def create_dict(fichero):
    fin = open(fichero)
    result = {}

    for line in fin:
        word = line.strip()
        result[word] = word
    return result

def rotate_word(s, cambio):
    result = ""
    for char in s:
        print char, ' <-----' 
        result += chr((((ord(char) + (cambio % 26)) % 123) % 97) + 97)
        print result, '**------'
    return result

def find_pairs():
    for word in words:
        all_rotations = []
        for i in range(1, 26):
            rotated = rotate_word(word, i)
            all_rotations += [rotated]
        for i in range(len(all_rotations)):
            if all_rotations[i] in words:
#                print word, i + 1, all_rotations[i]
                print word, all_rotations[i]
                    
try:

    fichero = sys.argv[1]      
    words = create_dict(fichero)
    find_pairs()
   
except:
    print 'Programa que encuentras pares de palabras que esten rotadas \n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], ' y un fichero, ej: words.txt'
