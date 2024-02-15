"""
Exercise 12:
Write a program that takes as input the amount of money withdrawn by a bank customer and returns how many notes
of each value will be needed to fulfill the withdrawal with the minimum number of notes possible. 
Notes of 100, 50, 20, 10, 5, 2, and 1 are available.

(PT-BR)
Exercício 12:
Escreva um programa que receba como entrada o valor do saque realizado pelo cliente
de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque
com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
"""

amount = int(input('Enter the withdrawal amount: '))

note100, note50, note20, note10, note5, note2, note1 = 0, 0, 0, 0, 0, 0, 0

while amount >= 100:
    amount -= 100
    note100 += 1

while amount >= 50:
    amount -= 50
    note50 += 1

while amount >= 20:
    amount -= 20
    note20 += 1

while amount >= 10:
    amount -= 10
    note10 += 1

while amount >= 5:
    amount -= 5
    note5 += 1

while amount >= 2:
    amount -= 2
    note2 += 1

while amount >= 1:
    amount -= 1
    note1 += 1

print(f'100 notes: {note100}\n50 notes: {note50}\n20 notes: {note20}\n'
      f'10 notes: {note10}\n5 notes: {note5}\n2 notes: {note2}\n1 note: {note1}')
