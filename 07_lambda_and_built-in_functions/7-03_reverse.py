# Exercise 3:
# Sort a list of words in reverse alphabetical order (from Z to A) using the sort function
# with a key argument.

# (PT-BR)
# Exercício 3:
# Ordene uma lista de palavras em ordem alfabética inversa (da Z para A) 
# usando a função sort com um argumento de chave (key).

fruits = ['kiwi', 'passion fruit', 'banana', 'apple', 'pear']
fruits.sort(key=lambda x: x, reverse=True)
print(fruits)
