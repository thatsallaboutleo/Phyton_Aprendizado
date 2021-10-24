"""
Entrada de dados

input : recebe string, para o usuário acrescentar informações;
input pode criar variáveis, tipo:

nome = input ("Qual seu nome?")  #variável nome será a informação acrescentada pelo usuário;

input sempre retorna string, por mais que seja número.

para trabalhar com input e numeros, ele deve ser convertido.
"""

nome = input("Digite seu nome: ")
old = input("Agora, sua Idade: ")

born = 2021-int(old)  #Para fazer a conta, foi nescessário converter "old" de str para int.

print()  #este print vazio serve para pular uma linha, fica mais bonitinho
print(f'{nome} tem {old} anos de idade e nasceu em {born}.')