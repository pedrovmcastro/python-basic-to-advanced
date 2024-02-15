# Exercise 10:
# Write a decorator called @log that takes a file name as an argument and writes to a text file the date, time, function name,
# and arguments of the function every time it is called.

# (PT-BR)
# Exercício 10:
# Escreva um decorator chamado @log que recebe um nome de arquivo como argumento e grava em um arquivo de texto a data, 
# a hora, o nome e os argumentos da função sempre que ela for chamada.

from datetime import datetime


def log(file_name):
    def decorator(func):
        def wrapper(*args):
            with open(file_name, 'a') as file:
                # Format the date and time using strftime
                date = datetime.now().strftime("%Y-%m-%d")
                time = datetime.now().strftime("%H:%M")
                arguments = ", ".join(str(arg) for arg in args)
                file.write(f'Function = {func.__name__}\nDate = {date}\nTime = {time}\nArguments = {arguments}\n\n')
                print('Function log saved successfully.')
            return f'Result of {func.__name__} = {func(*args)}'
        return wrapper
    return decorator


@log(file_name='test_decorator_log.txt')
def sum_arguments(*args):
    return sum(args)


@log(file_name='test_decorator_log.txt')
def max_argument(*args):
    return max(args)


# Testing:
print(sum_arguments(3, 5, 50))
print(max_argument(2, 9))