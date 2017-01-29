#!/usr/bin/python
# encoding: utf-8
import sys
'''
   __author__: "Ardiel Garcia Rodriguez"
   __email__: "alu0100266382@ull.edu.es"_
   __numero de ejercicio__: 14
   __enunciado__:Escriba una funcion que, dada una lista de cadenas,
   devuleva la cadena mas larga. Si dos miden lo mismo y son las mas
   largas, la funcion devolvera una cualquiera de ellas.
   __status__: "Terminado"
'''
def comp(lista):
    longitud_lista = len(lista)
    candidato = lista[0]
    for i in range(len(lista)):
        if (candidato < lista[i]):
            candidato = lista[i]
    return candidato
 
try:
    lista = []
    longitud_argumento = len(sys.argv)
    for i in range(longitud_argumento ):
        if i != 0:
            elemento = (sys.argv[i])
            lista.append(elemento)
    print comp(lista)
    
      
        
except:
    print comp(lista)
    print 'Este programa cadenas de texto y devuelve la mas larga \n\n'
    print 'la forma correcta de ejecutar este programa es', sys.argv[0], 'cadena 1, cadena 2,...'


