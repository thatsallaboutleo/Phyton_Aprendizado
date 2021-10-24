"""
tipos de dados:

str - string (textos);
int - inteiro (entram negativos e positovos);
float - números quebrados (para separar é utilizado . e nao ,);
bool - boleano, valores lógicos (true ou false);
"""

print('NOME', type('NOME'))  #str
print(12345, type(12345))  #int
print(1.0, type(1.0))  #float
print('2' == '3', type('2'=='3')) #bool

#bool nem sempre avalia true ou false para comparações, as vezes:
print('', type(''))
#caso ele se depare com listas vazias, também dará negativo

#String: nome
print('Leonardo', type('leonardo'))

#int: sua idade
print(26, type(26))

#float: altura
print(1.83, type(1.83))

#bool: se vc é maior de idade
print(26 > 18, type (26 > 18))