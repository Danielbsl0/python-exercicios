l1 = float(input('Insira a medida do lado: '))
l2 = float(input('Insira a medida do segundo lado: '))
l3 = float(input('Insira a medida de outro lado: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print(f'Os lados com as medidas: {l1}m, {l2}m, {l3}m, podem formar um triângulo!', end='\n')
    if l1 == l2 == l3:
        print(f'O triângulo formado é EQUILÁTERO')
    elif l3 == l1 != l3 or l2 == l1 > l3 != l2 or l2 == l3 != l1:
        print(f'O triângulo formado é ISÓSCELES')
    else:
        print(f'O triângulo formado é ESCALENO')
else:
    print(f'O lados informados NÃO podem formar um triângulo!')
