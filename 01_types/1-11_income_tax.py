"""
Exercise 11:
A company hires at $30.00 a day. Implement a program that prompts the user for the number of days worked
and prints the net amount to be paid, considering an 8% income tax deduction.

(PT-BR)
Exercício 11:
Uma empresa contrata a R$ 30,00 por dia. Faça um programa que solicite
o número de dias trabalhandos pelo encanador e imprima a quantia líquida
que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda
"""

days = int(input('Number of days worked: '))

amount = 30*days

print(0.92*amount)
