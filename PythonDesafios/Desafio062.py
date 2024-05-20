'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais
alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''
primeiro = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão da progressão: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(termo)
        termo += razao
        contador += 1
    mais = int(input('Quer mostrar quantos termos a mais? '))
print('Total de termos mostrados: {}'.format(total))
