"""
Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições com
valor zero. Para isso, todos os elementos à frente do valor zero, devem ser movidos uma posição para
trás no vetor
"""

vetor = []

for _ in range(15):
    vetor.append(int(input()))

while 0 in vetor:
    vetor.remove(0)

print(vetor)
