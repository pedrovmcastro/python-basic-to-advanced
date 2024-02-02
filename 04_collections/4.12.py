"""Leia uma matriz 5x10 que se refere respostas de 10 questões de múltipla escolha, referente a 5 alunos.
Leia também um vetor de 10 posições contendo o gabarito de respostas que podem ser a, b, c ou d. Seu programa
deverá comparar as respostas de cada candidato com o gabarito e emitir um vetor denominado resultado, contendo
a pontuação correspondente a cada aluno"""

questoes_alunos = []
for i in range(5):
    linha = []
    for j in range(10):
        linha.append(input())
    questoes_alunos.append(linha)

gabarito = []
for i in range(10):
    gabarito.append(input())

resultados = []
for i in range(5):
    acertos = 0
    for j in range(10):
        if questoes_alunos[i][j] == gabarito[j]:
            acertos += 1
    resultados.append(acertos)

print(resultados)
