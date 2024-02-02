"""
Faça um programa que faça operações simples de frações:
 - crie e leia duas frações p e q, compostas por um numerador e denominador;
 - encontre o máximo divisor comum entre o numerador e o denominador e simplifique as frações;
 - apresente a soma, a subtração, o produto e o quociente entre as frações lidas.
 Obs: cria uma função para cada item.
"""


def fraction_to_int(frac):
    frac = frac.split('/')
    return int(frac[0]), int(frac[1])


def int_to_fraction(num, den):
    return '/'.join([str(num), str(den)])


def simplify(frac):
    num, den = fraction_to_int(frac)

    mdc = max_divisor(num, den)

    num = int(num/mdc)
    den = int(den/mdc)

    frac = int_to_fraction(num, den)

    return frac


def max_divisor(num, den):
    while den:
        num, den = den, num % den
    return num


def min_multiple(d1, d2):
    return (d1 * d2) // max_divisor(d1, d2)


def somar(n1, d1, n2, d2):
    mmc = min_multiple(d1, d2)
    numerador = (mmc/d1)*n1 + (mmc/d2)*n2
    frac = int_to_fraction(int(numerador), int(mmc))
    return frac


def subtrair(n1, d1, n2, d2):
    mmc = min_multiple(d1, d2)
    numerador = (mmc/d1)*n1 - (mmc/d2)*n2
    frac = int_to_fraction(int(numerador), int(mmc))
    return frac


def multiplicar(n1, d1, n2, d2):
    numerador = n1*n2
    denominador = d1*d2
    frac = int_to_fraction(int(numerador), int(denominador))
    return frac


def dividir(n1, d1, n2, d2):
    numerador = n1*d2
    denominador = d1*n2
    frac = int_to_fraction(int(numerador), int(denominador))
    return frac


p = input('Digite a fracao p: ')
q = input('Digite a fracao q: ')

p = simplify(p)
q = simplify(q)

print(f'Fracoes simplificadas: {p}, {q}')

num1, den1 = fraction_to_int(p)
num2, den2 = fraction_to_int(q)

soma = somar(num1, den1, num2, den2)
subtracao = subtrair(num1, den1, num2, den2)
produto = multiplicar(num1, den1, num2, den2)
quociente = dividir(num1, den1, num2, den2)

print(f'SOMA = {simplify(soma)}')
print(f'SUBTRACAO = {simplify(subtracao)}')
print(f'PRODUTO = {simplify(produto)}')
print(f'QUOCIENTE = {simplify(quociente)}')
