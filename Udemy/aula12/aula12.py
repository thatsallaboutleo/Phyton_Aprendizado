"""
documentações
*estão funções postadas pelo python
"""

n1 = input('Digite um numero: ')
n2 = input('Digite outro numero: ')

# isnumeric / isdigit / isdecimal
# Números e positivos (12345)
#print(n1.isnumeric())
#print(n2.isnumeric())

try:
    n1 = float(n1)
    n2 = float(n2)
    print(n1 + n2)
except:
    print('ERRO')