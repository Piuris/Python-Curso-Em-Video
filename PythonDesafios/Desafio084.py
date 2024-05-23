'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em
uma lista. No final, mostre: Quantas pessoas foram cadastradas. Uma listagem
com as pessoas mais pesadas. Uma listagem com as pessoas mais leves.'''
import sys
maior = sys.float_info.min
menor = sys.float_info.max
lista = list()
pesadas = list()
leves = list()
dado = list()
cont = 0
escolha = True
while escolha:
    dado.append(str(input('Nome: ')).title())
    dado.append(float(input('Peso: ')))
    lista.append(dado[:])
    dado.clear()
    cont += 1
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    if opcao == 'N':
        escolha = False
    elif opcao == 'S':
        escolha = True
    else:
        while opcao != 'N' and opcao != 'S':
            print('Opcao invalida!')
            opcao = str(input('Quer continuar? [S/N] ')).upper()
for i in lista:
    if i[1] > maior:
        maior = i[1]
    if i[1] < menor:
        menor = i[1]
for i in lista:
    if i[1] == maior:
        pesadas.append(i[0])
    if i[1] == menor:
        leves.append(i[0])
print(f'O total de pessoas cadastradas foi {cont}')
print(f'O maior peso foi {maior}Kg. Peso de {pesadas}')
print(f'O menor peso foi {menor}Kg. Peso de {leves}')
