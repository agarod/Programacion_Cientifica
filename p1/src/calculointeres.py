#! /usr/bin/python
# encoding: utf-8
'''
   Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Asignatura: Programacion Cientifica
   Objetivo: Calcular la cantidad resultante de aplicar un capital con una tasa de interes durante un tiempo determinado en años
'''
print 'Introduzca un cantidad en euros: '
capital = float(raw_input())
print ' Introduzca una tasa de interes: '
interes = float(raw_input())
print ' Introduzca el numero de años: ' 
agno = float(raw_input())


cantidad = capital*(1+(interes/100))**agno

print '%.2f'% (cantidad)
