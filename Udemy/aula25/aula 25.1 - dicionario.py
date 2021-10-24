"""
dicionarios em python são similares as listas, a diferença é que a lista
gera um indice para você, já o dicionario este indice é gerado por você, são mutáveis

indices = chaves
"""

# d1 = {'chave1': 'valor da chave'}  #este é o formato mais usual
# d1['nova_chave'] = 'valor da nova chave'  #para acrescentar mais chaves no dicionario
#
# print(d1['chave1'])  #tudo que vem no colchetes é o que eu desejo acessar
#
# #outra maneira de criar dicionarios:
#
# d2 = dict(chave2 = 'valor da chave2', chave3 = 'valor da chave3')
# print(d2)

d1 = {
    'str':'valor',
    123:'outro valor',
    (1,2,3,4):'tupla',
}

# d1['naoexiste'] = 'agora existe'
#
# if 'naoexiste' not in d1:
#     print(d1['naoexiste'])  #caso você não tenha uma chave dentro do dicionario

# d1['nomedachave'] = 'agora ela existe'
#
# if d1.get('nomedachave') is not None:  #procurar e incluir chaves no dicionario
#     print(d1.get('nomedachave'))