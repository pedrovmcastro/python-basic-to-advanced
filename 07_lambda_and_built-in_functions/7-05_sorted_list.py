# Exercise 5:
# Sort a list of strings based on the length of each string, from shortest to longest, using the sorted function.

# (PT-BR)
# Exercício 5:
# Ordene uma lista de strings com base no comprimento de cada string, do menor para o maior, usando a função sorted.

fruits = ['kiwi', 'passion fruit', 'banana', 'avocado', 'pear']
print(sorted(fruits, key=lambda x: len(x)))
