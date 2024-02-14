"""
Exercise 18:
Create a program that reads an array of 15 positions and compresses it, eliminating positions with
a value of zero. To do this, all elements ahead of the zero value must be moved one position back in the array.


(PT-BR)
Exercício 18:
Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições com
valor zero. Para isso, todos os elementos à frente do valor zero, devem ser movidos uma posição para
trás no vetor
"""

arr = []

for _ in range(15):
    arr.append(int(input()))

while 0 in arr:
    arr.remove(0)

print(arr)
