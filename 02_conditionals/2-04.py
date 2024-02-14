"""
Exercise 4:
Prompt the user for the salary of a worker and the installment amount of a loan.
If the installment amount is greater than 20% of the salary print: Loan not granted, otherwise print: Loan granted.

Exercício 4 (PT-BR):
Leia o salário de um trabalhador e o valor da prestação de um empréstimo.
Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso contrário imprime: Empréstimo concedido.
"""

salary = float(input("Enter the salary: "))
in_amount = float(input("Enter the installment amount: "))

if in_amount > 0.2*salary:
    print("Loan not granted.")
else:
    print("Loan granted.")
