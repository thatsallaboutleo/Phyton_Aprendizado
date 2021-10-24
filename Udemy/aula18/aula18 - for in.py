"""
For in em python
iterando strings com for
função range(start=0, stop, step=1)
"""

texto = 'Python'
nv_str = ''

#continue - pula para o proximo laço
#break - para de repetir o laço

for letra in texto:
    if letra == 't':
        nv_str = nv_str + letra.upper()
    elif letra == 'h':
        nv_str = nv_str + letra.upper()
    else:
        nv_str += letra
print(nv_str)