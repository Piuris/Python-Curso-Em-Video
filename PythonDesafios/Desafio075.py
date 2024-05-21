'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final, mostre: Quantas vezes apareceu o valor 9. Em que
posição foi digitado o primeiro valor 3. Quais foram os números pares.'''
tupla = (int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')))
print(f'O número 9 apareceu: {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor três foi digitado na {tupla.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
