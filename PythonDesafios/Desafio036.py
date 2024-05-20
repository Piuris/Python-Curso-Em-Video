'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma
casa. O programa vai perguntar o valor da casa, o salário do comprador e em
quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
ela não pode exceder 30% do salário ou então o empréstimo será negado.'''
valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salario: '))
anos = float(input('Digite em quantos anos vai pagar: '))
prestacao = valor / (anos * 12)
if prestacao > salario * 0.3:
    print('Empréstimo negado! Valor da prestação maior do que o permitido!')
else:
    print('Empréstimo aprovado! Valor da prestação R${:.2f}'.format(prestacao))
