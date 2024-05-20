''' Faça um programa que leia o salário de um funcionário e mostre seu novo
salário, com 15% de aumento'''
salario = float(input('Digite o salário: '))
novosalario = salario + (salario * 0.15)
print("O novo salário é: R${:.2f}".format(novosalario))
