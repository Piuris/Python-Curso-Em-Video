'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No
final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
posições na lista. '''
import sys
menor = sys.float_info.max
maior = sys.float_info.min
lista = list()
posmaiores = []
posmenores = []
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {i + 1}: ')))
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
for i in range(0, 5):
    if maior == lista[i]:
        posmaiores.append(i)
    if menor == lista[i]:
        posmenores.append(i)
print(f'O maior valor foi {maior} nas posições {posmaiores}')
