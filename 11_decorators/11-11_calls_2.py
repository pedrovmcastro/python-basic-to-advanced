# Exercise 11:
# Create a dictionary to save the names of the called functions and the number of times they were executed. 
# The output should be: {'function1': calls1, 'function2': calls2}


# (PT-BR)
# Exercício 11:
# Crie um dicionário para salvar os nomes das funções chamadas e a quantidade de vezes que foi executada. 
# Saída deve ser: {'funcao1': calls1, 'funcao2': calls2} 


def calls_counter(cache):
    def decorator(func):
        def wrapper(a, b):
            if func.__name__ not in cache.keys():
                cache[func.__name__] = 1
            else:
                cache[func.__name__] += 1
            print(f'Result of function {func.__name__} = {func(a, b)}')
            return cache
        return wrapper
    return decorator


calls_cache = {}


@calls_counter(calls_cache)
def sum_numbers(a, b):
    return a + b


@calls_counter(calls_cache)
def subtract_numbers(a, b):
    return a - b
    

@calls_counter(calls_cache)
def multiply_numbers(a, b):
    return a * b


# Tests:
print(sum_numbers(1, 2))
print(sum_numbers(1, 3))
print(multiply_numbers(1, 2))
print(sum_numbers(1, 3))
print(subtract_numbers(9, 0))
print(sum_numbers(30, 1))
print(multiply_numbers(2, 3))
