"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este numero é par ou impar. Caso o usuário não digite um número inteiro,
informe que não é um número.
"""

a = input('Digite um número inteiro: ')

if a.isdigit():
    a = int(a)

    if a%2 == 0: # divide tudo por 2, caso sobre 1 ele é impar, caso não sobre nada 0, ele é par.
        print(f'{a} é par')
    else:
        print(f'{a} é impar')
else:
    print('Digite um numero inteiro')