'''Reescreva a função leiaInt() que fizemos no desafio 104, incuindo agora a
possibilidade da digitação de um número de tipo inválido. Aproveite e crie
também uma função leiaFloat() com a mesma funcionalidade.'''


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Digite um número inteiro válido!')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro! Digite um número real válido!')
            continue
        else:
            return n


# Programa Principal
ni = leiaInt('Digite um número inteiro: ')
nf = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {ni} e o número real {nf}')
