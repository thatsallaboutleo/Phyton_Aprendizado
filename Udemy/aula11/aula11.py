"""
Contagem de caracteres

funcao len - conta caracteres, mas n, nao funciona com numeros e boleanos
"""

user = input('Digite seu usuario: ')
qtd_char = len(user)

if qtd_char < 6:
    print('Digite pelo menos 6 caracteres')
else:
    print('Validado no sistema')