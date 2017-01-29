#!/usr/bin/python
# encoding: utf-8

'''
---------------------------------------
    Nombre: Ardiel Garcia Rodriguez
    Practica: A function object is a value you can assign to a variable or
    pass as an argument. For exameple, do_twice is a function that takes a 
    function that takes a function object as an argunment and calls it twice
    1.-Type this example into a script and test it
    2.-Modify do_twice so that it takes two arguments, a function object and
       calls the function twice, passing the value as an argument
    3.-Write a more general version of print_spam, called print_twice, that 
       takes a string as a parameter and prints it twice.
    4.-Use the modified version fo do_twice to call print_twice twice,
       passing 'spam' as an argunment
    5.-Define a new functino called do_four that takes a function object and
       a value and calls the function for times, passing the value as a 
       parameter. There should be only two statements in the body of this 
       funcion, not four
    Email: alu0100266382@ull.edu.es
    
---------------------------------------
'''
def do_twice(f, arg):
    f(arg)
    f(arg)
def print_twice(arg):
    print arg
    print arg

do_twice(print_twice, 'spam')

