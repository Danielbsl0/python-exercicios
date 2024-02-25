a = float(input('Insira o valor de A: '))
if a == 0:
    print('a = 0, a equação é do PRIMEIRO GRAU')
else:
    b = float(input('Insira o valor de B: '))
    c = float(input('Insira o valor de C: '))
    delta = b**2-4*a*c
    x1 = (-b + delta**1/2)/2*a
    x2 = (-b - delta**1/2)/2*a
    if delta <0:
        print(f'O DELTA é NEGATIVO. A equação não tem RAÍZES REAIS!')
    elif delta == 0:
        print(f'O DELTA é igual a ZERO. A equação só tem uma RAÍZ: x = {x1}')
    else:
        print(f"O DELTA  é POSITIVO. A equação possuí duas RAÍZES: x'= {x1}\nx''= {x2}")
print(f'FIM DO PROGRAMA')