'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela
os n primeiros elementos de uma sequência de fibonacci.'''
n = int(input('Digite quantos termos deseja ver: '))
n1 = 0
n2 = 1
contador = 0
while contador < n:
    print(n1)
    proximo = n1 + n2
    n1 = n2
    n2 = proximo
    contador += 1
