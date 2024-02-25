lit = float(input('Quantidade de litros: '))
comb = input('Tipo de combustível(G-GASOLINA, A-ÁLCOOL): ').strip().upper()
if comb == 'A':
    if lit <= 20:
        preco = (1.90 * lit)
        desc = preco - preco*3/100
    else:
        preco = (1.90 * lit)
        desc = preco - preco*5/100
    print(f'O valor a ser pago é R${desc}')
elif comb == 'G': 
    if lit <= 20:
        preco = (2.50 * lit)
        desc = preco - preco*4/100
    else:
        preco = (2.50 * lit)
        desc = preco - preco*6/100
    print(f'O valor a ser pago é R${desc}')
else:
    print(f'Combustível inserido é INVÁLIDO')