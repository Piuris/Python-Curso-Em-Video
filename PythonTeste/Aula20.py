def soma(a, b):
    s = a + b
    print(f'A soma de {a} + {b} vale: {s}')


def contador(*num):
    print(f'Números em ordem crescentes: {sorted(num)}')
    print(f'Total de números digitados: {len(num)}')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# Programa Principal
soma(4, 5)
soma(a=8, b=9)
soma(b=2, a=1)
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
