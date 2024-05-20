'''Crie um programa que faça o computador jogar jokenpô com você'''
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Digite a sua jogada: '))
print('O jogador escolheu: {}'.format(itens(jogador)))
print('O computador escolheu: {}'.format(itens(computador)))
if computador == 0:
    if jogador == 0:
        print('Empatou!')
    elif jogador == 1:
        print('Você ganhou!')
    elif jogador == 2:
        print('Você perdeu!')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('Você perdeu!')
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Voce ganhou!')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('Você ganhou!')
    elif jogador == 1:
        print('Você perdeu!')
    elif jogador == 2:
        print('Empatou!')
    else:
        print('Jogada inválida!')
