#!/usr/bin/python
# encoding: utf-8
import sys
import time
import rsa

'''Nombre: Ardiel
   Apellidos: Garcia Rodriguez
   Ejercicio:RSA
   email: alu0100266382@ull.edu.es
'''

PUB,PRIV = rsa.newkeys(256)

def code(texto):
    return rsa.encrypt(texto.encode('utf8'),PUB)

def decode(texto_codificado):
    return rsa.decrypt(texto_codificado,PRIV).decode('utf8')



try:

    text = (sys.argv[1])
    message_encrypt = code(text)
    print message_encrypt
    message_decrypt = decode(message_encrypt)
    print message_decrypt 
      
except:

    print 'Programa Funcion de ackerman con memoria \n\n'
    print 'Para su correcto uso debe introducirtse',sys.argv[0], 'texto a cifrar'

