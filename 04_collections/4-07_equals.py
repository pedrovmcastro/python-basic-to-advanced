"""
Exercise 7:
Implement a program that reads an array of 10 positions and checks if there are equal values, then displays them on the screen.

(PT-BR)
Exercício 7:
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela.
"""

arr, equals = [], []

for _ in range(10):
    arr.append(int(input()))

for value1 in arr:
    if str(value1) in equals:
        continue
    for value2 in arr[arr.index(value1)+1:]:
        if value1 == value2:
            equals.append(str(value1))
            break

print(f"Equal values: {', '.join(equals)}")
