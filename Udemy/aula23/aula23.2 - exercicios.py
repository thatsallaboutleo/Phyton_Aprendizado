"""
1 - crie uma função que exibe uma saudação com os parâmetros saudação e nome.

2- Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.

3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual. Retorne o valor do primeiro
somado do aumento do percentual do mesmo

4 - fizz buzz - se o parâmetro da função dor divisível por 3, retorne fizz, se o parâmetro for divisível por 5, retorne
buzz. Se o parâmetro da função for divisível por 5 e por 3, retorne fizzbuzz, caso contrário, retorne o número enviado.
"""

# 1

"""def fun1(saudacao='Olá, bom dia', nome='joao'):
    return f'{saudacao} {nome}'


a = fun1()
print(a)"""

# 2

"""def fun2(n1=input('Primeiro numero: '), n2=input('Segundo numero: '), n3=input('Terceiro numero: ')):
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    return n1 + n2 + n3


b = fun2()
print(b)"""


# 3

"""def fun3(pn=input('Digite um número:'), sn=input('Quanto por cento foi o aumento? ')):
    if pn.isnumeric():
        pn = int(pn)
    else:
        print('Apenas números.')

    sn = int(sn[:-1])

    return pn + ((sn / 100) * pn)

c = fun3()
print(f'Novo valor é {c}')"""


# 4

# def fun4(num=input('Digite um número: ')):
#     if num.isnumeric():
#         num = int(num)
#
#         if num % 3 == 0 and num % 5 == 0:
#             return 'FizzBuzz'
#         if num % 3 == 0:
#             return 'Fizz'
#         if num % 5 == 0:
#             return 'Buzz'
#
#         return num
#     else:
#         print('Digite apenas números')
#     return
#
# d = fun4()
# print(d)