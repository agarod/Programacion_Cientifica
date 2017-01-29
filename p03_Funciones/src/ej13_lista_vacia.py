#!/usr/bin/python
# encoding: utf-8
import sys
'''
   __author__: "Ardiel Garcia Rodriguez"
   __email__: "alu0100266382@ull.edu.es"_
   __numero de ejercicio__: 13
   __enunciado__:Considerando el siguiente codigo, hagta una traza para
   la llamada maximo([1, 10,-3, 0, 2, 6])¿Que ocurrirá si se llama a la funcion con una lista vacia?¿Como se podria solucionar el problema? Tenga
en cuenta que en Python hay un valor predefinido None que se utiliza
para denotar "ausencia de valor"
   __status__: "Terminado"
'''
def maximo(lista):
    if len(lista) > 0:
        candidato = lista[0]
        for elemento in lista:
            if elemento > candidato:
                candidato = elemento
        return candidato
    else:
        return None


try:
    lista = []
    longitud_argumento = len(sys.argv)
    for i in range(longitud_argumento ):
        if i != 0:
            numero = int(sys.argv[i])
            lista.append(numero)
    print maximo(lista)
    
      
        
except:
    print 'Este programa calcula el valor maximo de una lista y si es vacia devuelve None \n\n'
    print 'la forma correcta de ejecutar este programa es', sys.argv[0], 'numeros'


