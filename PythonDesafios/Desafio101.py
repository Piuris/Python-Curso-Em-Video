'''Crie um programa que tenha uma função chamada voto() que vai receber o ano
de nascimento de ua pessoa, retornando um valor literal indicando se uma pessoa
tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''


def votar(anonascimento):
    idade = 2024 - anonascimento
    if idade < 16:
        return f'com {idade} anos o voto é NEGADO'
    elif idade >= 65:
        return f'com {idade} anos o voto é OPCIONAL'
    elif idade >= 16 and idade < 18:
        return f'com {idade} anos o voto é OPCIONAL'
    else:
        return f'com {idade} anos o voto é OBRIGATÓRIO'


# Programa Principal
anonascimento = int(input('Digite o seu ano de nascimento: '))
resultado = votar(anonascimento)
print(resultado)
