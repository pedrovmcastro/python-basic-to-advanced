"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Dados n e dois números inteiros positivos, i e j, diferentes de 0,
imprimir em ordem crescente os n primeiros naturais que são multiplos
de i ou de j ou de ambos.
Exemplo:
Para n = 6, i = 2 e j = 3, a saída deverá ser: 0,2,3,4,6,8.
"""

n, i, j = 0, 0, 0

x, y = 0, 0

while n <= 0 or i <= 0 or j <= 0:
    n, i, j = int(input('Valor de n: ')), int(input('Valor de i: ')), int(input('Valor de j: '))

while x <= n:
    x += 1
    while True:
        if y % i == 0 or y % j == 0:
            print(f'{y} ', end='')
            y += 1
            break

