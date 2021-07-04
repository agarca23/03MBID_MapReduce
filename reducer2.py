#!/usr/bin/python
import sys

subproblema = None
array = []

def formatArray(array):
    string = array[0].rstrip()
    
    for i in range(1, len(array)):
        string = string+','+ array[i].rstrip()
    return string    
        

for claveValor in sys.stdin:
    cited, citing = claveValor.split(",", 1)
    #convertimos conteo a float
    #El primer subproblema es la primera persona
    if subproblema == None:
        subproblema = cited
        #si la persona es del subproblema actual, sumamos
    if subproblema == cited:
        array.append(citing)
    else: #si ya acabamos con el subproblema, emitimos
        listaParseada = formatArray(array)
        print("%s %s" % (subproblema, listaParseada))
        #Pasamos al siguiente subproblema
        subproblema = cited
        array.append(citing)
#el anterior bucle no emite el ultimo subproblema
listaParseada = formatArray(array)
print("%s %s" % (subproblema, listaParseada))

