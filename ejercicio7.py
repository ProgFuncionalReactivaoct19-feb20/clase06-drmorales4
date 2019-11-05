"""
	@drmorales4
	ejecicio7

	Dado el siguiente archivo:

	- Filtrar los registros cuyos países tengan en su nombre una longitud mayor a 10

	- Ordenar la lista en función del día de nacimiento.

"""

import csv

def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter="\t")

with open("data/trabajadores.csv") as midata:
	lineas = (list(lineasDiccionario(midata)))

	# Filtrar los registros cuyos países tengan en su nombre una longitud mayor a 10
	funcion1 = filter(lambda x: len(list(x.items())[2][1])>= 10, lineas)
	print("Nombres de paises con longitud mayor a 10:\n", list(funcion1))

	# linea de separacion
	print("\n--------------------------------------------------------------------------------------\n")

	# Ordenar la lista en función del día de nacimiento
	funcion2 = list(filter(lambda x: list(x.items()), lineas))
	ordener = sorted(funcion2, key = lambda x: list(x.items())[1][1].split("-")[2])
	print("Lista ordenada por dia de nacimiento:\n", ordener)
