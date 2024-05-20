nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Luana' or nome == 'Bengala':
    print('Que nome bacana!!')
elif nome in 'Ana Paula Lucas Felipe':
    print('Nome comunzinho...')
else:
    print('Seu nome é bem normal. ')
print('Tenha um bom dia, {}!'.format(nome))
