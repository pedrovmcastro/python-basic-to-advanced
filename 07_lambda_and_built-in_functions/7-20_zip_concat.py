# Exercise 20:
# Write a program that uses the zip function to create a list of strings, 
# where each string is the concatenation of elements from two lists of characters.

# (PT-BR)
# Exercício 20:
# Escreva um programa que use a função zip para criar uma lista de strings, 
# onde cada string é a concatenação dos elementos de duas listas de caracteres.

# Example input
list1 = ["a", "b", "c", "d", "e"]
list2 = ["f", "g", "h", "i", "j"]

# Example output
# result_list = ["af", "bg", "ch", "di", "ej"]

combined_list = list(zip(list1, list2))
print(combined_list)

concatenated_list = [x + y for x, y in combined_list]
print(concatenated_list)
