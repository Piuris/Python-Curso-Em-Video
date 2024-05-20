'''Refaça o desafio 009, mostrando a tabuada de um número que o usuário
escolher, só que agora utilizando um laço for'''
num = int(input('Digite o número para ver sua tabuada: '))
for i in range(0, 11):
    print('{} x {} = {}'.format(num, i, num * i))
