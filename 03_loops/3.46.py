"""
Faça um prorgama que gera um numero aleatorio de 1 a 1000. O usuario deve tentar acertar qual o numero foi gerado,
a cada tentativa o programa deverá informar se o chute é menor ou maior que o número gerado. O programa acaba quando
o usuario acerta o numero gerado. O programa deve informar em quantas tentativas o número foi descoberto.
"""
import random

x = random.randint(1, 1000)
tentativa = 0

while True:
    n = int(input('Digite um numero: '))
    tentativa += 1
    if n > x:
        print('Maior que o numero gerado!')
    elif n < x:
        print('Menor que o numero gerado!')
    else:
        print(f'Acertou! O numero era {x}')
        break

print(f'Tentativas = {tentativa}')
