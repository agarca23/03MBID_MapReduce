#!/usr/bin/python
import sys

subproblema = None
suma_cantidad = 0
for claveValor in sys.stdin:
    persona, cantidad = claveValor.split(";", 1)
    #convertimos conteo a float
    cantidad = float(cantidad)
    #El primer subproblema es la primera persona
    if subproblema == None:
        subproblema = persona
        #si la persona es del subproblema actual, sumamos
    if subproblema == persona:
        suma_cantidad = suma_cantidad + cantidad
    else: #si ya acabamos con el subproblema, emitimos
        print("%s;%s" % (subproblema, suma_cantidad))
        #Pasamos al siguiente subproblema
        subproblema = persona
        suma_cantidad = cantidad
#el anterior bucle no emite el ultimo subproblema
print("%s;%s" % (subproblema, suma_cantidad))
