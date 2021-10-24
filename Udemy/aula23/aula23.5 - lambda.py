
lista = [
    ['P1', 15],
    ['P2', 20],
    ['P3', 7],
    ['P4', 3],
    ['P5', 35],
]

print(sorted(lista, key=lambda i: i[1], reverse=True))
print(lista)