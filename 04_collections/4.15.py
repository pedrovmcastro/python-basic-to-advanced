"""Leia uma matriz de 3x3 elementos. Calcule e imprima a sua transposta"""
# leitura da matriz:
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'[{i},{j}]: ')))
    matriz.append(linha)

matriz_transposta = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz[j][i])
    matriz_transposta.append(linha)

print('-='*30)
print('Matriz Transposta:')
for i in range(3):
    for j in range(3):
        print(f'[{matriz_transposta[i][j]:5^}]', end='')
    print()
