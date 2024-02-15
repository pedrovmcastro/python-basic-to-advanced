# Exercise 6:
# Create a decorator called execution_time that measures the execution time of a function 
# and displays the elapsed time at the end of execution.


# (PT-BR)
# Exercício 6:
# Crie um decorator chamado tempo_execucao que mede o tempo de execução de uma função e exibe o tempo decorrido ao final da execução.

import time


def execution_time(func):
    def measure_time(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(f'Result = {result}')
        return f'Execution time = {end_time - start_time}'
    return measure_time


@execution_time
def sum_numbers(a, b):
    total_sum = 0
    for i in range(a, b):
        total_sum += i
    return total_sum


print(sum_numbers(1, 10000000))
