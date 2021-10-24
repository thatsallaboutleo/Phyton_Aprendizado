""""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva "seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"seu nome é normal"; maior que 6 escreva "seu nome é muito grande"
"""

a = input('Digite seu nome: ')

if len(a) <= 4:
    print('Seu nome é curto')

elif len(a) > 6:
    print('seu nome é muito grande')

elif len(a) > 5 or len(a) < 6:
    print('Seu nome é normal')

else:
    pass
