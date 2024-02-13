"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Faça um programa que leia um número inteiro positivo "n"
e calcule a soma dos "n" primeiros números naturais.
"""

inteiro, positivo = False, False

while not (inteiro and positivo):
    n = input('Digite um número inteiro positivo: ')
    if n.isdigit():
        inteiro = True
        n = int(n)
        if n > 0:
            positivo = True

soma = 0
for i in range(1, n+1):
    soma += i

print(soma)
