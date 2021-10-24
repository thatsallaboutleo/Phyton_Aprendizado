"""
Manipulação de strings

*Strings indices
*Fatiamento de strings
*funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo
"""

# positivos    [012345678]
texto        = 'PYTHON S2'
# negativos   -[987654321]

nova_str = texto[:6]  #fatiamento de string, do inicio até o caractere 6
print(nova_str)

nova_str = texto[:-1]  #para considerar os caracteres negativos
print(nova_str)

nova_str = texto[4:6]  #também, pode ser feito um range, do char 4 até o 6
print(nova_str)

nova_str = texto[0:6:2]  #começando do 0 até o 6, pulando de 2 em 2
print(nova_str)

nova_str = texto[0::3]  #até o final, pulando de 3 em 3
print(nova_str)