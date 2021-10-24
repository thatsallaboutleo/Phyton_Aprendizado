valor_merc = float(input())
quant_itens = int(input())

desc_fixo = 10/100
des_var = quant_itens/100
des_ttl = desc_fixo + des_var

if quant_itens > 40:
    print('Limite de compra por cliente é de 40 itens.')

valor_ttl = valor_merc*quant_itens
valor_ttl_c_desc = valor_ttl - (valor_ttl*des_ttl)

print(f'{valor_ttl:.2f}')
print(f'{valor_ttl_c_desc:.2f}')