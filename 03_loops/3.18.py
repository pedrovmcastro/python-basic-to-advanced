"""
Exercise:

(PT-BR)
Exercício:

"""

""""
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles
e quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.
"""

N = int(input('Quantos numeros ira digitar? '))

num = int(input('Digite um numero: '))
maior = num

cont = 0

for i in range(N):
    if i != 0:
        num = int(input('Digite um numero: '))
    if num > maior:
        maior = num
        cont = 1
    elif num == maior:
        cont += 1

print(f'O maior deles foi {maior}. Num de vezes: {cont}')
