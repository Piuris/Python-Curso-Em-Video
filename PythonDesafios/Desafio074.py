'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma
tupla. Depois disso, mostre a listagem de números gerados e também indique o
menor e o maior valor que estão na tupla.'''
from random import randint
import sys
maior = sys.float_info.min
menor = sys.float_info.max
numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100),
           randint(0, 100))
for i in range(0, 5):
    if maior < numeros[i]:
        maior = numeros[i]
    if menor > numeros[i]:
        menor = numeros[i]
print(f'A listagem de números sorteados foi: {numeros}')
print(f'O maior numero foi {maior} e o menor foi {menor}')
