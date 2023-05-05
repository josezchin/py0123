#!/usr/bin/env python
# coding: utf-8
#
# Programa principal de calculadora

from libfunc import *

oper={ 
  "+" : ("La suma",      "y",     suma ),
  "-" : ("La resta",     "y",     rest ),
  "*" : ("El producto",  "por",   mult ),
  "/" : ("El cociente",  "entre", divi ),
  "%" : ("El remanente", "y",     modu )
}

a=int(input("Ingrese el primer operando: "))
b=int(input("Ingrese el segundo operando: "))
op=(input("Ingrese la operación (+, -, *, / o %): "))

if op in oper :
    (nombre, union, func) = oper[op]
    print("{} de {} {} {} es: {}.".format(nombre,a,union,b,func(a,b)))
else :
    print("Operador inválido. Intente de nuevo más tarde.")
