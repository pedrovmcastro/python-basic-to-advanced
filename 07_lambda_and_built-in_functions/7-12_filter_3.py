# Exercise 12:
# Write a function that uses filter() to return a list with words that start with the letter 'a' from a given list.
# For example, if the list is ['apple', 'banana', 'pear', 'pineapple', 'apricot', 'avocado'], 
# the function should return ['apple', 'apricot', 'avocado'].

# (PT-BR)
# Exercício 12:
# Escreva uma função que use filter() para retornar uma lista com as palavras que começam com a letra ‘a’ de uma lista dada. 
# Por exemplo, se a lista for ['maça', 'banana', 'pera', 'damasco', 'abacate'], a função deve retornar [‘abacate'].

lista = ['apple', 'banana', 'pear', 'pineapple', 'apricot', 'avocado']
print(list(filter(lambda x: x[0] == 'a', lista)))

# List Comprehension:
print([fruit for fruit in lista if fruit[0] == 'a'])
