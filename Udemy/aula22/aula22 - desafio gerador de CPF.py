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
from random import randint  #importanto esta fução de random, é gerado 9 numeros
numero = str(randint(100000000, 999999999))

#após gerar os 9 numeros, é feito o mesmo esquema do desafio do CPF, gerando 2 digitos finais

nv_cpf = numero
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(nv_cpf[index]) * reverso

    reverso -= 1

    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0

        total = 0

        nv_cpf += str(d)

print(nv_cpf)