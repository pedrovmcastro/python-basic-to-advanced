"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Faça um programa que receba dois numeros. Calcule e mostre:
- a soma dos números pares desse intervalo de números, incluindo
os números digitados;
- a multiplicação dos numeros ímpares desse intervalo, incluindo os digitados;
"""
N = int(input('Digite dois numeros: '))
M = int(input())
maior, menor = 0, 0

# Verificar quem eh o maior:
if N > M:
    maior = N
    menor = M
elif N < M:
    menor = N
    maior = M

# a soma dos numeros pares:
soma = 0
for i in range(menor, maior+1):
    if i % 2 == 0:
        soma += i

# multiplicacao dos impares:
produto = 1
for i in range(menor, maior+1):
    if i % 2 != 0:
        produto *= i

print(f'Soma dos pares: {soma}\nProduto dos impares: {produto}')
