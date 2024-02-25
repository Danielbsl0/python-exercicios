n1 = int(input('Insira um número inteiro: '))
if n1 <1000:
    c = n1//100
    d = (n1 - c*100)//10
    u = (n1 - c*100) - d*10
    if c > 0:
        print(f'{c} centenas', end='')
    if d > 0:
        if c > 0:
            print(f',', end=' ')
        print(f'{d} dezenas', end=' ')
    if u > 0:
        if d > 0:
            print(f'e', end=' ')
        print(f'{u} unidades')
