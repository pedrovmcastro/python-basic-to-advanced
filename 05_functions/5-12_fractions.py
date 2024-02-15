"""
Exercise 12:
Create a program that performs simple fraction operations:
  - create and read two fractions p and q, each composed of a numerator and denominator;
  - find the greatest common divisor between the numerator and the denominator and simplify the fractions;
  - present the sum, subtraction, product, and quotient between the fractions read.
 Note: create a function for each item."


(PT-BR)
Exercício 12:
Faça um programa que faça operações simples de frações:
 - crie e leia duas frações p e q, compostas por um numerador e denominador;
 - encontre o máximo divisor comum entre o numerador e o denominador e simplifique as frações;
 - apresente a soma, a subtração, o produto e o quociente entre as frações lidas.
 Obs: cria uma função para cada item.
"""


def main():
    p = input('Enter fraction p: ')
    q = input('Enter fraction q: ')

    p = simplify(p)
    q = simplify(q)

    print(f'Simplified fractions: {p}, {q}')

    num1, den1 = fraction_to_int(p)
    num2, den2 = fraction_to_int(q)

    sum_result = add(num1, den1, num2, den2)
    subtraction_result = subtract(num1, den1, num2, den2)
    product_result = multiply(num1, den1, num2, den2)
    quotient_result = divide(num1, den1, num2, den2)

    print(f'SUM = {simplify(sum_result)}')
    print(f'SUBTRACTION = {simplify(subtraction_result)}')
    print(f'PRODUCT = {simplify(product_result)}')
    print(f'QUOTIENT = {simplify(quotient_result)}')


def fraction_to_int(frac):
    frac = frac.split('/')
    return int(frac[0]), int(frac[1])


def int_to_fraction(num, den):
    return '/'.join([str(num), str(den)])


def simplify(frac):
    num, den = fraction_to_int(frac)

    gcd = greatest_common_divisor(num, den)

    num = int(num/gcd)
    den = int(den/gcd)

    frac = int_to_fraction(num, den)

    return frac


def greatest_common_divisor(num, den):
    while den:
        num, den = den, num % den
    return num


def least_common_multiple(d1, d2):
    return (d1 * d2) // greatest_common_divisor(d1, d2)


def add(n1, d1, n2, d2):
    lcm = least_common_multiple(d1, d2)
    numerator = (lcm/d1)*n1 + (lcm/d2)*n2
    frac = int_to_fraction(int(numerator), int(lcm))
    return frac


def subtract(n1, d1, n2, d2):
    lcm = least_common_multiple(d1, d2)
    numerator = (lcm/d1)*n1 - (lcm/d2)*n2
    frac = int_to_fraction(int(numerator), int(lcm))
    return frac


def multiply(n1, d1, n2, d2):
    numerator = n1*n2
    denominator = d1*d2
    frac = int_to_fraction(int(numerator), int(denominator))
    return frac


def divide(n1, d1, n2, d2):
    numerator = n1*d2
    denominator = d1*n2
    frac = int_to_fraction(int(numerator), int(denominator))
    return frac


if __name__ == "__main__":
    main()