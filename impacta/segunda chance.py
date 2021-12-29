alunos = int(input())

nota_original = []
for i in range(alunos):
    nota_original.append(float(input()))

nota_segchance = []
for i in range(alunos):
    nota_segchance.append(float(input()))

notas_finais = []
notas_alteradas = 0
for i in range(alunos):
    if nota_segchance[i] == 10 and nota_original[i] < 10:
        nota_final = nota_original[i] + 2
        if nota_final > 10:
            nota_final = 10
        notas_finais.append(nota_final)
        notas_alteradas += 1
    else:
        notas_finais.append(nota_original[i])

print(f'NOTAS ALTERADAS: {notas_alteradas}')

for i in range(alunos):
    if nota_original[i] != notas_finais[i]:
        print(f'*({i + 1:03}) original: {nota_original[i]:05.2f} | final: {notas_finais[i]:05.2f}')
    else:
        print(f'-({i + 1:03}) original: {nota_original[i]:05.2f} | final: {notas_finais[i]:05.2f}')