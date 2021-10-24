entrada = input()
entrega = int(input())

um = 'domingo'
dois = 'segunda'
tres = 'terca'
quatro = 'quarta'
cinco = 'quinta'
seis = 'sexta'
sete = 'sabado'

## domingo
if entrada == um and entrega == 0:
    print('chega hoje!')
elif entrada == um and entrega > 6:
    print('entrega invalida')
elif entrada == um and entrega == 1:
    print(f'sera entregue {dois}')
elif entrada == um and entrega == 2:
    print(f'sera entregue {tres}')
elif entrada == um and entrega == 3:
    print(f'sera entregue {quatro}')
elif entrada == um and entrega == 4:
    print(f'sera entregue {cinco}')
elif entrada == um and entrega == 5:
    print(f'sera entregue {seis}')
elif entrada == um and entrega == 6:
    print(f'sera entregue {sete}')
## segunda
elif entrada == dois and entrega == 0:
    print('chega hoje!')
elif entrada == dois and entrega > 6:
    print('entrega invalida')
elif entrada == dois and entrega == 1:
    print(f'sera entregue {tres}')
elif entrada == dois and entrega == 2:
    print(f'sera entregue {quatro}')
elif entrada == dois and entrega == 3:
    print(f'sera entregue {cinco}')
elif entrada == dois and entrega == 4:
    print(f'sera entregue {seis}')
elif entrada == dois and entrega == 5:
    print(f'sera entregue {sete}')
elif entrada == dois and entrega == 6:
    print(f'sera entregue {um}')
## terça
elif entrada == tres and entrega == 0:
    print('chega hoje!')
elif entrada == tres and entrega > 6:
    print('entrega invalida')
elif entrada == tres and entrega == 1:
    print(f'sera entregue {quatro}')
elif entrada == tres and entrega == 2:
    print(f'sera entregue {cinco}')
elif entrada == tres and entrega == 3:
    print(f'sera entregue {seis}')
elif entrada == tres and entrega == 4:
    print(f'sera entregue {sete}')
elif entrada == tres and entrega == 5:
    print(f'sera entregue {um}')
elif entrada == tres and entrega == 6:
    print(f'sera entregue {dois}')
## quarta
elif entrada == quatro and entrega == 0:
    print('chega hoje!')
elif entrada == quatro and entrega > 6:
    print('entrega invalida')
elif entrada == quatro and entrega == 1:
    print(f'sera entregue {cinco}')
elif entrada == quatro and entrega == 2:
    print(f'sera entregue {seis}')
elif entrada == quatro and entrega == 3:
    print(f'sera entregue {sete}')
elif entrada == quatro and entrega == 4:
    print(f'sera entregue {um}')
elif entrada == quatro and entrega == 5:
    print(f'sera entregue {dois}')
elif entrada == quatro and entrega == 6:
    print(f'sera entregue {tres}')
## quinta
elif entrada == cinco and entrega == 0:
    print('chega hoje!')
elif entrada == cinco and entrega > 6:
    print('entrega invalida')
elif entrada == cinco and entrega == 1:
    print(f'sera entregue {seis}')
elif entrada == cinco and entrega == 2:
    print(f'sera entregue {sete}')
elif entrada == cinco and entrega == 3:
    print(f'sera entregue {um}')
elif entrada == cinco and entrega == 4:
    print(f'sera entregue {dois}')
elif entrada == cinco and entrega == 5:
    print(f'sera entregue {tres}')
elif entrada == cinco and entrega == 6:
    print(f'sera entregue {quatro}')
## sexta
elif entrada == seis and entrega == 0:
    print('chega hoje!')
elif entrada == seis and entrega > 6:
    print('entrega invalida')
elif entrada == seis and entrega == 1:
    print(f'sera entregue {sete}')
elif entrada == seis and entrega == 2:
    print(f'sera entregue {um}')
elif entrada == seis and entrega == 3:
    print(f'sera entregue {dois}')
elif entrada == seis and entrega == 4:
    print(f'sera entregue {tres}')
elif entrada == seis and entrega == 5:
    print(f'sera entregue {quatro}')
elif entrada == seis and entrega == 6:
    print(f'sera entregue {cinco}')
## sabado
elif entrada == sete and entrega == 0:
    print('chega hoje!')
elif entrada == sete and entrega > 6:
    print('entrega invalida')
elif entrada == sete and entrega == 1:
    print(f'sera entregue {um}')
elif entrada == sete and entrega == 2:
    print(f'sera entregue {dois}')
elif entrada == sete and entrega == 3:
    print(f'sera entregue {tres}')
elif entrada == sete and entrega == 4:
    print(f'sera entregue {quatro}')
elif entrada == sete and entrega == 5:
    print(f'sera entregue {cinco}')
elif entrada == sete and entrega == 6:
    print(f'sera entregue {seis}')