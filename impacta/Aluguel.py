deve = int(input())
pagou = int(input())
falta = deve - pagou
pag = 1

if deve < pagou:
    falta = 0
    print(f'pagamento: 1')
    print(f'antes = {deve}')
    print(f'depois = {falta}')
    print('-----')

else:
    print(f'pagamento: 1')
    print(f'antes = {deve}')
    print(f'depois = {falta}')
    print('-----')

tratamento = 0
while falta > 0:
    pag += 1
    print(f'pagamento: {pag}')
    if pagou > falta:
        falta = 0
        print(f'antes = {tratamento}')
        print(f'depois = {falta}')
        print('-----')
    else:
        print(f'antes = {falta}')
        falta -= pagou
        tratamento = falta
        print(f'depois = {falta}')
        print('-----')