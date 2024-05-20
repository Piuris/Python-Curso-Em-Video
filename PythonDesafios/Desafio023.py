''' Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um
dos digitos separados'''
num = int(input("Digite um numero entr 0 e 9999: "))
n = str(num)
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
