"""
Operadores relacionais

==, Igualdade
>, maior que
>=, maior que ou igual a
<, menor que
<=, menor que ou igual a
!=, diferente

#sempre retorna um valor booleano
"""

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
idade_minima = 20  #Muito jovem
idade_maxima = 30  #Passou da idade

if idade >= idade_minima and idade_maxima:
    print(f"{nome}, está liberado o emprestimo! ")
else:
    print(f"Desculpe, não conseguimos liberar o emprestimo. ")