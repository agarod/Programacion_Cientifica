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
def sumatorio(begin, end):
    resultado = 0
    if begin > end :
        return resultado
    else:
        for begin in range(end):
            print begin
            print resultado
            resultado = resultado + begin
            print resultado
        return resultado
 
try:
    print sumatorio(int(sys.argv[1]),int(sys.argv[2]))        
except:
    print sumatorio(int(sys.argv[1]),int(sys.argv[2]))
    print 'Este programa cadenas de texto y devuelve la mas larga \n\n'
    print 'la forma correcta de ejecutar este programa es', sys.argv[0], 'cadena 1, cadena 2,...'


