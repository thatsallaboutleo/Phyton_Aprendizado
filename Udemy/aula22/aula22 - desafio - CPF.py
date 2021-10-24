"""
CPF = 168.995.350-09
--------------------------------------------------------------------------------------
1*10= 10                     # 1*11 = 11<-
6*9=  54                     # 6*10 = 60
8*8=  64                     # 8*9  = 72
9*7=  63                     # 9*8  = 72
9*6=  54                     # 9*7  = 63
5*5=  25                     # 5*6  = 30
3*4=  12                     # 3*5  = 15
5*3=  15                     # 5*4  = 20
0*2=  00                     # 0*3  = 0
total=297                  -># 0*2  = 0 - primeiro digito obtido na primeira conta
                             #total = 343
11 - (297 % 11) = 11
11 > 9 = 0                   # 11 - (343 % 11) = 9
digito 1 = 0                 # digito 2 = 9
"""

cpf = '44780928850'
nv_cpf = cpf[:-2]  # eliminando 2 digitos finais, também poderia ser [0:9]
reverso = 10  # contador para fazer a segunda parte da contagem, após o index
total = 0  # este é o armazenador das somas

# verificar quantos loops serão para o programa todo, 9 no primeiro (10 até 2) e 10 no segundo (11 até 2)
for index in range(19):
    if index > 8:
        index -= 9  # index de cada valor do cpf, quando chega na 8 passada, voltam 9 passadas.

    total += int(nv_cpf[index]) * reverso
    # ficaria: (ind0*10) + (ind1*9) + (ind2*8) + (ind3*7) + (ind4*6) + (ind5*5) + (ind6*4) + (ind7*2) + (ind8*1) + (ind9*0)
    # ind = index (local onde está o caractere, exp: CPF: 0 C / 1 P / 2 F)

    reverso -= 1  # começa no 10 e vai diminuindo um até o 2.

    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)
        # após a conta to total, o codigo ja vem direto aqui para aplicar a formula de verificação dos 2 ultimos caracteres

        if d > 9:  # aplicando a formula, quando o resultado da soma total dividido por 11 modular for maior que 9, será 0
            d = 0

        total = 0  # cpf * reverso
        # Após o primeiro total ser feito, ele é zerado para realizar a segunda parte da formula
        # Sendo: (ind0*11) + (ind1*10) + (ind2*9) + (ind3*8) + (ind4*7) + (ind5*6) + (ind6*5) + (ind7*4) + (ind8*3) + (ind9*2)

        nv_cpf += str(d)  # digito saiu um numero inteiro, foi necessário converte-lo para string


if nv_cpf == cpf:
    print('Correto')
else:
    print('Incorreto')
