'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler
a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Nome do jogador: ')).title()
jogador['partidas'] = int(input('Quantidade partidas jogadas: '))
for i in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
    total += gols[i]
jogador['gols'] = gols
jogador['totalgols'] = total
print('-' * 30)
print(jogador)
print('-' * 30)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-' * 30)
print(f'O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.')
for i in range(0, len(gols)):
    print(f'Na partida {i + 1} fez {gols[i]} gols')
print(f'Foi um total de {total}')
