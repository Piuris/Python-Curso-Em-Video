'''Aprimore o desafio anterior, mostrando no final: A soma de todos os valores
pares digitados. A soma dos valores da terceira coluna. O maior valor da
segunda linha. '''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = terceira = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite o valor para a posição {i} {j}: '))
        if matriz[i][j] % 2 == 0:
            pares += matriz[i][j]
for i in range(0, 3):
    terceira += matriz[i][2]
if matriz[1][0] > matriz[1][1] and matriz[1][0] > matriz[1][2]:
    maior = matriz[1][0]
elif matriz[1][1] > matriz[1][2]:
    maior = matriz[1][1]
else:
    maior = matriz[1][2]
for i in range(0, 3):
    for j in range(0, 3):
        print(matriz[i][j], end=' ')
    print()
print(f'A soma de todos os números pares digitados foi {pares}')
print(f'A soma dos valores da terceira coluna foi {terceira}')
print(f'O maior valor da segunda linha é {maior}')
