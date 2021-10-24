"""
função f de variaveis
"""
nome = 'Leonardo'
idade = 26
altura = 1.83
peso = 106
maior_idade = idade > 18

imc = (peso / (altura ** 2))
print(f'{nome} tem {idade} idade e seu imc é {imc:.2f}')
#finalição em :.2f significa que o resultado será arredondado para im float de até suas casas decimais

print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))

print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
#para arredondar o resultado, como o caso a cima, final :.2f - numero = quantidades de casas, f = float