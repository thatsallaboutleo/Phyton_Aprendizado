"""
while em python
utilizado para realizar ações enquanto
uma condição for verdadeira

requisitos: entender condições e operadores
"""
while True:
    print()
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    operador = input('Digite o operador: ')

    if not n1.isdigit() or not n2.isnumeric():
        print('Você precisa digitar um número.')
        continue
    n1 = int(n1)
    n2 = int(n2)

    #+ - / *
    if operador == '+':
        a = n1+n2
        print(f'Resultado é {a}.')
    elif operador == '-':
        b = n1-n2
        print(f'Resultado é {b}.')
    elif operador == '/':
        c = n1/n2
        print(f'Resultado é {c}.')
    elif operador == '*':
        d = n1*n2
        print(f'Resultado é {d}.')
    else:
        print('Digite um operador viável')

    sair = input('Você deseja continuar? [S]im [N]Não: ')
    if sair == 'S' or 's':
        continue
    if sair == 'N' or 'n':
        break
    if not sair == 'S' or not sair == 'N' or not sair == 's' or not sair == 's':
        print('Digite S para sim e N para não.')