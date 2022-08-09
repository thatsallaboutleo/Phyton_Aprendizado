import random

print("Olá, bem vinda a sua própria versão do BBB!")
print("--------------------------------------------------------------------------------------------------------------")

participantes = []
cont_1 = 0
while cont_1 <= 3:
    a = input("Digite o nome do participante: ")
    if not a in participantes:
        participantes.append(a)
    else:
        print("")
        print("Participante já está na lista!")
        while a not in participantes:
            a = input("Digite o nome do participante: ")
            participantes.append(a)
    cont_1 += 1

print("--------------------------------------------------------------------------------------------------------------")
print(f'Participante 1: {participantes[0]}\n'
      f'Participante 2: {participantes[1]}\n'
      f'Participante 3: {participantes[2]}\n'
      f'Participante 4: {participantes[3]}\n')
print("--------------------------------------------------------------------------------------------------------------")

b = input("Podemos continuar? S/N: ")

while True:
    if b == "s" or b == "S":
        break
    else:
        b = input("Podemos continuar? S/N: ")

print("--------------------------------------------------------------------------------------------------------------")
print("Vamos de prova do lider!")

lider = random.choice(participantes)
print(f"Pelos resultados na prova, novo lider desta semana é: {lider}")
restante = []
restante.append(lider)
participantes.remove(lider)

print("--------------------------------------------------------------------------------------------------------------")
b = input("Podemos continuar? S/N: ")

while True:
    if b == "s" or b == "S":
        break
    else:
        b = input("Podemos continuar? S/N: ")

print("--------------------------------------------------------------------------------------------------------------")
print(f"Paredão! vote para sair: {participantes}")
print("--------------------------------------------------------------------------------------------------------------")
b = input("Podemos continuar? S/N: ")

while True:
    if b == "s" or b == "S":
        break
    else:
        b = input("Podemos continuar? S/N: ")

saiu = random.choice(participantes)
print(f"Esta votação foi histórico! batemos numeros de votos jamais vistos, infelizmente quem sai hoje é você, {saiu}!")
participantes.remove(saiu)
restante.append(participantes[0])
restante.append(participantes[1])

print("--------------------------------------------------------------------------------------------------------------")
b = input("Podemos continuar? S/N: ")

while True:
    if b == "s" or b == "S":
        break
    else:
        b = input("Podemos continuar? S/N: ")

print("--------------------------------------------------------------------------------------------------------------")
lider2 = random.choice(restante)
print(f"Pelos resultados na prova, novo lider desta semana é: {lider2}")
final = []
restante.remove(lider2)
final.append(lider2)

print("--------------------------------------------------------------------------------------------------------------")
b = input("Podemos continuar? S/N: ")

while True:
    if b == "s" or b == "S":
        break
    else:
        b = input("Podemos continuar? S/N: ")

print("--------------------------------------------------------------------------------------------------------------")
print(f"Paredão! vote para sair: {restante}")
b = input("Podemos continuar? S/N: ")

while True:
    if b == "s" or b == "S":
        break
    else:
        b = input("Podemos continuar? S/N: ")

print("--------------------------------------------------------------------------------------------------------------")
saiu = random.choice(restante)
print(f"Esta votação foi histórico! batemos numeros de votos jamais vistos, infelizmente quem sai hoje é você, {saiu}!")
restante.remove(saiu)
final.append(restante[0])

print("--------------------------------------------------------------------------------------------------------------")
print(f"Final! vote para ganhar: {final}")
b = input("Podemos continuar? S/N: ")

while True:
    if b == "s" or b == "S":
        break
    else:
        b = input("Podemos continuar? S/N: ")

print("--------------------------------------------------------------------------------------------------------------")
vencedor = random.choice(final)
print(f"Infelizmente chegamos ao final desta edição, hoje quem ganha é você, {vencedor}!")