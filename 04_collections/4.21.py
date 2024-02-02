"""
32. Leia dois vetores de inteiros x e y, cada um com 5 elementos(assuma que o usuário não informa
elementos repetidos). Calcule e mostre os vetores resultantes em cada caso abaixo:
-> Soma entre x e y: soma de cada elemento de x com o elemento da mesma posição em y;
-> Produto entre x e y: multiplicação de cada elemento de x com o elemento da mesma posição em y;
-> Diferença entre x e y: todos os elementos de x que não existem em y;
-> Intersecção entre x e y: apenas os elementos que aparecem nos dois vetores;
-> União entre x e y: todos os elementos de x, e todos os elementos de y que não estão em x."""


def ler_vetor():
    vetor = []
    for _ in range(5):
        vetor.append(int(input()))
    return vetor


x = ler_vetor()
y = ler_vetor()

vetor_soma, vetor_produto, vetor_diferenca, vetor_interseccao, vetor_uniao = [], [], [], [], []

for i, valor in enumerate(x):
    vetor_soma.append(x[i] + y[i])
    vetor_produto.append(x[i]*y[i])

vetor_diferenca = set(x).difference(y)
vetor_interseccao = set(x).intersection(y)
vetor_uniao = set(x).union(y)

print('Vetor x = ', x)
print('Vetor y = ', y)
print('Vetor soma = ', vetor_soma)
print('Vetor produto = ', vetor_produto)
print('Vetor diferença = ', list(vetor_diferenca))
print('Vetor intersecção = ', list(vetor_interseccao))
print('Vetor união = ', list(vetor_uniao))
