"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    sums = {}
    with open("files/input/data.csv", "r") as file:
        for line in file:
            columns = line.strip().split("\t")
            letter = columns[0]
            parts = [p for p in columns[4].split(",") if p]
            col5_sum = 0
            for item in parts:
                if ":" in item:
                    # take the part after the last ':' and convert to int
                    try:
                        value = int(item.split(":")[-1])
                    except ValueError:
                        # skip malformed numbers
                        continue
                else:
                    try:
                        value = int(item)
                    except ValueError:
                        continue
                col5_sum += value
            if letter in sums:
                sums[letter] += col5_sum
            else:
                sums[letter] = col5_sum
    result = dict(sorted(sums.items()))
    return result