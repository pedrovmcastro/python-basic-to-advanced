# 5). Crie um decorador chamado verifica_argumentos que verifica se os argumentos passados para uma função estão corretos
# de acordo com uma especificação dada. Por exemplo, se a função espera dois inteiros como argumentos, 
# o decorador deve verificar se os argumentos são inteiros.

def verifica_argumentos(*tipos):
    def verifica_funcao(funcao):
        def wrapper(*args):
            for valor, tipo in zip(args, tipos):
                if type(valor) != tipo:
                    return f'Entrada inválida. O argumento {valor} não é do tipo {tipo.__name__}.'
            return funcao(*args)
        return wrapper
    return verifica_funcao
        
@verifica_argumentos(int, int)
def soma_inteiros(a, b):
    return a + b

print(soma_inteiros(1, 2))
print(soma_inteiros(1, '2'))
print(soma_inteiros(1.0, 2))
