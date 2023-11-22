""" Identifica los tres productos lácteos más vendidos basados en la cantidad total vendida. """
""" Informe los productos que actualmente tienen una cantidad en stock por debajo del umbral mínimo, mostrando stock actual y umbral minimo. """
from llavebygurise import *
import csv


def stock(arch1):
    lst2 = []
    arch3 = csv.reader(arch1)
    for columna in arch3: #Leemos el archivo csv mediante un for para iterar cada objeto.
        umbralMin = float(columna[21])
        cant = float(columna[20])
        nombre = columna[6]
        if umbralMin > cant: #Comparamos el umbral Min con la cantidad, para saber si el stock es el acorde.
            tuplaBB = (umbralMin,cant,nombre)
            lst2.append(tuplaBB) #Agregamos la tupla creada anteriormente a una lst para luego poder printearla.
    for tupla in lst2:
        print(f"Umbral Minimo: {tupla[0]} Cantidad: {tupla[1]} Nombre: {tupla[2]}\n")


def calcular_vendidos(arch1):
    lst = []
    arch2 = csv.reader(arch1)
    for columna in arch2: #Leemos el archivo csv mediante un for para iterar cada objeto.
        tuplaAA = (int(columna[15]), columna[6])
        if tuplaAA not in lst: # Si la tupla con el stock y el nombre del producto no estan en la lista la agregamos.
            lst.append(tuplaAA)
            lst.sort() #Ordenamos la lista de menor a mayor por stock.
    for tupla in lst[-3:]: #Solamente nos pide los 3 mayores elementos, utilizamos el metodo split.
        print(f"Stock: {tupla[0]}\nProducto: {tupla[1]}\n")

def main():
    nombrearch = input("Ingrese el nombre del archivo seguido del .csv: ")
    try:
        arch29 = open(nombrearch,"r")
        arch29.readline()
        stock(arch29)
        arch29.close()
    except FileNotFoundError:
        print("ERROR archivo no encontrado. ")
    else:
        arch29.close()
    nombrearch2 = input("Ingrese el nombre del archivo seguido del .csv: ")
    try:
        arch1 = open(nombrearch2,"r")
        arch1.readline()
        calcular_vendidos(arch1)
    except FileNotFoundError:
        print("ERROR archivo no encontrado. ")
    else:
        arch1.close()
main()
