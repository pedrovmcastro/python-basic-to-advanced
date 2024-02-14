"""
Exercise 11:
Read a 5x10 matrix representing the answers to 10 multiple-choice questions for 5 students. 
Also, read an array of 10 positions containing the answer key, where the answers can be 'a', 'b', 'c', or 'd'.
Your program should compare each student's answers with the answer key and generate an array named "results" 
containing the corresponding scores for each student.

(PT-BR)
Exercício 11:
Leia uma matriz 5x10 que se refere respostas de 10 questões de múltipla escolha, referente a 5 alunos.
Leia também um vetor de 10 posições contendo o gabarito de respostas que podem ser a, b, c ou d. Seu programa
deverá comparar as respostas de cada candidato com o gabarito e emitir um vetor denominado resultado, contendo
a pontuação correspondente a cada aluno
"""

answers_students = []
for i in range(5):
    row = []
    for j in range(10):
        row.append(input())
    answers_students.append(row)

answer_key = []
for i in range(10):
    answer_key.append(input())

results = []
for i in range(5):
    correct_answers = 0
    for j in range(10):
        if answers_students[i][j] == answer_key[j]:
            correct_answers += 1
    results.append(correct_answers)

print(results)
