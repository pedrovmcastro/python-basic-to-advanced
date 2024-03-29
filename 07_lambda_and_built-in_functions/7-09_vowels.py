# Exercise 9:
# Given a list of words, write Python code that uses lambda expressions, map, and sorted to sort the words based on the number of vowels in each word,
# in descending order. In other words, words with more vowels should appear first in the list.

# (PT-BR)
# Exercício 9:
# Dada uma lista de palavras, escreva um código em Python que use expressões lambda, map e sorted para classificar as palavras
# com base no número de vogais em cada palavra, em ordem decrescente. Ou seja, as palavras com mais vogais devem aparecer primeiro na lista.

words = ["elephant", "giraffe", "dog", "cat", "monkey", "parrot"]
print(sorted(words, key=lambda x: sum(map(x.count, "aeiouAEIOU")), reverse=True))
