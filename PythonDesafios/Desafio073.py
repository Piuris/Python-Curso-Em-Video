'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
Apenas os 5 primeiros colocados. Os últimos 4 colocados na tabela. Uma lista
com os times em ordem alfabética. Em que posição na tabela está o time do
Internacional.'''
tabela = (
    'Athletico-PR', 'Bahia', 'Flamengo', 'Botafogo', 'São Paulo',
    'Cruzeiro', 'Atlético-MG', 'Bragantino', 'Palmeiras', 'Internacional',
    'Fortaleza', 'Grêmio', 'Vasco da Gama', 'Criciúma', 'Juventude',
    'Corinthians', 'Fluminense', 'EC Vitória', 'Atlético-GO', 'Cuiabá')
print(tabela[:5])
print(tabela[-4:])
print(sorted(tabela))
print(f'{tabela.index('Internacional') + 1}ª posição')
