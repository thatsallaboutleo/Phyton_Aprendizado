nt_trab = float(input())
nt_prov = float(input())
media = (nt_trab + nt_prov) / 2

if media >= 6:
    print('aprovado')

elif nt_trab < 2:
    print('reprovado')

elif nt_trab == 0:
    print('reprovado')

elif nt_trab >= 2:
    print('talvez com a sub')