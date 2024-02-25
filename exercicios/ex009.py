n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
if n1 > n2 > n3:
    print(f'Números em ordem decrescente:\n{n1}\n{n2}\n{n3}')
elif n2 > n1 > n3:
    print(f'Números em ordem decrescente:\n{n2}\n{n1}\n{n3}')
elif n2 > n3 > n1:
    print(f'Números em ordem decrescente:\n{n2}\n{n3}\n{n1}')
elif n1 > n3 > n2:
    print(f'Números em ordem decrescente:\n{n1}\n{n3}\n{n2}')
elif n3 > n1 > n2:
    print(f'Números em ordem decrescente:\n{n3}\n{n1}\n{n2}')
elif n3 > n2 > n1:
    print(f'Números em ordem decrescente:\n{n3}\n{n2}\n{n1}')
