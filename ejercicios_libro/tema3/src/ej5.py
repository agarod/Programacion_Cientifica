#!/usr/bin/python
# encoding: utf-8

'''
---------------------------------------
    Nombre: Ardiel Garcia Rodriguez
    Practica: This execise can be done using only the statements and other
    features we have learned so far 
    Email: alu0100266382@ull.edu.es
    
---------------------------------------
'''

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_border():
    print '+ - - -',

def print_slash():
    print '/      ',

def print_borders():
    do_twice(print_border)
    print '+'

def print_slashs():
    do_twice(print_slash)
    print '/'

def print_row():
    print_slashs()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid() 
