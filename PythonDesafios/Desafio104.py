'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
semelhante à função input() do Python, só que fazendo a validação para aceitar
apenas um valor numérico.'''


def leiaInt(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um número inteiro válido.')
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
