# Exercise 18:
# Write a program that uses the zip function to calculate the average of each student in a class, 
# given the grades of three exams.

# (PT-BR)
# Exercício 18:
# Escreva um programa que use a função zip para calcular a média de cada aluno em uma turma, 
# dadas as notas de três provas.

# Input example:
names = ["Alice", "Bruno", "Carlos", "Diana", "Eduard"]
exam1 = [8, 7, 6, 9, 10]
exam2 = [7, 6, 8, 10, 9]
exam3 = [9, 8, 7, 10, 8]

average_scores = list(zip(exam1, exam2, exam3))
average_scores = [round(sum(scores)/3, 2) for scores in average_scores]

print(average_scores)
