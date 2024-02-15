# Exercise 11:
# Write a function that uses filter() to return a list with the even numbers from a given list.
# For example, if the list is [1, 2, 3, 4, 5], the function should return [2, 4].

# (PT-BR)
# Exercício 11:
# Escreva uma função que use filter() para retornar uma lista com os números pares de uma lista dada. 
# Por exemplo, se a lista for [1, 2, 3, 4, 5], a função deve retornar [2, 4].

lista = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, lista)))

# List Comprehension:
print([num for num in lista if num % 2 == 0])
