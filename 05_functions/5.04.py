"""Faça uma função para verificar se um número é um quadrado perfeito. Um quadrado perfeito
é um número inteiro não negativo que pode ser expresso como o quadrado de outro número inteiro.
ex: 1, 4, 9..."""
import math


def quadrado_perfeito(num):
    if num % math.sqrt(num) == 0:
        return 'Quadrado perfeito'
    else:
        return 'Não é um quadrado perfeito'


print(quadrado_perfeito(int(input())))
