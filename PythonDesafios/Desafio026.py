'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
aparece a letra A, em que posição ela aparece a primeira vez e em que posição
ela aparece a primeira vez e em que posição ela aparece a última vez'''
frase = str(input('Digite uma frase: ')).upper()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira vez que A aparece é: {}'.format(frase.find('A')+1))
print('A última vez que A aparece é: {}'.format(frase.rfind('A')+1))
