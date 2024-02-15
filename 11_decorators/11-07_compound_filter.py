# Exercise 7:
# Develop a higher-order function called compound_filter that takes a list of filter functions and a list of data,
# and returns a list with only the elements that satisfy all the conditions of the filter functions.


# (PT-BR)
# Exercício 7:
# Desenvolva uma função de alta ordem chamada filtro_composto que aceita uma lista de funções de filtro 
# e uma lista de dados, e retorna uma lista apenas com os elementos que satisfazem todas as condições das funções de filtro.


def compound_filter(filters, data):
    result = data
    for func in filters:
        result = list(filter(func, result))
    return result


filters = [lambda x: isinstance(x, int), lambda x: x % 2 == 0, lambda x: x > 0]
data = [1, 0, 2, 3, -5, 7, 8, -10, 'a', 'b', 6, 22, 22.1]

print(compound_filter(filters, data))