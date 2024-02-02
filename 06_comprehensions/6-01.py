"""
Faça duas list comprehension para uma lista de números - uma para números pares dessa lista, outra
para números impares dessa lista.
"""
numeros = [1, 2, 3, 4, 8, 12, 9, 5, 13]

print([numero for numero in numeros if numero % 2 == 0])  # pares
print([numero for numero in numeros if numero % 2 != 0])  # impares
