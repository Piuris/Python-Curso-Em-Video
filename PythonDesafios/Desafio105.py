'''Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguites informações: Quantidade
de notas, a maior nota, a menor notar, a média da turma, a situação (opcional).
Adicione também as docstrings da função.'''


def notas(*notas, sit=False):
    """-> Função para analisa notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma."""
    global maior
    global menor
    global total
    global media
    global situacao
    soma = 0
    maior = notas[0]
    menor = notas[0]
    total = len(notas)
    for nota in notas:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
        soma += nota
    media = soma / total
    if sit:
        if media < 7.0 and media >= 5.0:
            situacao = 'RAZOÁVEL'
        elif media > 9.0 and media <= 10.0:
            situacao = 'MUITO BOA'
        elif media >= 7.0 and media < 9.0:
            situacao = 'BOA'
        elif media < 5.0 and media >= 0:
            situacao = 'RUIM'
        else:
            situacao = 'MÉDIA INVÁLIDA'
        return f'''Total: {total}, Maior: {maior}, Menor: {menor}, Média:
        {media}, Situação: {situacao}'''
    else:
        return f'''Total: {total}, Maior: {maior}, Menor: {menor}, Média:
        {media}'''


# Programa Principal
print(notas(7.0, 6.0, 5.0, 9))
print(notas(4.0, 7.0, 10.0, 7.0, sit=True))
help(notas)
