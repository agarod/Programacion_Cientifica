#!/usr/bin/python
# encoding: utf-8

'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio: A palindrome is a word that is spelled the same backward
 and forward, like “noon” and “redivider”. Recursively, a word is a 
palindrome if the first and last letters are the same and the middle 
is a palindrome.

The following are functions that take a string argument and return 
the first, last, and middle letters:
   email: alu0100266382@ull.edu.es
'''

def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

try:
    is_palindrome(sys.argv[1])
except:
    print 'Este programa calcula si una palabra es palindroma\n\n'
    print 'Debe seguir el modo de uso', argv[0], ' palabra'

