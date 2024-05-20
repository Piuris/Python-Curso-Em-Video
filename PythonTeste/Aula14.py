'''
i = 1
while i < 10:
    print(i)
    i += 1
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')'''
n = 1
pares = 0
impares = 0
while n != 0:
    n = int(input('Digite um valor não nulo ou digite 0 para terminar: '))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
print('O total de pares foi: {} e impares: {}'.format(pares, impares))
