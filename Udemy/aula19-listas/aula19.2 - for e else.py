"""
For / Else em python
"""

variavel = ['Leonardo', 'Joaozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):
        continue
    print(valor)

#isto serviu para excluir uma palavra que se iniciava em "j" da lista 