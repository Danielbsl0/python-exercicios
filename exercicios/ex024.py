n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
op = input('Qual a operação você deseja realizar?: ').strip().upper()
soma = n1+n2
sub = n1-n2
prod = n1*n2
div = n1/n2
pot = n1**n2
raiz = n1**1/n2
if op == 'SOMA' or op == 'SUBTRAÇÃO' or op == 'MULTIPLICAÇÃO' or op == 'DIVISÃO' or op == 'POTÊNCIA' or op == 'POTENCIAÇÃO' or op == 'RAIZ' or op == 'RADICIAÇÃO':
    if op == 'SOMA':
        op = soma
        print(f'{soma}', end='\n')
    elif op == 'SUBTRAÇÃO':
        op = sub
        print(f'{sub}')
    elif op == 'MULTIPLICAÇÃO':
        op = prod
        print(f'{prod}')
    elif op == 'DIVISÃO':
        op = div
        print(f'{div}')
    elif op == 'POTÊNCIA' or op == 'POTENCIAÇÃO':
        op = pot
        print(f'{pot}')
    elif op == 'RADICIAÇÃO' or op == 'RAIZ':
        op = raiz
        print(f'{raiz}')    
    if op % 2 == 0:
        print(f'O número inserido é par.')
    else:
        print(f'O número inserido é ímpar.')
    if op > 0:
        print(f'O número inserido é positivo')
    else:
        print(f'O número inserido é negativo')
    if round(op) == op:
        print(f'O número inserido é inteiro')
    else:
        print(f'O número inserido é decimal')
else:
    print(f'Operação inserida inválida')
