num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for posicao, i in enumerate(valores):
    print(f'Na posição {posicao} encontrei o valor {i}!')
print('Cheguei ao final da lista.')
for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
a = [2, 3, 4, 7]
b = a[:]  # cria uma copia de A em B ao invés de criar uma conexão entre eles
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
