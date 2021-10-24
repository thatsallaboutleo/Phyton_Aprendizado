"""
Funções - def em python (parte 1)
"""


def funcao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    return f'{msg} {nome}'

variavel = funcao()

print(variavel)