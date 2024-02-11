# 11). Crie um dicionário para salvar os nomes das funções chamadas e a quantidade de vezes que foi executada. 
# Saída deve ser: {'funcao1': calls1, 'funcao2': calls2} 

# 1ª forma:

def chamadas(cache):
    def decorator(func):
        def wrapper(a, b):
            if func.__name__ not in cache.keys():
                cache[func.__name__] = 1
            else:
                cache[func.__name__] += 1
            print(f'Resultado da função {func.__name__} = {func(a, b)}')
            return cache
        return wrapper
    return decorator

cache = {}

@chamadas(cache)
def somar(a, b):
    return a + b

@chamadas(cache)
def subtrair(a, b):
    return a - b
    
@chamadas(cache)
def multiplicar(a, b):
    return a * b

print(somar(1, 2))
print(somar(1, 3))
print(multiplicar(1, 2))
print(somar(1, 3))
print(subtrair(9, 0))
print(somar(30, 1))
print(multiplicar(2, 3))
