"""
1 - crie uma função1 que recebe uma função2 como parâmeto e retorne o valor
da função2 executada.

2- crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebem um número
diferente de argumentos.
"""


# 1

# def ola_mundo():
#     return 'Olá mundo!'
#
#
# def mestre(funcao):
#     return funcao()
#
#
# executando = mestre(ola_mundo)
# print(executando)

#2

# def mestre(funcao, *args, **kwargs):
#     return funcao(*args, **kwargs)
#
# def fala_oi(nome):
#     return f'oi {nome}'
#
# def saudacao(nome, saudacao, b):
#     return f'{saudacao} {nome} {b}'
#
# exe1 = mestre(fala_oi, 'Leo')
# exe2 = mestre(saudacao, 'Leo', saudacao='boa noite', b='uuuh')
#
# print(exe1)
# print(exe2)