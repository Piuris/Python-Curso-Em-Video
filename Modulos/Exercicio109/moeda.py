def aumentar(preco=0, porcentagem=0, formatar=True):
    aumento = porcentagem / 100
    res = preco * aumento + preco
    return res if formatar is False else moeda(res)


def diminuir(preco=0, porcentagem=0, formatar=True):
    reducao = porcentagem / 100
    res = preco - (preco * reducao)
    return res if formatar is False else moeda(res)


def metade(preco=0, formatar=True):
    res = preco / 2
    return res if formatar is False else moeda(res)


def dobro(preco=0, formatar=True):
    res = preco * 2
    return res if formatar is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
