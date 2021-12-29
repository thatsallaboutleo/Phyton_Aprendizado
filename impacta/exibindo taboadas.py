inicio = input()
inicio = int(inicio)
fim = input()
fim = int(fim)
multiplicador = 1

if inicio <= fim:
    while inicio <= fim:
        for i in range(1,11):
            result = i*inicio
            print(f'{inicio} x {i} = {result}')
        inicio += 1
        print('----------')

else:
    print('Nenhuma tabuada no intervalo!')