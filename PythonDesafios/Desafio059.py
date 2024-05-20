'''Crie um programa que leia dois valores e mostre um menu na tela: 1 para
somar, 2 para multiplicar, 3 maior, 4 novos números e 5 sair do programa. Seu
programa deverá realizar a operação solicitada em cada caso.'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('-' * 50)
    print('''               Menu
          [1] Somar
          [2] Multiplicar
          [3] Maior
          [4] Novos números
          [5] Sair do programa''')
    opcao = int(input('          Digite a opção: '))
    print('-' * 50)
    if opcao > 5:
        print('O valor é inválido!')
    elif opcao == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('{} X {} = {}'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        if num1 > num2:
            print('O maior número é: {}'.format(num1))
        elif num2 > num1:
            print('O maior número é: {}'.format(num2))
        else:
            print('Os números são iguais!')
    elif opcao == 4:
        num1 = int(input('Digite um novo valor para o primeiro número: '))
        num2 = int(input('Digite um novo valor para o segundo número: '))
