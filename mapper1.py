#!/usr/bin/python
import sys

for linea in sys.stdin:
    persona, articulo, cantidad, devolucion = linea.split(';')
    cantidad = float(cantidad)
    if devolucion == 'Cierto\n':
        cantidad = -cantidad
    else:
        cantidad = cantidad
    print("%s;%s" % (persona, cantidad))