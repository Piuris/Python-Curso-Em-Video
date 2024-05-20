'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M'
ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor
correto.'''
sexo = str(input('Digite M para masculino e F para feminino: ')).upper()
while sexo != 'M' and sexo != 'F':
    print('Valor inválido!')
    sexo = str(input('Digite M para masculino e F para feminino: ')).upper()
