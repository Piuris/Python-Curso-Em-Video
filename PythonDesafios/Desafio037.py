'''Escreva um programa que leia um número inteiro qualquer e peça para o
usuário escolher qual a base de conversão. 1 para binário, 2 para octal e 3
para hexadecimal'''
num = int(input('Digite um número inteiro: '))
print('Digite a base de conversão: ')
escolha = int(input('1 - Binario\n2 - Octal\n3 - Hexadecimal: '))
if escolha == 1:
    print('O número {} em binário é: {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número {} em octal é: {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número {} em hexadecimal é: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
