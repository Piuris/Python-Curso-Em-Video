'''Refaça o desafio 035 dos triângulos, acresentando o recurso de mostrar que
tipo de triângulo será formado: equilátero - todos os lados iguais, isósceles -
dois lados iguais ou escaleno - todos os lados diferentes.'''
r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))
if (r1 + r2) > r3 and (r2 + r3) > r1 and (r1 + r3) > r2:
    print('As retas podem formar um triângulo!')
    if r1 == r2 and r1 == r3:
        print('É um triângulo equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É um triângulo isósceles!')
    else:
        print('É um triângulo escaleno!')
else:
    print('As retas não podem formar um triângulo!')
