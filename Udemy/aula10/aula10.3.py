"""
Operadores lógicos
and, or, not
in e not in

-VERDADEIRO E VERDADEIRO = SÓ RETORNARÁ TRUE CASO OS DOIS COMPARATIVOS FOREM VERDADEIROS
COMPRAÇÃO1 AND COMPARAÇÃO2

-VERDADEIRO OU VERDADEIRO = QUALQUER UM TRUE, RETORNARÁ VERDADEIRO
COMP1 OR COMP2
"""

a = 2
b = 3

if not b > a:  #inversão de valores, neste caso "se não".
    print('b é maior do que a')
else:
    print('a é maior do que b')

"""
para variáveis vazias tbm utiliza-se o "not"

a = ''
b = 0

if not a:
   print('Por favor, preencha algum valor de A.)
******************************************************************************   
para in: 

nome = 'leonardo'

if 'e' in nome: 
    print('existe a letra e no seu nome.')
********************************************************************************
para not in: 

nome = 'leonardo'

if 'e' not in nome: 
    print('não existe e em seu nome')
"""