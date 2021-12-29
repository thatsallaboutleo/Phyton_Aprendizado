def prog():
    inicio = int(input())
    fim = int(input())
    num_prim = 0

    while inicio <= fim:
        if primo(inicio):
            num_prim += 1
            print(inicio)
        inicio += 1

    print(f'primos: {num_prim}')


def primo(num):
    ini = 1
    cont = 0

    while ini <= num:
        if num == 1:
            return False

        if num % ini == 0:
            cont += 1
        ini += 1

    if cont > 2:
        return False
    else:
        return True


prog()
