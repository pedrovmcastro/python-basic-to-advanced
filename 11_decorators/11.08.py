# 8). Crie um decorador chamado retry que permite que uma função seja executada novamente se ela lançar uma exceção específica. 
# O número máximo de tentativas deve ser configurável.

def retry(max_attempts):
    def exception(func):
        def wrapper(a, b):
            attempts = 0
            while attempts <= max_attempts:
                try:
                    if attempts > 0:
                        print('Entrada inválida. Tente novamente:')
                        a, b = float(input()), float(input())
                    return func(a, b)
                except (TypeError, ValueError, ZeroDivisionError):
                    attempts += 1
            return 'Valor máximo de tentativas excedido'
        return wrapper
    return exception

@retry(max_attempts=3)
def soma(a, b):
    return a + b

@retry(max_attempts=3)
def divide(a, b):
    return a / b

print(soma(10,2))
print(soma(10, 'a'))
print(divide(10, 'a'))
