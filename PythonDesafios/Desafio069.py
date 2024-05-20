'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No
final, mostre: Quantas pessoas tem mais de 18 anos. Quantos homens foram
cadastrados. Quantas mulheres tem menos de 20 anos.'''
continuar = True
mais18 = homens = mulheres20 = 0
while continuar:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper()
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    opcao = str(input('Deseja continuar [S/N]? ')).upper()
    if opcao == 'N':
        continuar = False
print(f'O total de pessoas com mais de 18 anos foi {mais18}')
print(f'O total de homens cadastrados foi {homens}')
print(f'O total de mulheres com menos de 20 anos foi {mulheres20}')
