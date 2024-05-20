'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual
foi o maior e o menor peso lidos.'''
import sys
maior = sys.float_info.min
menor = sys.float_info.max
for i in range(0, 5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i + 1)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso é: {}kg e o menor é: {}kg'.format(maior, menor))
