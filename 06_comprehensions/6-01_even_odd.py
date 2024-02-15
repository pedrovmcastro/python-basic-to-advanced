"""
Exercise 1:
Create two list comprehensions for a list of numbers - one for even numbers in that list, 
and another for odd numbers in that list.


(PT-BR)
Exercício 1:
Faça duas list comprehension para uma lista de números - uma para números pares dessa lista, outra
para números impares dessa lista.
"""

numbers = [1, 2, 3, 4, 8, 12, 9, 5, 13]

print([number for number in numbers if number % 2 == 0])  # evens
print([number for number in numbers if number % 2 != 0])  # odds
