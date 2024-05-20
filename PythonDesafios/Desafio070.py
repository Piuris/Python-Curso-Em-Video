'''Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre: Qual é o total
gasto na compra. Quantos produtos custam mais de R$1000. Qual é o nome do
produto mais barato.'''
import sys
continuar = True
total = produtos1000 = 0
menorpreco = sys.float_info.max
produtomaisbarato = ''
while continuar:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    total += preco
    if preco < menorpreco:
        produtomaisbarato = nome
    if preco > 1000:
        produtos1000 += 1
    opcao = str(input('Deseja continuar [S/N]? ')).upper()
    if opcao == 'N':
        continuar = False
print(f'O total gasto foi R${total:.2f}')
print(f'O total de produtos que custam mais de R$1000 é {produtos1000}')
print(f'O produto mais barato é {produtomaisbarato}')
