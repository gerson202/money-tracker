﻿import matplotlib.pyplot as plt


def calcularTotales():

    totalCategorias = {
        "Comida": 0,
        "Entretenimiento": 0,
        "Servicios": 0,
        "Ropa": 0,
        "Sueldo": 0,
        "Prestamo": 0,
        "Venta": 0,
    }

    with open("historial.txt", "r") as historial:
        lines = historial.readlines()

    i = 1

    for line in lines:
        line = line.rstrip("\n")

        if i % 4 == 0:
            totalCategorias[lines[i - 3].rstrip("\n")] += int(lines[i - 2].rstrip("\n"))

        i += 1

    return totalCategorias


def eliminarCeros(dict):
    dictOut = {}
    for x, y in dict.items():
        if y != 0:
            dictOut[x] = y

    return dictOut


def generar():

    dict = eliminarCeros(calcularTotales())

    labels = dict.keys()
    values = dict.values()

    plt.pie(values, labels=labels, autopct="%1.1f%%")

    plt.show()
