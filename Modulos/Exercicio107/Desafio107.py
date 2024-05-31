'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar()
diminuir(), dobro(), metade(). Faça também um programa que importe esse módulo
e use algumas dessas funções.'''
from Exercicio107 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobre do {p} é {moeda.dobro(p)}')
porcento = float(input('Digite a porcentagem de aumento: '))
print(f'Aumentando {porcento}% temos {moeda.aumentar(p, porcento)}')
porcento = float(input('Digite a porcentagem de redução: '))
print(f'Reduzindo {porcento}% temos {moeda.diminuir(p, porcento)}')
