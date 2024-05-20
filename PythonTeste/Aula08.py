from math import sqrt, floor
import random
import emoji
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raíz de {} é igual a {:.2f}'.format(num, floor(raiz)))
num2 = random.randint(1, 10)
print(num2)
print(emoji.emojize("Sexo :fire:"))
