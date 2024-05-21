'''Crie um programa que tenha uma tupla única com nomes de produtos e seus
preços, na sequência. No final, mostre uma listagem de preços organizando os
dados em forma tabular.'''
listagem = ('Mouse', 50.00, 'Teclado', 100.00, 'Fone', 70.50, 'Computador',
            1699.99, 'Mousepad', 15.34, 'Celular', 899.75, 'Caixa de som',
            48.00)
print('-' * 59)
print(f'{"Listagem de Preços":^59}')
print('-' * 59)
for i in range(0, len(listagem), 2):
    print(f'{listagem[i]:.<30}....................R${listagem[i+1]:>7.2f}')
