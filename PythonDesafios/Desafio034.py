'''Escreva um programa que pergunte o salário de um funcionário e calcule o
valor do seu aumento. Para salário superiores a R$1250,00, calcule um aumento
de 10%. Para os inferiores ou iguais, o aumento é de 15%'''
salario = float(input('Digite o salário: '))
if salario > 1250:
    print('O novo salário é: R${}'.format(salario + (salario * 0.1)))
else:
    print('O novo salário é: R${}'.format(salario + (salario * 0.15)))
