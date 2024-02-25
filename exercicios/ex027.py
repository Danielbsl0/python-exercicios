morango = int(input('Quantidade de morangos: '))
maca = int(input('Quantidade de maçãs: '))
if morango <= 5:
    valmor = morango*2.5
else:
    valmor = morango*2.2
if maca <= 5:
    valmac = maca*1.8
else:
    valmac = maca*1.5
valor = valmor + valmac
quilo = morango + maca
if quilo >8 or quilo >25:
    valor = valor-(valor*10/100)
print(f'O valor a ser pago será de R${valor}')

