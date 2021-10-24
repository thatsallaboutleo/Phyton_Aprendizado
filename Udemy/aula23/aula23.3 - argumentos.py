"""
Funções (def) em python - *args **kwargs
"""


def func(*args, **kwargs):  # asterisco serve para desempacotar listas e args
    print(args)

    nome = kwargs.get('nome')
    print(nome)

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='leo', sobrenome='auco')
