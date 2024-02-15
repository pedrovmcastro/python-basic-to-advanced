# Exercise 5:
# Create a decorator called check_arguments that verifies if the arguments passed to a function are correct
# according to a given specification. For example, if the function expects two integers as arguments, 
# the decorator should check if the arguments are integers.


# (PT-BR)
# Exercício 5:
# Crie um decorador chamado verifica_argumentos que verifica se os argumentos passados para uma função estão corretos
# de acordo com uma especificação dada. Por exemplo, se a função espera dois inteiros como argumentos, 
# o decorador deve verificar se os argumentos são inteiros.


def check_arguments(*types):
    def check_function(func):
        def wrapper(*args):
            for value, typ in zip(args, types):
                if type(value) != typ:
                    return f'Invalid input. Argument {value} is not of type {typ.__name__}.'
            return func(*args)
        return wrapper
    return check_function


@check_arguments(int, int)
def sum_integers(a, b):
    return a + b


print(sum_integers(1, 2))
print(sum_integers(1, '2'))
print(sum_integers(1.0, 2))
