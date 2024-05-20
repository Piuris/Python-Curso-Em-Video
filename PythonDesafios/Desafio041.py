'''A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9
anos - mirim, até 14 anos - infantil, até 19 anos - junior, até 20 anos -
senior e acima - master'''
anonasc = int(input('Digite o ano de nascimento: '))
idade = 2024 - anonasc
if idade <= 9:
    print('Categoria Mirim!')
elif idade <= 14:
    print('Categoria Infantil')
elif idade <= 19:
    print('Categoria Junior')
elif idade <= 20:
    print('Categoria Sênior')
else:
    print('Categoria Master')
