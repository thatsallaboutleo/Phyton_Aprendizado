"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
bom dia 0-11, boa tarde 12-17 e boa noite 18-23.
"""

print('Para a inserção a seguir, desconsidere os minutos.')
print('')

hora = input('Que horas são? ')
if hora.isdigit():  #verificar se o atribuido pode virar um numero.
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('Horário deve estar entre 0 e 23')
    else:
        if 0 >= hora or hora <= 12:
            print('Bom dia')
        elif 12 > hora or hora < 17:
            print('Boa tarde')
        elif 17 > hora or hora < 23:
            print('Boa noite')
        else:
            pass
else:
    print('Digite a hora corretamente')