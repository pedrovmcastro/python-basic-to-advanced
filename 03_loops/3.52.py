"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Escreva um programa que receba como entrada o valor do saque realizado pelo cliente
de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque
com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
"""

valor = int(input('Qual o valor do saque? '))

nota100, nota50, nota20, nota10, nota5, nota2, nota1 = 0, 0, 0, 0, 0, 0, 0

while valor >= 100:
    valor -= 100
    nota100 += 1

while valor >= 50:
    valor -= 50
    nota50 += 1

while valor >= 20:
    valor -= 20
    nota20 += 1

while valor >= 10:
    valor -= 10
    nota10 += 1

while valor >= 5:
    valor -= 5
    nota5 += 1

while valor >= 2:
    valor -= 2
    nota2 += 1

while valor >= 1:
    valor -= 1
    nota1 += 1

print(f'Notas de 100: {nota100}\nNotas de 50: {nota50}\nNotas de 20: {nota20}\n'
      f'Notas de 10: {nota10}\nNotas de 5: {nota5}\nNotas de 2: {nota2}\nNotas de 1: {nota1}')