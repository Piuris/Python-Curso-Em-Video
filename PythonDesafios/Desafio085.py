'''Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e
ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
lista = list()
pares = list()
impares = list()
for i in range(0, 7):
    num = int(input('Digite o {} valor: '.format(i + 1)))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
lista.append(pares)
lista.append(impares)
print(f'Os números pares digitados foram: {lista[0]}')
print(f'Os números ímpares digitados foram: {lista[1]}')
