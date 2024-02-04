"""
Exercise 13:
Write a program that receives from the user a text file containing the name and grade from various students
(in the following format: NAME: JOHN GRADE: 8), one student per line. 
Display on the screen the name and grade of the student with the highest grade.

(PT-BR)
Exercício 13:
Faça um programa que receba do usuário um arquivo que contenha o nome e a nota de diversos alunos (da seguinte forma:
NOME: JOÃO NOTA: 8), um aluno por linha. Mostre na tela o nome e a nota do aluno que possui a maior nota.
"""

grades = {}
lines = 0

with open('grades.txt') as file:
    for line in file:
        lines += 1
    file.seek(0)
    for _ in range(lines):
        line = file.readline().replace('NAME: ', '').replace('GRADE: ', '').strip() # Use strip to remove whitespaces
        name, grade = line.split()
        grades[name] = float(grade)
        
highest_grade = 0 
for name, grade in grades.items():
    if grade > highest_grade:
        highest_grade = grade
        student = name

print(f'NAME: {student} GRADE: {highest_grade}')
