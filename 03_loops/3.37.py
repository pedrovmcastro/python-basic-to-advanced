"""
Exercise:

(PT-BR)
Exercício:

"""
"""
Escreve um programa que verifique quais numeros entre 1000 e 9999 (inclusive)
possuem a propriedade seguinte: a soma dos dois dígitos de mais baixa
ordem com os dois dígitos de mais alta ordem elevado ao quadrado é igual ao próprio
número. Por exemplo, para o inteiro 3025, temos que:
30 + 25 = 55
55² = 3025
"""

for i in range(1000, 10000):
    i = str(i)
    if (int(i[0:2]) + int(i[2:4]))**2 == int(i):
        print(i)
