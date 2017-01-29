#!/usr/bin/python
# encoding: utf-8
import sys

def create_dict(fichero):
    fin = open(fichero)
    res = {}
        
    for line in fin:
        word = line.strip()
        res[word] = []
            
    for element in ["a", "i", ""]:
        res[element] = []

    return res

def add_children(d):
    for key in d.keys():
        children = []
        for i in range(len(key)):
            candidate = key[:i] + key[i+1:]
            if candidate in d and candidate not in children:
                children.append(candidate)
        d[key] = children
            
    return d

def recursive_trails(d):
    res = []

    def helper(key, result):
        if d[key] == []:
            return
        if key in ["a", "i", ""]:
            res.append((len(result[0]), result))
        else:
            for entry in d[key]:
                return helper(entry, result + [entry])
            
    for key,value in d.items():
        helper(key, [key])

    return res

def top_n(results):
    results.sort(reverse = True)
    print results[0]

                   
try:
    number = int(sys.argv[2])
    fichero = sys.argv[1]
    d = create_dict(fichero)
    add_children(d)
    trails = recursive_trails(d)
    top_n(trails)

except:
    print 'Encuentra anagramas\n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], 'fichero con lista de palabras, ej: words.txt , se mostrara el elemento mas grande'




