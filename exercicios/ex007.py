n1 = float(input('Insira um número: '))
n2 = float(input('Insira outro número: '))
n3 = float(input('Insira outro número: '))
if n2 < n1 > n3: 
    if n2 > n3:
        print(f'O maior valor é: {n1}\nO menor valor é: {n3}')
    elif n3 > n2:
        print(f'O maior valor é: {n1}\nO menor valor é: {n2}')
    elif n3 == n2:
        print(f'O maior valor é: {n1}\nNão existe menor valor')
    elif n1 == n2 and n3 < n2:
        print(f'Não existe maior valor\nE o menor valor é: {n3}')
    elif n1 == n3 and n3 > n2:
        print(f'Não existe maior valor\nE o menor valor é: {n2}')
elif n1 < n2 > n3:
    if n1 > n3:
        print(f'O maior valor é: {n2}\nO menor valor é: {n3}')
    elif n1 < n2 > n3 and n1 < n3:
        print(f'O maior valor é: {n2}\nO menor valor é: {n1}')
    elif n1 < n2 > n3 and n1 == n2:
        print(f'O maior valor é: {n2}\nNão existe menor valor')
    elif n2 == n1 and n1 > n3:
        print(f'Não existe maior valor\nO menor valor é: {n3}')
    elif n2 == n3 and n1 < n3:
        print(f'Não existe maior valor\nO menor valor é: {n1}')
elif n1 < n3 > n2: 
    if n1 < n2:
        print(f'O maior valor é: {n3}\nO menor valor é: {n1}') 
    elif n1 < n3 > n2 and n1 > n2:
        print(f'O maior valor é: {n3}\nO menor valor é: {n2}') 
    elif n1 < n3 > n2 and n1 == n2:
        print(f'O maior valor é: {n3}\nO menor valor não existe') 
    elif n3 == n2 and n1 < n2:
        print(f'O maior valor é: {n3}\nO menor valor é: {n1}') 
    elif n3 == n1 and n1 > n2:
        print(f'O maior valor é: {n3}\nO menor valor é: {n2}') 
else:
    print(f'Todos os valores são iguais')

        