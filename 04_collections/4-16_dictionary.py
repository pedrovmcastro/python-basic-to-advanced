"""
Exercise 16:
Create a program that reads ten sets of two values, where the first represents the student number
and the second represents their height in meters. Find the tallest and shortest students.
Display the student number and height for the tallest and shortest students.


(PT-BR)
Exercício 16:
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando
o número do aluno e o segundo representando a sua altura em metros. Encontre o aluno mais baixo
e o mais alto. Mostre o número do aluno miais baixo e do mais alto, juntamente com suas alturas
"""

dictionary = {}

for _ in range(10):
    student_number = int(input('Student number: '))
    student_height = float(input('Student height: '))
    dictionary[student_number] = student_height

for number, height in dictionary.items():
    if height == max(dictionary.values()):
        tallest_student = number
    if height == min(dictionary.values()):
        shortest_student = number

print(f'Student number for the tallest student = {tallest_student}\nHeight = {max(dictionary.values())}')
print(f'Student number for the shortest student = {shortest_student}\nHeight = {min(dictionary.values())}')
