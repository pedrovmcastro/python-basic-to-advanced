# Exercise 8:
# Create a decorator called retry that allows a function to be executed again if it raises a specific exception.
# The maximum number of attempts should be configurable.


# (PT-BR)
# Exercício 8:
# Crie um decorador chamado retry que permite que uma função seja executada novamente se ela lançar uma exceção específica. 
# O número máximo de tentativas deve ser configurável.


def retry(max_attempts):
    def handle_exception(func):
        def wrapper(a, b):
            attempts = 0
            while attempts <= max_attempts:
                try:
                    if attempts > 0:
                        print('Invalid input. Try again:')
                        a, b = float(input()), float(input())
                    return func(a, b)
                except (TypeError, ValueError, ZeroDivisionError):
                    attempts += 1
            return 'Maximum number of attempts exceeded'
        return wrapper
    return handle_exception


@retry(max_attempts=3)
def sum_numbers(a, b):
    return a + b


@retry(max_attempts=3)
def divide_numbers(a, b):
    return a / b


print(sum_numbers(10, 2))
print(sum_numbers(10, 'a'))
print(divide_numbers(10, 'a'))
