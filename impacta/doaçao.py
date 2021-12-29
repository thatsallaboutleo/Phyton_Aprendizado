vic_coin = float(input())
total = 0
real = 0

if vic_coin == -1:
    print(f'VC$ {total:.2f}')
    print(f'R$ {real:.2f}')
else:
    while vic_coin != -1:
        total += vic_coin
        real = total * 2.5
        vic_coin = float(input())

    print(f'VC$ {total:.2f}')
    print(f"R$ {real:.2f}")