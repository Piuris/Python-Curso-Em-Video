'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.'''
frase = str(input('Digite uma frase para verificar: '))
inverso = ''

frase = frase.replace(' ', '')

for i in range(len(frase) - 1, -1, -1):
    inverso += frase[i]
if inverso == frase:
    print('É palíndromo!')
else:
    print('Não é palíndromo')
