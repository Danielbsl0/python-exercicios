sexo = input('Insira o sexo(M/F): ').strip().upper()
if sexo == 'M':
    print(f'O sexo inserido foi: \033[34mMASCULINO\033[m')
elif sexo == 'F':
    print(f'O sexo inserido foi: \033[32mFEMININO\033[m')
else:
    print(f'O sexo inserido foi \033[31mINVÁLIDO\033[m')
