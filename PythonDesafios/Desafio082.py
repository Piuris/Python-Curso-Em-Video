'''Crie um programa que vai ler vários números e colocar em uma lista. Depois
disso, crie duas listas extras que vão conter apenas os valores pares e os
valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
três listas geradas.'''
lista = list()
pares = []
impares = []
continuar = True
while continuar:
    lista.append(int(input('Digite um número: ')))
    opcao = 'l'
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Deseja continuar? [S/N] ')).upper()
        if opcao == 'N':
            continuar = False
        elif opcao == 'S':
            continuar = True
        else:
            print('Opção inválida! Digite S ou N!!')
for i in range(0, len(lista)):
    if lista[i] == 0:
        print('Número nulo não é par nem ímpar! Número ignorado')
    elif lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])
print(f'A lista geral é {lista}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {impares}')
