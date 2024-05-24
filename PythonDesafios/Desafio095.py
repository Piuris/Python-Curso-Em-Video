'''Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
time = list()
jogador = dict()
gols = list()
total = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).title()
    jogador['partidas'] = int(input('Quantidade partidas jogadas: '))
    gols.clear()
    for i in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 40)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 60)
while True:
    busca = int(input('Mostrar dados de quem? (999 finaliza) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com o código {busca}!')
    else:
        print(f' -- Levantamento do Jogador {time[busca]['nome']}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols')
    print('-' * 30)
