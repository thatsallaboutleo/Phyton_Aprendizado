"""
desempacotamento de listas em python
"""

lista = ['Luiz', 'Joao', 'Maria']

n1,n2, *maisumalista = lista  #"*maisumalista" serve para criar uma nova lista com os termos que não foram citados
print(n1)