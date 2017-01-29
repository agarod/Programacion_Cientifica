#!/usr/bin/python
# encoding: utf-8
import sys
'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:Write a function that reads the words in words.txt and stores
 them as keys in a dictionary. It doesn’t matter what the values are. Then
 you can use the in operator as a fast way to check whether a string is in
 the dictionary.
   email: alu0100266382@ull.edu.es
'''

def store(fichero):
    fin = open(fichero)
    d1=dict()
    i=0
    for line in fin:
        words=line.split()
        for i in range(len(words)):
            d1[words[i]]=i
    return d1



try:
    fichero = sys.argv[1]
    print store(fichero)
except:
  
    print 'Inserta el contenido de un fichero en un diccionario \n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], 'nombre de fichero (ej: words.txt)'

