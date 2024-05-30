'''Adapte o código do desafio 107, criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado.'''
import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobre do {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
taxa = float(input('Digite a porcentagem de aumento: '))
print(f'Aumentando {taxa}% temos {moeda.moeda(moeda.aumentar(p, taxa))}')
taxa = float(input('Digite a porcentagem de redução: '))
print(f'Reduzindo {taxa}% temos {moeda.moeda(moeda.diminuir(p, taxa))}')
