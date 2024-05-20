'''Faça um programa que leia um número e mostre o seu dobro, triplo e raiz
quadrada'''
from math import sqrt
num = int(input("Digite um número: "))
print("O dobro de {} é: {}".format(num, num * 2))
print("O triplo de {} é: {}".format(num, num * 3))
print("A raíz quadrada de {} é: {}".format(num, sqrt(num)))
