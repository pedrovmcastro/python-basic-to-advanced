"""
Exercise 3:
Create a function to check whether a number is a perfect square. 
A perfect square is a non-negative integer that can be expressed as the square of another integer.

(PT-BR)
Exercício 3:
Faça uma função para verificar se um número é um quadrado perfeito. Um quadrado perfeito
é um número inteiro não negativo que pode ser expresso como o quadrado de outro número inteiro.
ex: 1, 4, 9..
"""

import math


def is_perfect_square(num):
    if num < 0:
        return 'Not a perfect square'
    if math.sqrt(num) % 1 == 0:     # check if the square root of {num} is an integer
        return 'Perfect square'
    else:
        return 'Not a perfect square'


print(is_perfect_square(int(input("Enter an integer: "))))
