# Exercise 22:
# Write a program that uses the zip function to create a list of numbers, 
# where each number is the sum of the squares of elements from two lists of numbers.

# (PT-BR)
# Exercício 22:
# Escreva um programa que use a função zip para criar uma lista de números, 
# onde cada número é a soma dos quadrados dos elementos de duas listas de números.

# Example input
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# Example output
# result_list = [37, 53, 73, 97, 125]

combined_list = list(zip(list1, list2))
print(combined_list)

result_list = [x*x + y*y for x, y in combined_list]
print(result_list)

# More direct way:
print([x*x + y*y for x, y in zip(list1, list2)])
