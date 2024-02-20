media = float(input('Insira a média do aluno: '))
if media == 10:
    print(f'\033[1;32mAPROVADO COM DISTINÇÃO\033[m')
elif media >= 7:
    print(f'\033[32mAPROVADO\033[m')
else:
    print(f'\033[1;31mREPROVADO\033[m')


