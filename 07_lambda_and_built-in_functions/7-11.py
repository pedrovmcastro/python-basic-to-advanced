# Exercise 11:
# Write a Python function that uses filter() to return a list with the prime numbers from a given list of integers.
# For example, if the list is [2, 3, 4, 5, 6, 7], the function should return [2, 3, 5, 7].

# (PT-BR)
# Exercício 11:
# Escreva uma função em Python que use filter() para retornar uma lista com os números primos de uma lista dada de inteiros.
# Por exemplo, se a lista for [2, 3, 4, 5, 6, 7], a função deve retornar [2, 3, 5, 7].

import math


def is_prime(num):
    if not isinstance(num, int) or num < 2:
        return False

    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


lista = [2, 3, 4, 5, 6, 7]
print(list(filter(is_prime, lista)))
