"""
Formatando valores com modificadores

:s - Texto (strings)
:d - inteiros (int)
:f - números de ponto flutuante (float)
:.(numero)f - quantidade de casas decimais (float)
:(caractere) (> ou < ou ^) (qunatidade) (tipo -s, d ou f)
> - esquerda
< - direita
^ - centro
"""

"""n1 = 10
n2 = 3
divisao = n1/n2
print('{:.2f}'.format(divisao))  #para considerar apenas 2 casas de um float
print(f'{divisao:.2f}')  #mesma coisa, mas, com o f strings
"""

"""num1 = 1
print(f'{num1:0>10}')  #preencher com 9 zeros (totalizando 10 caracteres) a esquerda do final da variavel

num2 = 1150
print(f'{num2:0>10}')  #similar ao de cima, apenas para dar 10 caracteres

# > acrescenta caracteres a esquerda
# < acrescenta caracteres a direita
# ^ deixa a variável no meio e atribui mais caracteres para chegar ao desejado

num3 = 2500
print(f'{num3:0>10.2f}')  #também, pode ser mesclado, acrescentando o numero e deixando o limite de casas decimais
"""

#também, pode ser utilizado com strings

nome = 'leonardo'
print(f'{nome:#^50}')