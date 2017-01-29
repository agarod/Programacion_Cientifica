#!/usr/bin/python
# encoding: utf-8
import sys
'''
   __author__: "Ardiel Garcia Rodriguez"
   __email__: "alu0100266382@ull.edu.es"_
   __numero de ejercicio__: 11
   __enunciado__:Escriba una funcion a la que se le pase un DNI y una letra
     y compruebe si es correcta.
   __status__: "Terminado"
'''
NUM_LETRAS = 23
LETRAS =  'TRWAGMYFPDXBNJZSQVHLCKE'
def comprobacion(numero, letra):
    resultado = numero % NUM_LETRAS
    return (LETRAS[resultado] == letra)

try:
    longitud = len(sys.argv[1])
    cadena = sys.argv[1]
    numero = int(cadena[:longitud -1])
    letra = cadena[longitud - 1]
    print comprobacion (numero, letra)
        
except:

    print 'Este programa comprueba la letra del DNI \n\n'
    print 'la forma correcta de ejecutar este programa es', sys.argv[0], 'numeor de DNI, ej: 12345678A'


