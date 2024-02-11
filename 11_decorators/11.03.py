# 3). Crie um decorador chamado memoize que armazena em cache os resultados de chamadas anteriores de uma função 
# e retorna o resultado armazenado se a mesma entrada ocorrer novamente.

def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return f'A função {func.__name__} já foi chamada com esses argumentos.'
        cache[key] = func(*args, **kwargs)
        return func(*args)
    return wrapper

@memoize
def soma(x, y):
    return x + y

@memoize
def multiplica(x, y):
    return x*y

print(soma(1, 2))
print(multiplica(1, 2))
print(soma(1, 2))
print(multiplica(1,2))
