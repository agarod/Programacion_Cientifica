#!/usr/bin/python
# encoding: utf-8

'''
   __author__: "Ardiel Garcia Rodriguez"
   __email__: "alu0100266382@ull.edu.es"_
   __numero de ejercicio__: 11
   __enunciado__:modulo de funciones matematicas
   __status__: "Terminado"

'''

def list_to_set(lista):
    return list(set(lista))


def union(a, b):
    a = list_to_set(a)
    b = list_to_set(b)
    return list_to_set(a + b)

def intersection(a, b):
    a = list_to_set(a)
    b = list_to_set(b)

    cto  = []
    for i in a:
        if i in b:
            cto.append(i)
    return cto

def difference(a, b):
    a = list_to_set(a)
    b = list_to_set(b)

    cto = []
    for i in a:
        if i not in b:
            cto.append(i)
    return cto

def equal(a, b):
    a = list_to_set(a)
    b = list_to_set(b)
    if sorted(a) == sorted(b):
        return True
    else: 
        return False
