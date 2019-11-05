"""
	@drmorales4
	Programacion Funcional:
		Funciones Puras
		Efectos Secundarios

"""
import csv

def lineas(archivo):
	return csv.reader(archivo, delimiter=";")

with open("data/data-estudiantes.csv") as midata:
	print(list(lineas(midata)))


# midata = open("data/data-eestudiantes.csv") # uso de grandes volumenes de \
		# datos es necesario cerrar el archivo *.
# print(list(lineas(midata)))
# midata.close()