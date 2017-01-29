#!/usr/bin/python
# encoding: utf-8
import sys
import time
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Write a program that lists all the words that solve the Puzzler. 
   email: alu0100266382@ull.edu.es
'''
    
def create_word_dict(fichero):
    d = dict()
    fin = open(fichero)
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d

def read(fichero):
    fin = open(fichero)
    d1=dict()
    i=0
    for line in fin:
        words=line.split()
        for i in range(len(words)):
            d1[words[i]]=i
    return d1

def homophones(a, b, phonetic):
    if a not in phonetic or b not in phonetic:
        return False

    return phonetic[a] == phonetic[b]


def check_word(word, dictionary, phonetic):
    word1 = word[1:] 
    if word1 not in dictionary:
        return False
    if not homophones(word, word1, phonetic):
        return False

    word2 = word[0] + word[2:]
    if word2 not in dictionary:
        return False
    if not homophones(word, word2, phonetic):
        return False

    return True

                    
try:

    fichero = sys.argv[1]
    phonetic = read(fichero)
    dictionary = create_word_dict(fichero)

    for word in dictionary:
        if check_word(word, dictionary, phonetic):
            print word, word[1:], word[0] + word[2:]



   
except:
    print 'Programa que encuentras pares de palabras que esten rotadas \n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], ' y un fichero, ej: words.txt'
