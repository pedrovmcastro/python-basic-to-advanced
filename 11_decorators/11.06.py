# 6). Crie um decorator chamado tempo_execucao que mede o tempo de execução de uma função e exibe o tempo decorrido ao final da execução.

import time

def tempo_execucao(func):
    def medir_tempo(*args):
        tmp_inicial = time.time()
        resultado = func(*args)
        tmp_final = time.time()
        print(f'Resultado = {resultado}')
        return f'Tempo de execução = {tmp_final - tmp_inicial}'
    return medir_tempo

@tempo_execucao
def somar(a, b):
    soma = 0
    for i in range(a, b):
        soma += i
    return soma

print(somar(1, 10000000))
