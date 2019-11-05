"""


"""

import csv


def lineas(archivo):
	return csv.reader(archivo, delimiter=";")


with open("data/data-estudiantes.csv") as midata:
	lista = list(lineas(midata))
	print(list(map(lambda x: x[1], filter(lambda x: x[1] != "email", lista))))
	# funcion = map(lambda x: x[1], lista)
	# funcion2 = filter(lambda x: x != "email", funcion)
	# print(list(funcion2))