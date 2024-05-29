'''Faça um mini-sistema que utilize o interactive help do Python. O usuário vai
digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra
'FIM', o programa se encerrará. OBS: use cores'''


def ajuda(comando):
    help(comando)


def titulo(msg, cor=0):
    padrao = '\033[m'
    tam = len(msg)
    print('~' * tam)
    print(cor, msg, padrao)
    print('~' * tam)


# Programa Principal
comando = ''
while True:
    titulo('Sistema de ajuda em Python', '\033[0;30;42m')
    comando = str(input("Função ou biblioteca: "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Finalizando', '\033[0;30;41m')
