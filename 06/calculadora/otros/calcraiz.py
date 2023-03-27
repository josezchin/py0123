#!/usr/bin/env python
# coding: utf-8
#
# Programa principal de calculadora

from libfuncraiz import *

oper={ 
  "√" : ("La raiz",      "de",     rai),
}

a=int(input("Ingrese el primer operando: "))
'''b=int(input("Ingrese el segundo operando: "))'''
op=(input("Ingrese la operación (√): "))

if op in oper :
    (nombre, union, func) = oper[op]
    print("{} de {} es: {}.".format(nombre,a,func(a)))
else :
    print("Operador inválido. Intente de nuevo más tarde.")
