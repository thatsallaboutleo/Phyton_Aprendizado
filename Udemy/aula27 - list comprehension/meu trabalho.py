string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'

#Fazer uma lista que separe em termos a string 0 a 9:

n = 10
lista = [string[i:i + n] for i in range(0, len(string), n)]

print(lista)

#Fazer a lista voltar a ser uma string e estar separada por um . em cada termo:

retorno = '.'.join(lista)

print(retorno)