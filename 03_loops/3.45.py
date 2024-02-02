"""
Faça um algoritmo que converta uma velocidade expressa em km/h
para m/s e vice-versa. Voce deve criar um menu com as duas opçoes
de conversão e com uma opçao para finalizar o programa. O usuario
podera fazer quantas conversões desejar, sendo que o programa
só sera finalizado quando a opçao de finalizar for escolhida.
"""

while True:
    N = int(input('Escolha uma opção: 1. km/h -> m/s; 2. m/s -> km/h; 3. Finalizar programa; (1, 2 ou 3?)\n'))
    if N == 1:
        km = float(input('Digite a velocidade (km/h): '))
        print(f'Velocidade = {(km*5/18):.2f} m/s')
    elif N == 2:
        ms = float(input('Digite a velocidade (m/s): '))
        print(f'Velocidade = {(ms*3.6):.2f} km/h')
    else:
        break
