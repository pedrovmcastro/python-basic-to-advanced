"""
Faça uma função e um programa de teste para o cálculo do volume de uma esfera.
Sendo que o raio é passado por parâmetro.
V = 4/3*pi*R³
"""


def volume_esfera(raio):
    pi = 3.1415
    return (4/3)*pi*raio**3


print(volume_esfera(int(input())))
