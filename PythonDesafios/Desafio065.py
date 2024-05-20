'''Crie um programa que leia vários números inteiros pelo teclado. No final da
execução, mostre a média entre todos os valores e qual foi o maior e o menor
valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.'''
import sys
maior = sys.float_info.min
menor = sys.float_info.max
continuar = 'S'
contador, soma = 0, 0
while continuar == 'S':
    num = int(input('Digite um número: '))
    if maior < num:
        maior = num
    if menor > num:
        menor = num
    soma += num
    contador += 1
    continuar = str(input('Deseja continuar [S/N]? ')).upper()
print('A média dos valores foi: {}'.format(soma / contador))
print('O maior valor foi: {} e o menor foi: {}'.format(maior, menor))
