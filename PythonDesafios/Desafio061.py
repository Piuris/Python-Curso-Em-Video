'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.'''
primeiro = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da progressão: '))
contador = primeiro
num = primeiro
while contador < primeiro + 10:
    print(num)
    num += razao
    contador += 1
