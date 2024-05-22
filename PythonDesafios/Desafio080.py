'''Crie um programa onde o usuário possa digitar cinco valores numérios e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
No final, mostre a lista ordenada na tela.'''
lista = list()
for i in range(0, 5):
    num = (int(input('Digite um valor: ')))
    if i == 0:
        lista.append(num)
        print(f'O valor {num} foi adicionado ao final da lista!')
    else:
        j = 0
        while j < len(lista) and num > lista[j]:
            j += 1
        lista.insert(j, num)
        print(f'O {num} foi adicionado na posição {j} da lista')
print(f'A lista em ordem crescente é: {lista}')
