# Exercise 9:
# Create a decorator called call_counter that keeps track of the number of times a function has been called. 
# This counter should be displayed at the end of the function's execution.


# (PT-BR)
# Exercício 9:
# Crie um decorador chamado contador_chamadas que mantém o número de vezes que uma função foi chamada. 
# Esse contador deve ser exibido ao final da execução da função.


def call_counter(**kwargs):
    def decorator(func):
        if func.__name__ not in kwargs.keys():
            kwargs[func.__name__] = 0
        def wrapper(*args):
            print(f'Result = {func(*args)}')
            kwargs[func.__name__] += 1
            return f'The function {func.__name__} has been called {kwargs[func.__name__]} time(s).\n'
        return wrapper
    return decorator


call_count = {}


@call_counter(**call_count)
def sum_numbers(a, b):
    return a + b


@call_counter(**call_count)
def multiply_numbers(a, b):
    return a * b


@call_counter(**call_count)
def double(a):
    return a * 2


# Tests:
print(sum_numbers(1, 2))
print(sum_numbers(1, 3))
print(multiply_numbers(1, 2))
print(multiply_numbers(1, 3))
print(sum_numbers(1, 2))
print(double(5))