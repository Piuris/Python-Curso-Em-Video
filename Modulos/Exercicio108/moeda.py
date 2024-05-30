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


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
