'''Crie um programa que leia vários números inteiros pelo teclado. O programa
só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos númeross foram digitados e qual foi a soma entre eles
(desconsiderando o flag).'''
n = contador = soma = 0
while n != 999:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'Foram digitados {contador} números e a soma deles é {soma}')
