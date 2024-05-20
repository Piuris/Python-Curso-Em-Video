'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida: média abaixo
de 5.0 - reprovado, média entre 5.0 e 6.9 - recuperação e média 7.0 ou
superior - aprovado'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('REPROVADO!')
elif media >= 7.0:
    print('APROVADO')
else:
    print('RECUPERAÇÃO')
