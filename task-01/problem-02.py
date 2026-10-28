# Problema 2. Frecuencia de palabras en un texto.
# Escribe una función que reciba por parámetro una lista de palabras y la ruta a
# un fichero de texto y devuelva un diccionario que muestre cuantas veces
# aparecen las disƟntas palabras de la lista en el fichero de texto. Haz un pequeño
# programa que la ponga a prueba.
# Requisitos:
# 1. Eliminar signos de puntuación y converƟr todo a minúsculas.
# 2. Usar un diccionario donde la clave sea la palabra y el valor su frecuencia.
# 3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra. 

import string

def word_frequency(words_list, path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        return f"Error: Fichero no encontrado '{path}'"

    # 1.
    content = content.lower()
    for punctuation_mark in string.punctuation:
        content = content.replace(punctuation_mark, "")

        
    words_in_text = content.split()

    # 2.
    frequencies = {}
    for word in words_list:
        clean_word = word.lower()
        frequencies[clean_word] = words_in_text.count(clean_word)

    # 3.
    sorted_frequencies = dict(sorted(frequencies.items()))

    return sorted_frequencies


def main():
    test_path = "sample_text.txt"
    with open(test_path, "w", encoding="utf-8") as f:
        f.write("Hello, hola. Esto es un test. Primer test en Python. Python es un lenguaje de programación.")

    words = ["Hola", "Python", "test", "programación"]

    result = word_frequency(words, test_path)

    print("Diccionario:")
    print(result)

main()