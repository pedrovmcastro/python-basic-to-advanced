"""
Faça um programa que receba um numero inteiro maior do que 1, e
verifique se o número fornecido é primo ou não.
"""

n = int(input())
primo = True

for i in range(2, n//2 + 1):
    if n%i == 0:
        print('nao eh primo')
        primo = False
        break

if primo:
    print('eh primo')
