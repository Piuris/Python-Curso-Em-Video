'''Faça um programa que leia um número qualquer e mostre o seu fatorial.'''
num = int(input('Digite um número: '))
contador = num - 1
fatorial = num
while contador > 0:
    fatorial *= contador
    contador -= 1
print('O valor do fatorial de {} é: {}'.format(num, fatorial))
