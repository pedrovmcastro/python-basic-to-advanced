"""
Exercise:

(PT-BR)
Exercício:

"""
"""Leia uma matriz de 3x3 elementos. Calcule a soma dos elementos que estão na diagonal secundária"""
# leitura da matriz:
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f'[{i},{j}]: ')))
    matriz.append(linha)

# busca da diagonal secundária:
i, j, soma = 0, 2, 0
while i <= 2:
    soma += matriz[i][j]
    i += 1
    j -= 1

print('=-'*30)
print(f'SOMA DA DIAGONAL SECUNDÁRIA = {soma}\n')
