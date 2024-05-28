'''Faça um programa que tenha uma função chamada maior(), que receba vários
parâmetros com valores inteiros. Seu programa tem que analisar todos os valores
e dizer qual deles é o maior. '''
from time import sleep


def maior(num):
    maior = num[0]
    print(f'Foram informados {len(num)} valores')
    for i in range(0, len(num)):
        print(num[i], end=' ')
        sleep(1)
        if num[i] > maior:
            maior = num[i]
    print(f'\nO maior número é: {maior}')


# Programa Principal
lista = list()
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if opcao in 'SN':
            break
        print('Erro! Digite S ou N')
    if opcao == 'N':
        break
maior(lista)
