"""
Faça um programa que some os termos de valor par da sequencia de
Fibonacci, cujos valores não ultrapassem quatro milhões
"""

# 0 1 1 2 3 5 8 13 21 34 55...
# a soma dos dois anteriores

n1, n2, soma = 0, 1, 0

while True:
    if n1 + n2 > 4000000:
        break

    if n1 % 2 == 0:
        soma += n1

    troca = n1
    n1 = n2
    n2 = troca + n2

print('A soma dos pares de Fibonacci eh:', soma)
