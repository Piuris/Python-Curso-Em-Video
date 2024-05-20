'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No
final mostre os 10 primeiros termos dessa progressão.'''
primeiro = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da progressão: '))
for i in range(primeiro, primeiro + 10):
    primeiro += razao
    print(primeiro)
