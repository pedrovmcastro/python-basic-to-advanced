"""
Exercise 3:
Create a program that reads two grades of a student, checks if the grades are valid, and displays the mean of these grades on the screen.
A valid grade must be, necessarily, a value between 0.0 and 10.0. In case the grade does not have a valid value, this information 
should be printed to the user, and the program terminates.

Exercício 3 (PT-BR):
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média dessas notas.
Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, 
este fato deve ser informado ao usuário e o programa termina.
"""

grade1 = float(input("Enter the first grade: "))
if 0 <= grade1 <= 10:
    grade2 = float(input("Enter the second grade: "))
    if 0 <= grade2 <= 10:
        print(f"Mean: {(grade1+grade2)/2}")
    else:
        print("The second grade is invalid.")        
else:
    print("The first grade is invalid.")
