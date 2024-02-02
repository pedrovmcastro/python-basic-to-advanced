"""
Faça uma função que recebe, por parâmetro, 2 vetores de 10 elementos inteiros e que calcule e retorne, também
por parâmetro, o vetor união dos dois primeiros.
"""


def uniao_vetores(vet1, vet2):
    uniao = set(vet1 + vet2)
    return list(uniao)


def main():

    v1 = [0, 1, 2, 4, 5, 6, 2, 0, 1, 7]
    v2 = [8, 1, 3, 6, 9, 10, 13, 6, 6, 1]

    uniao = uniao_vetores(v1, v2)

    print(uniao)


main()
