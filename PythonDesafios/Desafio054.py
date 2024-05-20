'''Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são
maiores.'''
maiores = 0
menores = 0
for i in range(0, 7):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa:'.format(i+1)))
    idade = 2024 - nasc
    if idade < 21:
        menores += 1
    else:
        maiores += 1
print('O total de menores de idade é: {} e de maiores é: {}'.format(menores,
                                                                    maiores))
