# Exercise 7:
# Create a lambda function that returns the last letter of a string and use it to sort a list of words based on the last letter
# of each word using the sort function.

# (PT-BR)
# Exercício 7:
# Crie uma função lambda que retorne a última letra de uma string e use-a para ordenar uma lista de palavras com base na última letra
# de cada palavra usando a função sort.

fruits = ['passion fruit', 'avocado', 'cashew', 'kiwi', 'pear']
fruits.sort(key=lambda x: x[-1])
print(fruits)
