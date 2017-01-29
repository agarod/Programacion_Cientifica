#!/usr/bin/python
# encoding: utf-8

'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio: Fermat’s Last Theorem says that there are no 
positive integers a, b, and c such that
an + bn = cn 
for any values of n greater than 2.
    Write a function named check_fermat that takes four
 parameters—a, b, c and n—and that checks to see if Fermat’s 
theorem holds. If n is greater than 2 and it turns out to be
 true that
    an + bn = cn 

    the program should print, “Holy smokes, Fermat was wrong!” 
Otherwise the program should print, “No, that doesn’t work.”
    Write a function that prompts the user to input values for
 a, b, c and n, converts them to integers, and uses check_fermat 
to check whether they violate Fermat’s theorem.
   email: alu0100266382@ull.edu.es
'''


def check_fermat(a, b, c, n):
    valor = (a ** n) + (b ** n)
    valor2 = (c ** n)
    if (valor == valor2) & (n > 2):
        print 'Fermat funciona'
    else:
        print 'Fermat no funciona'



a = int(raw_input('Introduzca un valor para a: '))
b = int(raw_input('Introduzca un valor para b: '))
c = int(raw_input('Introduzca un valor para c: '))
n = int(raw_input('Introduzca un valor para n: '))
check_fermat(a,b,c,n) 
