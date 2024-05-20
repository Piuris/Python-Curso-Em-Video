# Faça um programa que leia um número inteiro e mostra na tela a sua tabuada
num = int(input("Digite um numero: "))
for i in range(1, 11):
    print("{} x {} = {}".format(num, i, num * i))
