''' Faça um programa que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto'''
preco = float(input('Digite o preço de um produto: '))
novopreco = preco + (preco * 0.05)
print('O novo valor é: R${}'.format(novopreco))
