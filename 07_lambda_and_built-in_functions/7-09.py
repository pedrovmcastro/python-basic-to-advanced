# Exercise 9:
# Create a lambda function that takes two arguments and returns their sum. Use the map function to add elements from two lists of numbers
# element-wise.

# (PT-BR)
# Exercício 9:
# Crie uma função lambda que receba dois argumentos e retorne a soma deles. Use a função map para somar elementos de duas listas de números
# elemento a elemento.

list1 = [12, 44, 92, 16, 25]
list2 = [10, 20, 30, 40, 50]

print(list(map(lambda x, y: x + y, list1, list2)))
