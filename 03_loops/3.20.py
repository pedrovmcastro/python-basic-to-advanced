"""
Ler uma sequencia de números inteiros e determinar se eles são pares
ou não. Deverá ser informado o número de dados lidos e números de
valores pares. O processo termina quando for digitado o número 1000.
"""
N, i, par = 0, 0, 0

while N != 1000:
    N = int(input('Digite um número inteiro: '))
    i += 1
    if N % 2 == 0:
        par += 1

print(f'Dados lidos: {i}\nNumeros pares: {par}')
