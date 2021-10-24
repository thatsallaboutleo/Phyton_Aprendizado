"""
variaveis
"""
nome = 'Leonardo'
idade = 26
altura = 1.83
peso = 106
maior_idade = idade > 18

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É de maior:', maior_idade)

imc = (peso / (altura ** 2))
print(nome, 'tem', idade, 'idade e seu imc é', imc)