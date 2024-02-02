"""
Chico tem 1.50 m e cresce 2 cm por ano, enquanto Zé tem 1.10m e cresce 3 cm por ano.
Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.
"""

chico, ze = 1.5, 1.1
anos = 0

while ze < chico:
    chico += 0.02
    ze += 0.03
    anos += 1

print(anos)
