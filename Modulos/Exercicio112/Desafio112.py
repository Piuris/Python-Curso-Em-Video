'''Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo
chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de
funcionar como a função input(), mas com uma validação de dados para aceitar
apenas valores que sejam monetários.'''
from utilidadescev import dado, moeda

p = dado.leiaDinheiro('Digite o preço: R$')
taxaa = float(input('Digite a taxa de aumento: '))
taxar = float(input('Digite a taxa de redução: '))
moeda.resumo(p, taxaa, taxar)
