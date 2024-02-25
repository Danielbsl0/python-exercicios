prod1 = float(input('Preço do primeiro produto: R$: '))
prod2 = float(input('Preço do segundo produto: R$: '))
prod3 = float(input('Preço do terceiro produto: R$: '))
if prod2 > prod1 < prod3:
    print(f'Você deve comprar o produto que custa R${prod1}')
elif prod1 > prod2 < prod3:
    print(f'Você deve comprar o produto que custa R${prod2}')
elif prod1 > prod3 < prod2:
    print(f'Você deve comprar o produto que custa R${prod3}')
elif prod1 == prod2 == prod3:
    print(f'Todos os produtos têm o mesmo preço! Escolha o da sua preferência :)')
else:
    print(f'Há mais de um produto com o mesmo preço, escolha o da sua preferência.')
