'''Melhore o jogo do desafio 028 onde o computador vai pensar em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
computador = randint(0, 10)
contador = 1
num = int(input('Digite o seu palpite: '))
while num != computador:
    print('Palpite errado!')
    num = int(input('Digite o seu palpite: '))
    contador += 1
print('Parabéns você acertou em {} tentativas'.format(contador))
