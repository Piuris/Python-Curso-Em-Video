'''Crie um pacote chamada utilidadesCeV que tenha dois módulos internos
chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107,
108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando.'''
from utilidadescev import moeda

p = float(input('Digite o preço: R$'))
taxaa = float(input('Digite a taxa de aumento: '))
taxar = float(input('Digite a taxa de redução: '))
moeda.resumo(p, taxaa, taxar)
