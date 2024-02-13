"""
Exercise:

(PT-BR)
Exercício:

"""
"""
Leia uma matriz de 3x3 elementos. Calcule a soma dos elementos que estão acima da diagonal principal, a soma dos
elementos que estão abaixo da diagonal principal, e a soma dos elementos que estão na diagonal principal.
"""
# leitura da matriz:
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'[{i},{j}]: ')))
    matriz.append(linha)

soma_acima, soma_abaixo, soma_diagonal = 0, 0, 0

# comparando os índices:
for i in range(3):
    for j in range(3):
        if j > i:
            soma_acima += matriz[i][j]
        elif j < i:
            soma_abaixo += matriz[i][j]
        else:
            soma_diagonal += matriz[i][j]

print('=-'*30)
print(f'SOMA ACIMA = {soma_acima}\nSOMA ABAIXO = {soma_abaixo}\nSOMA DIAGONAL = {soma_diagonal}\n')
