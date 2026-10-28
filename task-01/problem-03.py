# Problema 3. Trabajo con conjuntos
# Escribe una función que reciba dos listas de enteros y devuelva un diccionario
# con la siguiente información (ES OBLIGATORIO USAR CONJUNTOS PARA
# CALCULARLOS)
# 1. La intersección de ambos conjuntos (elementos comunes).
# 2. La unión de ambos conjuntos (todos los elementos sin duplicados).
# 3. La diferencia simétrica (elementos que están en uno u otro conjunto,
# pero no en ambos). 

def organizer(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    

    intersection = set_1 & set_2
    union = set_1 | set_2
    difference = set_1 ^ set_2
    
    result = {
        "interseccion": list(intersection),
        "union": list(union),
        "diferencia_simetrica": list(difference)
    }
    
    return result

def main():
    l1 = [1, 2, 3, 4, 9, 10]
    l2 = [3, 4, 5, 6, 10]
    print(organizer(l1, l2))

main()