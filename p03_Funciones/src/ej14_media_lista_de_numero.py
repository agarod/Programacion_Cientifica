#!/usr/bin/python
# encoding: utf-8
import sys
'''
   __author__: "Ardiel Garcia Rodriguez"
   __email__: "alu0100266382@ull.edu.es"_
   __numero de ejercicio__: 14
   __enunciado__:Escriba una funcion que reciba una lista de numeros y
devuelva la media de dichos numeros. Tener en cuenta que para la lista
 vacia la media es cero
   __status__: "Terminado"
'''
def media(lista):
    longitud_lista = len(lista)
    resultado = 0.0
    if len(lista) > 0:
        candidato = lista[0]
        for elemento in lista:
            resultado = resultado + elemento
        return float(resultado / longitud_lista)
    else:
        return resultado 


try:
    lista = []
    longitud_argumento = len(sys.argv)
    for i in range(longitud_argumento ):
        if i != 0:
            numero = int(sys.argv[i])
            lista.append(numero)
    print media(lista)
    
      
        
except:
    print media(lista)
    print 'Este programa calcula el la media de la suma de los valores de una lista y si es vacia devuelve 0 \n\n'
    print 'la forma correcta de ejecutar este programa es', sys.argv[0], 'numeros'


