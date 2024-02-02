"""
Em Matemática, o número harmônico designado por H(n) define-se
como sendo a soma da série harmônica:

H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

Faça um programa que leia um valor n inteiro e positivo
e apresente o valor de H(n)
"""

inteiro, positivo = False, False

while not (inteiro and positivo):
    N = input('Digite um número inteiro positivo: ')
    if N.isdigit():
        inteiro = True
        N = int(N)
        if N > 0:
            positivo = True

Hn = 0
for i in range(1, N+1):
    Hn += 1/i

print(Hn)
