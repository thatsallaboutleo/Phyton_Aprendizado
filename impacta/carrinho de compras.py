l1 = input().split()

for i in range(len(l1)):
    l1[i] = int(l1[i])

com = input().split()

if com[0] == 'adicionar':
    l1.append(int(com[1]))


if com[0] == 'remover':
    if int(com[1]) in l1:
        l1.remove(int(com[1]))
    else:
        print(f'código {com[1]} não encontrado')

if com[0] == 'exibir':
    l1.sort()
    print(*l1)

while com[0] != 'encerrar':
    com = input().split()

    if com[0] == 'adicionar':
        l1.append(int(com[1]))

    if com[0] == 'remover':
        if int(com[1]) in l1:
            l1.remove(int(com[1]))
        else:
            print(f'código {com[1]} não encontrado')

    if com[0] == 'exibir':
        l1.sort()
        print(*l1)

if com[0] == 'encerrar':
    l1.sort()
    print(*l1)