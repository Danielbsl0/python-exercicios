n1 = float(input('Insira um número: '))
n2 = float(input('Insira outro número: '))
n3 = float(input('Insira outro número: '))
if n2 < n1 > n3:
    print(f'O maior valor é: {n1}')
elif n1 < n2 > n3:
    print(f'O maior valor é {n2}')
elif n1 < n3 > n2:
    print(f'O maior valor é: {n3}')
else:
    print(f'Não existe um valor maior do que todos')
