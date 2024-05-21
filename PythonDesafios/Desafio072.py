'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso de zero até vinte. Seu programa deverá ler número pelo teclado
entre 0 e 20 e mostrá-lo por extenso.'''
numeros = (
            'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
posicao = 0
posicao = int(input('Digite um número entre 0 e 20: '))
while posicao < 0 or posicao > 20:
    print('Posição inválida!')
    posicao = int(input('Digite um número entre 0 e 20: '))
print(numeros[posicao])
