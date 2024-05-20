print('\033[7;33;44mOlá Mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))
nome = 'Luana'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[32m',
         'pretoebranco': '\033[7;30m]'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome,
                                                           cores['limpa']))
'''
Style
0 - Normal
1 - Negrito
4 - Sublinhado
7 - Inverso
Text color
30 - Branco
31 - Vermelho
32 - Verde
33 - Amarelo
34 - Azul
35 - Roxo
36 - Ciano
37 - Cinza
Background Color
40 - Branco
41 - Vermelho
42 - Verde
43 - Amarelo
44 - Azul
45 - Roxo
46 - Ciano
47 - Cinza
'''
