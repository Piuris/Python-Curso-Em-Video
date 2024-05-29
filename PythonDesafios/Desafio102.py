'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
O primeiro que indique o número a calcular e o outro chamada show, que será um
valor lógico (opcional) indicando se será mostrado ou não na tela o processo de
cálculo do fatorial.'''


def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} X ', end='')
    return f


# Programa principal
print(fatorial(5))
print(fatorial(4, show=True))
