'''Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados, em
ordem crescente.'''
lista = list()
continuar = True
while continuar:
    num = (int(input('Digite um valor: ')))
    if num in lista:
        print('O número já está presente na lista!')
    else:
        lista.append(num)
    opcao = (str(input('Deseja adicionar mais valores: [S/N] '))).upper()
    if opcao == 'N':
        continuar = False
lista.sort()
print(lista)
