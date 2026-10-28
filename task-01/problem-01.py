# Problema 1. Procesamiento de una lista de enteros. 
# Crea una función que reciba una lista de enteros por parámetro y devuelva otra
# lista, de acuerdo a las siguientes acciones:
# 1. Eliminar los números negaƟvos de la lista.
# 2. Eliminar los valores que están repeƟdos, quedándonos con uno de ellos.
# 3. Ordenar los números resultantes de menor a mayor.
# Por ejemplo, si le pasara [4, -1, 2, 4, 3, -5, 2], debería retornar [2,3,4]. 

def processNumbers(numbers): 
    result = []

    for num in numbers:
        if num > 0:
            if num not in result:
                result.append(num)

    result.sort()
    return result

mi_lista = [4, -1, 2, 4, 3, -5, 2]
print(processNumbers(mi_lista))