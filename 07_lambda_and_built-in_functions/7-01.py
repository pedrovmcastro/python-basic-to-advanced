# Exercise 1:
# Create a lambda function that doubles a number and use it to double the elements of a list.

# (PT-BR)
# Exercício 1:
# Crie uma função lambda que dobre um número e use-a para dobrar os elementos de uma lista.

lista = [2, 4, 6, 8, 10]
print(list(map(lambda x: x*2, lista)))
