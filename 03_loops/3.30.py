"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Faça programas para calcular as sequintes sequências:
1) 1 + 2 + 3 + 4 + 5 ... + n
2) 1 - 2 + 3 - 4 + 5 ... + (2n-1)
3) 1 + 3 + 5 + 7 + 9 ... + (2n-1)
"""

N = int(input('Qual sequencia gostaria de escolher? (1/2/3) '))
soma = 0

if N == 1:
    for i in range(1, N+1):
        soma += i
elif N == 2:
    for i in range(1, 2*N):
        if i % 2 != 0:
            soma += i
        else:
            soma -= i
elif N == 3:
    for i in range(1, 2*N, 2):
        soma += i
else:
    print('Digite um número entre 1, 2 ou 3.')

print('Resultado: ', soma)

