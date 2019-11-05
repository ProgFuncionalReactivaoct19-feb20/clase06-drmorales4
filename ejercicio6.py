"""
	@drmorales4
	ejercicio6

"""

import csv


def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter=";")

with open("data/data-estudiantes.csv") as midata:
	lineas = (list(lineasDiccionario(midata)))
	
	resultado = map(lambda x: "%s - %s" % (list(x.items())[0][1].split(" ")[1], list(x.items())[1][1].split(".")[0]), lineas)
	
	print(list(resultado))