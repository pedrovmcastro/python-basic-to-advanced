"""
Faça um programa que calcula a associação em paralelo de dois
resistores R1 e R2 fornecidos pelo usuário via teclado. O programa
fica pedindo estes valores e calculando até que o usuário entre
com um valo para resistência igual a zero.

R = (R1*R2)/(R1+R2)
"""

R1, R2 = int(input('Digite os valores de R1 e R2: ')), int(input())
primeira_iteracao = True

while R1 > 0 and R2 > 0:
    if not primeira_iteracao:
        R1, R2 = int(input('Digite os valores de R1 e R2: ')), int(input())
    R = (R1*R2)/(R1+R2)
    print('Resistor equivalente: ', R)
    primeira_iteracao = False
