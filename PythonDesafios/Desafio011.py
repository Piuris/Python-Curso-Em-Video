''' Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e  a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados'''
largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
tinta = area/2
print("O total de litros de tinta necessários para pintar {} m de parede é: {}"
      .format(area, tinta))
