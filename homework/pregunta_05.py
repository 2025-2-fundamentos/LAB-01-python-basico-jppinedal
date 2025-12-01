"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    stats = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.split("\t")
            letter = columns[0]
            value = int(columns[1])
            if letter in stats:
                current_max, current_min = stats[letter]
                stats[letter] = (max(current_max, value), min(current_min, value))
            else:
                stats[letter] = (value, value)
    result = [(letter, max_min[0], max_min[1]) for letter, max_min in sorted(stats.items())]
    return result

