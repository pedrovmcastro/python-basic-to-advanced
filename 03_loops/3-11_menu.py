"""
Exercise 11:
Create a program that presents a menu of options for the calculation of the following operations between two numbers:

* addition (option 1)
* subtraction (option 2)
* multiplication (option 3)
* division (option 4)
* exit (option 5)

The program should allow the user to choose the desired operation, display the result, and return to the menu of options. 
The program only ends when the exit option is chosen (option 5).


(PT-BR)
Exercício 11:
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
    print('Choose an option:\n* addition (option 1)\n* subtraction (option 2)\n* multiplication (option 3)\n* division '
          '(option 4)\n* exit (option 5)')

    option = int(input())

    if option not in range(1, 6):
        print("Invalid input.")
    else:
        if option == 5:
            break
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        match option:
            case 1:
                print(f"Result: {(num1 + num2):.2f}")
            case 2:
                print(f"Result: {(num1 - num2):.2f}")
            case 3:
                print(f"Result: {(num1 * num2):.2f}")
            case 4:
                print(f"Result: {(num1 / num2):.2f}")
