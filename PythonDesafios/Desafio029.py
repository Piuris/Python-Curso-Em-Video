'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
80 km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar
R$27,00 por cada km acima do limite.'''
velocidade = int(input("Digite a velocidade do carro: "))
if velocidade > 80:
    multa = 27 * (velocidade - 80)
    print('Voce foi multado no valor de R${}'.format(multa))
