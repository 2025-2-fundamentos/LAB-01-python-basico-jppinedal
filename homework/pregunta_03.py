"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    sums = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.split("\t")
            letter = columns[0]
            value = int(columns[1])
            if letter in sums:
                sums[letter] += value
            else:
                sums[letter] = value
    result = sorted(sums.items())
    return result
