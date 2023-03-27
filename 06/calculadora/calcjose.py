#!/usr/bin/env python
# coding: utf-8
#
# Programa principal de calculadora

from libfuncjose import *
while True :
    oper={ 
      "+" : ("Resultado:",  suma ),
      "-" : ("Resultado:",  rest ),
      "*" : ("Resultado:",  mult ),
      "/" : ("Resultado:",  divi ),
      "%" : ("Resultado:",  modu ),
      "√" : ("Resultado:",  root )
    }
    op=(input("Ingrese la operación (+, -, *, /, % o √): "))
    if oper == ('+','-','*','/','%') :
        a=int(input("Ingrese el primer operando: "))
        b=int(input("Ingrese el segundo operando: "))
        (nombre, func) = oper[op]
        print("{} es: {}.".format(nombre,func(a,b)))
    else :
        if oper == '√' :
            a=int(input("Ingrese el primer operando: "))
            (nombre, func) = oper[op]
            print("{} es: {}.".format(nombre,func(a)))
        else :
            print("Operador inválido. Intente de nuevo más tarde.")
    
    continuar = input('Desea continuar? S / N :')
    if continuar.lower() in "s si y yes":
       continue
    else:
        break

