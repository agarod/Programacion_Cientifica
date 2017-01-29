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

def using_append(fichero):
    t = []
    fin = open(fichero)
    for line in fin:
        word = line.strip()
        t.append(word)
    return t
       
def using_suma(fichero):
    t = []
    fin = open(fichero)
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t
    
        
try:
    start_time = time.time()
    t = using_append(sys.argv[1])
    elapsed_time = time.time() - start_time
    print len(t)
    print t
    print elapsed_time, 'segundos'

    start_time = time.time()
    t = using_suma(sys.argv[1])
    elapsed_time = time.time() - start_time
    print len(t)
    print t
    print elapsed_time, 'segundos'

except:
    print 'El programa compara el tiempo de realizacion de un algoritmo'
    print 'El uso correcto del programa es:', sys.argv[0],' valor1'

