"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max

append - insere algo no final da lista
insert - insere algo em um ponto especifico da lista, deve dizer o indice
pop - exclui algo da lista
del - exclui um ponto especifico da lista, ou um range

max - pega o maior valor da lista
min - pega o menor valor da lista

função "list" - torna uma função interável
"""

secret = 'perfume'
digit = []
chance = 5

while True:
    if chance <= 0:
        print('Que pena! Acabaram suas chances.')
        break

    letra = input('Digite uma letra: ').lower()

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    digit.append(letra)

    if letra in secret:
        print(f'Joia! a letra "{letra}" está na palavra."')
    else:
        print(f'Puts! a letra "{letra}" não está na palavra.')
        digit.pop()

    secret_temp =''
    for letra_sec in secret:
        if letra_sec in digit:
            secret_temp += letra_sec
        else:
            secret_temp += '_'

    if secret_temp == secret:
        print(f'Acertou! a palavra era {secret_temp}')
        break
    else:
        print(f'Por enquanto temos: {secret_temp}')

    palavra_c = input('Imagina qual seja? digite: ')
    if palavra_c == secret:
        print('Aí sim! acertou miseravi!')
        break
    else:
        len(palavra_c) < len(secret)
        print('Não, tenta de novo')
        chance -= 1
        print()
        print(f'Você ainda tem {chance} chances.')