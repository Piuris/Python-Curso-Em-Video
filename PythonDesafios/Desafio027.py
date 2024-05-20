'''Faça um programa que leia o nome completo de uma pessoa, mostrando em
seguida o primeiro e o último nome separadamente'''
nome = str(input('Digite o nome completo: '))
print('O primeiro nome é: {}'.format(nome[0:nome.find(' ')]))
print('O último nome é: {}'.format(nome[nome.rfind(' '):]).strip())
