"""
Faça um programa que calcule a área de um triângulo,
cuja base e altura são fornecidas pelo usuário. Esse
programa não pode permitir a entrada de dados inválidos,
ou seja, medidas menores ou iguais a 0.
"""

while True:
    base, altura = int(input('Digite a base e a altura validas: ')), int(input())
    if base > 0 and altura > 0:
        break

area = base*altura/2

print(area)
