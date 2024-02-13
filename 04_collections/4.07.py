"""
Exercise:

(PT-BR)
Exercício:

"""
"""
Fazer um programa para ler 10 valores e, em seguida, mostrar a posição
onde se encontram o maior e o menor valor (caso haja mais de uma ocorrência do maior ou menor valor,
mostrar todas posições).
"""

lista, ind_max, ind_min = [], [], []

for _ in range(10):
    lista.append(int(input()))

for i, valor in enumerate(lista):
    if valor == max(lista):
        ind_max.append(str(i))
    if valor == min(lista):
        ind_min.append(str(i))
# ind_max = [str(i) for i, valor in enumerate(lista) if valor == max(lista)]
# ind_min = [str(i) for i, valor in enumerate(lista) if valor == min(lista)]
# Esse método é menos eficiente nesse caso pois o programa passaria por dois loop for

print(f'Maior = {max(lista)}\nPosição(s): {", ".join(ind_max)}')
print(f'Menor = {min(lista)}\nPosição(s): {", ".join(ind_min)}')
