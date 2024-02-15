# Exercise 1:
# Create a higher-order function called apply_function that takes a function function and a list data and returns 
# a list with the application of the function to each element of the list.


# (PT-BR)
# Exercício 1:
# Crie uma função de alta ordem chamada aplica_funcao que recebe uma função funcao e uma lista dados e retorna 
# uma lista com a aplicação da função em cada elemento da lista.


def apply_function(function, data):
    return list(map(function, data))


def square(num):
    return num * num


print(apply_function(square, [1, 2, 3, 4, 5]))
