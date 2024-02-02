"""
Elabore um programa que faça leitura de vários números inteiros,
até que se digite um número negativo. O programa tem que retornar
o maior e o menor número lido.
"""

maior = menor = n = int(input('Digite um numero: '))
primeira_iteracao = True

while n > 0:
    if not primeira_iteracao:
        n = int(input('Digite um numero: '))
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    primeira_iteracao = False

print(f'O maior eh {maior} e o menor eh {menor}')

"""
maior = menor = int(input('Digite um número: '))
primeira_iteracao = True

while True:
    if not primeira_iteracao:
        n = int(input('Digite um número: '))
        if n < 0:
            break
        maior = n if n > maior else maior
        menor = n if n < menor else menor
    primeira_iteracao = False

print(f'O maior é {maior} e o menor é {menor}')
"""