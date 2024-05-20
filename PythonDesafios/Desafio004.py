'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
primitivo e todas as informações possíveis sobre ele'''
dado = input('Digite algo: ')
print('O tipo primitivo é: ', type(dado))
print('Só tem espaços? ', dado.isspace())
print('É numérico? ', dado.isnumeric())
print('É alfabético? ', dado.isalpha())
print('É alfanumérico? ', dado.isalnum())
print('É decimal? ', dado.isdecimal())
print('É maiúsculo? ', dado.isupper())
print('É minúsculo? ', dado.islower())
print('É capitalizado? ', dado.istitle())
