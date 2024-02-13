"""
Exercise:

(PT-BR)
Exercício:

"""
"""
Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 numeros naturais
e o quadrado da soma.

Ex: A soma dos quadrados dos dez primeiros números naturais é:
1² + 2² + 3² + ... + 10² = 385
O quadrado da soma dos dez primeiros numeros naturais é,
(1+2+...+10)² = 55² = 3025
"""

soma_quadrados, soma = 0, 0

for i in range(1, 101):
    soma_quadrados += i**2
    soma += i

print('A diferença eh', soma**2 - soma_quadrados)
