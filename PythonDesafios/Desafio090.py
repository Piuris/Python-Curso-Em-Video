'''Faça um programa que leia nome e média de um aluno, guardando também a
situação em um dicionário. No final, mostre o conteúdoo da estrutura na tela'''
aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: ')).title()
aluno['media'] = float(input('Digite a média do aluno: '))
if aluno['media'] < 0 or aluno['media'] > 10.0:
    validacaomedia = False
else:
    validacaomedia = True
while not validacaomedia:
    print('A média deve ser um valor entre 0 e 10!')
    aluno['media'] = float(input('Digite a média do aluno: '))
    if aluno['media'] < 0 or aluno['media'] > 10.0:
        validacaomedia = False
    else:
        validacaomedia = True
if aluno['media'] < 7.0:
    aluno['situacao'] = 'Reprovado!'
elif aluno['media'] >= 7.0:
    aluno['situacao'] = 'Aprovado!'
for k, v in aluno.items():
    print(f'{k}: {v}')
