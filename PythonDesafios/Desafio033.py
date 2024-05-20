'''Faça um programa que leia três números e mostre qual é o maior e qual é o
menor. '''
maior = 0
menor = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n3:
    maior = n2
else:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n3:
    menor = n2
else:
    menor = n3
print('O maior número é: {} e o menor é: {}'.format(maior, menor))
