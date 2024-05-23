'''Crie um programa que ajude um jogador da MEGA SENA a criar palpites. O
programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
quantjogos = int(input('Quantos jogos você quer sortear? '))
palpites = list()
jogo = list()
tot = 1
while tot <= quantjogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    palpites.append(jogo[:])
    jogo.clear()
    tot += 1
for i in range(0, quantjogos):
    print(f'Jogo {i+1}: {palpites[i]}')
    sleep(1)
