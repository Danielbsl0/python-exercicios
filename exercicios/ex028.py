tipo = input('Qual é o tipo de carne(Filé Duplo/Alcatra/Picanha: ').strip().upper()
quant = float(input('Quantidade da carne em Kg: '))
pag = input('A compra será feita usando cartão Tabajara?(S/N): ').strip().upper()
if tipo == 'FILÉ DUPLO':
    if quant <= 5:
        preco = 4.9*quant
    else:
        preco = 5.8*quant
elif tipo == 'ALCATRA':
    if quant <= 5:
        preco = 5.9*quant
    else:
        preco = 6.8*quant
elif tipo == 'PICANHA':
    if quant <= 5:
        preco = 6.9*quant
    else:
        preco = 7.8*quant
else:
    print('TIPO DE CARNE INVÁLIDO')
if pag == 'S':
    pag = 'Cartão Tabajara'
    desc = preco*5/100
    precodesc = preco - desc
else:
    pag = 'Cartão comum'
    desc = 0
    precodesc = preco    
print(32*'-')
print('     NOTA FISCAL     ')
print(32*'-')
print(f'TIPO DE CARNE: {tipo}')
print(f'QUANTIDADE DE CARNE: {quant}Kg')
print(f'PREÇO TOTAL: R${preco}')
print(f'TIPO DE PAGAMENTO: {pag}')
print(f'VALOR DO DESCONTO: R${desc}')
print(F'VALOR A PAGAR: R${precodesc}')
