turno = input('TABELA DE TURNOS:\nM- Matutino\nV- Vespertino\nN - Noturno\nInsira qual o seu turno: ').strip().upper()
if turno == 'M':
    print('BOM DIA!')
elif turno == 'V':
    print('BOA TARDE!')
elif turno == 'N':
    print('BOA NOITE!')
else:
    print(f'Valor inválido')
