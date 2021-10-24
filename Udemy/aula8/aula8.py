"""
*Criar variáveis para nome (str), idade (int), altura (float) e peso (float);
*obter o ano de nascimento da pessoa (baseado na idade);
*obter o IMC da pessoa com 2 casas decimais
*Exibir um texto com todos os valores na tela usando F-strings.
"""

name = 'Leonardo'
old = 26
high = 1.83
weight = 106.3
year = 2021
year_old = year - old
IMC = (weight/(high**2))

print(f'{name} tem {old} anos, {high}m de altura e pesa {weight}kg;')
print(f'O IMC de {name} é de {IMC:.2f};')
print(f'Também, ele nasceu em {year_old}.')