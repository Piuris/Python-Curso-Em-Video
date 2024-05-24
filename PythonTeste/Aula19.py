pessoas = {'nome': 'João', 'sexo': 'M', 'idade': 19}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.')
del pessoas['sexo']
pessoas['peso'] = 60.3
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
estado = dict()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).title()
    estado['sigla'] = str(input('Sigla do Estado: ')).upper()
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
for e in brasil:
    for v in e.values():
        print(v, end=' - ')
    print()
