"""
Faça um algoritmo que leia um número positivo e imprima seus divisores.
"""

N = 0
while N <= 0:
    N = int(input('Digite um numero positivo: '))

# encontrar divisores:
# ex: N = 10
#     div = 1,2,5,10

for i in range(1, N+1):
    if N % i == 0:
        print(f'{i} ', end='')




