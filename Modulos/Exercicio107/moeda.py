'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar()
diminuir(), dobro(), metade(). Faça também um programa que importe esse módulo
e use algumas dessas funções.'''


def aumentar(preco=0, porcentagem=0):
    aumento = porcentagem / 100
    return preco * aumento + preco


def diminuir(preco=0, porcentagem=0):
    reducao = porcentagem / 100
    return preco - (preco * reducao)


def metade(preco=0):
    return preco / 2


def dobro(preco=0):
    return preco * 2
