'''nome = input('Qual é o seu nome? )
print('Prazer em te conhecer {:-^20}!'.format(nome))'''
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1**n2
print('A soma vale {}, a subtração vale {}'.format(s, sb), end=', ')
print('A multiplicação vale {}, a divisao vale {}'.format(m, d), end=', ')
print('A divisão inteira vale {} e a potencia vale {}'.format(di, e))
