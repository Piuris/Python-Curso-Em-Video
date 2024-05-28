'''Faça um programa que tenha uma função chamada contador(), que receba três
parâmetros: início, fim e passo e realize a contagem. Seu programa tem que
realizar três contagens através da função criada: De 1 até 10, de 1 em 1; De 10
até 0, de 2 em 2; Uma contagem personalizada.'''
from time import sleep


def contador(inicio, fim, passo):
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
            sleep(1)
    else:
        for i in range(inicio, fim - 1, passo):
            print(i, end=' ')
            sleep(1)
    print()


# Programa Principal
contador(1, 10, 1)
contador(10, 0, -2)
inicio = int(input('Digite o valor do início da contagem: '))
fim = int(input('Digite o valor do fim da contagem: '))
passo = int(input('Digite de quanto em quanto a contagem deve ser feita: '))
contador(inicio, fim, passo)
