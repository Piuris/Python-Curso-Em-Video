'''O mesmo professor do desafio 19 quer sortear a ordem de apresentação de
trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e
mostre a ordem sorteada.'''
import random
nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('A ordem é: {}'.format(lista))
