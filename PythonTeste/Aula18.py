teste = list()
teste.append('Gustavo')
teste.append(40)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Claudia', 50]]
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
print(galera[0])
print(galera[0][0])
for i in galera:
    print(f'{i[0]} tem {i[1]} anos de idade.')
dado = list()
totmaior = totmenor = 0
for i in range(0, 3):
    dado.append(str(input('Nome: ')).title())
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for i in galera:
    if i[1] >= 21:
        print(f'{i[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{i[0]} é menor de idade.')
        totmenor += 1
print(f'''Temos {totmaior} pessoas maiores de idade e {totmenor} pessoas
      menores de idade''')
