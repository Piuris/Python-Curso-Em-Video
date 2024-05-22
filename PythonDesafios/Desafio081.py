'''Crie um programa que vai ler vários números e colocar em uma lista. Depois
disso, mostre: Quantos números foram digitados. A lista de valores, ordenada de
forma decrescente. Se o valor 5 foi digitado e está ou não na lista.'''
lista = list()
cont = 0
continuar = True
while continuar:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    opcao = 'l'
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('Deseja continuar? [S/N] ')).upper()
        if opcao == 'N':
            continuar = False
        elif opcao == 'S':
            continuar = True
        else:
            print('Valor inválido! Digite apenas S ou N.')
print(f'Você digitou {cont} elementos')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O número 5 está presente na lista!')
else:
    print('O número 5 não está presente na lista!')
