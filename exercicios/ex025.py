#"Telefonou para a vítima?""Esteve no local do crime?""Mora perto da vítima?""Devia para a vítima?""Já trabalhou com a vítima?"
print(32*'-')
print('INTERROGATÓRIO SOBRE O CRIME')
print(32*'-')
p1 = input('Telefonou para a vítima?(S/N): ').strip().upper()
p2 = input('Esteve no local do crime?(S/N): ').strip().upper()
p3 = input('Mora perto da vítima?(S/N): ').strip().upper()
p4 = input('Devia para a vítima?(S/N): ').strip().upper()
p5 = input('Já trabalhou com a vítima?(S/N): ').strip().upper()
cont = 0
print('O seu estado de participação do crime é de: ', end='')
if p1 == 'S' or p1 == 'SIM':
    cont +=1
if p2 == 'S' or p2 == 'SIM':
    cont +=1
if p3 == 'S' or p3 == 'SIM':
    cont +=1
if p4 == 'S' or p4 == 'SIM':
    cont +=1
if p5 == 'S' or p5 == 'SIM':
    cont +=1
if cont == 2:
    print('SUSPEITO')
elif 2 < cont <=4:
    print('CÚMPLICE')
elif cont == 5:
    print('ASSASSINO')
else:
    print('INOCENTE')
