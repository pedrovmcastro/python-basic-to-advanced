# Exercise 3:
# Create a decorator called memoize that caches the results of previous calls to a function and returns the stored result
# if the same input occurs again.


# (PT-BR)
# Exercício 3:
# Crie um decorador chamado memoize que armazena em cache os resultados de chamadas anteriores de uma função 
# e retorna o resultado armazenado se a mesma entrada ocorrer novamente.


def memoize(func):
    cache = {}


    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return f'The function {func.__name__} has already been called with these arguments.'
        cache[key] = func(*args, **kwargs)
        return func(*args, **kwargs)
    
    
    return wrapper


@memoize
def sum(x, y):
    return x + y


@memoize
def multiply(x, y):
    return x * y


# Testing:
print(sum(1, 2))
print(multiply(1, 2))
print(sum(1, 2))
print(multiply(1, 2))
