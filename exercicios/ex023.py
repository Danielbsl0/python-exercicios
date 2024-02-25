n = float(input('Insira um número: '))
if round(n) == n:
    print(f'{n:.0f} é um número INTEIRO')
else:
    print(f'{n} é um número DECIMAL')