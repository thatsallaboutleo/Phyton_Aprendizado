g_tem = []
tem = 0
cont = 0


def somaL(list1):
    soma = 0
    for i in list1:
        if i >= 0:
            soma = soma + i
    return soma


while tem >= 0:
    tem = int(input())
    g_tem.append(tem)
    if tem >= 0:
        cont += 1

soma = somaL(g_tem)
media = soma/cont
print(f'MEDIA: {media:.2f}')

for i in g_tem:
    if media > i >= 0:
        print(i)