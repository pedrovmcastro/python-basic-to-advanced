"""
Exercise 9:
Create a program that reads an indeterminate number of ages of individuals (stop when the age 0 is entered)
and calculates the average age of this group.


(PT-BR)
Exercício 9:
Faça um programa que leia um numero indeterminado de idades de individuos (pare quando for informada a idade 0),
e calcule a idade media desse grupo.
"""

total_age, count = 0, 0

while True:
    age = int(input('Enter an age: '))
    if age <= 0:
        break
    total_age += age
    count += 1

print('Average age:', total_age / count)
