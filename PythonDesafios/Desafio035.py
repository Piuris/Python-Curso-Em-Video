'''Desenvolva um programa que leia o comprimento de três retas e diga ao
usuário se elas podem ou não formar um triângulo'''
r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))
if (r1 + r2) > r3 and (r2 + r3) > r1 and (r1 + r3) > r2:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
