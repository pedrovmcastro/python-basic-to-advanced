# 4). Escreva uma função chamada compor que aceita duas funções e retorna uma nova função que é a composição das duas funções.

def compor(funcao1, funcao2):
    def funcao_composta(x):
        return funcao2(funcao1(x))
    return funcao_composta

# Exemplos de uso:

def dobrar(num):
    return num * 2

def adicionar_um(num):
    return num + 1 

print(adicionar_um(dobrar(5))) # nem seria preciso de uma função para compor, mas...

print(compor(dobrar, adicionar_um)(5)) # do jeito mais prático

funcao_composta = compor(dobrar, adicionar_um)
print(funcao_composta(5))
