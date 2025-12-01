"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    sums = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            value = int(columns[1])
            letters = columns[3].split(",")
            for letter in letters:
                if letter in sums:
                    sums[letter] += value
                else:
                    sums[letter] = value
    result = dict(sorted(sums.items()))
    return result

