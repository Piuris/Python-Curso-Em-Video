''' Faça um programa que leia quanto dinheiro uma pessoa tem e
mostre quantos dólares ela pode comprar'''
real = float(input("Digite quantos reais você tem: "))
dolar = real / 5.17
print('Com R${} você consegue comprar ${:.2f}'.format(real, dolar))
