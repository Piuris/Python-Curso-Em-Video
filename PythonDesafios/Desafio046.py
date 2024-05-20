'''Faça um programa que mostre na tela uma contagem regressiva para o estouro
de fogos de artifício, inde de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
import time
import emoji
print('Contagem regressiva para os fogos de artífico!!!')
for i in range(11, 0, -1):
    print(i-1)
    time.sleep(1)
print(emoji.emojize(':fireworks: :fireworks: :fireworks: :fireworks:'))
