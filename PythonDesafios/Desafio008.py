''' Faça um programa que leia um valor em metros e o exiba convertido em
centímetros e milímetros'''
metros = float(input('Digite um valor em metros: '))
centimetros = metros * 100
milimetros = centimetros * 10
print("A medida {} metros em centímetros é: {}".format(metros, centimetros))
print("A medida {} metros em milímetros é: {}".format(metros, milimetros))
