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


def resumo(preco=0, taxaa=0, taxar=0):
    print('-' * 30)
    print('Resumo do valor'.center(30))
    print('-' * 30)
    print(f'preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco)}')
    print(f'Metade do preco: \t{metade(preco)}')
    print(f'Preço com aumento de {taxaa}%: \t{aumentar(preco, taxaa)}')
    print(f'Preço com redução de {taxar}%: \t{diminuir(preco, taxar)}')
    print('-' * 30)
