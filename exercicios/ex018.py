dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês: '))
ano = int(input('Insira o ano: '))
if mes%2 != 0 or mes == 8 or mes == 10 or mes == 12 and 0<dia<=31 or mes == 2 and 0<dia<=28 or mes%2 == 0 and mes != 8 and mes != 10 and mes != 12 and 0<dia<=30:
    print(f'A data inserida é válida!')
else:
    print(f'A data inserida é inválida!')

    