'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais'''
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador')
for i in palavras:
    print(f'\nNa plavra {i.upper()} temos ', end='')
    for j in i:
        if j.lower() in 'aeiou':
            print(j, end=' ')
