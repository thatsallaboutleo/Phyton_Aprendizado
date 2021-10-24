"""
Programa ficticio - login simples
"""

usuario = input('Nome de usuário:')
senha = input('Senha do usuário:')

usuario_bd = 'leo'
senha_bd = '5050'

if usuario_bd == usuario and senha_bd == senha:
    print('Logado.')
else:
    print('Usuário ou senha inválidos.')