"""
Faça um programa que apresente um menu de opções para o
cálculo das seguintes operações entre dois números:

* adição (opção 1)
* subtração (opção 2)
* multiplicação (opção 3)
* divisão (opção 4)
* saída (opção 5)

O programa deve possibilitar ao usuario a escolha da operação desejada,
a exibição do resultado e a volta ao menu de opções. O programa só termina quando for escolhida a opção de saída
(opção 5).
"""

while True:
    print('Escolha uma opcao:\n* adicao (opcao 1)\n* subtracao (opcao 2)\n* multiplicacao (opcao 3)\n* divisao (opcao '
          '4)\n* saida (opcao 5)')

    opcao = int(input())

    if opcao == 5:
        break
    elif opcao == 4:
        num1 = int(input('primeiro numero: '))
        num2 = int(input('segundo numero: '))
        print(num1/num2)
    elif opcao == 3:
        num1 = int(input('primeiro numero: '))
        num2 = int(input('segundo numero: '))
        print(num1*num2)
    elif opcao == 2:
        num1 = int(input('primeiro numero: '))
        num2 = int(input('segundo numero: '))
        print(num1 - num2)
    elif opcao == 1:
        num1 = int(input('primeiro numero: '))
        num2 = int(input('segundo numero: '))
        print(num1 + num2)
    else:
        break
