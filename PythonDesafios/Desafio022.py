'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome completo com todas as letras maiúsculas e minúsculas
- Quantas letras ao todo (sem considerar os espaços)
- Quantas letras tem o primeiro nome.'''
nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
dividido = nome.split()
print(len(nome) - nome.count(' '))
print(len(dividido[0]))
