lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(sorted(lanche))
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
print(lanche[2:])
print(lanche[-2:])
print(len(lanche))
for i in lanche:
    print(f'Eu vou comer {i} na posição {i}')

for i in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[i]}')

for posicao, i in enumerate(lanche):
    print(f'Eu vou comer {i} na posição {posicao}')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
print(c.index(2))
print(c.index(1))

pessoa = ('João', 19, 'M', 60.52)
