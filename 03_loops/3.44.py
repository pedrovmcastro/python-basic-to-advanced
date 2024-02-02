"""
Leia um número positivo do usuário, então, calcule e imprima a
sequencia Fibonacci até o primeiro número superior ao número lido.

Exemplo: se o usuario informou o numero 30,
a sequencia a ser impresa será 0 1 1 2 3 5 8 13 21 34
"""

# sequencia de Fibonacci:
N, n1, n2 = int(input('Digite um numero: ')), 0, 1
print('0 1 ', end='')

while True:
    print(n1+n2, '', end='')
    if n1+n2 > N:
        break
    troca = n1
    n1 = n2
    n2 = troca+n2

    n1, n2, soma = 0, 1, 0
    print('0 1 ', end='')



