#!/usr/bin/python
# encoding: utf-8
import sys
import random
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:More anagrams!

    Write a program that reads a word list from a file (see Section 9.1)
 and prints all the sets of words that are anagrams.

    Here is an example of what the output might look like:

    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    ['retainers', 'ternaries']
    ['generating', 'greatening']
    ['resmelts', 'smelters', 'termless']

    Hint: you might want to build a dictionary that maps from a set of
 letters to a list of words that can be spelled with those letters. The
 question is, how can you represent the set of letters in a way that can be
 used as a key?
2.-    Modify the previous program so that it prints the largest set of
 anagrams first, followed by the second largest set, and so on.

3.-    In Scrabble a “bingo” is when you play all seven tiles in your rack,
 along with a letter on the board, to form an eight-letter word. What set of
 8 letters forms the most possible bingos?
   email: alu0100266382@ull.edu.es
'''



def create_dict(fichero):
    fin = open(fichero)
    res = {}
    
    for line in fin:
        word = line.strip()
        s = list(word)
        s.sort()

        sorted_char_string = ""
        for char in s:
            sorted_char_string += char

        if sorted_char_string in res:
            res[sorted_char_string] += [word]
        else:
            res[sorted_char_string] = [word]
            
    return res

def sort_dict(d):
    res = []
      
    for key, value in d.items():
        res += [(len(value), value)]
    return res
                    


def print_anagrams(anagram_list, sorted):
    if sorted:
        anagram_list.sort(reverse = True)
    for (count, anagrams) in anagram_list:
        if count >= 2:
            print count, anagrams


def scrabble_bingos(anagram_list):

    res = []
    for (count, anagrams) in anagram_list:
        if len(anagrams[0]) == 8 and count >= 2:
            res += [(count, anagrams)]
            
    res.sort(reverse = True)
    print res[0]


try:

    dictionary = create_dict(sys.argv[1])
    anagram_list = sort_dict(dictionary)
    scrabble_bingos(anagram_list)
except:
    print 'Encuentra anagramas\n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], 'fichero con lista de palabras, ej: words.txt'

