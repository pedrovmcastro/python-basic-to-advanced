"""
Exercise 14:
Create a program that takes as input the number of students in a discipline. Dynamically allocate two arrays to store 
information about these students. The first array contains the names of the students, and the second contains their 
final grades. Create a file that stores, on each line, the name of the student and their final grade. Use names with 
a maximum of 40 characters. If the name does not have enough characters, complete with blank spaces.

(PT-BR)
Exercício 14:
Crie um programa que receba como entrada o número de alunos de uma disciplina. Aloque dinamicamente dois vetores para 
armazenar as informações a respeito desses alunos. O primeiro vetor contém o nome dos alunos e o segundo contém suas notas finais
Crie um arquivo que armazene, a cada linha, o nome do aluno e sua nota final. Use nomes com no máximo 40 caracteres. 
Se o nome não contém caracteres, complete com espaço em branco.
"""

num_students = int(input('Number of students: '))
names, grades = [], []

for _ in range(num_students):
    name = input('Student name: ')
    if len(name) < 40:
        name = name + (40 - len(name)) * ' '
    grade = float(input('Final grade: '))
    names.append(name)
    grades.append(grade)

with open('new_text.txt', 'w') as file:
    for name, grade in zip(names, grades):
        file.write(f'NAME: {name.title()} FINAL GRADE: {grade:.2f}\n')
        
