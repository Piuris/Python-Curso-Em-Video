''' Faça um programa que leia um ângulo qualquer e mostre na tela o valor do
seno, cosseno e tangente desse ângulo'''
from math import sin, cos, tan, radians
num = int(input('Digite o valor de um ângulo: '))
rad = radians(num)
print('O seno de {} é: {:.2f}'.format(num, sin(rad)))
print('O cosseno de {} é: {:.2f}'.format(num, cos(rad)))
print('A tangente de {} é: {:.2f}'.format(num, tan(rad)))
