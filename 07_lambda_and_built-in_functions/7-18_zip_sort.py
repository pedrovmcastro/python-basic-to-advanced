# Exercise 18:
# Write a program that uses the zip function to sort two lists in ascending order based on the values of the first list.

# (PT-BR)
# Exercício 18:
# Escreva um programa que use a função zip para ordenar duas listas em ordem crescente, de acordo com os valores da primeira lista.

list1 = [3, 1, 4, 2, 5]
list2 = ["c", "a", "d", "b", "e"]

combined_lists = list(zip(list1, list2))  # Combining the two lists into tuples.
print(combined_lists)

sorted_lists = sorted(combined_lists)  # The magic happens here. Sorting the two lists.
print(sorted_lists)

sorted_lists = list(zip(*sorted_lists))  # Splitting the values into two tuples.
print(sorted_lists)

list1, list2 = sorted_lists

print(f'List 1: {list(list1)}\nList 2: {list(list2)}')
