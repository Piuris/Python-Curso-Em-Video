'''Modifique as funções que foram criadas no desafio 107 para que eles aceitem
um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
formatado pela função moeda(), desenvolvida no exercício 108.'''
import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}')
print(f'O dobre do {moeda.moeda(p)} é {moeda.dobro(p)}')
taxa = float(input('Digite a porcentagem de aumento: '))
print(f'Aumentando {taxa}% temos {moeda.aumentar(p, taxa)}')
taxa = float(input('Digite a porcentagem de redução: '))
print(f'Reduzindo {taxa}% temos {moeda.diminuir(p, taxa)}')
