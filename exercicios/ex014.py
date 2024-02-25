n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira outra nota: '))
md = (n1 + n2)/2
if md <= 4:
    conc = 'E'
elif md < 6:
    conc = 'D'
elif md < 7.5:
    conc = 'C'
elif md < 9:
    conc = 'B'
else:
    conc = 'A'
print(f'1°Nota: {n1}\n2°Nota: {n2}\nMédia: {md}\nConceito: {conc}', end='\n')
if conc in 'ABC':
    print(f'APROVADO!')
else:
    print(f'REPROVADO!')
