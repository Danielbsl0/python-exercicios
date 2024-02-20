n1 = float(input('Digite um valor: '))
if n1 >0:
    print(f'O valor inserido é \033[32mpositivo\033[m.')
elif n1 < 0:
    print(f'O valor inserido é \033[31mnegativo\033[m')
else:
    print(f'O valor inserido é nulo.')