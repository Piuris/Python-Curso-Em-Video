'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoaas. No
final do programa, mostre: A média de idade do grupo. Qual é o nome do homem
mais velho. Quantas mulheres têm menos de 20 anos.'''
import sys
maior = sys.float_info.min
mulheres = 0
homem = ''
media = 0
for i in range(0, 4):
    nome = str(input('Digite o nome da primeira pessoa: '))
    sexo = str(input('Digite F para feminino e M para masculino: ')).upper()
    idade = int(input('Digite a idade da pessoa: '))
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M' and idade > maior:
        maior = idade
        homem = nome
    media += idade
media = media / 4
print('A média de idade é: {}'.format(media))
print('O nome do homem mais velho é: {}'.format(homem))
print('A quantidade de mulheres com menos de 20 anos é: {}'.format(mulheres))
