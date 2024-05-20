'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será
interrompido quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo'''
from random import randint
vitorias = soma = 0
resultado = True
while resultado:
    computador = randint(0, 10)
    n = int(input('Escolha um número: '))
    escolha = str(input('Digite a sua escolha Par ou Ímpar [P/I]? ')).upper()
    soma = n + computador
    if escolha == 'P' and soma % 2 == 0:
        print(f'O computador escolheu {computador}')
        print('Você venceu!')
        vitorias += 1
    if escolha == 'P' and soma % 2 == 1:
        print(f'O computador escolheu {computador}')
        print('Você perdeu!')
        resultado = False
    if escolha == 'I' and soma % 2 == 0:
        print(f'O computador escolheu {computador}')
        print('Você perdeu!')
        resultado = False
    if escolha == 'I' and soma % 2 == 1:
        print(f'O computador escolheu {computador}')
        print('Você venceu!')
        vitorias += 1
print(f'O total de vitórias consecutivas foram: {vitorias}')
