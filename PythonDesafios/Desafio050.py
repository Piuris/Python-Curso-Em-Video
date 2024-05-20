'''Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-
'''
soma = 0
for i in range(0, 6):
    num = int(input('Digite um número para leitura: '))
    if num % 2 == 0:
        soma += num
print(soma)
