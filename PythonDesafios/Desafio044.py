'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento: à vista dinheiro/
cheque - 10% de desconto, à vista no cartão - 5% de desconto, em até 2x no
cartão - preço normal ou 3x ou mais no cartão - 20% de juros'''
valor = float(input('Digite o valor a ser pago: '))
print('Escolha o método de pagamento')
print('1 - À vista dinheiro ou cheque\\n2 - À vista no cartão')
print('3 - 2x no cartão\n4 - 3x ou mais no cartão')
metpagamento = int(input('Método escolhido: '))
if metpagamento == 1:
    valor = valor - (valor * 0.1)
elif metpagamento == 2:
    valor = valor - (valor * 0.05)
elif metpagamento == 3:
    valor = valor
elif metpagamento == 4:
    valor = valor + (valor * 0.2)
else:
    print('O método de pagamento escolhido é inválido!')
print('Preço a ser pago R${}'.format(valor))
