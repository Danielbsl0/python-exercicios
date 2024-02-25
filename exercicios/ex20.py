n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
n3 = float(input('Insira a terceira nota: '))
md = (n1+n2+n3)/3
if 10>md >= 7:
    print(f'APROVADO')
elif md == 10:
    print(f'APROVADO COM DISTINÇÃO')
else:
    print(f'REPROVADO')
