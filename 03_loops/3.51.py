"""
Exercise:

(PT-BR)
Exercício:

"""

"""
Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais.
Em 1996 recebeu aumento de 1.5%. A partir de 1997, os aumentos sempre correspondem ao
dobro do ano anterior. Faça programas que determine o salário atual do funcionário.
"""

from decimal import Decimal, getcontext

getcontext().prec = 50  # Define a precisão desejada

salario = Decimal('2000')
aumento = Decimal('0.015')

for ano in range(1997, 2024):
    aumento *= 2
    salario += aumento * salario

print(f"O salário é de R${salario:.2f} em 2023.")
