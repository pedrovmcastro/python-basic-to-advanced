"""
Faça um programa que calcule o menor número divisível por cada
um dos números de 1 a 20?
Ex:
2520 é o menor número que pode ser dividido por cada um dos números
de um a 10, sem sobrar resto.
"""

k = 21
while True:
    cont = 0
    for i in range(1, 21):
        if k % i == 0:
            cont += 1
    if cont == 20:
        print(f'O menor numero eh {k}')
        break
    k += 1
