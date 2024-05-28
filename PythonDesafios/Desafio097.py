'''Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''


def escreva(texto):
    print('-' * (len(texto) + 4))
    print(f'  {texto}')
    print('-' * (len(texto) + 4))


# Programa Principal
texto = str(input('Digite o texto: '))
escreva(texto)
