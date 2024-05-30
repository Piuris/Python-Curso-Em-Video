'''Adicione ao módulo moeda.py criado nos desafios anteriores, uma função
chamada resumo(), que mostre na tela algumas informações geradas pelas funções
que já temos no módulo criado até aqui'''
import moeda

p = float(input('Digite o preço: R$'))
taxaa = float(input('Digite a taxa de aumento: '))
taxar = float(input('Digite a taxa de redução: '))
moeda.resumo(p, taxaa, taxar)
