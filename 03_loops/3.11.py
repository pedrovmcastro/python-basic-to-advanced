"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N
em ordem crescente

MÉTODO ALTERNATIVO:
A função isdigit() é um método de string em Python que verifica se todos os caracteres da string são
dígitos numéricos. Ela retorna True se todos os caracteres da string forem dígitos e False se houver
pelo menos um caractere não numérico.

Em Python, os dígitos são os caracteres numéricos que vão de 0 a 9. Isso inclui apenas os números inteiros,
sem sinais de adição, ponto decimal ou qualquer outro caractere especial.
Por exemplo, "123" é uma sequência de dígitos, enquanto "12.34" não é, porque contém o caractere "." (ponto).
"""

N = 0

while N <= 0:
    N = input('Digite um número inteiro positivo: ')
    for i in N:    # i = letra e N[i] = posição da letra
        if i == '.':
            N = 0
            break
    N = int(N)

for i in range(N+1):
    print(f'{i} ', end='')

