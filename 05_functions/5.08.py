"""Crie um programa que receba três valores (obrigatoriamente maiores que zero), representando as medidas
dos três lados de um triângulo. Elabore funções para:
a) Determinar se esses lados formam um triângulo, sabendo que:
    O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados
b) Determinar e mostrar o tipo de triângulo, caso as medidas formem um triângulo (equilatero, isósceles, escaleno)"""


def triangulo(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return 'valores inválidos'
    elif x < y + z and y < x + z and z < x + y:
        if x == y == z:
            return 'triangulo equilatero'
        elif x == y or x == z or y == z:
            return 'triangulo isósceles'
        else:
            return 'triangulo escaleno'
    else:
        return 'os lados não formam um triângulo'


print(triangulo(float(input()), float(input()), float(input())))
