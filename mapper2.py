#!/usr/bin/python
import sys

firstLine= True
for linea in sys.stdin:
    if firstLine:
        firstLine = False
        continue
    citing, cited = linea.split(',')
    cited = cited.rstrip()
    print("%s %s" % (cited, citing))