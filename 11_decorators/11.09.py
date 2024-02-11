# 9). Crie um decorador chamado contador_chamadas que mantém o número de vezes que uma função foi chamada. 
# Esse contador deve ser exibido ao final da execução da função.

def contador_chamadas(*args, **kwargs):
    def decorator(func):
        if func.__name__ not in kwargs.keys():
            kwargs[func.__name__] = 0
        def wrapper(*args):
            print(f'Resultado = {func(*args)}')
            kwargs[func.__name__] += 1
            return f'A função {func.__name__} teve {kwargs[func.__name__]} chamada(s).\n'
        return wrapper
    return decorator

chamadas = {}

@contador_chamadas(chamadas)
def soma(a, b):
    return a + b

@contador_chamadas(chamadas)
def multiplica(a, b):
    return a * b

@contador_chamadas(chamadas)
def dobra(a):
    return a * 2

# Testes:
print(soma(1, 2))
print(soma(1, 3))
print(multiplica(1, 2))
print(multiplica(1, 3))
print(soma(1, 2))
print(dobra(5))
