#!/usr/bin/python
# encoding: utf-8
import sys
'''
   __author__: "Ardiel Garcia Rodriguez"
   __email__: "alu0100266382@ull.edu.es"_
   __numero de ejercicio__: 11
   __enunciado__:Escriba una funcion que determine (mediante la devolucion
     de True o False) si dos numeros dados son amigos. Una paeja de enteros
     positivos a y b se llman numeros amigos si a es la suma de los 
     divisores propios de b y bes la suma de los divisores propios de a
   __status__: "Terminado"
'''

def menu_generico(lista):

    for i in range(len(lista)):
        print i,'. ',lista[i]
    elegir(lista)

def elegir(lista):
    ans = False
    tam_menu = (len(lista))
    while (ans == False):
        option = int(raw_input('Inserte el numero de su eleccion'))
        if (option < tam_menu) :
            print option, '.' , lista[option]
            ans = True
        else:
            print 'Ha elegido una opcion incorrecta'
            ans = False
try:
    lista = []
    longitud_argv = len(sys.argv)
    for i in range(longitud_argv):
        if i != 0:
            lista.append(sys.argv[i])
    menu_generico(lista)
        
        
except:
    if longitud_argv <= 1:
        print 'Este programa comprueba si dos numeros son amigos \n\n'
        print 'la forma correcta de ejecutar este programa es', sys.argv[0], 'numero1 numero2'


