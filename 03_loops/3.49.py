"""
O funcionario chamado Carlos tem um colega chamado Joao que recebe
um salario que equivale a um terco do seu salario. Carlos gosta de fazer
aplicacoes na caderneta de poupança e vai aplicar seu salário integralmente nela,
pois esta rendendo 2% ao mês. Joao aplicará seu salário integralmente
no fundo de renda fixa, que está rendendo 5% ao mês. Construa um programa que devera
calcular e mostrar a quantidade de meses necessários para que o valor pertencente
a João iguale ou ultrapasse o valor pertencente a Carlos. Teste com outros valores para taxas.
"""

valor_joao, valor_carlos = 1000, 3000
meses = 0

while valor_joao < valor_carlos:
    valor_joao += 0.05*valor_joao
    valor_carlos += 0.02*valor_carlos
    meses += 1

print(meses)
