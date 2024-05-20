'''Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o
número solicitado for negativo.'''
n = 1
while n >= 0:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    for i in range(0, 11):
        print(f'{n} X {i} = {n * i}')
