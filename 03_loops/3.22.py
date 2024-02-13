"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,
uma sequencia arbitrária de notas (válidas no intervalo de 10 a 20) e
que mostre na tela, como resultado, a correspondente média aritmética. O número de notas
com que o aluno pretenda efetuar o cálculo não será fornecido ao programa, o qual terminará
quando for introduzido um valor que não seja válido como nota de aprovação.
"""

# valores válidos - nota int ou float dentro do intervalo
# valores inválidos - valores fora do intervalo

N, soma, cont = 10, 0, -1

while 10 <= N <= 20:
    cont += 1
    if cont != 0:
        soma += N
    N = float(input('Digite uma nota (entre 10 e 20): '))

media = soma/cont

print(f'A media do aluno eh {media:.2f}')

"""
Pelo Gepeto:

soma, cont = 0, 0

while True:
    N = float(input('Digite uma nota (entre 10 e 20): '))
    
    if 10 <= N <= 20:
        soma += N
        cont += 1
    else:
        break

if cont > 0:
    media = soma / cont
    print(f'A média do aluno é {media:.2f}')
else:
    print('Nenhuma nota válida foi digitada.')
"""