"""
Exercise 8:
Read a sequence of integers and determine if they are even or not. 
The program should report the number of data points read and the number of even values. 
The process ends when the number 1000 is entered.


(PT-BR)
Exercício 8:
Ler uma sequencia de números inteiros e determinar se eles são pares
ou não. Deverá ser informado o número de dados lidos e números de
valores pares. O processo termina quando for digitado o número 1000.
"""
N, i, even = 0, 0, 0

while N != 1000:
    N = int(input('Enter an integer: '))
    i += 1
    if N % 2 == 0:
        even += 1

print(f'Data read: {i}\nEven numbers: {even}')