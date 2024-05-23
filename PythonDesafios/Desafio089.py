'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
em uma lista composta. No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente'''
boletim = list()
aluno = list()
notas = list()
escolha = True
while escolha:
    nome = str(input('Digite o nome do aluno: ')).title()
    nota1 = float(input('Digite a 1ª nota do aluno: '))
    nota2 = float(input('Digite a 2ª nota do aluno: '))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    boletim.append(aluno[:])
    aluno.clear()
    opcao = str(input('Deseja continuar? [S/N] ')).upper()
    if opcao == 'N':
        escolha = False
    elif opcao == 'S':
        escolha = True
    else:
        while opcao != 'S' and opcao != 'N':
            print('Opção inválida!')
            opcao = str(input('Deseja continuar? [S/N] ')).upper()
print(f'{'No.':<5}{'NOME':<15}MÉDIA')
print('-' * 30)
for i in range(0, len(boletim)):
    media = (boletim[i][1] + boletim[i][2]) / 2
    print(f'{i:<5}{boletim[i][0]:<15}{media:.2f}')
print('-' * 30)
mostrarn = 0
while mostrarn != 999:
    mostrarn = int(input('Mostrar as notas de qual aluno (999 interrompe)? '))
    if mostrarn == 999:
        break
    if mostrarn > len(boletim):
        print('Esse aluno não existe!')
    print(f'As notas de {boletim[mostrarn][0]} são {boletim[mostrarn][1:]}')
