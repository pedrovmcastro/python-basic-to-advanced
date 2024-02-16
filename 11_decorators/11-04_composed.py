# Exercise 4:
# Write a function called compose that takes two functions and returns a new function that is the composition of the two functions.


# (PT-BR)
# Exercício 4:
# Escreva uma função chamada compor que aceita duas funções e retorna uma nova função que é a composição das duas funções.


def compose(func1, func2):
    def composed_function(x):
        return func2(func1(x))
    return composed_function


# Usage examples:


def double(num):
    return num * 2


def add_one(num):
    return num + 1


print(add_one(double(5)))  # Not really needed to compose functions here, but...

print(compose(double, add_one)(5))  # The more practical way

composed_function = compose(double, add_one)
print(composed_function(5))
