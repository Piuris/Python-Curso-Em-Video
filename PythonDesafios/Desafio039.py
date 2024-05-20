'''Faça um programa que leia o ano de nascimento de um jovem e informe, de
acordo com sua idade: se ele ainda vai se alistar ao serviço militar, se é a
hora de se alistar ou se já passou do tempo do alistamento. Seu programa
também deverá mostrar o tempo que falta ou que passou do prazo.'''
anonasc = int(input('Digite o ano do seu nascimento: '))
anoatual = 2024
idade = anoatual - anonasc
if idade < 18:
    print('Você deverá se alistar daqui {} anos!'.format(18 - idade))
elif idade > 18:
    print('Você deveria ter se alistado há {} anos!'.format(idade - 18))
else:
    print('Você deve se alistar neste ano!!')
