# Exercise 14:
# Write a function that uses filter() to return a list with words that are palindromes from a given list.
# A palindrome is a word that is the same when read backward. 
# For example, if the list is ['ana', 'ball', 'house', 'radar'], the function should return ['ana', 'radar'].

# (PT-BR)
# Exercício 14:
# Escreva uma função que use filter() para retornar uma lista com as palavras que são palíndromos de uma lista dada. 
# Um palíndromo é uma palavra que é igual quando lida de trás para frente. 
# Por exemplo, se a lista for [‘ana’, ‘bola’, ‘casa’, ‘arara’], a função deve retornar [‘ana’, ‘arara’].

lista = ['ana', 'ball', 'house', 'radar']

print(list(filter(lambda x: x == x[::-1], lista)))

# With List Comprehension:
print([nome for nome in lista if nome == nome[::-1]])
