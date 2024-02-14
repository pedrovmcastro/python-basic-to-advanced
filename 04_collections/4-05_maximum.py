"""
Exercise 5:
Create a program that receives from the user an array with 10 positions. 
Next, the program should print the largest and smallest elements of the array.

(PT-BR)
Exercício 5:
Faça um programa que receba do usuário um vetor com 10 posições.
Em seguida deverá ser impresso o maior e o menor elemento do vetor.
"""

arr = []

for i in range(10):
    N = int(input())
    arr.append(N)

maxi = mini = arr[0]

for value in arr[1:]:
    if value > maxi:
        maxi = value
    if value < mini:
        mini = value

print(f'Maximum: {maxi}\nMinimum: {mini}')
vet = []