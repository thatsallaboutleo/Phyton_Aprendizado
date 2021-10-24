"""
*Enumerate - Enumerar elementos da lista
"""

lista = [
 #     0         1          2
    ['Jose', 'Claudia', 'Afonso'],  #0
    ['Augusto', 'Wiliam','Otavio'], #1
    ['Joao', 'Maria', 'Alice']     #2
]

for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome3)