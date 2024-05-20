'''Crie um programa que simule o funcionamento de um caixa eletrônico. No
início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
o programa vai informar quantas cédulas de cada valor serão entregues.
Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
saque = float(input('Digite quanto quer sacar: '))
total = saque
cinquenta = vinte = dez = um = 0
while total >= 50:
    total -= 50
    cinquenta += 1
while total >= 20:
    total -= 20
    vinte += 1
while total >= 10:
    total -= 10
    dez += 1
while total >= 1:
    total -= 1
    um += 1
print(f'notas de 50: {cinquenta}')
print(f'notas de 20: {vinte}')
print(f'notas de 10: {dez}')
print(f'notas de 1: {um}')
