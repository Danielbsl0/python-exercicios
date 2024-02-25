dia = int(input('Dias da semana:\n1- Domingo\n2 - Segunda\n3 - Terça\n4 - Quarta\n5 - Quinta\n6 - Sexta\n7 - Sábado\nInsira um número: '))
if dia == 1:
    print(f'{dia} - Domingo')
elif dia == 2:
    print(f'{dia} - Segunda')
elif dia == 3:
    print(f'{dia} - Terça')
elif dia == 4:
    print(f'{dia} - Quarta')
elif dia == 5:
    print(f'{dia} - Quinta')
elif dia == 6:
    print(f'{dia} - Sexta')
elif dia == 7:
    print(f'{dia} - Sábado')
else:
    print(f'{dia} é \033[1;31mINVÁLIDO\033[m')
    