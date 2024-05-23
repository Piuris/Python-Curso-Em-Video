'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta
'''
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        lista[i][j] = int(input(f'Digite o valor pra posição {i} {j}: '))

for i in range(0, 3):
    for j in range(0, 3):
        print(lista[i][j], end=' ')
    print()
