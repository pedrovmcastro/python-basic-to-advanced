# Exercise 2:
# Implement a function called filter_func that takes a filter function and a list, and returns a list 
# with only the elements that satisfy the filter function's condition.


# (PT-BR)
# Exercício 2:
# Implemente uma função chamada filtro que aceita uma função de filtro e uma lista,
# e retorna uma lista apenas com os elementos que satisfazem a condição da função de filtro.


def filter_func(func, lst):
    return list(filter(func, lst))


def even_filter(num):
    return num % 2 == 0


print(filter_func(even_filter, [1, 2, 3, 4, 5, 6, 7]))

# Alternative way:
print(filter_func(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7]))
