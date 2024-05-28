'''Faça um programa que tenha uma função chamada área(), que receba as
dimensões de um terreno retangular (largura e comprimento) e mostre a área do
terreno.'''


def area(largura, comprimento):
    terreno = largura * comprimento
    print(f'A área de um terreno {largura} X {comprimento} é de {terreno}m²')


# Programa Principal
largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
area(largura, comprimento)
