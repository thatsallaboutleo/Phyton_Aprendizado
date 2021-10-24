#       Índices
#       0123456789........................33

frase = 'o rato roeu a roupa do rei de roma'
tam_frase = len(frase)
contador = 0
nv_str = ''

usuario = input('Qual letra deseja colocar maiúscula? ')

while contador < tam_frase:
    letra = frase[contador]  #dentro das chaves foi colocado o indice de inicio
    if letra == usuario:
        nv_str += usuario.upper()
    else:
        nv_str += letra
    contador += 1
print(nv_str)

##interação seria a maneira de passar por uma string, fazendo modificações ou não
