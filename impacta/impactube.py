cont = int(input())

def exibe(tab):
    for reg in tab:
        print(f'{reg[0]}: R$ {reg[1]:.2f}')


entrada = []

while cont != 0:
    infos = input().split(';')
    infos[1] = int(infos[1])
    infos[2] = float(infos[2])
    if infos[3] == 'não':
        infos[3] = False
    else:
        infos[3] = True
    entrada.append(infos)
    cont -= 1

X = float(input())
Y = float(input())

bonus = []

for infos in entrada:
    if infos[3]:
        vl_bonus = infos[2] + (X * (infos[1] // 1000))
    else:
        vl_bonus = infos[2] + (Y * (infos[1] // 1000))
    bonus.append([infos[0], vl_bonus])

print(5 * '-')
print('BÔNUS')
print(5 * '-')
exibe(bonus)