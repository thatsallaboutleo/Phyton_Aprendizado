n = int(input())
linha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
coluna = 0

while coluna != n:
    if coluna == 0:
        print(linha[0]*1)
        coluna += 1

    else:
        if coluna == 1:
            print(linha[coluna] * (coluna+1))
            coluna += 1
        else:
            print(linha[coluna]*(coluna+1))
            coluna += 1