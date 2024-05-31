try:
    a = int(input('Numerado: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Infelizmente tivemos um problema com os tipos de dados digitados!')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
