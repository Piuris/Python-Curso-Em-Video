'''nome = str(input('Qual é seu nome? ))
if nome == 'Joao':
    print('Que nome lindo voce tem!')
print('Bom dia, {}'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua media foi {:.2f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! Parabéns!!')
else:
    print('Sua média foi ruim! Estude mais!')
