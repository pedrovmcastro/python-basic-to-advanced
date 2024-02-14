"""
Exercise 1:
Create a program that has an array named A to store 6 numbers.
The program should perform the following steps:
(a) Assign the following values to this array: 1, 0, 5, -2, -5, 7.
(b) Store in a simple integer variable the sum of the values at positions A[0], A[1], and A[5] of the array and display this sum on the screen.
(c) Modify the array at position 4, assigning the value 100 to this position.
(d) Display on the screen each value of array A, one on each line.


(PT-BR)
Exercício 1:
Faça um programa que possua um vetor denominado A que armazene 6 números.
O programa deve executar os seguintes passos:
(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
(b) Armazene em uma variável inteira (simples) a soma entre os valores das posições
A[0], A[1] e A[5] do vetor e mostre na tela esta soma.
(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
(d) Mostre na tela cada valor do vetor A, um em cada linha.
"""

A = [1, 0, 5, -2, -5, 7]

sum = A[0] + A[1] + A[5]
print(f"Sum: {sum}")

A[4] = 100

for valor in A:
    print(valor)
