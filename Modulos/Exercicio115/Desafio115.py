'''Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu
nome e idade em um arquvio de texto simples. O sistema só vai ter 2 opções:
cadastrar uma nova pessoa e listar todas as pessoas cadastradas.'''
import lib.interface as intface
import lib.arquivo as arq

arquivo = 'cursoemvideo.txt'
if not arq.arquivoExiste(arquivo):
    arq.criarArquivo(arquivo)

while True:
    resp = intface.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa',
                         'Sair do Sistema'])
    if resp == 1:
        arq.lerArquivo(arquivo)
    elif resp == 2:
        intface.cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = intface.leiaInt('Idade: ')
        arq.cadastrar(arquivo, nome, idade)
    elif resp == 3:
        print('Saindo do sistema')
        break
    else:
        print('Erro! Digite uma opção válida')
