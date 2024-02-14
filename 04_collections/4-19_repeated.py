"""
Exercise 19:
Create a program to read 10 DIFFERENT numbers to be stored in an array.
The data should be stored in the array in the order they are read.
If the user enters a number that has already been entered, the program should ask them to enter another number.
Note that each value entered by the user must be searched in the array to check if it already exists among the numbers provided.
Display the final array that was entered on the screen.


(PT-BR)
Exercício 19:
Faça um programa para ler 10 números DIFERENTES a serem armazenados em um vetor.Os dados deverão ser armazenados
no vetor na ordem que forem sendo lidos, sendo que caso o usuário digite um número que já foi digitado anteriormente,
o programa deverá pedir para ele digitar outro número. Note que cada valor digitado pelo usuário deve ser pesquisado
no vetor, verificando se ele existe entre os números que já foram fornecidos. Exibir na tela o vetor final que foi
digitado.
"""

array = []

while len(array) < 10:
    number = int(input())
    if number not in array:
        array.append(number)
    else:
        print('Repeated number. Please enter another number.')

print(array)
