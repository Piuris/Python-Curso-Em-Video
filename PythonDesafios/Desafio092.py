'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de
zero, o dicionário receberá também o ano de contrataçao e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
registro = dict()
registro['nome'] = str(input('Nome: ')).title()
datanascimento = int(input('Data Nascimento: '))
registro['idade'] = 2024 - datanascimento
registro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if registro['CTPS'] != 0:
    registro['contratacao'] = int(input('Ano de contratação: '))
    registro['salario'] = float(input('Salário: R$'))
    registro['aposentadoria'] = registro['contratacao'] - datanascimento + 35
for k, v in registro.items():
    print(f'{k}: {v}')
