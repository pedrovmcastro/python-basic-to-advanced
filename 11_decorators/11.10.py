# 10). Escreva um decorator chamado @log que recebe um nome de arquivo como argumento e grava em um arquivo de texto a data, 
# a hora, o nome e os argumentos da função sempre que ela for chamada.

from datetime import datetime

def log(nome_arq):
    def decorator(func):
        def wrapper(*args):
            with open(nome_arq, 'w') as arq:
                # Formatar a data e hora usando strftime
                data = datetime.now().strftime("%Y-%m-%d")
                hora = datetime.now().strftime("%H:%M")
                argumentos = ", ".join(str(arg) for arg in args)
                arq.write(f'Funcao = {func.__name__}\nData = {data}\nHora = {hora}\nArgumentos = {argumentos}\n\n')
                print('Log da função salvo com sucesso.')
            return f'Resultado de {func.__name__} = {func(*args)}'
        return wrapper
    return decorator

@log(nome_arq='test_decorator_log.txt')
def soma_argumentos(*args):
    return sum(args)

@log(nome_arq='test_decorator_log.txt')
def maior_argumento(*args):
    return max(args)

# Testando:
print(soma_argumentos(3, 5, 50))
print(maior_argumento(2, 9))
