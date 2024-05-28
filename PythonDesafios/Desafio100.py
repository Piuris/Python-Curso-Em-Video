'''Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores
PARES sorteados pela função anterior.'''
from random import randint as ri
from time import sleep


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    lista = (ri(0, 10), ri(0, 10), ri(0, 10), ri(0, 10), ri(0, 10))
    for i in range(0, len(lista)):
        print(lista[i], end=' ')
        sleep(1)
    return lista


def somaPar(lista):
    soma = 0
    print('\nSomando os valores: ', end='')
    for i in range(0, 5):
        if lista[i] % 2 == 0:
            print(lista[i], end=' ')
            soma += lista[i]
    print(f', temos {soma}')


# Programa Principal
lista = sorteia()
somaPar(lista)
